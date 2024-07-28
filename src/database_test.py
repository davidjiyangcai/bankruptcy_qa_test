import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import logging
import sys
import json
import numpy as np
import faiss
from pprint import pprint
from dotenv import load_dotenv
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
    ServiceContext,
    Document
)
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core import Settings

# Load environment variables from .env file
load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Configure logging
log_dir = './logs'  # Directory for logs
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'process_log.txt')

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# List the folder names in data directory
data_dir = './data/bankruptcy_dockets/documents'
folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]

# Track total costs
total_cost = 0

def get_embeddings(texts):
    response = client.embeddings.create(input=texts,
    model="text-embedding-ada-002")
    embeddings = [data["embedding"] for data in response.data]
    return np.array(embeddings)

def save_index(folder):
    global total_cost
    logger.info(f"Processing folder: {folder}")

    # Load PDFs
    documents = SimpleDirectoryReader(f"./data/bankruptcy_dockets/documents/{folder}").load_data()
    num_documents = len(documents)
    logger.info(f"Number of documents in folder '{folder}': {num_documents}")

    # Split into nodes
    node_parser = SentenceWindowNodeParser.from_defaults(
        window_size=2,
        window_metadata_key="window",
        original_text_metadata_key="original_sentence",
    )

    nodes = node_parser.get_nodes_from_documents(documents)
    num_nodes = len(nodes)
    logger.info(f"Number of nodes in folder '{folder}': {num_nodes}")

    # Generate embeddings for nodes and calculate token usage
    texts = [node.metadata.get("original_sentence", "") for node in nodes if node.metadata.get("original_sentence", "")]

    try:
        embeddings = get_embeddings(texts)
        total_tokens = sum(len(text.split()) for text in texts)
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        return

    logger.info(f"Total tokens used in folder '{folder}': {total_tokens}")

    # Calculate the cost
    cost_per_million_input_tokens = 5  # $5 per 1 million input tokens
    folder_cost = (total_tokens / 1_000_000) * cost_per_million_input_tokens
    total_cost += folder_cost
    logger.info(f"Cost for folder '{folder}': ${folder_cost:.4f}")

    # Initialize FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to the index
    index.add(np.array(embeddings, dtype='float32'))

    # Save nodes information to a JSON file
    os.makedirs(f"./data/bankruptcy_dockets/output/persist_{folder}", exist_ok=True)
    with open(f"./data/bankruptcy_dockets/output/persist_{folder}/nodes.json", 'w') as f:
        json.dump([node.to_dict() for node in nodes], f)

    # Save FAISS index
    faiss.write_index(index, f"./data/bankruptcy_dockets/output/persist_{folder}/faiss_index.bin")

for folder in folders:
    save_index(folder)

logger.info(f"Total cost for processing all folders: ${total_cost:.4f}")

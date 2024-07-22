# This is script for text and metadata extraction
import os
import openai

import logging
import sys
from pprint import pprint

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
    ServiceContext,
    Document
)

from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceWindowNodeParser, HierarchicalNodeParser, get_leaf_nodes
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.schema import MetadataMode
from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core import Settings

#from dotenv import load_dotenv
# load_dotenv()

# list the folder names in data directory
data_dir = './data/bankruptcy_dockets/documents'
folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]

def save_index(folder):
    print(folder)
    # load PDFs
    documents = SimpleDirectoryReader(f"./data/bankruptcy_dockets/documents/{folder}").load_data()

    # split into notes
    node_parser = SentenceWindowNodeParser.from_defaults(
    # how many sentences on either side to capture
    window_size=2,
    # the metadata key that holds the window of surrounding sentences
    window_metadata_key="window",
    # the metadata key that holds the original sentence
    original_text_metadata_key="original_sentence",
    )

    nodes = node_parser.get_nodes_from_documents(documents)
    logging.info(f"Number of nodes: {len(nodes)}")

    #embedding model

    Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-large", embed_batch_size=100
    )

    #build index
    index = VectorStoreIndex(nodes)

    # create a folder to store the embeddings and output
    os.makedirs(f"./data/bankruptcy_dockets/output/persist_{folder}",
    exist_ok=True)
    # store the index and embeddings
    index.storage_context.persist(persist_dir=f"./data/bankruptcy_dockets/output/persist_{folder}")

for folder in folders:
    save_index(folder)


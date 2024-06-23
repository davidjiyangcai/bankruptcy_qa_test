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
openai.api_key = os.environ['OPENAI_API_KEY']

from llama_index.core.postprocessor import MetadataReplacementPostProcessor
from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine

from define_questions import questions

def ask_question(question_name,retrieved_index):
    Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-large", embed_batch_size=100
    )
    llm = OpenAI(model="gpt-4o",temperature=0)
    Settings.llm = llm

    # configure retriever
    retriever = VectorIndexRetriever(
        index=retrieved_index,
        similarity_top_k=10,
        reranker_top_n=5,
        with_reranker=True
    )
    
    response_synthesizer = get_response_synthesizer(
        response_mode="tree_summarize",
        output_cls=questions[question_name]['output_class'],
    )

    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
        node_postprocessors=[
        MetadataReplacementPostProcessor(target_metadata_key="window")],
    )

    question_prompt = f"""
        You are a helpful legal assistant.
        Given the following variable: {question_name}, which is described here: {questions[question_name]['description']}, what is the value of the variable?
    """
    
    response = query_engine.query(question_prompt)
    return response

def run_rag(folder):
    #load index
    stored_index = StorageContext.from_defaults(persist_dir=f"../data/bankruptcy_dockets/output/persist_{folder}")
    retrieved_index = load_index_from_storage(stored_index)

    response_dict = {}
    for question_name,val in questions.items():
        
        response = ask_question(question_name,retrieved_index)

        response_dict[question_name+'_response'] = response
        
        # check if type is string
        if (type(response.val) == str) | (type(response.val) == float):
            response_dict[question_name+'_val'] = response.val
        else:
            response_dict[question_name+'_val'] = response.val.value

        
        response_dict[question_name+'_conf'] = response.confidence.value
        for i,source_node in enumerate(response.source_nodes):
            response_dict[question_name+f'_source_{i}'] = source_node.text
    
    return response_dict

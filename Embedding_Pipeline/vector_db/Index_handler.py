from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
from Embedding_Pipeline.Pinecone_setup import index_name
load_dotenv()

def Index_handler():
        pc = Pinecone(api_key= os.getenv("PINECONE_API_KEY"))
        dimension = 1024  

        if not pc.has_index(index_name):
            pc.create_index(
                name=index_name,
                dimension=dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud='aws',
                    region='us-east-1'  
                )
            )

        
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()


pc = Pinecone(api_key= os.getenv("PINECONE_API_KEY"))
index_name = "krushna-vani"
index = pc.Index(index_name)

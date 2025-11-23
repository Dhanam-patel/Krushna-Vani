from pinecone import Pinecone
from Embedding_Pipeline.Pinecone_setup import index

def Vector_searching(vectors: dict):
    Results = index.query(
        namespace="ns1",
        vector= vectors["values"],
        include_metadata=True,
        top_k=1,
    )
    
    return Results

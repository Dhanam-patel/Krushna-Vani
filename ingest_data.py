from Embedding_Pipeline.Data_Processing.cleaner import clean_data
from Embedding_Pipeline.vector_db.pinecone_vector import Pinecone_vector
from Embedding_Pipeline.vector_db.Index_handler import Index_handler
from Embedding_Pipeline.Pinecone_setup import index

def ingest_data():
    
    Index_handler()
    final = clean_data()

    vectors = Pinecone_vector(final)

    limit = len(vectors)//3
    index.upsert(
            vectors=vectors[:limit],
            namespace="ns1"  
        )
    index.upsert(
            vectors=vectors[limit:limit*2],
            namespace="ns1"  
        )   
    index.upsert(
            vectors=vectors[limit*2:],
            namespace="ns1"  
        )   
    print("Data ingested successfully into Pinecone index.")

ingest_data()
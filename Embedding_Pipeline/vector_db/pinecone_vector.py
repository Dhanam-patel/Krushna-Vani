from Embedding_Pipeline.Embedding.Embedder import get_embeddings
import os
from dotenv import load_dotenv
load_dotenv()


def Pinecone_vector(data: list):
    JINA_API_KEY = os.getenv("JINA_API_KEY")  
    
    dimension = 1024  
    vectors = []
    batch_size = 128

    if len(data) > 1:   
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            texts = [item["Text"] for item in batch]
            embeddings = get_embeddings(texts, dimensions=dimension)
            for j, item in enumerate(batch):
                embedding = embeddings["data"][j]["embedding"]
                vectors.append({
                    "id": item['Chunk_Id'],
                    "values": embedding,
                    "metadata": {'content': item['Text'], 'Book': 'Bhagavad-gita_As_It_Is english'}
                })
                print(f"Processed Chunk_Id: {item['Chunk_Id']}")
    else:
        embeddings = get_embeddings(data, dimensions=dimension)
        embedding = embeddings["data"][0]["embedding"]
        vectors.append({
            "values": embedding,
            # "metadata": {'content': item, 'Book': 'User_Input'}
        })        

    return vectors

    


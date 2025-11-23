# from Embedding_Pipeline.vector_db.pinecone_vector import Pinecone_vector
# from Vector_Search.Search import Vector_searching   



# user_input = ["i am feeling depressed how should i handle it"]
# vector = Pinecone_vector(user_input)

# # print({"response": vector, "type": type(vector)})
# result = Vector_searching(vector[0])
# final = ""
# for data in result.matches:
#     final = f"{final} + {data["metadata"]["content"]}"
# print(final)
# print(type(final))

from ingest_data import ingest_data
from Embedding_Pipeline.vector_db.Index_handler import Index_handler
from Embedding_Pipeline.Pinecone_setup import index_name
Index_handler()
# ingest_data()


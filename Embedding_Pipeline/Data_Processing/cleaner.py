from Embedding_Pipeline.Data_Processing.loader import Book_1
import re
from Embedding_Pipeline.Data_Processing.chunker import Chunking
import json

def clean_data():
    Pages = Book_1.pages
    Book_1_final = []
    Id = 0
    for page in range(0,len(Pages), 1):
        Text = re.sub(r'\s+', ' ', Pages[page].extract_text()).strip()
        Chunks = Chunking(Text, Id)
        Book_1_final.append(Chunks["Chunk1"])
        Id += 1
    print(f"Total Chunks Created: {Id}")
    return Book_1_final




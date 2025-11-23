
def Chunking(Text: str, Id: int):
    Text_1 = Text[:(len(Text)//2)+30]
    Text_2 = Text[(len(Text)//2)-30:]
    chunk_1 = {
        "Chunk_Id": f"Chunk_{Id}",
        "Text": Text_1
    }
    return {"Chunk1": chunk_1}

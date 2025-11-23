from typing import List
import requests


def get_embeddings(
    inputs: List[str],  # List of text or image URLs
    dimensions: 1024,
    task: str = None  # Set to 'retrieval.query' for text retrieval
):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {"jina_b5bd0443f24d45c8aa255a7f1235545dXLeN5UTR0qJkLxfbLYAhtKTG0-nW"}'
    }
    data = {
        'input': inputs,
        'model': 'jina-clip-v2',
        'dimensions': dimensions,
    }

    response = requests.post('https://api.jina.ai/v1/embeddings', headers=headers, json=data)
    return response.json()







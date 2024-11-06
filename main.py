from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from fastapi import FastAPI

app = FastAPI()

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

@app.get("/")
def get_answer():
    response = query_engine.query("Que dice el articulo 5")
    return str(response)
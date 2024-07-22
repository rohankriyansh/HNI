from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex , SimpleDirectoryReader

from IPython.display import Makedown display


document = SimpleDirectoryReader("data").load_data()

index = VectorStoreIndex.from_documents(document)
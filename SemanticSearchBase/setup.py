# setup.py

import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Meilisearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.document_loaders import JSONLoader

load_dotenv()

# exit if missing env vars
if "MEILI_HTTP_ADDR" not in os.environ:
    raise Exception("Missing MEILI_HTTP_ADDR env var")
if "MEILI_MASTER_KEY" not in os.environ:
    raise Exception("Missing MEILI_MASTER_KEY env var")
if "OPENAI_API_KEY" not in os.environ:
    raise Exception("Missing OPENAI_API_KEY env var")

# ... Rest of your setup code ...

# Load documents
loader = JSONLoader(
    file_path="./movies-lite.json",
    jq_schema=".[] | {id: .id, overview: .overview, title: .title}",
    text_content=False,
)
documents = loader.load()
print("Loaded {} documents".format(len(documents)))

# Store documents in Meilisearch
embeddings = OpenAIEmbeddings()
vector_store = Meilisearch.from_documents(documents=documents, embedding=embeddings)

print("Started importing documents")

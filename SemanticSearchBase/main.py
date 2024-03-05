# # main.py

# from dotenv import load_dotenv
# from langchain_community.vectorstores import Meilisearch
# from langchain_openai import OpenAIEmbeddings
# import meilisearch
# import os

# # Load environment variables
# load_dotenv()

# # Check for missing environment variables
# if "MEILI_HTTP_ADDR" not in os.environ:
#     raise Exception("Missing MEILI_HTTP_ADDR env var")
# if "MEILI_MASTER_KEY" not in os.environ:
#     raise Exception("Missing MEILI_MASTER_KEY env var")
# if "OPENAI_API_KEY" not in os.environ:
#     raise Exception("Missing OPENAI_API_KEY env var")

# # Create the vector store
# client = meilisearch.Client(
#     url=os.environ.get("MEILI_HTTP_ADDR"),
#     api_key=os.environ.get("MEILI_MASTER_KEY"),
# )

# # Initialize embeddings and vector store
# embeddings = OpenAIEmbeddings()s
# vector_store = Meilisearch(client=client, embedding=embeddings)

# # Define the main function to perform the search
# def main():
#     # Perform the similarity search
#     query = "superhero fighting evil in a city at night"
#     results = vector_store.similarity_search(
#         query=query,
#         k=3,
#     )

#     # Display results
#     for result in results:
#         print(result.page_content)

# # Run the main function if this script is executed directly
# if __name__ == "__main__":
#     main()

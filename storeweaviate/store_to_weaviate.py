import json
import os
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)  # Used for splitting large texts into manageable chunks.
from langchain_openai import (
    OpenAIEmbeddings,
)  # Interface for generating text embeddings using OpenAI models.
from langchain_community.vectorstores import (
    Weaviate,
)  # Utility for interacting with Weaviate, a vector search engine.
import weaviate  # Python client for Weaviate.

# Environment variables for Weaviate credentials and endpoint.
WEAVIATE_API_KEY = os.environ["WEAVIATE_API_KEY"]
WEAVIATE_URL = os.environ["WEAVIATE_URL"]


def handler(event, context):
    # Extract input text from the event object, assuming it's passed with the key "output_0".
    input = event.get("output_0")

    # Initialize a text splitter to divide input into chunks of 1000 characters with 200 characters overlap.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    # Generate document chunks from the input text.
    documents = text_splitter.create_documents([input])

    # Extract text content from each document object for embedding.
    texts = [doc.page_content for doc in documents]

    # Initialize OpenAI embeddings interface with a specific model for text embedding.
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

    # Generate embeddings for each text chunk.
    vectors = embeddings.embed_documents(texts)

    # Store the generated vectors in Weaviate and return operation status.
    return store_vectors(texts, vectors)


def store_vectors(texts, vectors):
    # Initialize Weaviate client with API credentials.
    client = weaviate.Client(
        url=WEAVIATE_URL,
        auth_client_secret=weaviate.auth.AuthApiKey(api_key=WEAVIATE_API_KEY),
    )

    # Check if the "Article" class exists in the schema, create if not.
    if not client.schema.exists("Article"):
        class_obj = {
            "class": "Article",
            "vectorizer": "none",  # Indicate no automatic vectorization; vectors are provided.
        }
        client.schema.create_class(class_obj)

    # Prepare data mapping between texts and their corresponding vectors.
    mapped_data = [
        {"vector": vector, "text": text} for vector, text in zip(vectors, texts)
    ]

    # Configure batch processing for efficient data import.
    client.batch.configure(batch_size=100)
    with client.batch as batch:
        # Import each text chunk as an "Article" object with its vector.
        for i, d in enumerate(mapped_data):
            properties = {"text": d["text"]}
            batch.add_data_object(properties, "Article", vector=d["vector"])

    # Return a success message upon completing the import process.
    return json.dumps({"output_0": "SUCCESS"})

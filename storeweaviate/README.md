# Triform.ai Template: Text Embedding and Vector Storage

## Overview

This Python module is designed for the Triform.ai platform to facilitate the process of text embedding and vector storage using OpenAI models and Weaviate. It handles large texts by splitting them into manageable chunks, embedding these chunks, and storing the resulting vectors in a vector search engine.

## How it Works

The module processes text input through a series of steps: splitting the text into chunks, generating embeddings for each chunk using OpenAI's text-embedding-3-large model, and storing these embeddings in Weaviate. The Weaviate client is configured with API keys and endpoint URLs provided as environment variables.

## Use Cases

- Enhancing search functionalities by embedding and indexing large volumes of text.
- Creating content-based recommendation systems.
- Supporting NLP tasks that require handling large datasets with vector search capabilities.

## Customization

To adapt this module to different contexts:
- Change the `chunk_size` and `chunk_overlap` in the text splitter to handle different sizes of text input.
- Switch the OpenAI model in the `OpenAIEmbeddings` initialization for different embedding qualities or characteristics.
- Configure different vector storage solutions by modifying the `store_vectors` function to interact with other vector databases.

## Environment Setup

Set the following environment variables in your Triform.ai environment:
- `WEAVIATE_API_KEY`: API key for Weaviate authentication.
- `WEAVIATE_URL`: URL endpoint for your Weaviate instance.
- `OPENAI_API_KEY`: API key for OpenAI authentication.

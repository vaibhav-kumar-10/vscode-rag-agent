# First, make sure you have the chromadb library installed.
# You can install it using pip:
# pip install chromadb

import chromadb

# 1. Initialize the ChromaDB Client
# This creates an in-memory client. The data will be lost when the script ends.
# For persistent storage, you would configure a persistent client.
client = chromadb.Client()

# 2. Create or Get a Collection
# A collection is where your documents, embeddings, and metadata are stored.
# If the collection 'my_documents' already exists, it will be retrieved.
collection = client.get_or_create_collection(name="my_documents")

# 3. Add Documents to the Collection
# We provide a list of IDs, documents (the text itself), and optional metadata.
# ChromaDB will automatically create embeddings for the documents using its
# default embedding function.
documents_to_add = [
    "The weather today is sunny and warm.",
    "The cat is sleeping soundly on the couch.",
    "This is a document about machine learning models.",
    "The sky is clear, and the birds are singing."
]

metadata_to_add = [
    {"source": "weather_report"},
    {"source": "home_life"},
    {"source": "technology"},
    {"source": "weather_report"}
]

ids_to_add = ["id1", "id2", "id3", "id4"]

collection.add(
    documents=documents_to_add,
    metadatas=metadata_to_add,
    ids=ids_to_add
)

print("Documents have been added to the collection.")
print("---")

# 4. Perform a Query
# We can now query the collection with a natural language query.
# The query() method will find the documents that are most semantically similar
# to the query text. We're asking for the top 2 results.
query_text = "What is the weather like?"
results = collection.query(
    query_texts=[query_text],
    n_results=2
)

# 5. Print the Results
# The results are a dictionary containing the IDs, documents, and distances.
print(f"Query: '{query_text}'")
print("\nResults:")
for i in range(len(results['ids'][0])):
    print(f"  Result {i + 1}:")
    print(f"    ID: {results['ids'][0][i]}")
    print(f"    Document: {results['documents'][0][i]}")
    print(f"    Distance (Lower is better): {results['distances'][0][i]}")
    print(f"    Metadata: {results['metadatas'][0][i]}")
    print("---")

# 6. Clean up (optional)
# This removes the collection and all its data.
# client.delete_collection(name="my_documents")

#Test connection from Taxii server and get collection ID 

from taxii2client import Server


collection_id="7f9137a7-59ff-4fc6-957a-a90cc66c91b5"


#define otx taxii server url
server_url = "https://otx.alienvault.com/taxii/"
server = Server(server_url)
#testing connection
print("Connected to TAXII server:", server_url)


api_root =  server.api_roots[0]
print(f"Listing connection for API root :{api_root.url}\n")

collections = api_root.collections

for collection in collections:
    print(f"Collection ID: {collection.id} - {collection.title}")


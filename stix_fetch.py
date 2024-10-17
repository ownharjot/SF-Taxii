#from taxii2client import connect_to_taxii
import keyword
import requests
from taxii2client import Collection
from taxii2client import Server

server_url = "https://otx.alienvault.com/taxii/"
server = Server(server_url)
api_root =  server.api_roots[0]
collection_id="7f9137a7-59ff-4fc6-957a-a90cc66c91b5"





def get_collection(api_root, collection_id):
    for collection in api_root.collections:
        if collection.id==collection.id:
            return collection
            print({collection})
        else: 
            print("not a match")
    return None
    
def get_objects(api_root_url, collection_id):
    headers = {
             "Accept": "application/taxii+json;version=2.1"
    }

    url = f"{api_root_url}/collections/{collection_id}/objects/"

    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        stix_data=response.json()
        return stix_data['objects']
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching STIX objects: {e}")
        return []

def filter_sf_data(stix_objects):
    salesforce_related_objects = []

    keywords = ['Salesforce', 'SFDC', 'salesforce.com']

    for obj in stix_objects:
         if any(keyword in obj.get('description', '') for keyword in keywords) or \
           any(keyword in obj.get('name', '') for keyword in keywords):
              salesforce_related_objects.append(obj)
    
    return salesforce_related_objects 



collection = get_collection(api_root, collection_id)

if collection:
    stix_objects = get_objects(api_root.url, collection_id)
    print(f"Fetched {len(stix_objects)} STIX objects from the collection.")
else:
    print(f"Collection with ID {collection_id} not found.")

salesforce_related_stix=filter_sf_data(stix_objects)

print(f"FOUND {len(salesforce_related_stix)} Salesforce-related STIX Objects")

for obj in salesforce_related_stix:
    print(f"Name: {obj.get('name', 'N/A')}, Description: {obj.get('description', 'No description')}")

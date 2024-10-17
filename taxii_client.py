from taxii2client import Server

server_url = "https://otx.alienvault.com/taxii/"
server = Server(server_url)
api_root = server.api_roots[0]

print("Connected to TAXII server:", server_url)
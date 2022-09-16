from xmlrpc.server import SimpleXMLRPCServer

# Synchrounous RPC casue of waiting...
def add(a, b):
    return a+b

def sort_list(li):
    return sorted(li)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")

server.register_function(sort_list, "sort_list")
server.register_function(add, "add")
server.serve_forever()
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    
    print("sumation of 2 and 3 =", proxy.add(2,4))
    li = [3,6,0,1,8,4,8,57]
    print("listed sorted on RPC - ", proxy.sort_list(li))
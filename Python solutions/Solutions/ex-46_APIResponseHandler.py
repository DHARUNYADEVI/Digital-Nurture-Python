import json
def process_api_response():
    response = '''
    {
        "id":101,
        "name":"Dharunya",
        "email":"dharunyadevi2006@gmail.com"
    }
    '''
    data = json.loads(response)
    print("User ID:", data["id"])
    print("Name:", data["name"])
    print("Email:", data["email"])
process_api_response()
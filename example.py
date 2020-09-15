
from pyjwt import create_jwt
from pyjwt import add_claim
from pyjwt import sign_jwt
from pyjwt import verify_jwt
from pyjwt import extract_jwt
from pyjwt import extract_claim

jwt: dict = create_jwt()
add_claim(jwt, "id", 1)
add_claim(jwt, "username", "John")

print(jwt) 
'''
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 1600427128.483922, 'id': 1, 'username': 'John'}
}
'''

token: str = sign_jwt(jwt)
print(type(token)) # <class 'str'>

print(verify_jwt(token)) # True

id: int = extract_claim(token, "id")
print(id)

jwt_extracted: dict = extract_jwt(token)
print(type(jwt), jwt)
'''
<class 'dict'> 
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 1600427537.49819, 'id': 1, 'username': 'John'}
}
'''
add_claim(jwt_extracted, "exp", 5 * 60 * 1000)
token = sign_jwt(jwt)
jwt_extracted = extract_jwt(token)
print(jwt_extracted)
'''
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 1600427704.153016, 'id': 1, 'username': 'John'}
}
'''



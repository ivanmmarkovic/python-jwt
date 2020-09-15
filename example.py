
from pyjwt import create_jwt
from pyjwt import add_claim
from pyjwt import sign_jwt
from pyjwt import verify_jwt
from pyjwt import extract_jwt
from pyjwt import extract_claim
from pyjwt import add_expiration

jwt: dict = create_jwt()
add_claim(jwt, "id", 1)
add_claim(jwt, "username", "John")

print(jwt) 
'''
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 1600429051.799972, 'id': 1, 'username': 'John'}
}
'''

token: str = sign_jwt(jwt)
print(type(token)) # <class 'str'>

print(verify_jwt(token)) # True

id: int = extract_claim(token, "id")
print(id) # 1

jwt_extracted: dict = extract_jwt(token)
print(type(jwt_extracted), jwt_extracted)
'''
<class 'dict'> 
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 1600429051.799972, 'id': 1, 'username': 'John'}
}
'''
add_claim(jwt_extracted, "id", 2)
add_expiration(jwt_extracted, 5 * 60 * 1000)
token = sign_jwt(jwt_extracted)
jwt_extracted = extract_jwt(token)
print(jwt_extracted)
'''
{
    'header': {'alg': 'HS256', 'typ': 'JWT'}, 
    'payload': {'exp': 300000, 'id': 2, 'username': 'John'}}

'''



# python-jwt
JWT implementation in Python - work in progress

### Create jwt

First create jwt.
Use *create_jwt* function. This function returns dictionary type. Expiration time is set to one hour. You can specify different expiration time in milliseconds.
For example, if you use 

```
jwt: dict = create_jwt()

```

expiration time is set to one hour. Here is set to 30 minutes :

```

jwt: dict = create_jwt(30 * 60 * 1000) # milliseconds

```

Or you can use *add_expiration_time* function to set expiration time:

```

add_expiration_time(jwt: dict, interval_milliseconds: int)

```

To add different claims, for example id or username use *add_claim* function. First argument is jwt returned from *create_jwt* function, second argument is claim and third is value.

```

add_claim(jwt, "id", 12)

```

Function *sign_jwt*, takes jwt and returns string type. That's token.

```

sign_jwt(jwt)

```

You can send this token to user.

### Validation

When performing validation, extract token from user and pass it to *verify_jwt* function. This function return boolean type.

```

verify_jwt(token: str) -> bool

```

### Extracting data from token

To extract data from token use *extract_claim* function. First argument is token, second is claim(must be string type).

```

extract_claim(token: str, claim)

```

### Extract jwt from token

You can extract jwt as a dictionary from token with *extract_jwt_dictionary_from_token* function which takes token as argument. Then you can set expiration time or overwrite other claims.

```

jwt_extracted: dict = extract_jwt(token)
add_claim(jwt_extracted, "id", 2)
add_expiration_time(jwt_extracted, 5 * 60 * 1000)
token = sign_jwt(jwt_extracted)

```

With *sign_jwt* you can obtain token and send it to user. Expiration time will be updated.

### Note

String key which is used for hashing, should be loaded from external file, not like this :

```

key = "E49756B4C8FAB4E48222A3E7F3B97CC3"

```

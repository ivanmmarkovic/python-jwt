# python-jwt
JWT implementation in Python - work in progress

#### Create JWT
- returns dict type
- expiration time is set to 5 minutes, by default

```

jwt: dict = create_jwt()

```

#### Add claims
- id or role for example

```

add_claim(jwt, "id", 12)

```
#### Create token
- returns token

```

token = sign_jwt(jwt)

```
#### Verify token

```

verify_jwt(token: str) -> bool

```

#### Extract claim
- extract id or role, for example

```

extract_claim(token, claim)

```

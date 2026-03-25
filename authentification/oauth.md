# 02 OAuth 2.0 distilled

## Roles
The framework defines four main roles involved in any flow:
- Resource owner
    - The entity granting access to resources, typically a user
- Resource server
    - The entity hosting the protected resources, typically a backend API
- Client
    - The application calling an API with an access token
- Authorization server
    - The entity that authenticates the resource owner and issues access tokens to the client

![Roles](image-5.png)

![The Abstract Flow](image-3.png)

There are two types of access tokens: opaque and structured tokens. Opaque
tokens are random strings with a (relatively) high entropy, and Structured tokens, with a format that is self-contained (JWT)

## client capabilities

Authorization servers should issue tokens only to clients they trust

The authorization server associates a set of client capabilities with a client ID. The client uses this client ID to identify itself at the authorization server, and its client credentials to authenticate (when
applicable)

![the code flow](image-4.png)


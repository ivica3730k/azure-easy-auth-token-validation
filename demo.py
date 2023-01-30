import os
import sys
import jwt
from aadtoken import get_public_key

client_id = os.environ.get('CLIENT_ID', '')
tenant_id = os.environ.get('TENANT_ID', '')

if len(sys.argv) > 1:
    token = sys.argv[1]
else:
    token = os.environ.get('TOKEN', "<your-token-goes-here>")

issuer = f"https://login.microsoftonline.com/{tenant_id}/v2.0"


public_key = get_public_key(token)
decoded = jwt.decode(token,
                     public_key,
                     verify=True,
                     algorithms=['RS256'],
                     audience=[client_id],
                     issuer=issuer
                     )
print(decoded)

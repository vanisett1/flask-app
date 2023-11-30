from flask import request
from config import TENANTS

def check_auth_token():
    token = request.headers.get('Authorization')
    if not token or not token.startswith("Bearer "):
        return False, None

    _, tenant_token = token.split(" ", 1)
    tenant_id, auth_token = tenant_token.split(":", 1)

    # Validate token based on tenant
    expected_token = TENANTS.get(tenant_id)
    return auth_token == expected_token, tenant_id

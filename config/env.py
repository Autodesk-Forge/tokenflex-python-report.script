import os
from urlparse import urljoin
access_token_url = os.getenv(
    'FORGE_TOKEN_URL',
    'https://developer.api.autodesk.com/authentication/v1/gettoken')
base_url = os.getenv('FORGE_BASE_URL', 'https://developer.api.autodesk.com')
base_tokenflex_api = os.getenv(
    'FORGE_TOKENFLEX_URL',
    'https://developer.api.autodesk.com/tokenflex/')
authorize_url = urljoin(
    base_url,
    os.getenv(
        'FORGE_AUTH_PATH',
        '/authentication/v1/authorize'))

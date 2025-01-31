from davidkhala.gcp.auth.options import ServiceAccountInfo
from typing import TypedDict


class AuthOptions(TypedDict):
    clientId: str
    clientEmail: str
    privateKey: str
    privateKeyId: str
    projectId: str


def from_service_account(info: ServiceAccountInfo) -> AuthOptions:
    return AuthOptions(
        clientId=info.get('client_id'),
        clientEmail=info.get('client_email'),
        privateKey=info.get('private_key'),
        privateKeyId=info.get('private_key_id'),
        projectId=info.get('project_id'),
    )

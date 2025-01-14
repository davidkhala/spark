from _typeshed import DataclassInstance
from dataclasses import dataclass, asdict

from davidkhala.spark import SessionDecorator


@dataclass
class AuthOptions(DataclassInstance):
    # TODO migrate to https://github.com/davidkhala/gcp-collections
    clientId: str
    clientEmail: str
    privateKey: str
    privateKeyId: str

    def to_dict(self):
        return asdict(self)

class Session(SessionDecorator):
    projectId: str

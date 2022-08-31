from dataclasses import dataclass


@dataclass(frozen=True)
class Packages:

    name: str
    version: str
    created: str
    description: str
    url: str

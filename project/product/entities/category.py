from project.libs.dataclasses import dataclass


@dataclass
class Category:
    id: int = None
    name: str = None
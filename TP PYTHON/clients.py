from dataclasses import dataclass

@dataclass
class Client:
   
    nom: str
    numero: int
    points_fidelite: int = 0
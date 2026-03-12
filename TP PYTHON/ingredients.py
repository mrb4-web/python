from boissons import Boisson

class DecorateurBoisson(Boisson):
    
    def __init__(self, boisson: Boisson):
        self._boisson = boisson 

class Lait(DecorateurBoisson):
    def cout(self) -> float:
        return self._boisson.cout() + 0.5  

    def description(self) -> str:
        return self._boisson.description() + ", Lait" 

class Sucre(DecorateurBoisson):
    def cout(self) -> float:
        return self._boisson.cout() + 0.2  

    def description(self) -> str:
        return self._boisson.description() + ", Sucre"  

class Caramel(DecorateurBoisson):
    
    def cout(self) -> float:
        return self._boisson.cout() + 0.7

    def description(self) -> str:
        return self._boisson.description() + ", Caramel"
from abc import ABC, abstractmethod

class Boisson(ABC):
    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    # Redéfinition de l'opérateur + pour combiner deux boissons [cite: 125]
    def __add__(self, other: 'Boisson') -> 'Boisson':
        class BoissonCombinee(Boisson):
            def __init__(self, b1: Boisson, b2: Boisson):
                self.b1 = b1
                self.b2 = b2
            
            def cout(self) -> float:
                return self.b1.cout() + self.b2.cout()
            
            def description(self) -> str:
                return self.b1.description() + " + " + self.b2.description()
        
        return BoissonCombinee(self, other)

class Cafe(Boisson):
    def cout(self) -> float:
        return 2.0  # [cite: 58]

    def description(self) -> str:
        return "Cafe simple"  # [cite: 60]

class The(Boisson):
    def cout(self) -> float:
        return 1.5  

    def description(self) -> str:
        return "The" 
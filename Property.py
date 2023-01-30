from abc import ABC, abstractmethod

class Property(ABC):
    """
    General class for inheritance
    """
    def __init__(self, pk, name):
        """
        Getting input from the user and hiding them: 
        __pk => primary key of the property
        __name => name of the property
        """
        self.__pk = pk
        self.__name = name

    # Getters for all of the private members
    def getPrimaryKey(self):
        return self.__pk
    
    def getName(self):
        return self.__name

    @abstractmethod
    def giveReport():
        pass

    @abstractmethod
    def save(self):
        pass

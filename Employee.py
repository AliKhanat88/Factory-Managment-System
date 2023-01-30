from abc import ABC, abstractmethod

class Employee(ABC):
    """
    General class for inheritance
    """
    def __init__(self, pk, name, designation, possession):
        """
        Getting input from the user and hiding them: 
        __pk => primary key of the employee
        __name => name of the emplyee
        __designation => role of the emplyee in factory
        __possesions => Things owned by the employee
        """
        self.__pk = pk
        self.__name = name
        self.__designation = designation
        self.__possessions = possession

    # Getters for all of the private members
    def getPrimaryKey(self):
        return self.__pk
    
    def getName(self):
        return self.__name

    def getDesignation(self):
        return self.__designation

    def getPossessions(self):
        return self.__possessions

    @abstractmethod
    def save(self):
        pass


    @abstractmethod
    def giveReport(self):
        pass
    


class Order:
    def __init__(self, worker, admin, machine, product, toWork, toDo):
        self.__worker = worker
        self.__admin = admin
        self.__machine = machine
        self.__product = product
        self.__toWork = toWork
        self.__toDo = toDo

    def getMachine(self):
        return self.__machine

    def getWorker(self):
        return self.__worker
    
    def getAdmin(self):
        return self.__admin

    def getProduct(self):
        return self.__product

    def getWork(self):
        return self.__toWork

    def getDo(self):
        return self.__toDo


    

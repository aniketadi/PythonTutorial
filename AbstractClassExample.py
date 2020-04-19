from abc import ABC , abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Inside Process")


l = Laptop();
l.process()


nums = [1,23,4,6,4,2,3,4,5,'test','obj', 5.12]
i = iter(nums)

while i.__hash__()-1:
    print(i.__next__())
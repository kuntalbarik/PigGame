from abc import ABC,abstractmethod


class action(ABC):
    @abstractmethod
    def role(self):
        pass
    @abstractmethod
    def hold(self):
        pass

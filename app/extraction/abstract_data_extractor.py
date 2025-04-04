from abc import ABC, abstractmethod

class AbstractDataExtractor(ABC):

  @abstractmethod
  def extract(self,data):
    pass

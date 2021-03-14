from abc import ABC, abstractmethod
from Canvas import Canvas


class GeometryObject(ABC):

    def __init__(self, geoType, penStyle):
        self.canvas = Canvas.getInstance()
        self.type = geoType
        self.penStyle = penStyle

    @abstractmethod
    def drawToCanvas(self):
        pass

    @abstractmethod
    def checkGeometryObjectConstraints(self):
        pass
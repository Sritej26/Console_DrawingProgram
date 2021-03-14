from Canvas import Canvas
from GeometryType.Line import Line
from GeometryType.Rectangle import Rectangle
from GeometryType.BucketFill import BucketFill
from InputParameterValidation import parseInputArg, validateInputString, validateInputArgv


def main(argv):
    geometryObj = None
    geoType = argv[0].upper()
    if geoType == 'C':
        Canvas(argv[1], argv[2])
    elif geoType == 'L':
        geometryObj = Line(argv[1], argv[2], argv[3], argv[4])
    elif geoType == 'R':
        geometryObj = Rectangle(argv[1], argv[2], argv[3], argv[4])
    elif geoType == 'B':
        geometryObj = BucketFill(argv[1], argv[2], argv[3])
    elif geoType == 'Q':
        return False
    else:
        print('Geometry type not recognized')
        return True

    canvas = Canvas.getInstance()
    if not canvas:
        print('Need to initiate Canvas for this command')
        return True

    if geometryObj and geometryObj.checkGeometryObjectConstraints():
            canvas.addToCanvas(geometryObj)

    canvas.printc()
    return True


if __name__ == '__main__':
    
    notQuit = True
    
    while notQuit:
        command = input('Enter command: ')

        if not validateInputString(command):
            continue

        argv = parseInputArg(command.split())
        if not argv:
            continue

        if not validateInputArgv(argv):
            continue

        notQuit = main(argv)

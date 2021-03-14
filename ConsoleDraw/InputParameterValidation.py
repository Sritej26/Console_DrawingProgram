def parseInputArg(inputArg):
    argv = [inputArg[0]]

    if inputArg[0].upper() == 'B':
        for i in inputArg[1:-1]:
            try:
                argv.append(int(i))
            except:
                print('Input parameter must be numeric')
                return []
        argv.append(inputArg[-1])
    else:
        for i in inputArg[1:]:
            try:
                argv.append(int(i))
            except:
                print('Input parameter must be numeric')
                return []
    return argv

def validateInputString(command):
    inputArg = command.split()

    if not inputArg or (len(inputArg[0]) > 1) or (not inputArg[0].isalpha()):
        print('format of Command is wrong')
        return False

    return True

def validateInputArgv(inputArg):
    type = inputArg[0].upper()

    if type == 'Q':
        numInputArgs = 0
    elif type == 'C':
        numInputArgs = 2
    elif type == 'L':
        numInputArgs = 4
    elif type == 'R':
        numInputArgs = 4
    elif type == 'B':
        numInputArgs = 3
    else:
        print('Command must start with either C , B , L , R or Q')
        return False

    if len(inputArg[1:]) != numInputArgs:
        print('Wrong number of input arguments for {} command'.format(type))
        return False

    return True

def getInputData(file):
    path = "days/data/" + file
    f = open(path, "r")
    input_array = f.read().splitlines()
    return input_array
def getInputData(file):
    if file == "eight" or file == "eight_test":
        path = "days/data/{}".format(file)
        f = open(path, "r")
        array = f.read().splitlines()
        input_array=[]
        input_array.append(array[0])
        input_array.append([])
        for entry in array[2:None]:
            input_array[1].append(entry)
        return input_array
    
    if file == "seven" or file == "seven_test":
        path = "days/data/{}".format(file)
        f = open(path, "r")
        array = f.read().splitlines()
        input_array=[]
        for entry in array:
            x = entry.split()
            input_array.append((x[0], int(x[1])))
        return input_array
    else:    
        path = "days/data/" + file
        f = open(path, "r")
        input_array = f.read().splitlines()
        return input_array
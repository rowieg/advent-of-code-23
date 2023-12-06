import re

data_store = []

special_char='[@_!$%^&*()<>?/\|}{~:]#+=-'
test = "*@-+#%=/$&"

def get_numbers(array):
    for index, line in enumerate(array):
        numbers_in_line = re.findall('\d+', line)
        for number in numbers_in_line:
            pattern = re.compile("(\D|^)"+number+"(\D|$)")
            r = pattern.search(line)
            if r:
                lower_index = 0
                upper_index = 0

                group = r.group()
                if group[0].isdigit():
                    lower_index = r.start()
                else:
                    lower_index = r.start() + 1

                if group[-1].isdigit():
                    upper_index = r.end() - 1
                else:
                    upper_index = r.end() -2

                check_for_symbol(number, lower_index, upper_index, index, array)
    return sum_data()

def check_for_symbol(number, x1, x2, y, array):
    start_x = x1 - 1 if x1 > 0 else 0
    end_x = x2 + 1 if x2 < len(array[y])-1 else x2
    start_y = y - 1 if y > 0 else 0
    end_y = y + 1 if y < len(array)-1 else y

    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if array[y][x] in special_char:
                data_store.append(number)
                return        

def sum_data():
    sum = 0
    for data in data_store:
        sum = sum + int(data)
    print(sum)
    return sum

def get_gears(array):
    gears = []
    for index, line in enumerate(array):
        pattern = re.compile("\*")
        r = pattern.search(line)
        if r:
            gears.append((r.start(), index))
    return gears

def get_gear_ratio(data, gears):
    for gear in gears:
        x = gear[0]
        y = gear[1]
        x_start = x - 1 if x > 0 else 0
        x_end = x + 1 if x < len(data[y])-1 else x
        y_start = y - 1 if y > 0 else 0
        y_end = y + 1 if y < len(data)-1 else y
        #print("Search for gears in :", "(", x_start, y_start, ")", " - ", "(", x_end, y_end, ")")
        for y in range(y_start, y_end+1):
            for x in range(x_start, x_end+1):
                if data[y][x].isdigit():
                    #print("Found digit at: ",data[y][x])
                    return data[y][x]
                    

def run(data_input):
    print("Day three puzzle a is:")
    get_numbers(data_input)

    print("Day three puzzle b is:")
    get_gears(data_input)
    

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
                #print(r.start())
                #print(r.end()-1)

                #lower_index = line.find(number)
                #upper_index = lower_index + len(number) -1
                lower_index = 0
                upper_index = 0

                group = r.group()
                print(group)
                if group[0].isdigit():
                    lower_index = r.start()
                else:
                    lower_index = r.start() + 1

                if group[-1].isdigit():
                    upper_index = r.end() - 1
                else:
                    upper_index = r.end() -2

                #print(index, number, numbers_in_line, lower_index, upper_index)
                check_for_symbol(number, lower_index, upper_index, index, array)
    return sum_data()

def check_for_symbol(number, x1, x2, y, array):
    start_x = x1 - 1 if x1 > 0 else 0
    end_x = x2 + 1 if x2 < len(array[y])-1 else x2
    start_y = y - 1 if y > 0 else 0
    end_y = y + 1 if y < len(array)-1 else y

    print("Check Symb for: ", start_x, end_x, start_y, end_y, " - ", number)

    for y in range(start_y, end_y+1):
        for x in range(start_x, end_x+1):
            if array[y][x] in special_char:
                #print("Special in ", array[y][x])
                data_store.append(number)
                print("Found with: ", number)
                return        

def sum_data():
    print("Summ up!")
    sum = 0
    for data in data_store:
        sum = sum + int(data)
    print("sum: ", sum)
    return sum

def run(data_input):
    print("Day three puzzle 1a is:")

    get_numbers(data_input)
    

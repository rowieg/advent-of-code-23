from days import one, two, three, six
from utils import input

data_input_one = input.getInputData("one")
data_input_two = input.getInputData("two")
data_input_three = input.getInputData("three")

one.run(data_input_one)
two.run(data_input_two)
three.run(data_input_three)
six.run()
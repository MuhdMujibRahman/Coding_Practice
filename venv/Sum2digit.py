

class sumDigit:
    def  __init__(self):
        self.digits = []

    def get_value_of_digit(self,digit):
        self.digits.append(digit)

    def sum_value(self,list_of_digit):
        return sum(list_of_digit)

class getInput:
    def  __init__(self):
        self.input_value = input("Enter a number: ")
        self.list_of_digits = []

    def getValue(self):
        return self.__turn_into_init()

    def __turn_into_init(self):
        return [int(x) for x in self.input_value.split(' ') if x is not None]


# sumDigit = sumDigit()
# sumDigit.sum_value(getInput().getValue())

#
def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    sumDigit = sumDigit()
    val = sumDigit.sum_value(getInput().getValue())
    print(val)
    # a, b = map(int, input().split())
    # print(sum_of_two_digits(a, b))


# print(str()))


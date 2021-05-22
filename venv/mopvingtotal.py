class MovingTotal:
    def __init__(self):
        self.list_of_number = []

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        if len(numbers) > 1:
            self.list_of_number.append(sum(numbers))
        else:
            count = 0
            num = []
            num.append(numbers[0])
            n = numbers[0]
            while count != 2:
                n-=1
                num.append(n)
                count += 1

            self.list_of_number.append(sum(num))

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        if total in self.list_of_number:
            return True
        else:
            return False


if __name__ == "__main__":
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))
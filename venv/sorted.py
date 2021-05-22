import math
def count_numbers(sorted_list, less_than):
    count = 0
    if len(sorted_list)%2 == 0:
        mid = int((len(sorted_list)/2)-1)
    else:
        mid = int(len(sorted_list)/2)

    if sorted_list[mid]<less_than:
        count = len(sorted_list[:mid+1])
        for i in sorted_list[mid+1:]:
            if i < less_than:
                count = len(sorted_list[:sorted_list.index(i)+1])
            else:
                break
        return count
    else:
        return 0

if __name__ == "__main__":
    sorted_list = [1,2,3,3,7]
    print(count_numbers(sorted_list, 4)) # should print 2
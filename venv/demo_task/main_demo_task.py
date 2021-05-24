import sys
import os

n = int(sys.argv[1])
inner = int(sys.argv[2])
outer = int(sys.argv[3])

test = int(sys.argv[4])

# n = int(input())
# inner = int(input())
# outer = int(input())
#
# test = int(input())
# test = int(input())
# #
# n = int(input())
for i in range(test):
    print("Test_#" + str(i))

    os.system("python3 demo_taks_generator.py " + str(n) + " " + str(inner) +" "+ str(outer) + " " + str(i)+ " > demo_input.txt")

    os.system("python3 demo_task2.py < demo_input.txt > model_demo.txt")
    os.system("python3 demo_task_.py < demo_input.txt > main_demo.txt")

    with open('model_demo.txt') as f:
        model = f.read()
    print("Model: ", model)

    with open('main_demo.txt') as f:
        main = f.read()
    print("Main: ", main)
    if model != main:
        break
import random
import os
import sys

test = int(sys.argv[1])

n = int(sys.argv[2])
# test = int(input())
# #
# n = int(input())
for i in range(test):
    print("Test_#"+str(i))

    os.system("python3 Gen.py "+str(n)+" "+str(i)+" > input.txt")

    os.system("python3 modelPairWise.py < input.txt > model.txt")
    os.system("python3 mainPairWise.py < input.txt > main.txt")

    with open('model.txt') as f : model = f.read()
    print("Model: ",model)
    
    with open('main.txt') as f : main = f.read()
    print("Main: ",main)
    if model != main:
        break
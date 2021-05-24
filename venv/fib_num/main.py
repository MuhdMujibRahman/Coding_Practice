import sys
import os

n = int(sys.argv[1])

print("Test_#" + str(1))


os.system("python3 modelMethod.py "+str(n)+" > model.txt")
os.system("python3 mainMethod.py "+str(n)+" > main.txt")

with open('model.txt') as f:
    model = f.read()
print("Model: ", model)

with open('main.txt') as f:
    main = f.read()
print("Main: ", main)

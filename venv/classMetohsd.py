class A_Dog:
    def __init__(self,robotic_part:str):
        self.fur = 'short'
        self.legs = '4'
        self.additional_Parts = robotic_part

    def toPrint(self):
        print(self.fur,self.legs)
        self._privatePart()

    def _privatePart(self):
        print('cock')


callDog = A_Dog('robot_legs')
callDog.toPritn()

try:
    nothing = None
    nothing.lower()
except Exception as e:
    print(e)

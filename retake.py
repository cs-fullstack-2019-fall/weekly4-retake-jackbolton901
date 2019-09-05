# problem1
# name = input("what is your name? ")
# age = input("what is your age? ")
# print(f'{name} is {age} years old')

# Problem2
# realAge = int(input("Enter age "))
# if realAge < 1 or realAge > 125:
#     print("Not real age!!!")
# else:
#     print("Real age")

# Problem3

# for x in range(-50, 50, 4):
#     print(x)

# problem4

useNum= int(input("enter a number or 0 to quit adding"))
while useNum != 0:
    useNum = int(input("press 0 to quit adding"))
    sumNum = useNum

print(sumNum)

# problem 5

arr= ["Kobe", "Michael", "Nash", "Conley"]
print(f'{arr[0]}, {arr[1]}, {arr[2]}, {arr[3]}')

problem 6
def cal(num1,num2,num3):
    print(num1 + num2)
    prod = num2 * num3
    return prod

cal(2,5,10)

# problem 7

class Boardgame:
    def __init__(self, name, price, piececount, publisher):
        self.name = name
        self.price= price
        self.piece = piececount
        self.pub = publisher

    def priceChange(self):
        newPrice = input("change the price ")
        self.price = newPrice



candy = Boardgame("CandyLand", "$15", "4", "Mr. Cane")
mono = Boardgame("Monopoly", "$17", "6", "That Guy")
sor = Boardgame("uno", "$7", "6", "Somebody")
print(candy)


# Problem 8

def strArr(arr):


# problem 9

def pos(array):
    for x in array:
        if x > 0:
            print(x)


arr1 = [-1, 9, 5, -3]
pos(arr1)


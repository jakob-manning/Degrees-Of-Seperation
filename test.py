x = 3

print("hello world!")
print(x) 
print(type(x))
y = 1+ 1 * 256
z = y // 3
b = 2**0.5
myBoolean = True
myFakeBoolean = "True"
result = myBoolean != 1
myRange = 1 < 2 > 3
a = [1, 2, 3]
b = [1, 2, 3]
value = a == b
pointer = a is b
sentence = "my" " first" " sentence"
test = None is None
comment = "yay" if 1<0 else "Nay"
myFirstList = [1, 2, 3, 4, 5]
check = 1 in myFirstList
length = len(myFirstList)
popped = myFirstList.pop()
remainingList = myFirstList
a, b, c, d, e = myFirstList


tuplesArePermenantLists = (1, 2, 3)
element = tuplesArePermenantLists[-1]
length = len(tuplesArePermenantLists)

filled_dict = {"one": 1, "two": 2, "three": 3}
el = filled_dict["one"]
el = "seven" in filled_dict
el = list(filled_dict.keys())

var = 10
if var < 10:
    a = 4
elif var > 10:
    a = 3
else:
    a = 10

for animal in ["dog", "cat", "mouse"]:
    print("{} is an animal".format(animal))

for i in range(4):
    print(i)

for i in range(4,8):
    print(i)

try:
    raise IndexError("Out of indes")
except IndexError as e:
    pass

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(5)

ans = (lambda x: x > 2)(3)

number = 5

number =" hello world"


myDict = {"Jakob": 28, "Lewis": 28, "Marty": 29}
stringForm = str(myDict)


def solution(x, y):
    unique_X = set(x)
    unique_Y = set(y)
    x_venn = unique_X - unique_Y
    if len(x_venn) > 0:
        return x_venn
    Y_venn = unique_Y - unique_X
    return Y_venn

solution([13, 5, 6, 2, 5], [5, 2, 5, 13])

solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])

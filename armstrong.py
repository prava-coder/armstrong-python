#python program to check the armstong number

number=int(input("enter a number:"))
result=0
n=len(str(number))
temp=number

while (temp!=0):
    digit = temp % 10
    result = result + digit ** n
    temp = temp // 10


if number == result:
    print(number, "is an armstrong number")
else:
    print(number,"is not an armstrong number")
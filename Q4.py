#Ques4
num = int(input("Enter a number:"))
sum = 0
while num != 0:
    sum = sum + (num % 10)
    num = num//10
print(sum)
if sum%3==0:
    print("Divisble")
else:
    print("Not Divisble")
    
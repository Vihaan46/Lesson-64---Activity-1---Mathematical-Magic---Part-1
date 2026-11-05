num = int(input("Input your number: "))
digits = len(str(num))

resultnumber = 0

temp = num
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digits
    temp //= 10

if num == resultnumber:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
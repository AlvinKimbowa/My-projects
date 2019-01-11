#def cube(num):
#    return num*num*num

#print(cube(3))

def power(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

print(power(float(input("Enter a number: ")), int(input("Enter the power: "))))

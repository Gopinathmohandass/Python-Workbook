str="hello all, today is {0}"
print(str.format("Monday"))

str1="I am {1}, and My age is {0}"
print(str1.format(43,"Gopi"))

str2="The sum of {0} and {1} is {2:f}".format(5,6,5*6)
print(str2)

n1 = "Hello"
n2 = "how"
n3 = "are you"

print("3 digit decimal rounding of pi is {0:.3f}".format(3.14596))
print("123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||".format(n1,n2,n3))
print("Hex value of the given number {0} is {0:X}".format(1234))

layout = "{0:<4}{1:<6}{2:<8}{3:>12}"
print(layout.format("i","i**2","i**3","i**4"))
for i in range(1,5):
    print(layout.format(i,i**2,i**3,i**4))
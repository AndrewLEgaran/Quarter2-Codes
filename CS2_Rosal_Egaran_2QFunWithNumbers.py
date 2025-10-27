age = int(input("Hi there! Please enter your age: "))
total = 0
for facade in range(1, age + 1):
     total += facade
print(f"The sum of all numbers from 1 to", age, "is:", total)
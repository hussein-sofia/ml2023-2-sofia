n = int(input("Enter the size of the array: "))
numbers = []

for i in range(n):
    numbers.append(int(input("Enter a number to add to the array: ")))

numberToSearch=int(input(f"Enter the integer to be searched: "))

if numberToSearch in numbers:
    index = numbers.index(numberToSearch)+1
    print(f"The first occurence of number {numberToSearch} is at index {index}")
else:
    print("-1")

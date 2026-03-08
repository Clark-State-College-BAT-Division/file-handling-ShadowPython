#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:



#in case the file is called somthing else
file_path = input("Name of the file path:")

with open(file_path, "r") as t:
    count = [int(x) for x in t.read().split()]

total = sum(count)

advrage = total / len(count)

highest = max(count)
lowest = min(count)

print(f"There are {len(count)} numbers in the file")
print(f"The total of all the numbers is {total}")
print(f"the adverage is {advrage}")
print(f"The highest number is {highest}")
print(f"The lowest number is {lowest}")


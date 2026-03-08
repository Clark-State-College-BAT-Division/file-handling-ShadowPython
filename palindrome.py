#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 



file_path = input("File Path:")


with open(file_path, "r") as t:
    list_of_words = t.read().lower().split()


count = 0

for x in list_of_words:
   if x[::-1] == x:
    count += 1



print(f"The Number of palindromes is {count}")

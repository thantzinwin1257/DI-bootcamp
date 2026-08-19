# Challenge: 1
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multiples_list = []

for count in range(1, length + 1):
    answer = number * count
    
    multiples_list.append(answer)

print(multiples_list)

# Challenge:2

user_word = input("Enter a word: ")

clean_word = ""

previous_letter = ""

for letter in user_word:
    
    if letter != previous_letter:
       
        clean_word = clean_word + letter
        
    previous_letter = letter

print(clean_word)

MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 
# Step 1
matrix = [list(line) for line in MATRIX_STR.strip().split('\n') if line]

num_rows = len(matrix)
num_cols = len(matrix[0])

# Step 2
raw_column_chars = []

for col in range(num_cols):
    for row in range(num_rows):    
        raw_column_chars.append(matrix[row][col])

# Step 3
temporary_string = []

for char in raw_column_chars:
    if char.isalpha():
        temporary_string.append(char)
    else:
        temporary_string.append(char)

# Step 4
decoded_message = ""
in_symbol_block = False

for i in range(len(temporary_string)):
    current_char = temporary_string[i]
    
    if current_char.isalpha():       
        if in_symbol_block:

            decoded_message += " "
            in_symbol_block = False
        decoded_message += current_char

    else:       
        has_alpha_ahead = False
        for j in range(i, len(temporary_string)):
            if temporary_string[j].isalpha():

                has_alpha_ahead = True
                break

        if has_alpha_ahead and len(decoded_message) > 0:
            in_symbol_block = True
        else:
            if in_symbol_block:
                decoded_message += " "
                in_symbol_block = False
            decoded_message += current_char

# Step
print(decoded_message)

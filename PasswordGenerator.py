import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
loop_range=nr_letters+nr_symbols+nr_numbers
random_range_letter=len(letters)
random_range_num=len(numbers)
random_range_sym=len(symbols)
# res=""
# for i in range(0,loop_range,3):
#     letter_id=random.randint(0,random_range_letter-1)
#     # res+=letters[letter_id]
#     res+=random.choice(letters)
#     num_id=random.randint(0,random_range_num-1)
#     res+=numbers[num_id]
#     sym_id=random.randint(0,random_range_sym-1)
    
#     res+=symbols[sym_id]
# print(res)
res=[]
for i in range(0,loop_range,3):
    res.append(random.choice(letters))
    res.append(random.choice(numbers))
    res.append(random.choice(symbols))
random.shuffle(res)
password=""
for i in res:
    password+=i
print(password)



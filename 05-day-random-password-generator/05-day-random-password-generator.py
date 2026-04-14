
# # --------------------------------------------------------

# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
#            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print('Welcome to the PyPassword Generator!')
# nr_letters = int(input('How many letters would you like in your password?\n'))
# nr_symbols = int(input(f'How many symbols would you like?\n'))
# nr_numbers = int(input(f'How many numbers would you like?\n'))

# # --------------------------------------------------------

# #  Easy-level
# password = ''
# letters_chosen = []
# while len(letters_chosen) < nr_letters:
#     random_letter = random.choice(letters)
#     if random_letter not in letters_chosen:
#         letters_chosen.append(random_letter)
#         password += random_letter
#
#
# numbers_chosen = []
# while len(numbers_chosen) < nr_numbers:
#     random_number = random.choice(numbers)
#     if random_number not in numbers_chosen:
#         numbers_chosen.append(random_number)
#         password += random_number
#
#
# symbols_chosen = []
# while len(symbols_chosen) < nr_symbols:
#     random_symbol = random.choice(symbols)
#     if random_symbol not in symbols_chosen:
#         symbols_chosen.append(random_symbol)
#         password += random_symbol
#
#
# print(password)

# # --------------------------------------------------------

# # Intermediate-level
# passkey_list = []
#
# letters_chosen = []
# while len(letters_chosen) < nr_letters:
#     random_letter = random.choice(letters)
#     if random_letter not in letters_chosen:
#         letters_chosen.append(random_letter)
#         passkey_list += random_letter
#
# numbers_chosen = []
# while len(numbers_chosen) < nr_numbers:
#     random_number = random.choice(numbers)
#     if random_number not in numbers_chosen:
#         numbers_chosen.append(random_number)
#         passkey_list.append(random_number)
#
# symbols_chosen = []
# while len(symbols_chosen) < nr_symbols:
#     random_symbol = random.choice(symbols)
#     if random_symbol not in symbols_chosen:
#         symbols_chosen.append(random_symbol)
#         passkey_list.append(random_symbol)
#
# random.shuffle(passkey_list) # with effect
#
# password = ''
# for char_p in passkey_list:
#     password += char_p
#
# print(f'Your password is: {password}')
#
# # --------------------------------------------------------

# Hard-level using 'secrets' and 'string' modules
import secrets
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like?\n'))
nr_numbers = int(input(f'How many numbers would you like?\n'))

password_chars = (
    [secrets.choice(letters) for _ in range(nr_letters)] +
    [secrets.choice(numbers) for _ in range(nr_numbers)] +
    [secrets.choice(symbols) for _ in range(nr_symbols)]
)

secrets.SystemRandom().shuffle(password_chars)

generated_password = ''.join(password_chars)

print(f'Your password is: {generated_password}')

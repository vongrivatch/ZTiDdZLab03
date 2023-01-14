import string
import random

# wszystkie znaki są przechowywane w liście
pass_lowercase = list(string.ascii_lowercase)
pass_uppercase = list(string.ascii_uppercase)
pass_digits = list(string.digits)
pass_punctuation = list(string.punctuation)

# generator wybiera dowolną liczbę z przedziału, by określić długość hasła
length_range = list(range(8, 25))
password_length = random.choice(length_range)

# mieszanie znaków przechowywanych w listach
random.shuffle(pass_lowercase)
random.shuffle(pass_uppercase)
random.shuffle(pass_digits)
random.shuffle(pass_punctuation)

# obliczenie 30% i 20% liczby znaków w haśle
part1 = round(password_length * (30 / 100))
part2 = round(password_length * (20 / 100))

# generowanie hasła - 60% to litery a 40% znaki i liczby
shuffled_chars = []

for x in range(part1):
	shuffled_chars.append(pass_lowercase[x])
	shuffled_chars.append(pass_uppercase[x])

for x in range(part2):
	shuffled_chars.append(pass_digits[x])
	shuffled_chars.append(pass_punctuation[x])

# wynik pomieszania znaków przechowywanych w listach
random.shuffle(shuffled_chars)

# tworzenie hasła z pomieszanych znaków
password = "".join(shuffled_chars)
print("Twoje silne hasło to: ", password)
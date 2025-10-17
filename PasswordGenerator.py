import string
import random

while True:
    user_input = input("How many characters do you want in your passcode?\nMinimum 8 characters: ")

    try:
        char_num = int(user_input)
        if char_num < 8:
            print("Passcode is too short. Needs to be at least 8 characters.")
        else:
            break
    except ValueError:
        print("Use a numeric value only.")
        user_input = input("How many characters do you want in your passcode? ")

app = input("What is the password for: ")

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

part1 = round(char_num * (30/100))
part2 = round(char_num * (20/100))
result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):

    result.append(s3[x])
    result.append(s4[x])
random.shuffle(result)

password = "".join(result)
print(f"{app}: {password}")
with open("passwords.txt", "a") as file:
    file.write(f"{app}: {password}\n")

print("Password saved to passwords.txt ✅")
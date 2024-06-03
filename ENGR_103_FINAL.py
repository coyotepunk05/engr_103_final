# import dictionary, common password
import random
import string

# Make List of Spec Char ASCII Codes
Spec_ASCII = []

for l in [range(33,48) , range(58,65) , range(91,97), range(123,127)]:
    for n in l:
        Spec_ASCII.append(n)

# make list for fault analysis
fault = {"number":0,"upper":0,"lower":0}

#List of Tuples (Incl. Left, Excl. Right)
numberFaultIndices = []
upperFaultIndices = []
lowerFaultIndices = []

# define commands
def generate(pw=""):

    # Generate Random Password If none provided
    if pw == "":
        return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = random.randint(19,30)))
    
    newstring = list(pw)
    #fix consecutive numbers
    if fault["number"] == 1:
        
        for tup in numberFaultIndices:
            # Excl Endpoints of each Block
            for i in range(tup[0]+1,tup[1]-1):
                if random.choice([True,False]):
                    newstring[i] = random.choice(string.ascii_letters + string.punctuation)

    #fix consecutive upper letters
    if fault["upper"] == 1:
        pass
        
    #fix consecutive lower letters
    if fault["lower"] == 1:
        pass
    #fix length
    
    return "".join(newstring)


# function to check list of commonly used passwords
file_path = "password_list_1000000"
def check_password_list(password):
    file_path = "engr_103/engr_103_final/password_list_1000000.txt"
    file = open(file_path, "r") 
    for line in file:
        if password in line:
            return True
    return False


# function to convert certain special characters to their associated letters
def convert_password(password):
    target_chars = {
        '@': 'a',
        '$': 's',
        '0': 'o'
    }

    converted_password = ""
    for char in password:
        if char in target_chars:
            converted_password += target_chars[char]
        else:
            converted_password += char

    return converted_password


def analyze(string):
    
    rating = 0

    # Counts # of Characters (Assuming 1 pt per)
    rating += len(string)

    # Count # of Numbers (Assuming 1 pt per)
    for c in string:
        if ord(c) < 58 and ord(c) > 47:
            rating += 1
    
    # Count Spec. Char (Assuming 1 pt per)
    for c in string:
        if ord(c) in Spec_ASCII:
            rating += 1

    # Count Upper cases (Assuming 1 pt per)
    for c in string:
        if ord(c) in range(65,91):
            rating += 1
    
    # Count Little Letters (Assuming 1 pt per)
    for c in string:
        if ord(c) in range(97,123):
            rating += 1
    
    # Substring Analysis to Count Certain Consecutive Characters (Sliding Window Technique) (min ASCII Code, max ASCII Code, min str length of consec char to deduct pts)
    # Returns a Negative Value to be Added to Rating, and list of tuples of Indices that contain said substrings (Incl. Left, Excl. Right)
    def substringConsec(m,n,minL):
        l = 0
        r = 0
        L = []
        subtract = 0
        while r != len(string):
            if not (ord(string[r]) < n and ord(string[r]) > m):
                r += 1
            else:
                l = r
                while (ord(string[r]) < n and ord(string[r]) > m):
                    r += 1
                    if r == len(string):
                        break
                if r - l >= minL:
                    subtract -= r - l
                    L.append((l,r))
                l = r

        return subtract, L

    # Count Consecutive Numbers
    global numberFaultIndices
    tmp, numberFaultIndices = substringConsec(47,58,4)
    print(numberFaultIndices)
    if tmp < 0:
        fault["number"] = 1
    rating += tmp

    # Count Consecutive Upper Letters
    tmp, upperFaultIndices = substringConsec(65,91,7)
    if tmp < 0:
        fault["upper"] = 1
    rating += tmp

    # Count Consecutive Lower Letters
    tmp, lowerFaultIndices = substringConsec(97,123,7)
    if tmp < 0:
        fault["lower"] = 1
    rating += tmp

    return rating


# take password input
while True:

    password = input("Input Password: ")

    # password aquisition

    if password == "":
        print(generate())
        quit()

    if not all(ord(c) < 128 for c in password):
        print("Please Input ASCII Characters!")
    elif check_password_list(password.lower()) or check_password_list(convert_password(password.lower())):
        print("This is a commonly used password. Please choose a new password.")
    else:
        break


# New Variable to Improve Runtime Efficiency
score = analyze(password)

print(f'Password Strength: {score}')

# tell user password strength and prompt for generation

req = {5:"Very Weak",12:"Weak",15:"Moderate",25:"Strong",99999:"Very Strong"}

for number in req:
    if score <= number:
        print(f'Password Rating: {req[number]}')
        strength = req[number]
        break

if strength == "Very Weak" or strength == "Weak" or strength == "Moderate":
    while True:
        yn = input("Would you like to automatically increase your password's strength? (yes/no): ").lower()
        if yn == "yes":
            print(generate(password))
            break
        elif yn == "no":
            break
        else:
            print("Enter 'yes' or 'no'.")
            continue


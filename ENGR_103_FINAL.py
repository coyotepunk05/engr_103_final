# import dictionary, common password

# Make List of Spec Char ASCII Codes
Spec_ASCII = []

for l in [range(33,48) , range(58,65) , range(91,97), range(123,127)]:
    for n in l:
        Spec_ASCII.append(n)

# define commands
def generate():
    pass

file_path = "password_list_1000000"

def check_password_list(password):
    file_path = "/engr_103/engr_103_final/password_list_1000000.txt"
    file = open(file_path, "r")
    for line in file:
        if password in line:
            return True
    return False


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
    def substringConsec(m,n,minL):
        l = 0
        r = 0
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
                l = r

        return subtract

    # Count Consecutive Numbers
    rating += substringConsec(47,58,4)

    # Count Consecutive Upper Letters
    rating += substringConsec(65,91,7)

    # Count Consecutive Lower Letters
    rating += substringConsec(97,123,7)

    

    return rating


# take password input
while True:

    password = input("Input Password: ")

    # password aquisition

    if password == "":
        generate()
        quit()

    if not all(ord(c) < 128 for c in password):
        print("Please Input ASCII Characters!")
    else:
        break


if not check_password_list(password):
    print(analyze(password))
else:
    print("in most common password")





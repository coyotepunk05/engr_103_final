# import dictionary, common password

Spec_ASCII = range(33,48) + range(58,65) + range(91,97) + range(123,127)

# define commands
def generate():
    return

def analyze(string):
    
    rating = 0

    # Counts # of Characters (Assuming 1 pt per)
    rating += len(string)

    # Count $ of Numbers (Assuming 1 pt per)
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

    

    return rating

# take password input
while True:

    password = input("Input Password: ")

    # password aquisition

    if password == "":
        generate()
        quit()

    if all(ord(c) < 128 for c in password):
        print("Please Input ASCII Characters!")
    else:
        break


print(analyze(password))







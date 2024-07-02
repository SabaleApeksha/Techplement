import datetime

def gen_ran_password(length):
    # Define the characters to use in the password
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    spc_symbol = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    # Combine all characters
    characters = letters + digits + spc_symbol
    char_length = len(characters)

    # Get the current time in microseconds for maintaining randomness every time
    now = datetime.datetime.now()
    microseconds = now.microsecond
    
    # Derive random numbers from the current time
    multiplier = (microseconds % 10) + 1  # Ensure it's between 1 and 10
    increment = (microseconds // 1000 % 10) + 1  # Ensure it's between 1 and 10
    
    password = ''
    
    # Random generation based on manual iteration
    for i in range(length):
        # Use the derived numbers to pick a character
        index = (i * multiplier + increment) % char_length
        password += characters[index]
    
    return password

# Get the desired password length from the user
password_length = int(input("Enter the length for the password: "))

# Generate and print the random password
password = gen_ran_password(password_length)
print(f"The Generated password is: {password}")
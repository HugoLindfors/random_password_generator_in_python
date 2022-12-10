import random, string, keyboard

while True:
    no_of_passwords = int(input('How many passwords do you want? '))
    char_count = int(input('How many characters do you want? '))
    print('\n')

    def generate_random_password(length):
        letters = string.ascii_letters + string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        print(result_str)
        
    for i in range(no_of_passwords):
        generate_random_password(char_count)
    
    if (input('Do you want to continue? (y/n)\n')):
        break
    

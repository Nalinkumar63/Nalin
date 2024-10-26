'''
1. Password should be at least * char length.
2. At least 1 upper case char
3. At least 1 lower case char
4. At least 1 number
5. At least 1 special char

'''

import random
alphabets = ["A","B","C","D","E","F"]

small = ['a','b','c','e','p','t']

numbers = [1,2,3,4,5,6,7,8,9,0]

chars = ['!','@','#','$','%','&','*','?']

ran_1 = random.choice(alphabets)+str(random.choice(numbers))+random.choice(small)+random.choice(chars)
ran_2 = random.choice(alphabets)+str(random.choice(numbers))+random.choice(small)+random.choice(chars)

print('Your Random Password:',ran_1+ran_2)

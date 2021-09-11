print('How many cats do you have?')
num_cats = input()
try:
    if int(num_cats) >= 4:
        print('That is a lot of cats')
    elif int(num_cats) <0:
        raise
    else:
        print('That is not that many cats')
except ValueError:
    print('You did not enter a valid number')
    
    
    

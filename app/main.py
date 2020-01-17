import functions as fc
### dictionary to keep all possible options
pwdOptions = {}

print("Welcome to the Password generator.\nThis small app has the capability to generate really strong passwords. How would like to proceed, default options, or custom options?")
mode = False


while mode not in [1,2]:
    mode = int(input("Please choose:\n1 - Default Options (recommended)\n2 - Custom Options\nYour choice: "))

if mode == 1:
    #generate password with default settings;
    pwdOptions['length'] = 16
    pwdOptions['alpha'] = True
    pwdOptions['caseSensitive'] = True
    pwdOptions['num'] = True
    pwdOptions['symbols'] = True
    pwdOptions['similar'] = False
elif mode == 2:
    #ask user input for the Options
    pwdOptions = fc.presentOptions()
else:
    #this should not happen, EVER!!!
    raise ValueError("Incorrect option passed. This should not happen please investigate.")
if mode and pwdOptions:
    print("We have all the information needed, so let's start\nThe password will be generated with the following options:")
    pwdConfig = fc.prepareOptions(pwdOptions)
    password = fc.generatePassword(pwdConfig)
    print("Your password is:", ''.join(password))
    

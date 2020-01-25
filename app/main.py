import functions as fc
# import termcolor
# dictionary to keep all possible options
defaultOptions = {'length': 16, 'alpha': True, 'caseSensitive': True, 'num': True, 'symbols': True, 'similar': False}
print("Welcome to the Password generator.\nThis small app has the capability to generate really strong passwords.")
print("How would like to proceed, default options, or custom options?\nThe default options are:")
print("Password Length:", defaultOptions['length'])
print("Letters:", defaultOptions['alpha'])
print("Case sensitive:", defaultOptions['caseSensitive'])
print("Numbers:", defaultOptions['num'])
print("Symbols:", defaultOptions['symbols'])
print("Include similar characters:", defaultOptions['similar'])
mode = False

while mode not in [1, 2]:
    try:
        mode = int(input("Please choose:\n1 - Default Options (recommended)\n2 - Custom Options\nYour choice: "))
    except:
        print("Warning: That's not a valid option. Let's try again.")
if mode == 1:
    pwdOptions = defaultOptions
elif mode == 2:
    # ask user input for the Options
    pwdOptions = fc.presentOptions()
else:
    # this should not happen, EVER!!!
    raise ValueError("Incorrect option passed. This should not happen please investigate.")
if mode and pwdOptions:
    print("Generating Password")
    pwdConfig = fc.prepareOptions(pwdOptions)
    success = False
    while not success:
        password = ''.join(fc.generatePassword(pwdConfig))
        print("Your password is:", password)
        if fc.inHistory(password):
            print("Password exists...we need a new one")
        else:
            success = True
    if fc.savePassword(password):
        print("Password saved successfully")
    else:
        print("Failed to save password. Please check file permissions")

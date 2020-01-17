import string
import random

def yesnoQuestion(q):
    a = False
    while a not in ['Y','y','N','n']:
        a = input(q + " [Y/N]: ")
    if a is 'y' or a is 'Y':
        return True
    elif a is 'n' or a is 'N':
        return False
    else:
        raise ValueError("Incorrect option passed. This should not happen please investigate.")

def presentOptions():
    options = {}
    options['length'] = False
    while options['length'] not in range(6,129):
        options['length'] = int(input("How long do you want your password to be?(Min: 6 Max:128): "))
    options['alpha'] = yesnoQuestion("Include alpha characters (a-z)?")
    options['caseSensitive'] = yesnoQuestion("Case Sensitive (A-Z,a-z)?")
    options['num'] = yesnoQuestion("Include numerical characters (0-9)?")
    options['symbols'] = yesnoQuestion("Include symbols (!@#$%^&*())?")
    if True not in options.values():
        print("You need to select at least one option. Let's try it again.")
        options.clear()
        presentOptions()
    options['similar'] = yesnoQuestion("Include similar characters (I,l,1,0,o,O)?")
    return options

def prepareOptions(options):
    #grab values from dict
    charToUse = {}
    charToUse['length'] = options['length']
    if options['alpha']:
        #include similar characters
        alpha = list(string.ascii_lowercase)
        if not options['similar']:
            similar = set(['i','l','o'])
            alphaSet = set(alpha)
            diff = alphaSet.difference(similar)
            alpha = list(diff)
        charToUse['alpha'] = alpha
    if options['caseSensitive']:
        caseSensitive = list(string.ascii_uppercase)
        if not options['similar']:
            similar = set(['I','L','O'])
            caseSet = set(caseSensitive)
            diff = caseSet.difference(similar)
            caseSensitive = list(diff)
        charToUse['caseSensitive'] = caseSensitive
    if options['num']:
        num = list(string.digits)
        if not options['similar']:
            similar = set(['0'])
            numSet = set(num)
            diff = numSet.difference(similar)
            num = list(diff)
        charToUse['num'] = num
    if options['symbols']:
        symbols = list(string.punctuation)
        symbols.remove('\\')
        charToUse['symbols'] = symbols
    return charToUse

def generatePassword(config):
    length = config['length']
    password = []
    del config['length']
    #get the first chars for each set of chars. This step is necessary to ensure that at least one char from each charset is used
    for c in config:
        password.append(random.choice(config[c]))
    #fill the remaing chars
    while len(password) < length:
        #select random item from dictionary
        charset = random.choice(list(config.keys()))
        char = random.choice(config[charset])
        password.append(char)
    return password

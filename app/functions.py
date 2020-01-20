import string
import random
import hashlib


def yesnoQuestion(q):
    a = False
    while a not in ['Y', 'y', 'N', 'n']:
        a = input(q + " [Y/N]: ")
    if a is 'y' or a is 'Y':
        return True
    elif a is 'n' or a is 'N':
        return False
    else:
        raise ValueError("Incorrect option passed. This should not happen please investigate.")


def presentOptions():
    options = {'length': False}
    while options['length'] not in range(15, 87):
        options['length'] = int(input("How long do you want your password to be?(Min:15 Max:86): "))
    options['alpha'] = yesnoQuestion("Include alpha characters (a-z)?")
    options['caseSensitive'] = yesnoQuestion("Case Sensitive (A-Z,a-z)?")
    options['num'] = yesnoQuestion("Include numerical characters (0-9)?")
    options['symbols'] = yesnoQuestion("Include symbols (!@#$%^&*())?")

    if True not in options.values() :
        print("You need to select at least one option. Let's try it again.")
        options.clear()
        presentOptions()
    options['similar'] = yesnoQuestion("Include similar characters (I,l,1,0,o,O)?")
    return options


def prepareOptions(options):
    # grab values from dict
    charToUse = {}
    charToUse['length'] = options['length']
    if options['alpha']:
        # include similar characters
        alpha = list(string.ascii_lowercase)
        if not options['similar']:
            similar = set(['i', 'l', 'o'])
            alphaSet = set(alpha)
            diff = alphaSet.difference(similar)
            alpha = list(diff)
        charToUse['alpha'] = alpha
    if options['caseSensitive']:
        # include uppercase characters
        caseSensitive = list(string.ascii_uppercase)
        if not options['similar']:
            similar = set(['I', 'L', 'O'])
            caseSet = set(caseSensitive)
            diff = caseSet.difference(similar)
            caseSensitive = list(diff)
        charToUse['caseSensitive'] = caseSensitive
    if options['num']:
        # include numverical characters
        num = list(string.digits)
        if not options['similar']:
            similar = set(['0'])
            numSet = set(num)
            diff = numSet.difference(similar)
            num = list(diff)
        charToUse['num'] = num
    if options['symbols']:
        # include symbols
        symbols = list(string.punctuation)
        symbols.remove('\\')
        charToUse['symbols'] = symbols
    return charToUse


def generatePassword(config):
    password = []
    length = config['length']
    del config['length']
    # Check if can generate password with only unique chars
    totalLen = 0
    unique = True
    for c in config:
        totalLen += len(config[c])
    # Get the first chars for each set of chars.
    # This step is necessary to ensure that at least one char from each charset is used
    if totalLen < length:
        print("Warning: Impossible to generate password with only unique chars. Removing restrictions")

        unique = False
    for c in config:
        char = random.choice(config[c])
        password.append(char)
        if unique: config[c].remove(char)
    # Shuffle current list to prevent order of first chars to be the same all the time
    random.shuffle(password)
    # fill the remaining chars until desired character amount
    while len(password) < length:
        # select random item from dictionary
        charset = random.choice(list(config.keys()))
        if len(config[charset]) == 0:
            del config[charset]
        else:
            char = random.choice(config[charset])
            # remove char to avoid repetition:
            if unique: config[charset].remove(char)
            password.append(char)
    return password


def inHistory(pwd):
    # check in history if password was generated before
    f = open("history.txt", "r")
    history = [p.replace("\n", "") for p in f.readlines()]
    f.close()
    pwdSecure = hashlib.md5(pwd.encode()).hexdigest()
    if pwdSecure in history:
        return True
    else:
        return False


def savePassword(pwd):
    f = open("history.txt", "a")
    pwdSecure = hashlib.md5(pwd.encode()).hexdigest()
    if f.write(pwdSecure+"\n"):
        f.close()
        return True
    else:
        f.close()
        return False

<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Strong Password Generator
 Pedro Moreira

Data Part time Bootcamp, Amsterdam, 2020

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project will generate a Strong password following a set of pre-defined rules. The user has the ability to choose a 
few options before generating the password. It's recommended that the default rules are chosen.  

## Rules
A passowrd to be considered strong consists of a string of at least 15 Characters that meet the following conditions:
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

A strong password should **not** contain/be:
- Your username
- Your name, your friend’s name, your family member’s name, or a common name
- Your date of birth
- Dictionary word
- Be one of your previous passwords
- Not a keyboard pattern


## Organization
To organize my work I created a kanban board and split the work that need to be done into multiple tasks. 
Link to Kanban board can be found bellow in the Links Section.

#### Repository structure:
```
└── project-1
    ├── app
    │   ├── functions.py
    │   ├── history.txt (not uploaded to repository. Excluded via .gitignore)
    │   └── main.py
    └── README.md
```

functions.py - contains all the necessary functions to the execution of the program.

main.py - main program file.

history.txt - Contains the password history off all the generated passwords (MD5) in order to prevent double passwords.

## Links

[Repository](https://github.com/pmoreira1/project-1)

[Presentation](https://drive.google.com/open?id=1HzsVX0M0xqazrUJc6gfNoYoIGj5f1-hdzmFbg9msXs4)

[Trello](https://trello.com/b/QoLnW4cq/project-1-create-your-own-game)

[Password Strength Meter](http://www.passwordmeter.com/)

[How Strong is My Password](https://howsecureismypassword.net/)


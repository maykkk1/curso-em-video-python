name = str(input('\033[;1;97mDigite o nome da cidade onde você mora '))
name = name.lower().strip()
name = name.split()
while name[0] == 'santo':
    print('\033[;1;92mTrue')
    break
while name[0] != 'santo':
    print('\033[;1;91mFalse')
    break





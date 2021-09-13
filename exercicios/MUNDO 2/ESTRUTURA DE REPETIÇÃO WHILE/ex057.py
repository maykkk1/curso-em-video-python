gender = ()
while gender != 'M' and gender != 'F':
    gender = str(input('Enter your gender: ')).upper().strip()
    if gender != 'M' and gender != 'F':
        print('Failure! Enter your gender correctly: ')
print('Gender successfully registered!')
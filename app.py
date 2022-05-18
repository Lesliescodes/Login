import time

username = 'Leslie'
password = 'slientpassword'
print('Please wait')
time.sleep(5)
print('ok... Loading...')
time.sleep(1)
print('...')
print('Alright you have security clearance. Pulling up the secret mainframe.')
username_input = ('username:')
password_input = ('password:')

if username_input == username and password_input == password:
    print('Access granted')
elif username_input == username and password_input != password:
    print('Password incorrect')
elif username_input != username and password_input == password:
    print('Username incorrect')
else:
    print('Incorrect entry please check your username and password')

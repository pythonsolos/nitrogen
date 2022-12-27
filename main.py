import string, secrets, os, pyfiglet
print(pyfiglet.figlet_format("N I T R O", font = "alligator2"))
d = string.ascii_letters + string.digits
print('Made by gui!#0979\n')
input = int(input('How many codes to generate: '))
output = ''
for b in range(0, input):
    password = "".join(secrets.choice(d) for i in range(16))
    output = output + 'https://discord.gift/'+ password +'\n'
    print('https://discord.gift/'+password)
with open(str(input)+'codes.txt', 'w') as f:
    print('\n\nCodes generated. Check ['+os.getcwd()+'] to see them all.')
    f.write('https://github.com/pythonsolos\n\n\n'+output)

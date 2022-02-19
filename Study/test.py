file=open('test.txt', 'w')
file.write('my name is bright\n')
#file.close()
lines=['bright\n', 'mind\n', 'gogo\n']
file.writelines(lines)
file.close()
with open('test.txt', 'r') as file:
    out = file.readlines()
    print(out)

with open('test.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readlines()
        print(line)
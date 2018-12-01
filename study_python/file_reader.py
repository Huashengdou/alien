
with open('pi_digits.txt') as  file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    #content = file_object.read()
    #print(content)

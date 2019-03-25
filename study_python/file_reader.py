
with open('pi_digits.txt') as  file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

file_name = 'programming.txt'
with open(file_name, 'a') as file_obj:
    file_obj.write('i love python.\n')
    file_obj.write('i love programming\n\n')
    #content = file_object.read()
    #print(content)


with open('example.txt', 'w') as f:
    f.write('Hello, this is an example file.\n')
    f.write('We are writing to it using Python file handling operations.\n')


with open('example.txt', 'r') as f:
    content = f.read()
    print(content)

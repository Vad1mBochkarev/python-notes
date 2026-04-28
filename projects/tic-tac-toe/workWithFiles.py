file = open('example.txt', 'w', encoding='utf-8')

file.write("Hello, world!\nThis is a test file.\n")

file.write("Another line of text.")

conent = file.read(14)

print(conent)

file.close()
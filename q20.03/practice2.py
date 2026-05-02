file_path = './q20.03/data.txt'

with open(file_path, 'r') as f:
    text = f.read()
    f.close()

    result = ''

    for char in text:
        if char.isalpha():
            if char == 'z':
                result += 'a'
            else:
                result += chr(ord(char)+ 1)
        else:
            result += char

with open('./q20.03/encrypted.txt', 'w') as f2:
    f2.write(result)
    f2.close()
print('successfully')
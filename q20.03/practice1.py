file_path = './q20.03/data.txt'

with open(file_path, 'r') as f:
    file_content = f.read()

with open('backup.txt', 'w') as f:
    f.write(file_content)
print('file copy successfully')
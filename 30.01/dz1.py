size = 10

while True:
    print("оберіть фігуру: а, б, в, г, д, е, ж, з, и, к")
    print("або введіть 'exit' для виходу")
    
    choice = input("")
    
    if choice == 'exit':
        break
    
    for i in range(size):
        for j in range(size):
            result = False
            if choice == 'а': result = (j >= i)
            elif choice == 'б': result = (j <= i)
            elif choice == 'в': result = (j >= i and j <= size - 1 - i)
            elif choice == 'г': result = (j <= i and j >= size - 1 - i)
            elif choice == 'д': result = (j >= i and j <= size - 1 - i) or (j <= i and j >= size - 1 - i)
            elif choice == 'е': result = (j <= i and j <= size - 1 - i) or (j >= i and j >= size - 1 - i)
            elif choice == 'ж': result = (j <= i and j <= size - 1 - i)
            elif choice == 'з': result = (j >= i and j >= size - 1 - i)
            elif choice == 'и': result = (j <= size - 1 - i)
            elif choice == 'к': result = (j >= size - 1 - i)

            if result:
                print("*", end=" ") # if result == true
            else:
                print(" ", end=" ") # if result == false
        print()
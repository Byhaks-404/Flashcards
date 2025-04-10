import random
import csv
from flashcards_functions import load_database
from flashcards_functions import save_flashcard
from flashcards_functions import remove_flashcard


basesDatos = []
with open('db.csv', 'r', newline='', encoding='utf-8') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        basesDatos.append(row['data_bases'])
        
while True:
    try: 

        print("0. Create new DB")
        i=1
        for i, db in enumerate(basesDatos, 1):  
            print(f"{i}. {db}")

        print("\nWith what Data Base you want to operate? ")
        chooseDB = int(input())

        if chooseDB == 0:
            nameCSV = input("name: ")
            if not nameCSV.endswith('.csv'):
                nameCSV += '.csv'
            basesDatos.append(nameCSV)

            # Create the new CSV file
            with open(nameCSV, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['first_name', 'last_name']  
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

            # Update db.csv
            temp_data = []
            try:
                with open('db.csv', 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        temp_data.append(dict(row))
            except FileNotFoundError:
                temp_data = []

            fieldnames = ['data_bases']
            temp_data.append({'data_bases': nameCSV})

            with open('db.csv', 'w', newline='', encoding='utf-8') as csvfile:  # Fixed from 'filename'
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(temp_data)

            
            filename = basesDatos[len(basesDatos)-1]
        else:    
            filename = basesDatos[chooseDB-1]
        first_names, last_names = load_database(filename)
        break

    except:
        
        print("not valid \n")



while True:


    print("1. Add FlashCard")
    print("2. Remove FlashCard")
    print("3. Memorize")
    print("4. Salir \n")

    try:
        choose = int(input("What do you want to do: "))
            
        if choose == 1:

            nom = input("value 1: ")
            nom2 = input("value 2: ")
            save_flashcard(filename, nom, nom2)
            print("\nFlashcard added successfully!")
            updated_first, updated_last = load_database(filename)
            print("Updated value 1:", updated_first)
            print("Updated value 2:", updated_last)
                
        elif choose == 2:
            updated_first, updated_last = load_database(filename)
            value = input("Enter value 1 or value 2 to remove: ")
            if remove_flashcard(filename, value):
                updated_first, updated_last = load_database(filename)
                print("\nFlashcard removed successfully!")
                print("Updated values 1:", updated_first)
                print("Updated values 2:", updated_last)
            else:
                print("No matching flashcard found!")

        elif choose == 3:
            updated_first, updated_last = load_database(filename)
            
            tecla = ''
            
            while tecla=='':
                j = random.randint(0,len(updated_first)-1)
                print(f"{updated_first[j]}: ", end='')
                tecla = input()
                print(updated_last[j]+'\n')
        elif choose == 4:
            break
        else:
            print("Invalid option")
                
    except ValueError:
        print("Please enter a valid number")
import csv

def load_database(filename):
    first_names = []
    last_names = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                first_names.append(row['first_name'])
                last_names.append(row['last_name'])
        return first_names, last_names
    except FileNotFoundError:
        return [], []
    
def save_flashcard(filename, first_name, last_name):
    temp_data = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_data.append(dict(row))
    except FileNotFoundError:
        temp_data = []
    
    fieldnames = ['first_name', 'last_name']
    temp_data.append({'first_name': first_name, 'last_name': last_name})
    
    # Write all data back to file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(temp_data)

def remove_flashcard(filename, value):
    temp_data = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_data.append(dict(row))
    except FileNotFoundError:
        return False
    
    fieldnames = ['first_name', 'last_name']
    filtered_data = []
    
    for row in temp_data:
        if row['first_name'] != value and row['last_name'] != value:
            filtered_data.append(row)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)
    return True
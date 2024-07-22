import os, json, csv

# Relative path to the files
relative_path = "files/"

# Desired keys
required_keys = ['first_name', 'last_name', 'email']

# Function find JSON files - complete path
def find_json(directory):
    json_list = [os.path.join(directory, file) for file in os.listdir(directory) if (os.path.splitext(file)[1]) == ".json" and '_' in file] 
    return json_list
 
# Function to read the content of found JSON files
def precti_json(file):
    try:
        with open(file, "r", encoding="utf-8") as json_data:
            return(json.load(json_data))
    except FileNotFoundError:
        print(f"File {json_data} not found")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {file}.")
            
# Function to filter the content of the files
def filtr_klicu(zadouci, puvodni_zaznam):
    vycisteny_zaznam = {klic: puvodni_zaznam[klic] for klic in zadouci if klic in puvodni_zaznam}
    return vycisteny_zaznam

# Function to save files to CSV locally
def zapis_csv(final_file, zaznamy):
    if not zaznamy:
        print("No records to write to CSV.")
        return

    with open(final_file, "w", encoding="utf-8", newline="") as csvystup:
        sloupecky = zaznamy[0].keys()
        zapis = csv.DictWriter(csvystup, fieldnames=sloupecky)
        zapis.writeheader()
        zapis.writerows(zaznamy)
        print(f"Soubor {final_file} zapsán na disk")
        
def json_to_csv():
    json_files = find_json(relative_path)
    obsah_jsonu = [filtr_klicu(required_keys, record) for json_file in json_files for record in precti_json(json_file)]
    
    zapis_csv("soubor1.csv", obsah_jsonu)  


 
json_to_csv()     
        

            
    




            
            

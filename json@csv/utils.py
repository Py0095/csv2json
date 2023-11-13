import csv
import json


def json_to_csv(json_path, csv_path):
    try:
        with open(json_path, 'r') as json_file:
            data = eval(json_file.read())

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            with open(csv_path, 'w') as csv_file:
                # Write header
                header = ','.join(data[0].keys())
                csv_file.write(f"{header}\n")

                # Write data
                for row in data:
                    values = ','.join(str(val) for val in row.values())
                    csv_file.write(f"{values}\n")

            print(f"JSON to CSV conversion successful. CSV file is at: {csv_path}")
        else:
            print("Incorrect JSON format. JSON should be a list of dictionaries.")
    except FileNotFoundError:
        print(f"Error: File not found. Check the path of the JSON file: {json_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



def csv_to_json(csv_path, json_path, separator=','):
    try:
        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=separator)
            data = list(reader)

        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return 'Fichier JSON créé avec succès.'
    except FileNotFoundError:
        return f'Erreur : Fichier introuvable. Vérifiez le chemin du fichier CSV : {csv_path}'
    except PermissionError:
        return 'Erreur : Permission refusée. Assurez-vous d’avoir les autorisations nécessaires pour accéder au fichier.'
    except Exception as e:
        return f'Une erreur s’est produite : {e}'







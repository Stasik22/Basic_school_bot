import json

NOTES_FILE = "notes.json"

def notes_load():
    try:
        with open(NOTES_FILE, "r", encoding= "utf-8") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return{}

def notes_save(notes):
    with open(NOTES_FILE, "w", encoding= "utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

notes_data = notes_load()




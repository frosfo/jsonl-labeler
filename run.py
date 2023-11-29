import os
import json
from shutil import move

dir = os.path.dirname(__file__)

def process(file_name):
    try:
        path = os.path.join(dir, file_name)
        with open(path, 'r',encoding='utf-8') as file:
            print("Processing",path,":\n",'-'*20)
            non_hate = os.path.join(dir, "outputs", "non_Hateful_" + file_name)
            hate = os.path.join(dir, "outputs", "Hateful_" + file_name)
            os.makedirs(non_hate, exist_ok=True)
            os.makedirs(hate, exist_ok=True)
            for line in file:
                try:
                    object = json.loads(line)
                    categorize(object, hate, non_hate)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
            print("Processed",path,":\n",'-'*20)
    except Exception as e:
        print("Error processing ",path,": ",e)

def categorize(object,hate,non_hate):
    print(object["id"],": ")
    if object['label']:
        print("Hateful, writing to txt")
        with open(os.path.join(hate,object['id']), 'w',encoding='utf-8') as txt:
            txt.write(object['text'])
        image = os.path.join(dir,object['img'])
        if os.path.exists(image):
            print("Moving Image")
            move(image, hate)
        else:
            print(image, " does not exists")
    else:
        print("Non hateful, writing to txt")
        with open(os.path.join(non_hate,object['id']), 'w',encoding='utf-8') as txt:
                txt.write(object['text'])
        image = os.path.join(dir,object['img'])
        if os.path.exists(image):
            print("Moving Image")
            move(image, non_hate)
        else:
            print(image," does not exists")

if __name__ == "__main__":
    print("Initiated")
    for file in os.listdir(dir):
        print("Checking ",file)
        if file.endswith(".jsonl"):
            path = os.path.join(dir, file)
            process(file)
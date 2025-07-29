# data_store.py
import json
import os

DATA_FILE = "user_data.json"

# Create empty file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_user_cart(username, grocery_list, blinkit_results):
    data = load_data()

    data[username] = {
        "grocery_list": grocery_list,
        "cart": blinkit_results
    }

    save_data(data)

def get_user_cart(username):
    data = load_data()
    return data.get(username, None)



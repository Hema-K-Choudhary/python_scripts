import configparser
import json
import sqlite3
import os
from flask import Flask, jsonify

CONFIG_FILE = "./config.ini"
DB_FILE = "./config_data.db"

app = Flask(__name__)

def parse_config(file_path):
    print("reading config from the file..")


    # using config parser to read contents of .ini config file.
    config = configparser.ConfigParser()
    parsed_data = {}

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found.")

    config.read(file_path)

    for section in config.sections():
        parsed_data[section] = dict(config.items(section))

    return parsed_data

def save_to_db(data, db_path):
    print("saving config to DB..")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)")

    # Clear previous data
    cursor.execute("DELETE FROM config")

    # Insert new data
    cursor.execute("INSERT INTO config (data) VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()

def load_from_db(db_path):
    print("Loading config details from DB..")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT data FROM config ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])
    return {}

@app.route('/config', methods=['GET'])
def get_config():
    try:
        config_data = load_from_db(DB_FILE)
        return jsonify(config_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        parsed_config = parse_config(CONFIG_FILE)
        save_to_db(parsed_config, DB_FILE)
        app.run(debug=True)

    except FileNotFoundError as err:
        print(err)

    except Exception as e:
        print(f"Exception: {e}")

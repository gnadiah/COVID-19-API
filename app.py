import urllib.request
import requests
import time
import json
from flask import *
from flask_restful import *
from flask_cors import *
from html_table_parser.parser import HTMLTableParser

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

WORLD_START = 0
VN_START = 0
WAITING_TIME = 60

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def json_decoder(data):
    while True:
        try:
            data = data.json()
            return data
        except Exception as e:
            print(e)

def get_vn_api_hec_key():
    response = requests.get("https://api.apify.com/v2/key-value-stores/p3nS2Q9TUn6kUOriJ/records/LATEST")
    return json_decoder(response)

def get_vn_api_data():
    response = requests.get("https://api.apify.com/v2/key-value-stores/ZsOpZgeg7dFS1rgfM/records/LATEST")
    return json_decoder(response)

def get_url_contents(url):
    opener = AppURLopener()
    response = opener.open(url)
    contents = response.read()
    return str(contents)


def find_table(contents):
    p = HTMLTableParser()
    p.feed(contents)
    return p

def get_table_contents(tables):
    data = []
    for row in tables:
        try:
            int(row[0])
            if row[1] == "Vietnam":
                vietnam_data = get_vn_api_data()
                data.append({
                    "id": int(row[0]),
                    "country": row[1],
                    "total_cases": vietnam_data["infected"],
                    "total_deaths": vietnam_data["deceased"],
                    "total_recovered": vietnam_data["recovered"],
                    "being_treated": vietnam_data["treated"]
                })
            else:
                data.append({
                    "id": int(row[0]),
                    "country": row[1],
                    "total_cases": int(row[2].replace(",","")),
                    "total_deaths": int(row[4].replace(",","")),
                    "total_recovered": int(row[6].replace(",","")),
                    "being_treated": int(row[8].replace(",","")),
                })
        except ValueError:
            if "World" in row[1]:
                data.append({
                    "country": "World",
                    "total_cases": int(row[2].replace(",","")),
                    "total_deaths": int(row[4].replace(",","")),
                    "total_recovered": int(row[6].replace(",","")),
                    "being_treated": int(row[8].replace(",",""))
                })
    return data

def save_world_data():
    contents = get_url_contents("https://www.worldometers.info/coronavirus/")
    group_table = find_table(contents)
    data = get_table_contents(group_table.tables[0])
    with open("world_data.json","w") as file:
        json.dump(data, file)

def save_vn_data():
    vn_hec_key_list = get_vn_api_hec_key()
    vn_data_list = get_vn_api_data()
    data = []
    data.append({
        "province": "Vietnam",
        "total_cases": vn_data_list["infected"],
        "total_deaths": vn_data_list["deceased"],
        "total_recovered": vn_data_list["recovered"],
        "being_treated": vn_data_list["treated"]
    })
    for i in vn_data_list["detail"]:
        for j in vn_hec_key_list["key"]:
            if j["hec-key"] == i["hc-key"]:
                province = j["name"]
        data.append({
            "province": province,
            "total_cases": i["value"],
            "total_deaths": i["socatuvong"],
            "total_recovered": i["socakhoi"],
        })
    with open("vn_data.json", "w") as file:
        json.dump(data, file)

def get_world_data_json():
    with open("world_data.json", "r") as file:
        data = json.load(file)
    return data

def get_vn_data_json():
    with open("vn_data.json", "r") as file:
        data = json.load(file)
    return data

class world_covid_19_data(Resource):
    def get(self):
        global WORLD_START
        current_time = time.time()
        print(current_time - WORLD_START)
        if WORLD_START == 0 or current_time - WORLD_START >= WAITING_TIME:
            WORLD_START = time.time()
            save_world_data()
            WORLD_START = time.time()
        return get_world_data_json()

class vn_covid_19_data(Resource):
    def get(self):
        global VN_START
        current_time = time.time()
        print(current_time - VN_START)
        if VN_START == 0 or current_time - VN_START >= WAITING_TIME:
            VN_START = time.time()
            save_vn_data()
            VN_START = time.time()
        return get_vn_data_json()

api.add_resource(world_covid_19_data, "/api/get-world-data", "/api/get-world-data/")
api.add_resource(vn_covid_19_data, "/api/get-vn-data", "/api/get-vn-data/")

if __name__ == "__main__":
    app.run(debug=True)

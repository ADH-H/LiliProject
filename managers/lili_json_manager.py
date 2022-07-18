import json

def init():

    #Opens and loads the JSON config file, and places into a variable (lili_config_json)
    with open('lili_config.json', 'r', encoding='utf-8') as r:

        #Makes lili_config_json avalible across the file
        global lili_config_json

        #Loads the JSON
        lili_config_json = json.load(r)

def currentLili(setting, value):
    if setting == "blinkTime":
        lili_config_json["blinkConfig"]["blinkTime"] = value
    with open('lili_config.json', 'w', encoding='utf-8') as w:
        json.dump(lili_config_json, w, indent=4)

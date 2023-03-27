
import db
import requests
import json

data_base = db.DatabaseClass()
response = requests.get('https://steamspy.com/api.php?request=all&page=1')
game_data = json.loads(response.text)
print(game_data)
for game_code in game_data:
    game = game_data[game_code]
    print(game['appid'])
    game_name = game['name']
    game_id = game['appid']
    try:

        data_base.insert_data(game_id = game_id, game_name = game_name)
    except Exception as e:
        print(e)
        continue
# team = "pur"
import requests

def getTeamData(team : str):
    url = f"https://api.sportsdata.io/v3/cbb/scores/json/PlayersBasic/{team}"

    querystring = {"key": "API_KEY"}

    response = requests.get(url, params=querystring).json()
    return response
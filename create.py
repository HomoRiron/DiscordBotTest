import requests

url = "https://discordapp.com/api/v6/guilds"

ServerName = ""

token  = ""

json = {
    "name":ServerName,
    "region":"japan",
    "icon":None
}

header = {
    "authorization":token
}

Response = requests.post(url,json=json,headers=header)

Serverid = Response.json()["id"]

url=f"https://discordapp.com/api/v6/channels/{Serverid}/invites"

data = {
    "validate":None,
    "max_age":"86400"
}

r=requests.post(url,headers=header,json=data)

TicketId = r.json()["code"]

print("https://discord.gg/"+TicketId)
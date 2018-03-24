import requests

LoginUrl="https://discordapp.com/api/v6/auth/login"

Email = ""

Password = ""

JsonData = {
    "email":Email,
    "password":Password
}

Response=requests.post(json=JsonData,url=LoginUrl)

ResponseJson = Response.json()

if ("captcha_key" in ResponseJson):
    print("Invalid email")
    exit()
if ("password" in ResponseJson):
    print("Password does not match.")

print(ResponseJson["token"])
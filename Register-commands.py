import requests
import yaml
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("token")
appid = "1203489932002205728"
url = f"https://discord.com/api/v9/applications/1203489932002205728/commands"

with open("Discord-commands.yaml", "r") as file:
        yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization" : f"Bot {token}", "Content-Type" : "application/json"}

for command in commands:
    response = requests.post(url, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")
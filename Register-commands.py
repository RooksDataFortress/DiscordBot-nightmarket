import requests
import yaml

token = "MTIwMzQ4OTkzMjAwMjIwNTcyOA.GSn5NA.TUKY4nE9gX53gkRj6WG0Dkfb8xGz8rg8B00U6M"
appid = "1203489932002205728"
url = f"https://discord.com/api/v9/applications/1203489932002205728/commands"

with open("discord_commands.yaml", "r") as file:
        yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization" : f"Bot {token}" "Content-Type" : "application/json"}

for command in commands:
    response = requests.post(url, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")
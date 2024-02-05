import os
from flask import Flask, jsonify, request
from discord_interactions import verify_key_decorator

pubkey = os.getenv("pubkey")

app = Flask(__name__)



@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)


@verify_key_decorator(pubkey)
def interact(raw_request):
    if raw_request["type"] == 1:  # discord in
        response_data = {"type": 1}  # bot out
    else:
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "hello":
            message_content = "Hello there!"
        elif command_name == "market":
            message_content = f"Echoing: {original_message}"

        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)


#if __name__ == "__main__":
#    app.run(debug=True)
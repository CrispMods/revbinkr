from flask import Flask, request, jsonify
import time
import sys

app = Flask(__name__)

def dump_request(tag):
    try:
        raw = request.get_data()
        body = raw.decode("utf-8", errors="replace")
    except:
        body = None

    log = {
        "time": time.time(),
        "tag": tag,
        "method": request.method,
        "path": request.path,
        "query": request.args.to_dict(flat=False),
        "headers": dict(request.headers),
        "body": body
    }

    print("==== INCOMING REQUEST ====")
    for k, v in log.items():
        print(f"{k}: {v}")
    print("==========================", flush=True)

@app.route("/api/CachePlayFabId", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def cache_playfab_id():
    dump_request("CachePlayFabId")
    return jsonify({"status": "ok"}), 200

@app.route("/api/PlayFabAuthentication", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def playfab_auth():
    dump_request("PlayFabAuthentication")
    return jsonify({"status": "ok"}), 200

@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
@app.route("/<path:path>", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def catch_all(path):
    dump_request("catch-all")
    return jsonify({"status": "ok"}), 200

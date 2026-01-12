from flask import Flask, request, jsonify
import time

app = Flask(__name__)

logs = []

def log_request(tag=None):
    try:
        body = request.get_data(as_text=True)
    except:
        body = None

    logs.append({
        "time": time.time(),
        "tag": tag,
        "method": request.method,
        "path": request.path,
        "query": request.args.to_dict(flat=False),
        "headers": dict(request.headers),
        "body": body
    })

@app.route("/api/CachePlayFabId", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def cache_playfab_id():
    log_request("CachePlayFabId")
    return jsonify({"status": "ok"}), 200

@app.route("/api/PlayFabAuthentication", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def playfab_auth():
    log_request("PlayFabAuthentication")
    return jsonify({"status": "ok"}), 200

@app.before_request
def log_everything_else():
    if request.path.startswith("/api/"):
        return
    log_request("catch-all")

@app.route("/", defaults={"path": ""}, methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
@app.route("/<path:path>", methods=["GET","POST","PUT","PATCH","DELETE","OPTIONS"])
def catch_all(path):
    return jsonify({"status": "ok"}), 200

@app.route("/_logs", methods=["GET"])
def get_logs():
    return jsonify(logs)

@app.route("/_clear", methods=["POST"])
def clear_logs():
    logs.clear()
    return jsonify({"cleared": True})

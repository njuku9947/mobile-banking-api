from flask import Flask

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

@app.route("/")
def home():
    return "Mobile Banking API Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





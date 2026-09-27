from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    visits = r.incr("visits")

    return f"""
    <html>
        <head>
            <title>Docker Compose Project</title>
        </head>
        <body>
            <h1>Docker Compose Application</h1>
            <h2>Hello from Flask + Redis!</h2>
            <p>Page visits: {visits}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "Application is healthy!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

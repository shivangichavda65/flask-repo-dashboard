from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #2c3e50;
                color: white;
                padding: 15px;
                text-align: center;
            }
            .container {
                padding: 20px;
            }
            .card {
                background: white;
                padding: 20px;
                margin-bottom: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>

        <header>
            <h1>My Static Dashboard</h1>
        </header>

        <div class="container">
            <div class="card">
                <h3>Status</h3>
                <p>Application is running successfully 🚀</p>
            </div>

            <div class="card">
                <h3>Environment</h3>
                <p>Docker + Flask</p>
            </div>

            <div class="card">
                <h3>Version</h3>
                <p>v1.0</p>
            </div>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

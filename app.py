import os
import requests
from flask import Flask, render_template, request as req, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Load API token from environment variable
API_TOKEN = os.getenv("HF_API_TOKEN", "your_hf_token")

# Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer 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"}

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["POST"])
def Summarize():
    if req.method == "POST":
        data = req.form["data"]
        maxL = int(req.form["maxL"])
        minL = maxL // 4

        # Function to make API request
        def query(payload):
            try:
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()  # Raise an error for bad responses
                return response.json()
            except requests.exceptions.RequestException as e:
                flash(f"Error contacting the API: {e}")
                return None

        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })

        # Check if the API returned a valid response
        if output and "summary_text" in output[0]:
            return render_template("index.html", result=output[0]["summary_text"])
        else:
            flash("Failed to summarize the text. Please try again.")
            return redirect(url_for("Index"))

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')

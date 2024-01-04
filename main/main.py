from flask import Flask, render_template, request
import pandas as pd
import Event
from Event import Event
import Letter
from Letter import Letter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    return "This is a test!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"
    
    eventTitle = request.form['Event Name'].lower()
    timeframe = request.form['Timeframe'].lower()
    location = request.form['Location'].lower()

    if file and file.filename.endswith('.xlsx'):
        # Process the Excel file (example: read data using pandas)
        df = pd.read_excel(file)

        event = Event(eventTitle.title(), location, timeframe)
        
        letters = []

        for entry in df.values:
            letter = Letter(event, location, entry[0], entry[1], entry[2], entry[3], 'sincerely', 'J. Matthew Myers')
            letters.append(letter)

        return f'{letters[0]}'
    else:
        return "Invalid file format. Please upload a .xlsx file"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
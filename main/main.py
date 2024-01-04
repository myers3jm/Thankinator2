from flask import Flask, render_template, request, send_file
import pandas as pd
import Event
from Event import Event
import Letter
from Letter import Letter
import pdfkit
import zipfile
from io import BytesIO

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
        
        pdfLetters = []

        for entry in df.values:
            letter = Letter(event, location, entry[0], entry[1], entry[2], entry[3], 'sincerely', 'J. Matthew Myers')
            try:
                pdfLetter = pdfkit.from_string(str(letter))
                pdfLetters.append(pdfLetter)
            except Exception as e:
                return f'Failure during conversion to PDF: {e.with_traceback()}'
            
        def create_zip_archive(pdf_data_list):
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for index, pdf_data in enumerate(pdf_data_list):
                    # Add each PDF to the zip archive with a unique name
                    pdf_filename = f'document_{index + 1}.pdf'
                    zip_file.writestr(pdf_filename, pdf_data)
            zip_buffer.seek(0)
            return zip_buffer
        zip_file = create_zip_archive(pdfLetters)
        return send_file(zip_file, download_name='letters.zip', as_attachment=True, mimetype='application/zip')

    else:
        return "Invalid file format. Please upload a .xlsx file"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
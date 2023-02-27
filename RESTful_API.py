"""
Purpose of RESTful_API.py

Handle API calls

    -   POST generateReceipt
            - INPUT:  JSON input to generate receipt
            - PROCESS : Generate Receipt from JSON
            - RETURN : QR code image , ID of receipt
            -

    -   GET receiptQR
            - INPUT:  ID of reciept
            - PROCESS : Search for receipt if exists
            - RETURN : QR code image (if exists)

    -   GET receipt
        - INPUT:  ID of reciept
        - RETURN : return website to download and preivew receipt

    -   GET downloadReceipt
        - INPUT : ID of Receipt
        - PROCESS : facilitate the download of Reciept


"""

from flask import Flask, render_template,make_response
import pdfkit

app = Flask(__name__)

config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf\\bin\\wkhtmltopdf.exe")

# path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/pdf/")
def index():
    # installed https://wkhtmltopdf.org/
    html = render_template("index.html")
    pdf = pdfkit.from_string(html,configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import os
import base64
from flask import Flask, render_template, url_for, send_from_directory
import pdfkit


app = Flask(__name__)
IMG_PATH = './static/img/meme.jpeg'
PDF_DIR = 'pdfs'
PDF_FNAME = 'out_target.pdf'
PDF_PATH = os.path.join(PDF_DIR, PDF_FNAME)
PDF_OPTIONS = {
    'page-size': 'A4',
    'margin-top': '5mm',
    'margin-right': '5mm',
    'margin-bottom': '5mm',
    'margin-left': '5mm',
    'encoding': 'UTF-8',
}
PAGES_DATA = [1, 2, 3, 4, 5, 6, 7, 8]
INCLUDE_CSS = ['static/style/bulma.min.css', 'static/style/more.css']

def get_image_file_as_base64_data(fpath):
    with open(fpath, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/render')
def render():
    # img_b64 = get_image_file_as_base64_data(IMG_PATH)
    # return render_template('target.html', img_b64=img_b64)
    return render_template('target_2.html', data=PAGES_DATA)


@app.route('/save_pdf')
def save_pdf():
    # img_b64 = get_image_file_as_base64_data(IMG_PATH)
    # html_content = render_template('target.html', img_b64=img_b64)
    html_content = render_template('target_2.html', data=PAGES_DATA)
    pdfkit.from_string(input=html_content, output_path=PDF_PATH, options=PDF_OPTIONS, css=INCLUDE_CSS)
    return f'''Saved pdf. It\'s in {PDF_PATH}<br> \
        <a href="{url_for('index')}"><button>Back to Home</button></a> \
        <a href="{url_for('download')}"><button>Download converted pdf</button></a>'''


@app.route('/download')
def download():
    if os.path.exists(PDF_PATH):
        return send_from_directory(directory=PDF_DIR, path=PDF_FNAME)
    else:
        return f'''No pdf to download<br><a href="{url_for('index')}">Back to Home</a>'''


if __name__ == '__main__':
    pass

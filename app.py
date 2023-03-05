from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('images', filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <html>
        <head>
            <title>File Upload</title>
        </head>
        <body>
            <h1>File Upload</h1>
            <form action="/" method="post" enctype="multipart/form-data">
                <label for="file">Choose a file to upload:</label>
                <input type="file" id="file" name="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'<h2>Uploaded file: {filename}</h2><img src="images/{filename}">'

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')
    app.run()

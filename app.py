from flask import Flask, render_template, request, redirect, session, url_for, send_file
from flask import jsonify, send_from_directory
import youtube_dl
import os
import subprocess
from subprocess import call


# init_application
app = Flask(__name__)


@app.route('/')
def home():
    render_template('index.html')


@app.route('/download_video')
def download_mp4():
    url = request.args.get('url')
    filename = str(int(time.time() * 100000))

    cmd = 'youtube-dl -o var/www/html/app/export_tmp/videos/'+ filename+ ' --no-cache-dir ' + url
    call(cmd.split(' '), shell=False)

    file_list = glob.glob("var/www/html/app/export_tmp/videos/*")
    for fname in file_list:
        if fname in filename:
            print('name', fname)
            break

    return send_file('export_tmp/videos/' + fname[35:], as_attachment=True, attachment_filename=fname[35:-5] + '.mp4', mimetype='video/mp4')

@app.route('/download_music')
def download_mp3():
    url = request.args.get('url')
    filename = str(int(time.time() * 100000))
    print('filename', filename)

    cmd = 'youtube-dl -o var/www/html/app/export_tmp/'+ filename + '.%(ext)s --extract-audio --audio-format mp3 --audio-quality 0 --no-cache-dir ' + url
    call(cmd.split(' '), shell=False)

    file_list = glob.glob("var/www/html/app/export_tmp/*")
    for fname in file_list:
        if fname in filename:
            print('name', fname)
            break

    return send_file('export_tmp/' + filename + '.mp3', as_attachment=True, attachment_filename=filename + '.mp3', mimetype='audio/mpeg')



if __name__ == "__main__":
    app.run(debug=True)

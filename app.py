from flask import Flask, render_template, request, send_file
from subprocess import call


# init_application
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/download_video')
def download_mp4():
    url = request.args.get('url')
    filename = 'test'

    cmd = 'youtube-dl -o export_tmp/videos/' + \
        filename + ' --no-cache-dir ' + url
    call(cmd.split(' '), shell=False)

    try:
        return send_file(
            'export_tmp\\videos\\test.mp4',
            as_attachment=True,
            attachment_filename='test.mp4',
            mimetype='video/mp4'
        )
    except:
        return send_file(
            'export_tmp\\videos\\test.mkv',
            as_attachment=True,
            attachment_filename='test.mp4',
            mimetype='video/mp4'
        )
    else:
        return send_file(
            'export_tmp\\videos\\test.webm',
            as_attachment=True,
            attachment_filename='test.mp4',
            mimetype='video/mp4'
        )


if __name__ == "__main__":
    app.run(debug=True)

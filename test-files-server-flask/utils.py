import os

from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = ['mp3']


def get_files(path):
    arr = os.listdir(path)
    return arr


def delete_file(directory, path):
    absolute_path = os.path.join(directory, path)
    os.remove(absolute_path)


def create_file(directory, file):
    filename = secure_filename(file.filename)
    if not allowed_file(filename):
        return False

    serial_no = 0
    while True:
        if serial_no:
            absolute_path = os.path.join(directory, str(serial_no)+'-'+filename)
        else:
            absolute_path = os.path.join(directory, filename)
        if not os.path.exists(absolute_path):
            break
        serial_no += 1
    file.save(absolute_path)
    return True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

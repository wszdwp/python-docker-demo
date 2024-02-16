from werkzeug.utils import secure_filename
from flask import current_app
import os

class FileUtil:    
    def __init__(self, baseUploadPath, allowedExtensions) -> None:
        self.baseUploadPath = baseUploadPath
        self.allowedExtensions = allowedExtensions

    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in self.allowedExtensions
            
    def saveFile(self, file):
        if not file or file.filename == '':
            current_app.logger.error('file or fileName is None or empty')
            return 'No selected file'
        if not self.allowed_file(file.filename):
            current_app.logger.error('Not allowed file %s', file.filename)
            return 'Not allowed file: ' + file.filename
        filename = secure_filename(file.filename)
        fullPath = os.path.join(self.baseUploadPath, filename)
        file.save(fullPath)
        current_app.logger.info('saved file to fullPath: %s', fullPath)
        return fullPath

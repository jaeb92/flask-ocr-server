import os

from flask import request, Blueprint
from flask_restx import Resource, Namespace
from werkzeug.datastructures import FileStorage
from ocr.ocr_service import ocr_text, file_save

UPLOAD_FILE_PATH = f"{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}\\static\\upload\\img"

ocr_bp = Blueprint('ocr', __name__)
ocr_api = Namespace('ocr_api', '/ocr')


upload_parser = ocr_api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@ocr_api.route('')
@ocr_api.response(404, "Not Found")
@ocr_api.response(201, "Found")
class OcrRequest(Resource):
    ALLOWED_EXTENSION = ['jpg', 'jpeg', 'gif', 'png']
    SUCCESS_CODE = [200, 201]

    @ocr_api.expect(upload_parser)
    def post(self):
        print('request=', request.root_path)
        file = upload_parser.parse_args()['file']
        filename = file.filename
        print('req filename=', filename)
        save_path = os.path.join(UPLOAD_FILE_PATH, filename)
        print("save path=", save_path)
        result_msg, result_code = file_save(file, save_path)
        if result_code not in self.SUCCESS_CODE:
            return {'message': result_msg}, result_code

        print('===========================result===========================')
        print(result_msg, result_code)
        print('===========================================================')
        if result_code in self.SUCCESS_CODE:
            ocr_result_msg, ocr_result_code = ocr_text(save_path)

        return {'message': ocr_result_msg}, ocr_result_code



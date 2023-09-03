from flask import Flask
from flask_cors import CORS
from flask import request
import sheet

api = Flask(__name__)

@api.route('/get_all_sheet_name',methods=['POST','GET'])
def getallsheetname():
    res = sheet.get_all_sheet_name()
    return res

@api.route('/get_sheet_content',methods=['POST','GET'])
def getsheetcontent():
    req = request.form.to_dict()
    res = sheet.get_sheet_content(req['index'])
    return res

if __name__ == '__main__':
    CORS(api, supports_credentials=True)
    from gevent import pywsgi
    server = pywsgi.WSGIServer(('0.0.0.0',8089),api)
    server.serve_forever()

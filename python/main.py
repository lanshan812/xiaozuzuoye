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
    api.run(port=8089,debug=True,host='127.0.0.1') # 启动服务

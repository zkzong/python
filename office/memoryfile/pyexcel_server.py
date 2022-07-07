import sys
from flask import Flask, request, render_template, jsonify, make_response
import pyexcel as pe

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'excel' in request.files:
        # 处理上传文件
        filename = request.files['excel'].filename
        extension = filename.split(".")[1]
        # 获取文件扩展名和内容,传递一个元组而不是文件名。
        content = request.files['excel'].read()
        if sys.version_info[0] > 2:
            # 为了支持Python，必须将字节解码为STR。
            content = content.decode('ANSI')
        sheet = pe.get_sheet(file_type=extension, file_content=content)
        # 然后像往常一样使用它
        sheet.name_columns_by_row(0)
        # 用JSON回应
        return jsonify({"result": sheet.dict})
    return render_template('upload.html')


data = [
    ["REVIEW_DATE", "AUTHOR", "ISBN", "DISCOUNTED_PRICE"],
    ["1985/01/21", "Douglas Adams", '0345391802', 5.95],
    ["1990/01/12", "Douglas Hofstadter", '0465026567', 9.95],
    ["1998/07/15", "Timothy \"The Parser\" Campbell", '0968411304', 18.99],
    ["1999/12/03", "Richard Friedman", '0060630353', 5.95],
    ["2004/10/04", "Randel Helms", '0879755725', 4.50]
]


@app.route('/download')
def download():
    sheet = pe.Sheet(data)
    output = make_response(sheet.csv)
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output


if __name__ == "__main__":
    # 启动Web Server
    app.run()

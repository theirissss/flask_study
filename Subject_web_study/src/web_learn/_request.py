# # request包含前端发送过来的所有请求数据
# from flask import Flask, render_template,request
#
# app = Flask(__name__)
#
# @app.route('/index', methods=['GET', 'POST'])
# def index():
#     if request.method=='GET':
#         return render_template('_index.html')  # 模板渲染
#     if request.method=='POST':
#         name=request.form.get('name')
#         password=request.form.get('password')
#         print(name,password)
#         return 'this is post'
# #     if request.method == 'GET':
# #         # name = request.args.get("name") # 如果是 GET，要用 request.args.get("name")（因为是 URL 参数,直接从url里面就能看到）；
# #         # password=request.args.get('password') # 如果是 POST，用 request.form.get("name")（因为是请求体里的数据，必须从form里面获取拆封）；
# #         # print(name,password)
# #         return render_template('_index.html')
# #     if request.method == 'POST':
# #         name = request.form.get("name") # 如果是 GET，要用 request.args.get("name")（因为是 URL 参数）；
# #         password=request.form.get('password') # 如果是 POST，用 request.form.get("name")（因为是请求体里的数据）；
# #         print(name,password)
# #         return 'this is POST'
# if __name__ == '__main__':
#     app.run(debug=True)
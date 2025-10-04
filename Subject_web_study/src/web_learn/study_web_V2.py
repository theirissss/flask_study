"""重新学习web，Flask相关知识"""

# 轻量级后端框架
# 1.Flask路由，用来匹配url
# 2.request对象、abort
# 3.模板
# 4.数据库
# 5.form表单 前端表单提交post请求
# 6.ajax
# 7.管理系统小案例

import os
import typing as t

from flask import Flask,request

# app=Flask(__name__) # 实例化Flask类
# 搜索http://127.0.0.1:5000/，匹配到根目录‘/’，找到后端注册的@app.route('/')，与其键值对的视图函数是index，运行index，
# return得'<h1>hello world<h1>'，页面渲染
# @app.route('/') # 注册路由
# def index():
#     return '<h1>hello world<h1>'
#
# if __name__ == '__main__':
#
#     app.run()
# 客户端把请求发送给服务器，服务器把请求发送给网页，服务器把请求发送给Flask应用实例，需要知道url运行哪些代码，url和py路由形成一个映射关系

""""""
"""
端点才是员工号吧？毕竟‘唯一标识符’，路由比较自由，可以叫“AAA建材王哥”对外联系，函数名是真正的那个员工,或许有两个叫王富贵的呢？
"""
# app=Flask(__name__)
# # url和函数映射关系，指的是“url指向这个函数”
# @app.route('/hello',methods=['GET',"POST"],endpoint='hello_1') # 注册路由,映射函数hello(),不接受get请求
# # 405 Method Not Allowed（允许，支持） ‘The method is not allowed for the requested URL.’
# def hello():
#     print(f'端点{request.endpoint}')
#     return 'hello world'
#
# @app.route('/hi',methods=['GET',"POST"],endpoint='hello_2')
# def hello():
#     print(f'端点{request.endpoint}')
#     return 'hi hi'
#
# # print(app.url_map)
# # 当两个路由重名只匹配第一个
# if __name__ == '__main__':
#     app.run()

""""""
# app=Flask(__name__)
# # string：接受任何不包含斜杠的文本
# # int：接受正整数
# # float：接受正浮点数
# # path：接受包含斜杠的文本（路径）
# @app.route('/user/<float:id>')# 正则匹配,默认匹配str
# def index(id):
#     # if id=='1':
#     #     return 'python'
#     # if id==str(2):
#     #     return 'django'
#     # if int(id)==3:
#     #     return 'flask'
#     if id==1.1:
#         return 'python'
#     if id==2.2:
#         return 'django'
#     if id==3.3:
#         return 'flask'
#     return 'hello,world'
#
# if __name__ == '__main__':
#     app.run(port=8080)

"""自定义转化器"""
# from werkzeug.routing import BaseConverter  # 基础转换器
#
# app=Flask(__name__)
#
# class RegexConverter(BaseConverter):
#     """自定义转换器类"""
#     def __init__(self,url_map,regex):
#         super().__init__(url_map)
#         self.regex=regex
#
#     def to_python(self, value: str) -> t.Any: # 重写父类
#         print(f'to_python方法已被调用')
#         return value # 没有逻辑，只匹配，不加工
#
# app.url_map.converters['re']=RegexConverter # 注册转换器
#
# @app.route('/user/<re("123"):user_id>')# 正则匹配,默认匹配str,***路由变量名必须和函数形参完全一致，不然会报错***
# # for example:TypeError: index() got an unexpected keyword argument 'user_id'
# # for example:函数期望得到一个id=……的键值对，但是url传来一个user_id=……的键值对，导致关键字传参失败了
# def index(user_id):
#     print(user_id)
#     return 'hello,world'
# # print(app.url_map.__dict__)
# if __name__ == '__main__':
#     app.run(port=8000)

"""
自定义转换器类
总共需要三个参数，一个路由表（url_map/自动传入），一个匹配规则（regex/需显式传入），一个待转换值（value/自动传入，如上文的id）
"""

"""learn重定向（302）"""
# from flask import Flask,redirect,url_for,make_response,json,jsonify
#
# app=Flask(__name__)
# # app.config['JSON_AS_ASCII']=False
# @app.route('/index')
# def index():
#     data={
#         'name':'张三'
#     }
#     # response=make_response(json.dumps(data,ensure_ascii=False))
#     # response.mimetype='application/json'
#     response = jsonify(data)
#     response.data = json.dumps(data, ensure_ascii=False)# 我靠我tm真服了，上次百思不得其解的问题这次竟然无心插柳解决了
#     return response
#
# """
# ①make_response(data)，前端{"name":"\u5f20\u4e09"}，content-type application/json
# ②make_response(json.dumps(data))，前端{"name":"\u5f20\u4e09"}，content-type text/html; charset=utf-8
# ③make_response(json.dumps(data,ensure_ascii=False))，前端{"name": "张三"}，content-type text/html; charset=utf-8
# ④response=make_response(json.dumps(data,ensure_ascii=False))\nresponse.mimetype='application/json'，前端{"name": "张三"}，content-type application/json
# """
# # @app.route('/index')
# # def index():
# #     return redirect(url_for('hello')) # 返回字符串“/hello”
# # """两种重定向方式，一种直接写网址（可以用外部路由），一种用url_for（这种只能用自己的端点）***注意，这里用的是endpoint而不是func"""
# # @app.route('/hello')
# # def hello():
# #     return '<h1>this is hello<h1>'
#
# if __name__ == '__main__':
#     app.run(port=5050)

# abort约等于raise


# from flask import Flask,redirect,url_for,make_response,json,jsonify,abort,render_template
#
# app=Flask(__name__)
#
# @app.route('/index',methods=['GET',"POST"])
# def index():
#     if request.method=="GET":
#         return render_template('_index.html')
#     if request.method=='POST':
#         name=request.form.get('name')
#         password=request.form.get('password')
#         if name=='123'and password=='123':
#             return 'login success'
#         else:
#             return abort(404)
#
# @app.errorhandler(404) # 错误控制器,注册错误处理，“当发生 404 错误时，请调用这个函数来处理”
# def handle_404_error(err): # Flask调用handle_404_error 函数，并自动将这个"错误对象"作为第一个参数（err）传递进去(自动传参)
#     # return f'出现了404错误，错误类型是{err}'
#     return render_template('404.html') # 什么都没有？？？？？？？？
# """
# render_template('404.html')的'404.html'里面只有图片不行，还得有图片高宽，不然显示空白
# 只有高宽没有static（放在template里面）也不行，浏览器找不到
# 有static也不行，得是../static/404.png，因为绝对路径不行，没有static也不行
# 只有放在static包里面，路径为上一级路径../static/……，再有高宽才能显示，不如直接{{url_for('static',filename='_picture404.png')}}一劳永逸
# """
#
# if __name__ == '__main__':
#     app.run()

"""
开启模板学习jijia2
"""


#     data={
#         'name':'张',
#         'age':'18'
#     }
#     response=jsonify(data)
#
#     my_list=[1,2,3,4,5,6]
#     张三=[111,222]
#     return render_template('_index2.html',data=data,list=my_list,张三=张三)# 这个data给到的是前端，前端可以用模板操作来分别取值
    # # print(response.data,1)
    # print(response.__dict__)
    # print(request.__dict__)
# 这里关键字传参，并且关键字可以自定义，是的，可以随意命名，只要形参存在



# from flask import Flask,redirect,url_for,make_response,json,jsonify,abort,render_template
#
# app=Flask(__name__)
#
# @app.route('/',methods=['GET','POST'])
# def index():
#     if request.method=="GET":
#         return render_template('_index.html')
#     if request.method=='POST':
#         name=request.form.get('name')
#         password=request.form.get('password')
#         if name=='wangxinzhi' and password=='20040729':
#             return render_template('_nuli.html')
#         else:
#             abort(403)
# if __name__ == '__main__':
#     app.run()


"""
以前都是学习笔记，后面的是自己实践的项目=======================================================================================
"""


from flask import Flask,redirect,url_for,make_response,json,jsonify,abort,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import math

app=Flask(__name__)

app.config['SECRET_KEY']='iris_smith'
VERSION='0.02.00'
VERSION_TEXT='新增了输入验证'
"""
主版本号（Major）：当你做了不兼容的 API 修改
次版本号（Minor）：当你做了向下兼容的功能性新增
修订号（Patch）：当你做了向下兼容的问题修正
"""

class Input(FlaskForm):
    """
    输入验证的基类
    """
    input_value=StringField(label='默认标签',validators=[DataRequired()]) # 默认字段

    def __init__(self,labelname=None,**kwargs):
        super().__init__(**kwargs) # 调用超类
        if labelname: # 如果存在labelname
            self.input_value.label.text=labelname # 修改label文本/实例.类参数名.类参数（实例）的label属性.属性的text属性

@app.route('/')
def index():
    """
    这是首页的视图函数
    :return:
    """
    return render_template('project.html',version=[VERSION,VERSION_TEXT])

@app.route('/zuobiaozhengsuan',methods=['GET','POST'])
def zheng_zb(): # 坐标正算
    """
    这是坐标正算页面的视图函数
    :return:目标坐标的x，y值
    """
    form=[
    Input('请输入坐标x值'),
    Input('请输入坐标y值'),
    Input('请输入坐标方位角'),
    Input('请输入两坐标之间距离')]
    if request.method=="GET":
        return render_template('zuobiaozhengsuan.html',form=form)
    elif request.method=="POST":
        x0=float(form[0].input_value.data)
        y0=float(form[1].input_value.data)
        fangweijiao=float(form[2].input_value.data)
        l=float(form[3].input_value.data)
        alpha = math.radians(fangweijiao)
        x = x0 + l * math.cos(alpha)
        y = y0 + l * math.sin(alpha)
        data=[round(x,4),round(y,4)]
        return render_template('zuobiaozhengsuan_ok.html',data=data)

@app.route('/zuobiaofansuan',methods=['GET','POST'])
def fan_zb():
    """
    这是坐标反算的视图函数
    :return:两坐标之间的方位角和距离
    """
    form=[
    Input('请输入A坐标x值'),
    Input('请输入A坐标y值'),
    Input('请输入B坐标x值'),
    Input('请输入B坐标y值')]
    if request.method=="GET":
        return render_template('zuobiaofansuan.html',form=form)
    elif request.method=="POST":
        print(request.form.__dict__)
        xi=float(form[0].input_value.data)
        yi=float(form[1].input_value.data)
        x0=float(form[2].input_value.data)
        y0=float(form[3].input_value.data)
        # xi=float(request.form.get('xi'))
        # yi=float(request.form.get('yi'))
        # x0=float(request.form.get('x0'))
        # y0=float(request.form.get('y0'))
        delta_x = xi - x0
        delta_y = yi - y0
        d_param = delta_x ** 2 + delta_y ** 2
        d = math.sqrt(d_param) # 距离
        alpha = math.atan2(delta_y, delta_x) # 角度
        print(xi,yi,x0,y0)
        print(d,alpha)
        data=[round(d,4),alpha]
        return render_template('zuobiaofansuan_ok.html',data=data)

@app.route('/.well-known/appspecific/com.chrome.devtools.json')
def response_to_chrome_devtools():
    """
    我认为有必要骂探针一句
    :return: "fuck you", 200
    """
    return "fuck you", 200

if __name__ == '__main__':
    app.run(port=8080)




import logging
import os
import json
import inspect
from hashlib import sha256

# ------------------------日志配置区------------------------
#
# LOG_FILE = 'my_logging.log'
# RECORD_FILE = '.logged_once_auto.json'
#
# # 初始化 logging（只初始化一次）
# if not logging.getLogger().handlers:
#     # 文件输出（仅你自己使用）
#     logging.basicConfig(
#         format='%(levelname)s (%(asctime)s): %(message)s (Line:%(lineno)d [%(filename)s])',
#         datefmt='%d/%m/%Y %I:%M:%S %p',
#         level=logging.DEBUG,
#         filename=LOG_FILE,
#         encoding='utf-8'
#     )
#
#     # 控制台输出（所有日志共享）
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.DEBUG)
#     console_handler.setFormatter(logging.Formatter(
#         '%(levelname)s (%(asctime)s): %(message)s (Line:%(lineno)d [%(filename)s])',
#         datefmt='%d/%m/%Y %I:%M:%S %p'
#     ))
#     logging.getLogger().addHandler(console_handler)
#
#     # 设置 werkzeug 日志器（只输出到控制台）
#     werkzeug_logger = logging.getLogger('werkzeug')
#     werkzeug_logger.handlers.clear()  # 清除继承的文件 handler
#     werkzeug_console = logging.StreamHandler()
#     werkzeug_console.setLevel(logging.INFO)
#     werkzeug_console.setFormatter(logging.Formatter(
#         '[Werkzeug] %(message)s'
#     ))
#     werkzeug_logger.addHandler(werkzeug_console)
#     werkzeug_logger.propagate = False  # 防止向上冒泡写入文件
#
# # ------------------------log_once 工具区------------------------
#
# # 读取记录文件
# if os.path.exists(RECORD_FILE):
#     with open(RECORD_FILE, 'r', encoding='utf-8') as f:
#         _log_record = json.load(f)
# else:
#     _log_record = {}
#
# def _generate_log_id():
#     """根据调用位置自动生成唯一 log_id"""
#     frame = inspect.stack()[2]
#     filename = os.path.abspath(frame.filename)
#     lineno = frame.lineno
#     raw = f"{filename}:{lineno}"
#     return sha256(raw.encode()).hexdigest()
#
# def log_once(message, level='info'):
#     log_id = _generate_log_id()
#     if log_id not in _log_record:
#         getattr(logging, level)(message)
#         _log_record[log_id] = True
#         with open(RECORD_FILE, 'w', encoding='utf-8') as f:
#             json.dump(_log_record, f, indent=2, ensure_ascii=False)
#
# # ------------------------测试调用区------------------------
#
# log_once('你好')


# logging.basicConfig(level=logging.DEBUG)
# logging.debug("DEBUG") # 诊断问题
# logging.info("DEBUG") # 确认程序按预期执行 # 翻译：资料
# logging.warning("DEBUG") # 发生了某种以外状况，但程序仍然会继续运行 # 从这里开始显示 # 翻译：警告
# logging.error("DEBUG") # 当程序无法运行
# logging.critical("DEBUG") # 程序无法继续运行，严重的问题 # 翻译：至关重要的，危急的

# import typing as t
# from flask import Flask
# # """最小应用案例"""
# app=Flask(__name__) # 这里必须传参
# print(__name__) # 这里必须要传参，因为其他参数都有默认值（eg：None）但是他没有，所以必须传参
# @app.route('/')
# def index():
#     return 'hello,world'
#
# if __name__=="__main__":
#     app.run() # debug=True
#
# """
# * Serving Flask app 'web_study'  # 你的Flask应用名称（默认取文件名）
# * Debug mode: on                # 调试模式已开启（代码修改会自动重启服务）
# WARNING: This is a development server...  # 安全提示（见下方说明）
# * Running on http://127.0.0.1:5000  # 本地访问地址
# Press CTRL+C to quit            # 停止服务器的方法
# * Restarting with stat          # 调试模式下检测到文件变化会自动重启
# * Debugger is active!           # 调试器已激活（浏览器可显示错误详情）
# * Debugger PIN: 549-624-233     # 调试器安全PIN码（用于访问调试界面）
# """
"""====================================================================================================================="""
#==========================================================================================================================
"""
轻量级的后端框架
1.flask路由  用来匹配url
2.requests对象  abort函数
3.模板(eg：html)
4.flask数据库  
5.表单（例如输入密码就是提交数据）
6.ajax
7.管理系统小案例
"""
"""
class Flask:
    def __init__(self):
        self.url_map = {}  # 空路由表：准备存储 路径 → 函数对象 的映射

# @app.route('/') 是 app.route('/')(hello_world) 的语法糖*** # 这里传了两个参数，一个是路由('/')，一个是函数(hello_world)

    def route(self, path):
        def decorator(func):
            self.url_map[path] = func  # 注册：path → 函数对象本身（不是函数返回值！）# url_map 实际存储的是：{'/': <function home at 0x7f8b7c3b5e18>}
            return func  # 确实返回原函数，不做修改
        return decorator
"""
"""
app = Flask()

# 以下代码：
@app.route('/')
def home():
    return "Hello"

# 等价于：
def home(): ...  # 1. 先定义函数
home = app.route('/')(home)  # 2. 应用装饰器
#            ↑ 先执行app.route('/')返回decorator
#                     ↑ 再执行decorator(home)
"""
"""
所以，完整流程：
定义阶段：

python
@app.route('/')  # 等价于 home = app.route('/')(home)
def home():
    return "Hello"
app.route('/') 执行后返回 decorator 函数
decorator(home) 做了两件事：
注册映射：url_map['/'] = home（存储函数对象）
返回原函数：return home（不修改函数）
→ 此时 url_map = {'/': <function home at 0x...>}

访问阶段：
当用户访问 http://xxxx.com/ 时：
Flask 内部查找 url_map 发现 '/' 对应 home 函数
执行 home() 得到返回值 "Hello"
将 "Hello" 作为HTTP响应返回给用户
"""
# # # 导入库
# from flask import Flask
# # 创建实例
# app = Flask(__name__)
# # 创建url_map键值对，注册路由
# @app.route('/')
# def home():
#     # 返回包含可点击链接的HTML
#     return """
#     <h1>hello，好久不见</h1>
#     <a href="/about">点击叙叙旧</a>
#     """
#
# @app.route('/about')
# def about():
#     return "<h1>hello,my friend</h1>"
# # 单元测试
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8000)

"""
HTTP 状态码速查:
2xx：成功（如 200 OK）
3xx：重定向（如 301 永久移动）
4xx：客户端错误（如 400 错误请求、403 禁止访问）
5xx：服务器错误（如 500 内部错误）
"""
# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/crash")
# def crash():
#     raise ValueError("这是一个故意制造的异常！")  # 未处理的异常 → 500
#
# app.run()

# def jisuanqi(x,y):
#     return x+y

# from flask import Flask
#
# app=Flask(__name__)
#
# @app.route('/hello',methods=['GET','POST']) # '/'表示匹配根目录，直接在浏览器输入网址就是get请求（突然想起以前学过的爬虫request.get）
# def say_hello(): # 这里必须是methods，不是method
#     return '<h1>HELLO</h1>'
#
# @app.route('/hi',methods=['POST'])
# def say_hi():
#     return '<h1>hi hi</h1>'
#
# # @app.route('/jisuan')
# # def ji_suan(x,y):
# #     result = jisuanqi(x,y)  # 显式调用可信函数
# #     return str(result)
# # string：接受任一不包含斜杠的文本
# # int：接受正整数
# # float：接受浮点数
# # path：接受包含斜杠的文本,即‘路径’
# @app.route('/user/<float:id>')# <>表示动态参数/提取参数，<float：id>转换器
# def index(id):
#     if id==2.1: # 因为URL传进来的是字符串，不是int
#         return 'python'
#     if id==2.2:
#         return 'django'
#     if id==2.3:
#         return 'flask'
#     return 'hello,world'
#
# if __name__ == '__main__':
#     app.run(debug=True)
"""
<Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>
部分	含义
'/static/<filename>'	路由路径，匹配以 /static/xxx 开头的 URL，xxx 会传给 filename 参数
<filename>	路由参数，会匹配任意字符串（使用 string 转换器）
(OPTIONS, HEAD, GET)	支持的 HTTP 方法
-> static	endpoint 名为 'static'，Flask 内部使用，用于寻找处理函数
"""
# from werkzeug.routing import BaseConverter # 自定义转换器必须导入的包
# from flask import Flask
#
# app=Flask(__name__)
#
# class RegexConverter(BaseConverter):
#     """
#     自定义转换器类
#     总共需要三个参数，一个路由表（url_map/自动传入），一个匹配规则（regex/需显式传入），一个待转换值（value/自动传入，如上文的id）
#     """
#     def __init__(self,url_map,regex):# regex翻译正则表达式，__init__(url_map)需要显式传参是因为父类明确需要这个参数self.url_map = url_map
#         super(RegexConverter,self).__init__(url_map)# super(RegexConverter,self)是python2时代的旧写法了，但是__init__(url_map)确实需要显式传参
#         self.regex=regex
#
#     def to_python(self, value: str) -> t.Any:
#         # 父类的方法，功能已经实现好了
#         print("to_python方法被调用")
#         return value
#     """
#     rule._regex = "(?P<uid>[0-9]+)"这句看懂了，怪不得不用导re，原来所谓‘int’的底层也是re，我不过是把[0-9]+换成了^1[5-9]{2}\d{8}$而已
#     """
# # 将自定义的转换器类添加到flask中
# """
# @app.route("/user/<int:uid>")
# 这里的 <int:uid>，不是字符串替换语法，而是告诉 Flask：“请用名叫 'int' 的转换器类，来解析这个 uid 的部分。”
# """

# app.url_map.converters['re']=RegexConverter # {'re':RegexConverter}
#
# @app.route('/index/<re(r"^1[5-9]{2}\d{8}$"):value>') # 所有类型匹配的底层都是re
# def index(value):
#     print(value)
#     return 'hello,world'
#
# if __name__ == '__main__':
#     app.run()

"""浏览器发请求(get) → 
url_map 解析(到app.url_map里面找类型键，默认string) → converters 找到该键的对应值的正则匹配(此时实例化类)(例如:<int>就是(?P<uid>[0-9]+)) → 
to_python(执行该方法) → 视图函数执行(前文匹配完成后执行视图函数)"""

from werkzeug.routing.converters import UnicodeConverter
"""
app.url_map
│
├── rules (真实路由映射：每条URL对应哪个函数)
│     └── Rule("/", endpoint="home", methods=["GET"])
│
└── converters（关键词 → 转换器类）
      ├── "int"    → IntegerConverter
      ├── "float"  → FloatConverter
      ├── "path"   → PathConverter
      ├── "re"     → RegexConverter（你自己加的）
      └── ...
Flask 解析 <int:uid>，查找 url_map.converters['int']
创建一个 IntegerConverter 实例，把它嵌入 Rule("/user/<uid>")
这个 Rule 最终存入 url_map.rules（即真正的路由列表）
当请求到达 /user/42 时：
Flask 用正则匹配这个 Rule
匹配成功后调用 IntegerConverter.to_python("42") → 得到 Python 整数 42
把 uid=42 作为参数传入 get_user(uid)

"""

# print(app.url_map)
# print(app.url_map.converters)

"""request包含前端发送过来的所有请求"""

# from flask import Flask,render_template,request
#
# app=Flask(__name__)
#
# @app.route('/')
# def home():
#     print("主页被访问了")
#     return "hello,world"
#
# @app.route('/index',methods=['GET','POST'])
# def index():
#     if request.method == 'GET':
#         # name = request.args.get("name") # 如果是 GET，要用 request.args.get("name")（因为是 URL 参数,直接从url里面就能看到）；
#         # password=request.args.get('password') # 如果是 POST，用 request.form.get("name")（因为是请求体里的数据，必须从form里面获取拆封）；
#         # print(name,password)
#         return render_template('_index.html')
#     if request.method == 'POST':
#         name = request.form.get("name") # 如果是 GET，要用 request.args.get("name")（因为是 URL 参数）；
#         password=request.form.get('password') # 如果是 POST，用 request.form.get("name")（因为是请求体里的数据）；
#         print(name,password)
#         return 'this is POST'
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
"""
| 标签             | 正确术语                 | 说明                       |
| --------------- | -------------------     | -----------------         |
| `<form>`        | 表单（form）             | HTML 标签中用于提交数据的容器 |
| `<input>`       | 表单控件（input element） | 单个输入框、按钮、密码框等    |
| `name="xxx"`    | 字段名                   | 后端用来取值的“键”          |
| `method="post"` | 表单提交方式              | GET/POST/PUT 等           |
| `action=""`     | 提交目标地址              | 留空 = 当前 URL            |
"""
'''
GET：如果把改成<form method="get">，那么浏览器会明文显示http://127.0.0.1:5000/index?name=123&password=456，不安全
POST：浏览器地址仍然是 /index，但数据是藏在请求体（request body）里的，不会暴露在地址栏上。
结论：提交密码、登录信息、私密表单时，必须用 POST。
'''

# from flask import Flask,redirect,url_for # redirect重定向,url_for
#
# app=Flask(__name__)
# # print(app.url_map)
# @app.route('/index') # 等价于app.add_url_rule('/submit', 'submit', submit, methods=['POST']（可选）)
# def home():
#     # return redirect('https://www.baidu.com') # redirect重定向
#     return redirect(url_for('hello')) # 所以这里用的函数名（endpoint端点），而不是路由（rule），如果路由改变，可以找到端点对应的新路由，然后执行
#     # url_for：转到另一个路由，也可以redirect('/123')
# @app.route('/123')
# def hello():
#     return 'this is hello haha'
#
# if __name__ == '__main__':
#     app.run()
# from flask import Flask, jsonify
#
# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False  # 关键配置：禁用 ASCII 转义
#
# @app.route('/')
# def index():
#     data = {'name': '张三'}
#     return jsonify(data)  # 自动处理中文
#
# if __name__ == '__main__':
#     app.run()
# from flask import Flask,make_response,json,jsonify # make_response传输数据
#
# app=Flask(__name__)
# app.config['JSON_AS_ASCII']=False
#
# @app.route('/')
# def index():
#     data={
#         'name':'张三'
#     }
#     #             ④       ③json处理   ①本体      ②限定格式
#     response=make_response(json.dumps(data,ensure_ascii=False)) # ensure翻译：确保
#     response.mimetype='application/json' # mime多用途互联网邮件扩展：application（类型）/json（子类型）
#     return response
#
# if __name__ == '__main__':
#     app.run()

"""abort 在网页中主动抛出异常"""
# from flask import Flask,abort,request,render_template # 导包1（导4个）
#
# app=Flask(__name__) # 创建实例2
#
# @app.route('/index',methods=['GET',"POST"]) # 注册路由，并指定访问方式3（注意是methods）
# def index(): # 定义视图函数4
#     if request.method=="GET": # 访问url,4.1（request.method是字符串）
#         return render_template('_index.html') # 链接（render_template模板渲染）
#     if request.method=='POST': # 还是原本的URL，只不过提交数据4.2
#
#         name=request.form.get('name') # 获取提交的数据的name键的值，并赋值给变量name
#         password=request.form.get('password') # 获取password的值，并赋值给password
#         if name=='zhangsan'and password=='123': # 条件判断4.2.1
#             print(request.form)
#             print(name,password)
#             return '登录成功'#判断成功
#         else:
#             abort(404) # 判断失败，abort主动抛出异常4.2.2
#
# if __name__ == '__main__':# 测试5
#     app.run(port=8000)# 创建实例6

# from flask import Flask,request,render_template,abort
#
# app=Flask(__name__)
#
# @app.route('/index',methods=['GET','POST'])
# def index():
#     if request.method=='GET':
#         return render_template('_index.html')
#     if request.method=="POST":
#         name=request.form.get('name')
#         password=request.form.get('password')
#         print(name,password)
#         if name=='zhangsan'and password=='123':
#             return '登录成功'
#         else:
#             abort(403)
#
# """自定义错误"""
# @app.errorhandler(403)
# def handle_404_error(error):
#     return render_template('403.html'),403
# """这三行才是今天的重点，第一行注册错误代码的视图，第二行定义视图函数，第三行链接模板渲染（包含静态资源的调用）
# 当我把abort(403)和@app.errorhandler(403)都由404换成403时又成功运行了，说明该路由与主动报错强相关"""
# if __name__ == '__main__':
#     app.run(port=8080,debug=True)
# import socket
#
# def is_port_in_use(port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         return s.connect_ex(('localhost', port)) == 0
#
# print(is_port_in_use(8080))  # True 表示已被占用
"""
今天学了什么
make_response构造响应
render_template模板渲染
methods请求方法
static静态资源（例如图片）
僵尸进程占用端口↑
主动抛出异常（abort）及其视图函数注册@app.errorhandler(404) 
注：必须是和abort相同的状态码才行，比如我把@app.errorhandler(404)改成403就不是该视图了

"""

# from flask import Flask,request,render_template,abort
#
# app=Flask(__name__)
#
# @app.route('/') # 第一层接受路由'/'，第二层接受函数index，第三层接受函数参数（这里没有）
# def index():
#     data={'name':'iris',
#           'age':18,
#           'mylist':[0,1,2,3,4,5,6]}
#     return render_template('index_2.html',data=data)
#
# def list_step(li):# 关键=====================================
#     """自定义过滤器"""
#     return li[::2] # 把原列表切片# 关键=====================================
#
# app.add_template_filter(list_step,'li2')# 关键=====================================
#
# if __name__ == '__main__':
#     app.run()

# """自定义装饰器"""
# def filter_zhuangshi(name_new):
#     def zhuangshi_filter(func):
#         app.add_template_filter(func, name_new)
#         return func
#     return zhuangshi_filter
# """原来官方有过滤器装饰器，那我这个自定义没用了"""

"""
2025年6月27日00:36:53，今天学了什么？
render_template()把后端数据返回给模板，模板编辑处理数据（eg：data.mylist，data.name）
模板的基础使用①{{……}}相当于print②{%……%}相当于py语句③{#……#}相当于注释
过滤器：使用：相当于func()，语法“ | func ”，注册：self.add_template_filter(func,'name_new/old')
再次探索装饰器原理：外层传参（函数），内层传参（原函数的参数）///特例：更外层传参（注册键）
以及，冷饭新炒，彻底放弃jsonify，根本传不出去汉语json，注意self.mimetype='application/json'
"""
"""
from flask import Flask, render_template,request
from flask_wtf import FlaskForm  # Flask 的表单基类
from wtforms import StringField, PasswordField, SubmitField  # 表单字段类型
from wtforms.validators import DataRequired, EqualTo  # 验证器

app=Flask(__name__)

app.config['SECRET_KEY']='IRIS'
# 定义表单模型类
class Register(FlaskForm): # 对应第三行import，继承FlaskForm，所有表单都要继承这个基类，Register翻译：注册
    user_name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')]) # va'li'da'tors验证
    password = PasswordField(label='请输入密码',validators=[DataRequired('密码不能为空')]) # E夸
    password2 = PasswordField(label='请确认密码',validators=[DataRequired('密码不能为空'),EqualTo('password')]) # Field字段
    # 对应第四行import，DataRequired验证是否为空，EqualTo验证两次输入是否相同（所以以上代码在调用框里面写了'password'
    submit=SubmitField(label='提交') # 不需要填东西所以没有validators（验证）data required（数据必填）Equal to（等于）


@app.route('/',methods=['GET','POST'])
def register(): # 翻译：注册
    # 创建表单对象
    form =Register()
    if request.method=="GET":
        return render_template('_register.html', form=form)
    if request.method=="POST":
        # 验证器form.validate_on_submit()
        if form.validate_on_submit():
            username=form.user_name.data
            password=form.password.data
            password2=form.password2.data
            print(username,password,password2)
        else:
            print('验证失败')
        return render_template('_register.html', form=form)

if __name__ == '__main__':
    app.run()
"""
# log_once('今天是2025年6月29日01:02:39')
# log_once('今天开始学数据库了')
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app=Flask(__name__)
#
# class Config:
#     """配置参数"""
# SQLALCHEMY_DATABASE_URL=''
"""
============= API 核心知识体系 =============
→ 关键词：#契约层 #协议 #请求响应 #Python实现

1. 【本质定义】
   - API = 应用程序接口 (Application Programming Interface)
   - 核心角色：软件组件间的「通信契约」，规定交互规则而不暴露实现细节
   - 类比：插座系统（API=插座设计标准，请求=插入插头，响应=获得电力）

2. 【与Web和协议的关系】
   ● Web：基于HTTP协议的超文本信息系统（用户通过浏览器访问）
   ● 协议：更底层的通信规则（如HTTP/TCP/IP），相当于「宪法」
      → HTTP定义：请求方法(GET/POST)、状态码(200/404)、消息结构
   ● API：构建在协议之上的业务规则，相当于「法律」
      → 规定：资源路径(/users)、数据格式(JSON)、认证方式

3. 【请求-响应全流程】
   ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
   │  客户端       │──请求─▶│  API服务端    │──响应─▶│  客户端       │
   │ - 构造请求    │       │ 1. 认证鉴权    │       │ - 解析数据     │
   │ - 发送数据    │◀──────│ 2. 业务逻辑    │◀──────│ - 处理错误     │
   └──────────────┘       │ 3. 数据库操作  │       └──────────────┘
                          └──────────────┘

4. 【请求四要素】 (Python requests库示例)
   ✓ 方法类型  : GET(查) / POST(增) / PUT(改) / DELETE(删)
   ✓ URL端点   : 资源定位符 (e.g. `https://api.com/users`)
   ✓ 请求头    : 元数据容器 (认证/格式声明)
        headers = {"Authorization": "Bearer token", "Content-Type": "application/json"}
   ✓ 请求体    : 传输业务数据 (POST/PUT专用)
        data = {"name": "Alice", "email": "alice@example.com"}
        
5. 【高级认知】
   ● 协议是土壤，API是作物 → 没有HTTP协议，API无法存在
   ● 优秀API设计原则：
      - 无状态性：每个请求包含完整上下文
      - 版本控制：`/v1/users` → `/v2/users`
      - 超媒体驱动(HATEOAS)：响应中携带后续操作链接
   ● 生产级实践：
      - 异常处理：捕获网络超时/JSON解析错误
      - 重试机制：对瞬时错误自动重试
      - 速率限制：避免触发API的429错误

# 每日自问：
1. GET请求的params和POST的json参数区别是？ 
2. 为什么POST请求更适合传输敏感数据？
3. HTTP状态码200/401/404/500分别代表什么？
"""
# file_1='D:\study_py\py-learn\python_web_study\web_study_old_1.py'
# file_2='D:\study_py\py-learn\Subject_web_study\_study_web_V1.py'
# with open(file_1,'r',encoding='utf-8') as f1, open(file_2,'w',encoding='utf-8') as f2:
#     content=f1.read()
#     f2.write(content)

# print('hello world')

#
# print(os.getcwd())
#
# print(os.listdir('\AAA_new_program\Subject_web_study'))
# print(os.getcwd())
# open(r'D:\AAA_new_program\Subject_web_study\src\web_learn\study_web_V2.py','w')


from flask import Flask, request,render_template
from flask_wtf import FlaskForm# 导入相关库（中的类，用以继承重写） 表单基类
from wtforms import StringField,PasswordField,SubmitField # 字段 # 类型
from wtforms.validators import DataRequired,EqualTo # 验证

app=Flask(__name__)

app.config['SECRET_KEY']='irissmith' # 秘钥

class Register(FlaskForm):
    user_name=StringField(label='用户名',validators=[DataRequired('用户名不能为空')]) # 实例化字段类
    password=PasswordField('密码',validators=[DataRequired('密码不能为空')])
    password2=PasswordField('密码',validators=[DataRequired('密码不能为空'),EqualTo('password')])
    submit=SubmitField('提交')

# A secret key is required to use CSRF.跨站请求伪造500
@app.route('/register',methods=['GET',"POST"])
def register():
    # 创建表单对象
    form=Register()
    # user_name=request.form.
    if request.method=='GET':
        return render_template('_register.html',form=form)
    elif request.method=='POST':
        name_user=form.user_name.data
        password=form.password.data
        password2=form.password2.data
        return '666'

if __name__ == '__main__':
    app.run()






















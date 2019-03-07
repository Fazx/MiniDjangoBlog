
## 生产环境下需要注意的

### 环境隔离

使用`virtualenv`创建单独的虚拟运行环境，无论是学习开发(**方便管理**)还是在生产环境(**避免依赖冲突**)都是很有必要的。

![](http://ww1.sinaimg.cn/large/b12bdb25ly1g0tg01pnn1j20du05ejrf.jpg)

### 安全

- 关闭DEBUG模式，但需要添加处理404页面
- 保护好`SECRET_KEY`，别直接一股脑都传gayhub了
- 更改默认的admin管理路径
- 使用Django提供的ORM以避免注入
- 设置`ALLOWED_HOSTS`
- API调用安全...目前还不会
- CSRF Token，下面会专门再提到

### 稳定

- 使用`Gunicorn`或`uWSGI`作为网关接口服务以替换Django自带的WSGI
- 增加一层Nginx反向代理，处理静态资源等
- 使用`supervisor`守护Django进程，避免意外中断导致Web服务宕机

## Others

### Templates

模板文件最好建立自己的命名空间，也就是放入和自身应用同名的文件夹中。这是因为Django无法区分多个应用中重名的模板文件。

### Migrate

改变模型需要这三步：

- 编辑 `models.py` 文件，改变模型。
- 运行 `python manage.py makemigrations` 为模型的改变生成迁移文件。
- 运行 `python manage.py migrate` 来应用数据库迁移。

> 每当你修改了models.py文件，都需要用makemigrations和migrate这两条指令迁移数据。


![](http://ww1.sinaimg.cn/large/b12bdb25ly1g0tg0dwyarj20qr0ah3zu.jpg)

使用`python3 manage.py sqlmigrate blog 0001`可以将数据库的迁移文件转换成SQL语句查看。

![](http://ww1.sinaimg.cn/large/b12bdb25ly1g0tg0t0z7vj20n40a3jt7.jpg)


### Django Filter

过滤器： `{% raw %}{{ value | filter }}{% endraw %}`

对接Markdown解析器时，Django出于安全考虑会将HTML转义，在使用markdown组件时会造成渲染的HTML无法正常显示，因此需要添加safe过滤器 `{% raw %}{{ article.body|safe }}{% endraw %}`，告诉Django这段字符不需要转义。

### CSRF Token

所有针对内部URL的POST表单都应该使用CSRF Token模板标签，在base模板页面中添加`{% raw %}{% csrf_token %}{% endraw %}`是最简洁的方法。

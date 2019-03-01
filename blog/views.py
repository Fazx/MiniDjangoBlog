import markdown

from django.shortcuts import render,redirect # redirect重定向

from django.http import HttpResponse

from .forms import ArticleForm

# import User model
from django.contrib.auth.models import User

# Create your views here.

from .models import Article

# write articles
def article_create(request):
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("blog:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'blog/create.html', context)

# 文章列表
def article_list(request):
    # fetch all articles
    articles = Article.objects.all()
    # 传递给模板对象
    context = { 'articles': articles }
    # render函数载入模板并返回context对象
    return render(request,'blog/list.html',context)

# 文章详情
def article_detail(request,id):
    article = Article.objects.get(id=id) # id为自动生成的pk

    # 渲染markdown为html样式
    article.body = markdown.markdown(article.body,
        extensions=[
            # 缩写、表格等常用扩展
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request,'blog/detail.html',context)

def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect("blog:article_list")
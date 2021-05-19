from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

# 계획 -> 주소, urls.py -> 기능. 함수. views.py -> 출력(탬플릿)

# 아 홈화면 만들거야. -> 주소? '127.0.0.1' -> 모든 블로그글을 보여주면 views.py -> 출력 (템플릿, html, 탬플릿태그)


def home(request):
    blog_articles = Blog.objects.all()
    return render(request, "index.html", {"articles": blog_articles})


# 글쓰는 기능. -> 글쓰는 그 폼(박스) 페이지를 보여주고 저장하게 하자.


# 글쓰는 화면을 만들거에요 -> /postnew 주소 -> 기능? 화면을 보여줘야. views -> 템플릿코드 form.
#-> /postcreate 주소로 그 화면에서 저장을 하는 기능. postcreate는 views 함수. -> 템플릿코드.


def postcreate(request):
    # 글쓰는 화면으로 이동 (글쓰는 화면을 보여준다)
    # 리퀘스트, 질의가 어떤방식? get, post, 지금의 로그인한 유저정보 (세션정보)... 인증정보...

    if (request.method == "POST"):
        post = Blog()
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.save()
        return redirect("home")
    else:
        return render(request, "postnew.html")

# 계획 -> 주소, urls.py -> 기능. 함수. views.py -> templates(html), 템플릿태그(홈,틈).
# read -> 주소, detail -> 기능은 내용을 보여주는거. views -> 탬플릿 html. 틈~(home);
# read -> 주소, detail/<id> -> 기능은 내용을 보여주는거. views -> 탬플릿 html. 틈~(home);

def detail(request, post_id):

    one_post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'detail.html', {'article': one_post})

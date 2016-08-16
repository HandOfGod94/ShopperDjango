from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def user_comment(request):
    return render(request, "user_comment.html", {})

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login


class UserIndexView(TemplateView):
    template_name = "user/index.html"


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/inventory')
        else:
            return render(request, 'user/index.html', {'error_message': 'Invalid login. Please try again.'})
    else:
        return render(request, 'user/index.html')

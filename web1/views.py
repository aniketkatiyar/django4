from django.shortcuts import render


from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        # fm = UserCreationForm(request.POST)
        # if fm.is_valid():
        #     fm.save()
        # else:
        #     fm = UserCreationForm()
        return HttpResponseRedirect(request, "signup.html", {'form': UserCreationForm})
    # {'form': fm})


def about(request):
    return render(request, "about.html")


def services1(request):
    return render(request, "services1.html")


def services2(request):
    return render(request, "services2.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")


def login(request):
    return render(request, "login.html")

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user_profile.models import MainCycle
from user_profile.forms import UserForm


def user_login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return True, 'index', {}
        else:
            return False, 'login.html', {'invalid': True}
    else:
        return False, 'login.html', {'invalid': False}


def user_logout(request):
    logout(request)
    return 'login'


def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            mainCycle = MainCycle()
            mainCycle.user = user
            mainCycle.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return True, 'index', {}
        else:
            return False, 'registration.html', {'invalid': True, 'form': form}
    else:
        form = UserForm()
        return False, 'registration.html', {'invalid': False, 'form': form}

# def user_registration(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         existing_user = User.objects.filter(username=username)
#         if len(existing_user) == 0:
#             password = request.POST["password"]
#             if not check_password_safety(password):
#                 return render(request, 'registration.html', {'invalid': True})
#             user = User.objects.create_user(username, '', password)
#             user.save()
#             mainCycle = MainCycle()
#             mainCycle.user = user
#             mainCycle.save()
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return render(request, 'index.html', {'user': user})
#         else:
#             return render(request, 'registration.html', {'invalid': True})
#     else:
#         return render(request, 'registration.html', {'invalid': False})
#
#
# def check_password_safety(password):
#    pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{6,}$')
#    return pattern_password.match(password)

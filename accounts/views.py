from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.role == "supervisor":
                return redirect("dashboard")

            elif user.role == "inspector":
                return redirect("dashboard")

            elif user.role == "supplier":
                return redirect("dashboard")

            return redirect("dashboard")

    else:
        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


def logout_view(request):
    logout(request)
    return redirect("login")
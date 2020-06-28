from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "Thanks for visiting, see you again soon!")
    return redirect(reverse('home'))


def register(request):
    """Allow new user to create account"""
    if request.user.is_authenticated:
        # Prevent logged in user from going back to login page
        messages.success(request, request.user.first_name +
                         ", you are already signed in!")
        return redirect(reverse('index'))
    if request.method == "POST":
        # Register the user using form data
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome, " + user.first_name +
                                 "! Your account was successfully created.")
                return redirect(reverse('test'))
            else:
                registration_form.add_error(
                    request("Sorry, we are unable to register your account at this time."))

    else:
        registration_form = UserRegistrationForm
    context = {
        "form": registration_form,
        "form_title_upper": "Create a new account",
        "form_title_lower": "Register now!",
        "button_text": "Create account",
        "wrong_page_redirect": "<p>Do you already have an account? " +
                               "You can <a href='/accounts/login'>sign in</a> instead.</p>"
    }
    return render(request, "form.html", context)


def login(request):
    """Return Login page"""
    if request.user.is_authenticated:
        # Prevent logged in user from going back to login page
        messages.success(request, request.user.first_name +
                         ", you are already signed in!")
        return redirect(reverse('test'))
    if request.method == "POST":
        # Log in the user using form data
        form = UserLoginForm(request.POST)

        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Welcome, " + user.first_name + "!")
                return redirect(reverse('test'))
            else:
                form.add_error(None, "Your username or password is incorrect.")
    else:
        form = UserLoginForm
    context = {
        "form": form,
        "form_title_upper": "Welcome back!",
        "form_title_lower": "Please log in",
        "button_text": "Log me in",
        "wrong_page_redirect": "<p><strong>If you were redirected here after password reset, " +
                               "please sign in again with your new password.</strong></p>" +
                               "<p>If you forgot your password, you can " +
                               "<a href='password-reset'>reset</a> it.</p>" +
                               "<p>You don't have an account yet? " +
                               "You can <a href='register'>sign up</a> instead.</p>"
    }
    return render(request, "form.html", context)


def testpage(request):
    return render(request, "testpage.html")
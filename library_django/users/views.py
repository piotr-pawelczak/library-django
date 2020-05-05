from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.surname = form.cleaned_data.get('surname')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.street = form.cleaned_data.get('street')
            user.profile.city = form.cleaned_data.get('city')
            user.profile.post_code = form.cleaned_data.get('post_code')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            if form.cleaned_data.get('profile_picture'):
                user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.rules_agreement = form.cleaned_data.get('rules_agreement')
            user.profile.pesel = form.cleaned_data.get('pesel')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            messages.success(response, 'User successfully registered')
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(response, user)
            return redirect('../login/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(response, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            username = user_update_form.cleaned_data.get('username')
            messages.success(request, f"profile upgraded for {username}")
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    profile = Profile.objects.filter(user=request.user).first()
    context = {'user_update_form': user_update_form,
               'profile_update_form': profile_update_form,
               'profile': profile}

    return render(request, 'users/profile.html', context)


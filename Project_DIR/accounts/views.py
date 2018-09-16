from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

@login_required() #only logged in users should access this
def edit_user(request):
    pk = request.user.pk
    #querying the User object with pk from url
    user = User.objects.get(pk=pk)

    #populate the available User modal info 
    user_form = UserForm(instance=user)

    #appending UserProfile modal with User modal
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('photo','bio', 'website', 'role', 'organization', 'github_handle', 'linkedin_handle', 'irc_name', 'sex'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit = False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "core/account_update.html",{
            "noodle":pk,
            "noodle_form":user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied



# Create your views here.

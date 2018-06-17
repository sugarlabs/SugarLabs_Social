from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from core.forms import UserForm


# from core.models import Post

# Create your views here.
def index(request):
    # latest_posts = Post.objects
    # t = loader.get_template('index.html')
    # context_dict = {'latest_posts': latest_posts}
    # c = Context(context_dict)
    # return HttpResponse(t.render(c))
    return render(request, 'index.html')


#Auth views
def register(request):
    #A boolean value is added to tell the template
    #whether the registration was successful
    #Initially it is set to False. It will change
    #to True when registration succeeds.
    registered = False

    #if it's a HTTP POST, processing of form data should done :D.
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)


        if user_form.is_valid():
            user = user_form.save()

            #saving the password after hashing wtih the set_password method
            user.set_password(user.password)
            user.save()

            #Updating variable to indicate that the template
            #registration was successful
            registered = True
        else:
            #Invalid form - mistaken something?
            #lets Print the problem
            print(user_form.errors)
    else:
        #Not a HTTP POST? render the form again :D
        user_form = UserForm()


    #Render the template with context
    return render(request,
                'register.html',
                {
                'user_form':user_form,
                'registered':registered
                })

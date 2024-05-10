from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import UpdateUserForm

# Create your views here.
def user_list(request):
    users=User.objects.all()
    return render(request, "user_list.html", {"users": users})

def add_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        User.objects.create(username=username,password=password)
        return redirect('user_list')
    return render(request,"register.html")

def delete_user(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request,"delete_user.html",{'user':user})

def update_user(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    if request.method == "POST":
        form = UpdateUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UpdateUserForm(instance=user)
    return render(request,"update_user.html",{'form':form,'user':user})
    
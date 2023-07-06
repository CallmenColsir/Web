from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import TodoItems


def home_page(request):
    data = {}
    username = request.user  # this is username that login
        
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        userItems = TodoItems.objects.filter(user=user)
            
        data = {
            'userItems': userItems,
        }
    else:
        return redirect("login-form")
    
    return render(request, "todo/home-page.html", data)

def add_items(request):
    
    if request.method == 'POST':
        username = request.user
        item = request.POST['item']
        user = User.objects.get(username=username)
            
        new_item = TodoItems.objects.create(user=user, text=item)
        new_item.save()
            
        return redirect("home-page")
    
def delete_items(request, pk):
    if request.method == "POST":
        item = TodoItems.objects.filter(pk=pk)
        item.delete()       
        return redirect("home-page")
        
from django.shortcuts import render
from .models import ToDoList
from users import views as v

# Create your views here.

def home(response):
    if response.user.is_authenticated:
        ls = ToDoList.objects.get(name=response.user.username)

        if ls in response.user.todolist.all():

            if response.method == "POST":
                
                if response.POST.get("delete"):
                    for item in ls.item_set.all():
                        if response.POST.get("it" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        if item.complete == True:
                            item.delete()

                elif response.POST.get("save"):
                    for item in ls.item_set.all():
                        if response.POST.get("it" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()
                    
                elif response.POST.get("newItem"):
                    txt = response.POST.get("new")

                    if len(txt) > 2:
                        ls.item_set.create(text=txt, complete=False)
                    else:
                        print("invalid")
            return render(response, "home/home.html", {"ls":ls})
    else:
        return v.register(response)

def create(response):
    u = response.user
    n = response.user.username
    t = ToDoList(user=u,name=n)
    response.user.todolist.add(t)
    return

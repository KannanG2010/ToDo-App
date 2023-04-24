from django.shortcuts import render ,redirect
from todo_app.models import ToDolist

# Create your views here.

def add_task(request):
    """
    this function get the text from form(add_task.html) and saved it in our database ToDolist
       
    """

    if request.method=="POST":
        text=request.POST['text']
        s=ToDolist(text=text)
        s.save()
        return redirect('Task/')
    return render(request,'add_task.html')

def Task(request):
    """
    it read the data  from in the database ToDolist and creating the tables in (task.html)
    """
    todo_list=ToDolist.objects.all()
    return render(request,'task.html',{'items': todo_list})

def delete(request,id):
    """
    this function get the text from form(add_task.html) and saved it in our database ToDolist
       
    """
    s=ToDolist.objects.get(id=id)
    s.delete()
    return redirect('Task')
from django.shortcuts import render, redirect
from .models import Todo_Task
from .forms import TodoForm, StatusForm

def create(request):
    template_name = "todoapp/insert.html"
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'forms':form}
    return render(request,template_name,context)

def show_task(request):
    template_name = "todoapp/show.html"
    obj = Todo_Task.objects.all()
    context = {'tasks': obj}
    return render(request,template_name,context)

def update_task(request, pk):
    template_name = "todoapp/insert.html"
    obj = Todo_Task.objects.get(pk=pk)
    form = StatusForm(instance=obj)  
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'forms': form} 
    return render(request, template_name, context)

def delete_task(request,pk):
    template_name = "todoapp/delete.html"
    obj = Todo_Task.objects.get(pk=pk)
    if request.method == 'GET':
        context = {"task":obj}
        return render(request,template_name,context)
    obj.delete()
    return redirect('list')

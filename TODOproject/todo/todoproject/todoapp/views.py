from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
class Tasklistview(ListView):
    model=Task
    template_name='add.html'
    context_object_name='task'
class Taskdetailview(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name ='task'
class Taskupdateview(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields = ('task','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = Task
    template_name ='delete.html'
    success_url=reverse_lazy('cbvadd')

# Create your views here.
def add(request):
    task2 = Task.objects.all()
    if request.method=='POST':
        task=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=Task(task=task,priority=priority,date=date)
        task1.save()
    return render(request,'add.html',{'task':task2})

def detail(request,id):
    return render(request,'detail.html')
# def index(request):
#     return render(request,'index.html',)
def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})

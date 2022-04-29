from django.shortcuts import get_object_or_404, redirect, render
from app.forms import QuestionForm
from app.models import Question

def index(request):
    questions = Question.objects.all()
    context = { 'questions': questions }
    return render(request, 'app/index.html', context)

def create(request):
    context = {}
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/app')
         
    context['form'] = form
    return render(request, 'app/create.html', context)

def update(request, id):
    context = {}
    obj = get_object_or_404(Question, id = id)
    form = QuestionForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/app")
    context["form"] = form
    return render(request, 'app/update.html', context)


def delete(request, id):
    obj = get_object_or_404(Question, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect("/app")
    return render(request, "app/delete.html")

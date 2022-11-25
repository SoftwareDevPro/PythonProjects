from django.shortcuts import render, redirect
from .models import QuizModel
from .forms import *

def home(request):
  if request.method == "POST":
    questions = QuizModel.objects.all()
    score = 0
    wrong = 0
    correct = 0
    total = 0
    for q in questions:
      total += 1
      if q.answer == request.POST.get(q.question):
        score += 1
        correct += 1
      else:
        wrong += 1

    context = { "score": f"{score}/{total}",
        "correct": correct,
        "wrong": wrong,
        "total": total
    }
    return render(request, "result.html", context)
  else:
    questions = QuizModel.objects.all()
    context = { "questions": questions }
    return render(request, "home.html", context)

def addQuestion(request):
  form = AddQuestionForm()
  if request.method == "POST":
    form = AddQuestionForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("addQuestion")
  context = { "form": form }
  return render(request, "addquestion.html", context)








from django.forms import ModelForm
from .models import *

class AddQuestionForm(ModelForm):
    class Meta:
        model = QuizModel
        fields = "__all__"

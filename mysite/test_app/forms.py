from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text', 'date_of_publication')

class ChoiceForm(form.ModelForm):
    class Meta:
        model = Choice
        fields = ('__all__')

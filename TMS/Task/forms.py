from django import forms

from .models import Task, Friend, CommonTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    priority = forms.ChoiceField(choices=Task.LEVELS, required=True, label='Priority')
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommonTaskForm(TaskForm):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=Friend.objects.none(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CommonTask
        fields = TaskForm.Meta.fields + ['shared_with']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CommonTaskForm, self).__init__(*args, **kwargs)
        if user:
            # self.fields['shared_with'].queryset = Friend.objects.filter(user=user)
            friends = Friend.objects.filter(user=user)
            # self.fields['shared_with'].queryset = friends
            self.fields['shared_with'].widget.choices = [(friend.friend.username, friend.friend.username) for friend in friends]




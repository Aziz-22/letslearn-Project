from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from .models import User, Course, Lesson, User_Profile, Quiz, Question



#forms for profile shahad

class User_Profile(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email','password']
            widgets = {
                'username' : forms.TextInput(attrs={'class':'form-control'}),
                'first_name' : forms.TextInput(attrs={'class':'form-control'}),
                'last_name' :forms.TextInput(attrs={'class':'form-control'}),
                'email' : forms.TextInput(attrs={'class':'form-control'}),
                'password':forms.TextInput(attrs={'class':'form-control'})
            }




class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),

        }


class Preview_Image():
    class Meta:
        model = User_Profile
        fields = ['image']


class PasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']
        widgets = {

            'password': forms.TextInput(attrs={'type': 'password'}),
        }

# START Maryam Work


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'subject_title', 'level',
                  'duration', 'description', 'course_image', 'user')
        subjects = (
            ('', 'Select a subject'),
            # First one is the value of select option and second is the displayed value in option
            ('Math', 'Math'),
            ('English', 'English'),
            ('Scince', 'Scince'),
        )
        levels = (
            ('', 'Select a levels'),
            # First one is the value of select option and second is the displayed value in option
            ('1st garde', '1st garde'),
            ('2st garde', '2st garde'),
            ('3st garde', '3st garde'),
        )
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_title': forms.Select(choices=subjects, attrs={'class': 'form-control'}),
            'level': forms.Select(choices=levels, attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
            

class QuizForm(forms.ModelForm):
    class Meta:
            model = Quiz
            fields = ['quiz_name','user', 'course']

            widgets = {
                'course' : forms.Select(attrs={'class':'form-control'}),
                'quiz_name' : forms.TextInput(attrs={'class':'form-control'}),
                'user' : forms.Select(attrs={'class':'form-control'}),
            }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'lesson_link', 'course']
        widgets = {
            'course' : forms.Select(attrs={'class':'form-control'}),
            'lesson_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lesson_link': forms.TextInput(attrs={'class': 'form-control'}),
        }



class QuestionForm(forms.ModelForm):
    class Meta:
            model = Question
            fields = ['question_name','choices', 'correct_answer']

            widgets = {
                'question_name' : forms.TextInput(attrs={'class':'form-control'}),
                'choices' : forms.TextInput(attrs={'class':'form-control'}),
                'correct_answer' : forms.TextInput(attrs={'class':'form-control'}),
            }

# ArticleFormSet = formset_factory(ArticleForm, extra=2)

        


# Create your views here.
# main_app/views.py
from django.contrib.auth.models import User, auth
from django.http.response import HttpResponseRedirect
from main_app.models import User_Profile,Course, Lesson, Quiz, Question,Enrollment, User_Answer
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import User_Profile, AddCourseForm, LessonForm, QuizForm, QuestionForm, Preview_Image, PasswordForm, User_Profile_Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
from django.forms import modelformset_factory, inlineformset_factory,formset_factory
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
import logging

# from django.contrib.auth.hashers import make_password




# Afnan code



# START Maryam Work 

def index(request):
    return render(request, 'index.html')



# Abdulaziz's Code


class ProfileUpdate(UpdateView):
    print("UPDATE")
    template_name = "teacher_profile.html"
    model = User
    # fields = ['major', 'image']
    form_class = User_Profile_Form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        messages.success(self.request, 'Updating Successfully!')
        return HttpResponseRedirect('/teacher/profile/' + str(self.object.pk) + '/update')


class ProfileUpdateImage(UpdateView):
    print("IMAGE")
    template_name = "teacher_profile.html"
    model = User_Profile
    fields = ['image']
    form_class = User_Profile_Form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return HttpResponseRedirect('/teacher/profile/' + str(self.object.pk) + '/update')


def preview(request, pk):
    user = request.user.user_profile
    form = User_Profile(instance=user)

    if request.method == 'POST':
        form = User_Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'teacher_profile.html', context)

# /Abdulaziz's Code


def lessons(request):
    return render(request, 'lessons.html')




# Afnan code

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST.get('role', True)

        if role == 'teacher':
            role = True
        else:
            role = False
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    is_staff=role, username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                print('user created')
                return redirect ('login')

        else:
            messages.info(request, 'passowrd not matching')
            print('passowrd not matching')
            return redirect('signup')
        return redirect('/')
 
        


    else:
        return render(request, 'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.is_authenticated and user.is_staff == True:
                return redirect('/teacher/profile/' + str(user.id) + '/update') #Go to student profile
            elif user.is_authenticated and user.is_staff == False:
                return redirect('/profile/' + str(user.id) + '/update') #Go to teacher profile
            return redirect('/')
        else:
            messages.info(request,'The username and/or password is incorrect.')
            return redirect('login')

    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
# end Afnan code




# profile update shahad
class profileUpdate(UpdateView):
    template_name = "profile.html"
    model = User
    form_class = User_Profile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        return HttpResponseRedirect('/profile/' + str(self.object.pk)+ '/update')


def ShowQuiz(request, course_id):
    quiz = Quiz.objects.get(course_id=course_id)
    qustions = Question.objects.filter(quiz_id = quiz.pk)
    return render(request, 'Quiz.html', {'quiz': quiz, 'qustions': qustions})

# def takeQuiz(request):
#     return render(request, 'takeQuiz.html')


def courseDetails(request, courseId):
    course = Course.objects.get(id = courseId)
    lessons = Lesson.objects.filter(course = courseId)
    newLink = []
    for lesson in lessons:
        newLink.append(lesson.lesson_link.replace("watch?v=", "embed/"))
    # quiz = Quiz.objects.filter(course = courseId)
    # question = Question.objects.filter(course = courseId)
    return render(request, 'lessons.html', {'course':course, 'lessons':lessons, 'newLink': newLink})




def addCourse(request):
    return render(request, 'AddCourse.html')



class CourseCreate(CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = "AddCourse.html"
    # fields = ['course_name', 'subject_title', 'level' ,'duration','user']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/TeacherCourses/' + str(self.object.user_id))


class LessonCreate(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "AddLesson.html"
    # fields = ['course_name', 'subject_title', 'level' ,'duration','user']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/lessons/' + str(self.object.course_id))



class QuestionCreate(InlineFormSetFactory):
    model = Question 
    form_class = QuestionForm


class QuizCreate(CreateWithInlinesView):
    model = Quiz 
    inlines = [QuestionCreate]
    form_class = QuizForm
    template_name = "AddQuiz.html"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/TeacherCourses/' + str(self.object.user_id))



class CourseUpdate(UpdateView):
    model = Course
    form_class = AddCourseForm
    template_name = "AddCourse.html"
    # fields = ['course_name', 'subject_title', 'level' ,'duration','user']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/TeacherCourses/' + str(self.object.user_id))



def CoursesTeacher(request, user_id):
      courses = Course.objects.filter(user_id=user_id)
      template_name = "CoursesTeacher.html"
      return render(request, 'CoursesTeacher.html', {'courses': courses})



def courses_teacher(request, user_id):
    courses = Course.objects.filter(user_id=user_id)
    template_name = "CoursesTeacher.html"
    return render(request, 'TeacherCourses/CoursesTeacher.html', {'cousres': courses})

def courseView(request):
    courses = Course.objects.all()
    model = Course
    template_name = "index.html"
    return render(request, 'index.html', {'courses': courses})

    
@login_required(login_url='login')
def EnrollCourse(request,course_id):
    def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
    user = Enrollment.objects.create(course_id = course_id, user_id = request.user.id)
    user.save()
    return HttpResponseRedirect('/')
#end of work

class CourseDelete(DeleteView):
    model = Course 
    template_name = 'course_confirm_delete.html'
    success_url = '../'

def takeQuiz(request, question_id):
    template_name = "Quiz.html"
    if request.method =='POST':
        print("question ID", question_id)
        user_answer=request.POST.get('choices')
        # answer = request.POST['selectedAnser']
        question = Question.objects.get(id = question_id)
        correctAnswer = question.correct_answer 
        if user_answer == correctAnswer:
            score = 1 
            messages.info(request,'Answer is correct.')
        elif user_answer != correctAnswer:
            score = 0 
            messages.info(request,'Answer is incorrect.')

        def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
        UserAnswer = User_Answer.objects.create(learner_answer=user_answer, question_id=question_id, user_id=request.user.id, score=score )
        UserAnswer.save()
        # return redirect('/takeQuiz/'+str(question_id))
        return render(request,'Quiz.html', {'score': UserAnswer})
        # HttpResponseRedirect('/takeQuiz/' + str(quesstion_id))

# def getScore():


def EnrolledCourses(request):
    def form_valid(self, form):
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
    enroll = Enrollment.objects.filter(user_id = request.user)
    for i in enroll:
        courses = Course.objects.filter(id = i.course_id)
    return render(request, 'EnrolledInCourses.html', {'courses':courses})

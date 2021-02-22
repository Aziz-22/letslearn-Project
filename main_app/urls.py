# main_app/urls.py
from django.urls import path
from main_app import views


# Afnan code
urlpatterns = [
    path('', views.index, name='index'),
    # Abdulaziz's Code
    path('teacher/profile/<pk>/update/',
         views.ProfileUpdate.as_view(), name='profile_update'),

    #     path('teacher/profile/<int:pk>/update/password/',
    #          views.PasswordUpdate.as_view(), name='password_update'),

    path('teacher/profile/<int:pk>/update/image/',
         views.preview, name='image_update'),
    # END Abdulaziz's Code
    path('lessons/<int:courseId>', views.courseDetails, name='lessons'),
    # Afnan code
    path('signup/', views.signup, name='signup'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('takeQuiz/', views.takeQuiz, name='takeQuiz'),

    #  End Afnan code
    # START Maryam Work 
    path('TeacherCourses/', views.addCourse, name='addCourse'),
    path('TeacherCourses/create/', views.CourseCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/update/<int:pk>', views.CourseUpdate.as_view(), name='addCourse_create'),
    path('TeacherCourses/<int:user_id>/', views.CoursesTeacher, name='courses_teacher'),
    path('quiz/<int:course_id>/', views.ShowQuiz, name='course_quiz'),
    path('TeacherCourses/course/create/', views.CourseCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/lesson/create/', views.LessonCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/quiz/create/', views.QuizCreate.as_view(), name='addCourse_create'),

    # END Maryam Work 

    path('addCourse', views.addCourse, name='addCourse'),
    path('addCourse/create/', views.CourseCreate.as_view(), name='addCourse_create'),
    path('TeacherCourses/<int:user_id>/',
         views.courses_teacher, name='courses_teacher'),
    # END Maryam Work
    # Start Shahad Work

    path('profile/<int:pk>/update',
         views.profileUpdate.as_view(), name='User_Profile'),
    path('profile/<int:pk>/update/', views.profileUpdate.as_view(), name='User_Profile'),


]

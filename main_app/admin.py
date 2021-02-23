from django.contrib import admin
from .models import Course, Lesson,User_Profile, Quiz, Question, User_Answer

# Register your models here.

admin.site.register(User_Profile)
# START Maryam Work 
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(User_Answer)
# END Maryam Work 
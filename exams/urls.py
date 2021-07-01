from django.urls import path

from exams.views import teacher, institute

urlpatterns = [
    path('teacher', teacher.TeacherList.as_view(), name="index_teacher"),
    path('teacher/<int:pk>', teacher.TeacherShow.as_view(), name="show_teacher"),
    path('teacher/<int:pk>/edit', teacher.TeacherUpdate.as_view(), name="edit_teacher"),
    path('teacher/<int:pk>/delete', teacher.TeacherDelete.as_view(), name="delete_teacher"),
    path('teacher/new', teacher.TeacherCreate.as_view(), name="create_teacher"),

    # Institute URLS

    path('institute', institute.InstituteList.as_view(), name="index_institute"),
    path('institute/<int:pk>', institute.InstituteShow.as_view(), name="show_institute"),
    path('institute/<int:pk>/edit', institute.InstituteUpdate.as_view(), name="edit_institute"),
    path('institute/<int:pk>/delete', institute.InstituteDelete.as_view(), name="delete_institute"),
    path('institute/new', institute.InstituteCreate.as_view(), name="create_institute"),
]

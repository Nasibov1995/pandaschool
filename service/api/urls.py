from django.urls import path
from service.api import views

urlpatterns = [
    path("branch-list/<email>/",
         views.BranchListAPIView.as_view(), name="branch-list"),
    path("branch-create/", views.BranchCreateAPIView.as_view(), name="branch-create"),
    path("branch-retrieve-update-delete/<int:id>/",
         views.BranchRetrieveUpdateDestroyAPIView.as_view(), name="branch-retrieve-update-delete"),

    path("branch-season-list/<int:id>/",
         views.BranchSeasonListAPIView.as_view(), name="branch-list"),
    path("season-create/", views.SeasonCreateAPIView.as_view(), name="season-create"),
    path("season-retrieve-update-delete/<int:id>/",
         views.SeasonRetrieveUpdateDestroyAPIView.as_view(), name="season-retrieve-update-delete"),

    path("season-student-list/<int:id>/",
         views.SeasonStudentListAPIView.as_view(), name="season-student-list"),
    path("category-season-student-list/<int:season_id>/<int:category_id>/",
         views.CategorySeasonStudentListAPIView.as_view(), name="category-season-student-list"),
    path("student-create/", views.StudentCreateAPIView.as_view(),
         name="student-list-create"),
    path("student-retrieve-update-delete/<int:id>/",
         views.StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-retrieve-update-delete"),

    path("season-teacher-list/<int:id>/",
         views.SeasonTeacherListAPIView.as_view(), name="season-teacher-list"),

    path("teacher-create/", views.TeacherCreateAPIView.as_view(),
         name="teacher-create"),
    path("teacher-retrieve-update-delete/<int:id>/",
         views.TeacherRetrieveUpdateDestroyAPIView.as_view(), name="teacher-retrieve-update-delete"),

    path("block-list-create/", views.BlockListCreateAPIView.as_view(),
         name="block-list-create"),
    path("block-retrieve-update-delete/<int:id>/",
         views.BlockRetrieveUpdateDestroyAPIView.as_view(), name="block-retrieve-update-delete"),

    path("class-list-create/", views.ClassListCreateAPIView.as_view(),
         name="class-list-create"),
    path("class-retrieve-update-delete/<int:id>/",
         views.ClassRetrieveUpdateDestroyAPIView.as_view(), name="class-retrieve-update-delete"),

    path("subject-list-create/", views.SubjectListCreateAPIView.as_view(),
         name="subject-list-create"),
    path("subject-retrieve-update-delete/<int:id>/",
         views.SubjectRetrieveUpdateDestroyAPIView.as_view(), name="subject-retrieve-update-delete"),

    path("group-list-create/", views.GroupListCreateAPIView.as_view(),
         name="group-list-create"),
    path("group-retrieve-update-delete/<int:id>/",
         views.GroupRetrieveUpdateDestroyAPIView.as_view(), name="group-retrieve-update-delete"),

    path("category-list-create/", views.StudentCategoryListCreateAPIView.as_view(),
         name="category-list-create"),
    path("category-retrieve-update-delete/<int:id>/",
         views.StudentCategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-retrieve-update-delete"),

    path("language-list-create/", views.LanguageListCreateAPIView.as_view(),
         name="language-list-create"),
    path("language-retrieve-update-delete/<int:id>/",
         views.LanguageRetrieveUpdateDestroyAPIView.as_view(), name="language-retrieve-update-delete"),

]

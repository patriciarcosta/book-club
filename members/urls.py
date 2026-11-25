from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

app_name = "members"

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>/", views.hello, name="hello"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("info/", views.request_info, name="info"),
    path("members/", views.MemberListView.as_view(), name="list"),
    path("members/add/", views.add_member, name="add_member"),
    path("members/<int:pk>/", views.MemberDetailView.as_view(), name="detail"),
    re_path(
        r"^members/archive/(?P<year>[0-9]{4})/$",
        views.members_by_year,
        name="archive-year",
    ),
    re_path(
        r"^members/initial/(?P<letter>[A-Za-z])/$",
        views.members_by_initial,
        name="initial",
    ),
    re_path(
        r"^members/joined/(?P<year>[0-9]{4})-(?P<month>[0-9]{1,2})/$",
        views.members_by_month,
        name="joined-month",
    ),
    path("people/", RedirectView.as_view(pattern_name="members:list"), name="people"),
]

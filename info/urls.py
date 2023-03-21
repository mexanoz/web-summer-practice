from django.urls import path

from . import views

app_name = "info"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name = "update"),
    path("search/", views.SearchView.as_view(), name = "search"),
    path("results/", views.SearchResultsView.as_view(), name = "search_results"),
]
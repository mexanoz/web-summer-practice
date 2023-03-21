from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *

def redirect_view(request):
    return HttpResponseRedirect(reverse("info:index"))

class IndexView(generic.ListView):
    template_name = "info/index.html"
    model = Teacher

    def get_ordering(self):
        return "name"


class DetailView(generic.DetailView):
    template_name = "info/detail.html"
    model = Teacher


class UpdateView(generic.UpdateView):
    template_name = "info/update.html"
    model = Teacher
    fields = ["name", "position", "education", "photo", "room", "additional_work", "lessons"]
    success_url = "/info/{id}/"


class SearchView(generic.TemplateView):
    template_name = "info/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["position_list"] = Position.objects.all()
        context["education_level_list"] = Education.objects.all().values_list("level").distinct()
        context["education_field_list"] = Education.objects.all().values_list("field").distinct()
        context["room_list"] = Room.objects.filter(room_type__exact="TE")
        context["lesson_list"] = Lesson.objects.all()
        return context
    

class SearchResultsView(generic.ListView):
    template_name = "info/search_results.html"
    model = Teacher

    def get_queryset(self):
        GET = self.request.GET

        name_query = GET.get("name")
        query = Q(name__iregex = name_query)

        position_query = GET.getlist("position")
        pquery = Q()
        for p in position_query:
            pquery |= Q(position__id = p)
        query &= pquery

        education_level_query = GET.getlist("education_level")
        education_field_query = GET.getlist("education_field")
        equery = Q()
        for el in education_level_query:
            if el == "":
                equery |= Q(education__isnull = True)
                continue
            for ef in education_field_query:
                equery |= Q(education__level = el) & Q(education__field = ef)
        query &= equery

        room_query = GET.getlist("room")
        rquery = Q()
        for r in room_query:
            if r == "":
                rquery |= Q(room__isnull = True)
            else:
                rquery |= Q(room__id = r)
        query &= rquery 

        # lesson_query = GET.getlist("lesson")
        # teachers_with_lessons = [t for t in Teacher.objects.all() if set(lesson_query) <= set(t.lessons.all())]
        # query &= Q(id__in = teachers_with_lessons)

        return Teacher.objects.filter(query).order_by("name")
from django.views.generic import CreateView, ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Entry


# Renders home page with all entry objects sorted by
# latest creation date.


class LatestEntryView(ListView):
    queryset = Entry.objects.all().order_by("-created_at")
    paginate_by = 10
    template_name = "latest_entries.dhtml"
    context_object_name = "entries"


# Renders home page with all entry objects sorted by
# most number of likes.


class TopEntriesView(ListView):
    queryset = Entry.objects.all().order_by("-likes")
    paginate_by = 10
    template_name = "top_entries.dhtml"
    context_object_name = "entries"


# Creates new entry in database


class CreateEntryView(CreateView):
    model = Entry
    fields = ("content",)
    success_url = reverse_lazy("latest_entries")
    template_name = "create_entry.dhtml"


# Increases the amount of lieks on a certain entrie by one,
# then returns to new number to the page so javascript can update
# dom to accurately reflect the databases' information


class LikeEntryView(View):
    def post(self, request, id):
        entry = Entry.objects.get(id=id)
        entry.likes += 1
        entry.save()
        return JsonResponse({"likes": entry.likes})

from django.views.generic import CreateView, ListView, View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Entry


class LatestEntryView(ListView):
    queryset = Entry.objects.all().order_by("-created_at")
    paginate_by = 10
    template_name = "latest_entries.dhtml"
    context_object_name = "entries"


class TopEntriesView(ListView):
    queryset = Entry.objects.all().order_by("-likes")
    paginate_by = 10
    template_name = "top_entries.dhtml"
    context_object_name = "entries"


class CreateEntryView(CreateView):
    model = Entry
    fields = ("content",)
    success_url = reverse_lazy("latest_entries")
    template_name = "create_entry.dhtml"


class LikeEntryView(View):
    def post(self, request, id):
        entry = get_object_or_404(Entry, id=id)
        entry.likes += 1
        entry.save()
        # return JsonResponse({"likes": entry.likes})

        # totally understand that this is not the correct way to do this,
        # however i could not for life of me figure out how to fix the issue
        # of getting sent to a page with just the json response,
        # and this accomplishes the goal to my knowledge,
        # judge however you see fit, I understand if it's not satisfactory
        return redirect("/entries")

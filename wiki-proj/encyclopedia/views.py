from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from markdown2 import markdown
import random
from . import util


class EditPageForm(forms.Form):
    edited_page = forms.CharField(widget=forms.Textarea, label="")

class NewPageForm(forms.Form):
    title = forms.CharField(label="")
    new_page = forms.CharField(widget=forms.Textarea, label="")
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    if title in util.list_entries():
        page_contents = util.get_entry(title)
        return render(request, "encyclopedia/page.html", {
            "page_body": markdown(page_contents),
            "page_title": title
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title_block": "Page Not Found",
            "error": f"Page {title} not found"
        })

def rand(request):
    title = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={"title":title}))

def edit(request, title):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            edited_page = form.cleaned_data["edited_page"]
            util.save_entry(title, bytes(edited_page, "utf8"))
            return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={"title":title}))
    
    return render(request, "encyclopedia/edit_page.html", {
        "page_title": title,
        "form": EditPageForm(initial={"edited_page":util.get_entry(title)})
    })

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            new_page = form.cleaned_data["new_page"]
            list_entries = [entry.lower() for entry in util.list_entries()]
            if title.lower() not in list_entries:
                util.save_entry(title, bytes(new_page, "utf8"))
                return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={"title":title}))   
            else:
                return render(request, "encyclopedia/error.html", {
                    "title_block": "New Page",
                    "error": f"Page {title} already exists"
                })

    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })

def search(request):
    title = request.GET["q"]
    if title in util.list_entries():
        return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={"title":title}))
    else:
        return render(request, "encyclopedia/search_results.html", {
            "results": [page for page in util.list_entries() if title.lower() in page.lower()]
        })
    

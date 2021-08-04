from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from research.models import Journal, Encyclopedia_Chapter, Book

def research_index(request):
    latest_journal_list = Journal.objects.order_by('-pub_date')[:5]
    latest_chapter_list = Encyclopedia_Chapter.objects.order_by('-pub_date')[:5]

    context = {
        'latest_journal_list': latest_journal_list,
        'latest_chapter_list': latest_chapter_list
    }

    return render(request, 'research/index.html', context)

def journal_detail(request, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    return render(request, 'research/journal_detail.html', {'journal': journal})

def chapter_detail(request, chapter_id):
    chapter = get_object_or_404(Encyclopedia_Chapter, pk=chapter_id)
    return render(request, 'research/chapter_detail.html', {'chapter': chapter}
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Candidate, Poll, Choice
import datetime
from django.db.models import Sum

# Create your views here.
def index(request):
    return render(request, 'elections/index.html')

def candidate(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'elections/candidate.html', context)

def areas(request, area):
    today = datetime.datetime.now()
    try:
        poll = Poll.objects.get(area = area, start_date__lte = today, end_date__gte = today)
        candidates = Candidate.objects.filter(area = area)
    except:
        poll = None
        candidates = None

    context = {'poll': poll, 'candidates': candidates, 'area': area}

    return render(request, 'elections/area.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    selection = request.POST['choice']

    try:
        choice = Choice.objects.get(poll_id = poll_id, candidate_id = selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id = poll_id, candidate_id = selection, votes = 1)
        choice.save()

    return HttpResponseRedirect("/candidate/areas/{}/results".format(poll.area))

def results(request, area):
    candidates = Candidate.objects.filter(area = area)
    polls = Poll.objects.filter(area = area)
    poll_result = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        result['total_votes'] = float(total_votes['votes__sum'])
        rates = []
        for candidate in candidates:
            try:
                choice = Choice.objects.get(poll_id = poll.id, candidate_id = candidate.id)
                rates.append(round(choice.votes * 100 / result['total_votes'], 1))
            except:
                rates.append(0)

        result['rates'] = rates
        poll_result.append(result)
    
    context = {'candidates': candidates, 'area': area, 'poll_result': poll_result}
    return render(request, 'elections/result.html', context)
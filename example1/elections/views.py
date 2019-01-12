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
        polls = Poll.objects.filter(area = area)
        print(polls)
    except:
        polls = None

    context = {'polls': polls, 'area': area}

    return render(request, 'elections/area_list.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    selection = request.POST['choice']
    print("*******")
    print(Poll.id)
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
        result['total_votes'] = total_votes['votes__sum']
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

def create_candidate(request):
    name = request.POST.get("name")
    area = request.POST.get("area")
    introduction = request.POST.get("introduction")
    party_number = request.POST.get("party_number")
    msg="null"
    err=""
    try:
        candidates = Candidate.objects.filter(
            area = area
            )
        #해당 지역에 candidate가 없을때
        if candidates.count() == 0:
            err = "값이 비어있습니다."
            #강제로 에러코드 발생
            4/0
        #해당 지역에 같은후보번호 혹은 이름을 가진 후보자가 있는지 검출 
        for candidate in candidates:
            if candidate.party_number == int(party_number):
                msg = "이미 있는 후보번호 입니다."
                err = "이미 있는 후보번호"
            if candidate.name == name:
                msg = "이미 있는 후보자 입니다."
                err = "이미 있는 후보자" 
        #candidate생성으로 이동
        if msg == "null":
            #강제로 에러코드 발생
            4/0
        print("error :", err)
        print("************************\n")
        context = {'msg': msg}
        return render(request, 'elections/index.html', context)
    except:
        candidate = Candidate(
            name = name,
            introduction = introduction,
            area = area,
            party_number = party_number
        )
        candidate.save()
        print("'",candidate,"' 가 바르게 생성되었습니다.")
        print("************************\n")
        msg = "{}가 바르게 생성되었습니다.".format(candidate.name)
        context = {'msg': msg}
    
    print("error :", err)
    return render(request, 'elections/index.html', context)

def form_poll(request):
    return render(request, 'elections/poll.html')

def create_poll(request):
    start_date = request.POST.get("start_date")
    end_date = request.POST.get("end_date")
    area = request.POST.get("area")
    candidates = Candidate.objects.filter(area = area)
    try:
        poll = Poll.objects.get(area = area, start_date__lte = start_date, end_date__gte = start_date)
        msg = "이미 진행중인 투표가 있습니다. \n{}\n~\n{}".format(poll.start_date, poll.end_date)
        context = {'msg': msg}
        return render(request, 'elections/poll.html', context)
    except:
        poll = Poll(
            start_date = start_date,
            end_date = end_date,
            area = area
        )
        poll.save()
        msg = "{}지역 새로운 투표가 생성되었습니다.".format(poll.area)
        context = {'msg': msg, 'poll': poll, 'candidates': candidates, 'area': area }

    return render(request, 'elections/area.html', context)

def show_poll(request):
    today = datetime.datetime.now()
    poll_id = request.POST.get('poll_id')
    area = request.POST.get("area")
    try:
        poll = Poll.objects.get(id = poll_id)
        print("show poll\n")
        print(poll)
        candidates = Candidate.objects.filter(area = area)
    except:
        poll = None
        candidates = None
    msg = "{} \n {}".format(poll.start_date, poll.end_date)
    context = {'poll': poll, 'candidates': candidates, 'area': area, 'msg': msg}
    return render(request, 'elections/area.html', context)
import json
from django.shortcuts import render, redirect
from .models import schedule

def index(request):
    all_schedule = schedule.objects.all()
    data = dict();
    for i in range(1,8):
        data[str(i)] = []
        day_list = schedule.objects.filter(day=i)
        for mission in day_list:
            data[str(i)].append([mission.start_time,mission.end_time,mission.title])

    return render(request, 'wkcalendar/examples/index.html', {'all_schedule': json.dumps(data)})

def index2(request):
    all_schedule = schedule.objects.all()
    data = dict();
    for i in range(1,8):
        data[str(i)] = []
        day_list = schedule.objects.filter(day=i)
        for mission in day_list:
            data[str(i)].append([mission.start_time,mission.end_time,mission.title, ])

    return render(request, 'wkcalendar/examples/index0.html', {'all_schedule': json.dumps(data)})


def popup(request):
    return render(request, 'wkcalendar/examples/popup.html', {})

def add_schedule(request):
    if request.method == 'POST':
        schedule.objects.create(
            title = request.POST['title'],
            location = request.POST['location'],
            day = request.POST['day'],
            start_time = request.POST['start'],
            end_time = request.POST['end']
        )
    return redirect('wkcalendar:index')

def delete_schedule(request):
    if request.method == 'POST':
        day = request.POST['day']
        time = request.POST['time']
        day_schedule = schedule.objects.filter(day=day)
        for mission in day_schedule:
            if mission.start_time <= time <= mission.end_time:
                mission.delete()

    return redirect('wkcalendar:index')

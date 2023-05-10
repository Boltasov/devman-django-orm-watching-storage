from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []

    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        non_closed_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
        }
        non_closed_visits.append(non_closed_visit)


    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

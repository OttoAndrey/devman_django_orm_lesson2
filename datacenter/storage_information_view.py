from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []
    not_leaved_visits = Visit.objects.filter(leaved_at=None)

    for not_leaved in not_leaved_visits:
        duration = not_leaved.get_duration()
        visit = {
            "who_entered": not_leaved.passcard.owner_name,
            "entered_at": not_leaved.entered_at,
            "duration": format_duration(duration),
            "is_strange": not_leaved.is_long()
        }
        non_closed_visits.append(visit)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

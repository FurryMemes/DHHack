from django.shortcuts import render
from .forms import GroupForm


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    form = GroupForm(request.POST)
    return render(request, 'default.html',
                  { 'mapbox_access_token': 'pk.eyJ1IjoibWFzaGF0cmV0MjAwNiIsImEiOiJjazNia2c1amYwajNwM2NsZGpheHB1Y29mIn0.QegkEY39EJLAuB1Y_ba47A',
                    'form': form
                   })

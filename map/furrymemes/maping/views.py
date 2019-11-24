from django.shortcuts import render
from .models import Group
from .forms import GroupForm
import vk_api
import json

def get_id_users(group):
    idd = '9f79d9a11e43730af251d10434201eefb9a665c637eba51e27466f6c4d7557c399484a80ca5aa29adb765'
    vk_session = vk_api.VkApi(token=idd)
    #print(vk_session.method('groups.getMembers', {'group_id': group}))
    try:
        return vk_session.method('groups.getMembers', {'group_id': group})['items']
    except:
        return vk_session.method('groups.getMembers', {'group_id': 80799846})['items']

def get_posts_data(group_id, count):
    users_id = get_id_users(group_id)
    vk_session = vk_api.VkApi(token='9f79d9a11e43730af251d10434201eefb9a665c637eba51e27466f6c4d7557c399484a80ca5aa29adb765')
    points = []

    for i in range(min(1000, count)):
        posts = {}
        tr = False
        try:
            posts = vk_session.method('wall.get', {'owner_id': users_id[i], 'count': 25})
            tr = True
            # print('not_bad_error')
        except:
            # print('bad_error')
            pass
        if tr and 'items' in posts.keys():
            z = 0
            for post in range(len(posts['items'])):
                if 'geo' in posts['items'][post].keys():
                    z += 1
                    geo = posts['items'][post]['geo']
                    points.append([geo['coordinates'].split()[0], geo['coordinates'].split()[1]])
                    # print(points)

            if z != 0:
                try:
                    posts = vk_session.method('wall.get', {'owner_id': id, 'count': 200, 'offset': 25})
                    # print('not_bad_error')
                except:
                    # print('bad_error')
                    pass
                for post in range(len(posts['items'])):
                    if 'geo' in posts['items'][post].keys():
                        geo = posts['items'][post]['geo']
                        points.append([geo['coordinates'].split()[0], geo['coordinates'].split()[1]])
                        # print(points)
    return points



def arr_to_geojson(arr):
    d = {}
    for i in range(len(arr)):
        d[i] = {'latitude': arr[i][0], 'longitude': arr[i][1]}
    dump = json.dumps(d)
    return dump

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            points = arr_to_geojson(get_posts_data(request.POST.get('group_name'), 50))
    else:
        form = GroupForm()
        points = {}
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
          { 'mapbox_access_token': 'pk.eyJ1IjoibWFzaGF0cmV0MjAwNiIsImEiOiJjazNia2c1amYwajNwM2NsZGpheHB1Y29mIn0.QegkEY39EJLAuB1Y_ba47A',
            'form': form,
            'points': points,
           })

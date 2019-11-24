import vk_api
from get_id_users import get_id_users

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

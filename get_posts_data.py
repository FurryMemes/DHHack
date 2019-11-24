import vk_api
from get_id_users import get_id_users

def get_posts_data(group_id):
    users_id = get_id_users(group_id)
    vk_session = vk_api.VkApi(token='1c62622a5c606fe72b7aa7f54af6101552df0a725ab4a53ed1422be0d0f4571674709f47d84fbd45d5dbb')
    points = []
    for id in users_id:
        try:
            posts = vk_session.method('wall.get', {'owner_id': id, 'count': 25})
            # print('not_bad_error')
        except:
            # print('bad_error')
            pass
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

if __name__ == "main":
    get_posts_data(80799846)

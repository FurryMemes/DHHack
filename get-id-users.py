# https://vk.com/dev/groups
import vk_api

def get_id_users():
    idd = '1f21b45de665984483f3f48ea811cb27be1d330d1afdef5ce06e4246efcf46acff15f8b388807d6c29cbb'
    vk_session = vk_api.VkApi(token=idd)
    print(vk_session.method('groups.getMembers', {'group_id': 80799846}))

get_id_users()

# https://vk.com/dev/groups
import vk_api

def get_id_users(group):
    idd = '9f79d9a11e43730af251d10434201eefb9a665c637eba51e27466f6c4d7557c399484a80ca5aa29adb765'
    vk_session = vk_api.VkApi(token=idd)
    #print(vk_session.method('groups.getMembers', {'group_id': group}))
    try:
        return vk_session.method('groups.getMembers', {'group_id': group})['items']
    except:
        return vk_session.method('groups.getMembers', {'group_id': 80799846})['items']

if __name__ == '__main__':
    print(get_id_users(80799846))

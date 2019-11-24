# https://vk.com/dev/groups
import vk_api

def get_id_users(group):
    idd = '1c62622a5c606fe72b7aa7f54af6101552df0a725ab4a53ed1422be0d0f4571674709f47d84fbd45d5dbb'
    vk_session = vk_api.VkApi(token=idd)
    #print(vk_session.method('groups.getMembers', {'group_id': group}))
    try:
        return vk_session.method('groups.getMembers', {'group_id': group})['items']
    except:
        return vk_session.method('groups.getMembers', {'group_id': 80799846})['items']

if __name__ == '__main__':
    print(get_id_users(80799846))

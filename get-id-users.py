# https://vk.com/dev/groups
import vk_api

def get_id_users():
    idd = 'f58f9323564c7f94a25546fd2c30ba07619d2695cebcb65acb0e004154f0891de989b5a09a621db83a143'
    vk_session = vk_api.VkApi(token=idd)
    return vk_session.method('groups.getMembers', {'group_id': 80799846})['items']

if __name__ == '__main__':
    print(get_id_users())

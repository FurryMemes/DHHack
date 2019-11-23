# https://vk.com/dev/groups
import vk_api

def get_id_users(group):
    idd = 'f58f9323564c7f94a25546fd2c30ba07619d2695cebcb65acb0e004154f0891de989b5a09a621db83a143'
    vk_session = vk_api.VkApi(token=idd)
    #print(vk_session.method('groups.getMembers', {'group_id': group}))
    return vk_session.method('groups.getMembers', {'group_id': group})['items']

if __name__ == '__main__':
    print(get_id_users(80799846))

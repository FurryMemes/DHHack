import vk_api
import json
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
idd = '1c62622a5c606fe72b7aa7f54af6101552df0a725ab4a53ed1422be0d0f4571674709f47d84fbd45d5dbb'

tags = ['айти', 'программист', 'кодер', 'хакатон' , 'питон', 'c++', 'код', 'софт', 'бэкап', 'opengl', 'json', 'джаваскрипт', 'дибаг', 'дебаг', 'репозиторий', 'гитхаб', 'репа', 'прода', 'говнокод', 'print', 'helloworld', 'принт', 'фор', 'default', 'windows', 'linux', 'ubuntu', 'убунту', 'сервер', 'взлом', 'сервак', 'хакер', 'development', 'fix', 'developer', 'javascript', '']
arr = []

def check_id(id):
    print(arr)
    vk_session = vk_api.VkApi(token=idd)
    posts = vk_session.method('wall.get', {'owner_id' : id})
    for elem in posts['items']:
        print('hey')
        if 'geo' in elem.keys():
            arr.append([int(elem['geo']['coordinates'].split()[0]), int(elem['geo']['coordinates'].split()[1])])
            

if __name__ == '__main__':
    check_id(540540251)
    for i in range(10):
        try:
            check_id(i)
        except:
            pass
    
    #with open('output.txt', 'wb') as outfile:
        #json.dump(arr, outfile)

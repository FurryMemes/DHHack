import vk_api
import json
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
idd = '9f79d9a11e43730af251d10434201eefb9a665c637eba51e27466f6c4d7557c399484a80ca5aa29adb765'

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
    for i in range(20):
        try:
            check_id(i)
        except:
            pass
    print(arr)
    #with open('output.txt', 'wb') as outfile:
        #json.dump(arr, outfile)

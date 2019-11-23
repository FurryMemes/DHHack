import vk_api
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
idd = 'f58f9323564c7f94a25546fd2c30ba07619d2695cebcb65acb0e004154f0891de989b5a09a621db83a143'

tags = ['айти', 'программист', 'кодер', 'хакатон' , 'питон', 'c++', 'код', 'софт', 'бэкап', 'opengl', 'json', 'джаваскрипт', 'дибаг', 'дебаг', 'репозиторий', 'гитхаб', 'репа', 'прода', 'говнокод', 'print', 'helloworld', 'принт', 'фор', 'default', 'windows', 'linux', 'ubuntu', 'убунту', 'сервер', 'взлом', 'сервак', 'хакер', 'development', 'fix', 'developer', 'javascript', '']
#tags = ['', '', '', '', '' , '', '', '', '', '']
arr = []

def check_id(id):
    vk_session = vk_api.VkApi(token=idd)
    posts = vk_session.method('wall.get', {'owner_id' : id})
    for elem in posts['items']:
        if 'geo' in elem.keys():
            arr.append([elem['geo']['coordinates'].split()[0], elem['geo']['coordinates'].split()[1]])
            print('add')
        #text = elem['text']
        #print(text)
        #for word in text.split(' '):
            #t = morph.parse(word)[0].normal_form.capitalize()
            #if word in tags or t in tags:
                #print(text)
            

if __name__ == '__main__':
    #check_id(540540251)
    for i in range(1000):
        try:
            check_id(i + 1000)
        except:
            pass
    print(len(arr))

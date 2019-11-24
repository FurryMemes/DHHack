from igramscraper.instagram import Instagram
import datetime
import matplotlib.pyplot as plt

def get_graph(tag):
    instagram = Instagram()
    instagram.with_credentials('dimafedkk75', '030693Fsa')
    instagram.login()
    
    medias = instagram.get_medias_by_tag(tag, count=2000)
    a = []
    for i in range(24):
        a.append(0)
    for posts in medias:
        a[int(str(datetime.datetime.fromtimestamp(posts.created_time))[11:13])] += 1
    for i in range(24):
        plt.scatter(i, a[i], marker='o', cmap="blue")
    plt.plot([i for i in range(24)], a)
    plt.show()

get_graph('еда')
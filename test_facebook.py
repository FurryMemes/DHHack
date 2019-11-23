import facebook
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

graph = facebook.GraphAPI(access_token="EAAGmQ4MzA2gBAETZCnjyArOXG3qMZB6P38sYMVj8TOYcux23Vc3uTnuvm9RHZC0ecpZAIo8xol66Hak6eIouIeiRePftoSweo27GJSSZB6EiyqASixd2O1B0ypaan4MgYLD22yosZBWigenGa73R1eYxuBIbIRo6kGUkuteu5kMQZDZD", version="3.1")

#morph.parse(nm)[0].normal_form.capitalize()

places = graph.search(type='place',
                      center='55.751694, 37.617218',
                      fields='name, location')

# Each given id maps to an object the contains the requested fields.
for place in places['data']:
    print(place)
    post = graph.get_object(id=int(place['id']), fields='message')
    
    #print(post)

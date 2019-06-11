
from japronto import Application
from jinja2 import Environment
Jinja2 = Environment()
import requests

def hello(request):
    # name = request.values.get('name')

    name = request.query['name']
    print (name)
    print ("============")
    # if request localhost:8080?name={{7*7}}
    # value name is 49
    print ( Jinja2.from_string('Hello ' + name).render()) # Hallo 49 
    return Jinja2.from_string('Hello ' + name)

app = Application()

r = app.router
r.add_route('/', hello, method='GET')
app.run(debug=True)


'''
curl -s localhost:8080?name={{7*7}}
 
'''
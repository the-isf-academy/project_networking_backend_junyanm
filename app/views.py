# views.py

from banjo.urls import route_get, route_post
from settings import BASE_URL

@route_get(BASE_URL + 'all')
def all_drills(args):
    
    for fortune in Fortune.objects.all():
        fortunes_list.append(fortune.json_response())


    
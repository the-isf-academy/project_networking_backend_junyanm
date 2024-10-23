# views.py
from banjo.urls import route_get, route_post
from app.models import Swim_drill
from settings import BASE_URL


@route_get(BASE_URL + 'all')
def all_drills(args):
    if Swim_drill.objects.exists():
        swimdrills_list = []
       
        for swim_drill in Swim_drill.objects.all():
            swimdrills_list.append(swim_drill.json_response())

        return {'Swim Drills': swimdrills_list}
     
    else:
       
        return {'error': 'no drill exists'}


@route_post(BASE_URL + 'new', args={'drillname':str, 'instructions':str, 'distance': int, 'repetitions': int, 'difficulty': int})
def new_drill(args):
    new_drill = Swim_drill(
        drillname = args['drillname'],
        instructions = args['instructions'],
        distance = args['distance'],
        repetitions = args['repetitions'],
        difficulty = args['difficulty']

    )

    new_drill.save()
   
    return {'swim_drill': new_drill.json_response()}


@route_get(BASE_URL + 'one', args={'id':int})
def one_drill(args):
    if Swim_drill.objects.filter(id=args['id']).exists():
        Swim_drill.object.get(id=args['id'])
        
        return {one_drill.json_response()}
    else:
         return {'error': 'no drill exists'}
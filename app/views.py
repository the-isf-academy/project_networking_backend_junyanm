# views.py
from banjo.urls import route_get, route_post
from app.models import Swim_drill
from settings import BASE_URL

#RETURN ALL DRILLS ENDPOINT

@route_get(BASE_URL + 'all')
def all_drills(args):
    if Swim_drill.objects.exists():
        swimdrills_list = []
       
        for swim_drill in Swim_drill.objects.all():
            swimdrills_list.append(swim_drill.json_response())
        return {'Swim Drills': swimdrills_list}
    else:
        return {'error': 'no drill exists'}



#CREATE NEW DRILL ENDPOINT

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



#RETURN ONE DRILL ENDPOINT

@route_get(BASE_URL + 'one', args={'id':int})
def one_drill(args):
    if Swim_drill.objects.filter(id=args['id']).exists():
        one_drill = Swim_drill.objects.get(id=args['id'])
        
        return {'swim_drill' : one_drill.json_response()}
    else:
         return {'error': 'no drill exists'}



#DIFFICULTY ENDPOINT

@route_get(BASE_URL + 'difficulty', args={'difficulty':int})
def difficulty_drill(args):

    if Swim_drill.objects.filter(id=args['difficulty']).exists():
        difficulty_drill = Swim_drill.objects.get(id=args['difficulty'])
        return {'swim_drill': difficulty_drill.json_response()}

    else:
        return{'error':'no drills found'}



# LIKES ENDPOINT

@route_post(BASE_URL + 'like', args={'id':int})
def drill_likes(args):
    if Swim_drill.objects.filter(id=args['id']).exists():
        drill_likes = Swim_drill.objects.get(id=args['id'])
        drill_likes.increase_likes()
        return {'swim_drill': drill_likes.json_response()}
    else:
         return {'error': 'no drill exists'}
    










        








    


    

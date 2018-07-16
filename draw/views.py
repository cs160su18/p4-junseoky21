from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from hashlib import sha256
from django.http import HttpResponse
import random, base64
# from django.utils import simplejson

def index(request):
    return render(request, 'draw/index.html', {})
def treasure(request):
    fname = 'TreasureData.txt'
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip().split('\t') for x in content]
    jsondata = json.dumps(content)
    print(jsondata)
    return render(request, 'draw/treasure.html', {"TreasureData": jsondata})

@method_decorator(csrf_exempt, name='dispatch')
def addtreasure(request):
    uname = request.POST.get('uname', None)
    tName = request.POST.get('tName', None)
    tDescription = request.POST.get('tDescription', None)
    tPicture = request.POST.get('tPicture', None)
    tLat = request.POST.get('tLat', None)
    tLng = request.POST.get('tLng', None)
    if uname is not None and tPicture is not None:
        print ("Gone through!")
        f = open('TreasureData.txt', 'a')
        rand = random.seed()
        randnum = str(random.randint(0, 400000)).encode("utf-8")
        hashed = sha256(randnum).hexdigest()
        print(tPicture)
        imgName = hashed + ".jpeg"
        imgPath = "draw/img/" + imgName
        f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (uname, tName, tDescription, tLat, tLng, imgName))
        f.close()
        fpic = open(imgPath, 'wb')
        fpic.write(base64.b64decode(str(tPicture)))
        fpic.close()


    return render(request, 'draw/addtreasure.html', {})

def img(request):
    imgAddr = request.GET.get('img', None)
    print (imgAddr + " requested!!")
    image_data = open('draw/img/' + imgAddr, "rb").read()
    
    return HttpResponse(image_data, content_type="image")

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
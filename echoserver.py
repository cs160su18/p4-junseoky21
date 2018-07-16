import asyncio
import json
import logging
import websockets

logging.basicConfig()

USERS = set()

def users_event():
    return json.dumps({'type': 'users', 'count': len(USERS)})

async def notify_message(message):
    if USERS:  
        await asyncio.wait([user.send(message) for user in USERS])

async def register(websocket):
    USERS.add(websocket)

async def unregister(websocket):
    USERS.remove(websocket)

async def something(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        print ("Launch Successful")
        # await websocket.send("From Server: Hi, Registration was SUCCESSFUL!")
        

        async for message in websocket:
            jmsg = json.loads(message)
            if jmsg['type'] == "SetTreasure":
                None
            elif jmsg['type'] == "GetTreasure":
                None
            elif jmsg['type'] == "GetAllTreasure":
                None
            elif jmsg['type'] == "DelTreasure":
                a = 1
            await notify_message(message)
    finally:
        await unregister(websocket)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(something, '0.0.0.0', 8765))
asyncio.get_event_loop().run_forever()



# switcher = {
#     "SetTreasure":setTreasure,
#     "GetTreasure":getTreasure,
#     "DelTreasure":delTreasure
# }

# def setTreasure(name, lat, lng, description):

#     return
# def getTreasure(rid):
#     return
# def getAllTreasure():

#     return
# def delTreasure():
#     return
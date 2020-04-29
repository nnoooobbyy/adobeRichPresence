from pypresence import Presence
from handler import updateInfo
import traceback
import time

client_id = '704850028602195978'
discordPresence = Presence(client_id)
discordPresence.connect()
#startTime = int(time.time())

'''
print(discordPresence.update(
    #details (str) – what the player is currently doing
    #state (str) – the user’s current status
    #start (int) – epoch time for game start
    #large_image (str) – name of the uploaded image for the large profile artwork
    #large_text (str) – tooltip for the large image
    #small_image (str) – name of the uploaded image for the small profile artwork
    #small_text (str) – tootltip for the small image
    details="Photoshop",
    state="Inactive",
    start=startTime,
    large_image="photoshop_large",
    large_text="Adobe Photoshop",
    small_image="photoshop_small",
    small_text="Adobe Photoshop"
    ))
'''

while True:  # The presence will stay on as long as the program is running
    try:
        newInfo = updateInfo()
        if newInfo == None:
            print("No Adobe application, clearing presence")
            discordPresence.clear()
        else:
            processName = newInfo[0]
            startTime = newInfo[1]
            largeImage = "{}_large".format(processName.lower())
            smallImage = "{}_small".format(processName.lower())
            print(discordPresence.update(
            details= processName,
            start= startTime,
            large_image= largeImage,
            large_text= processName,
            small_image= smallImage,
            small_text= processName))
    except Exception:
        traceback.print_exc()
    time.sleep(10)
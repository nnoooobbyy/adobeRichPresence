from pypresence import Presence
from handler import updateInfo
from PIL import Image
import traceback
import time
import sys

client_id = '704850028602195978'
discordPresence = Presence(client_id)
discordPresence.connect()

while True:  # the presence will run as long as the program is running
    try:
        newInfo = updateInfo()
        if newInfo == None:
            print("No Adobe application, clearing presence")
            discordPresence.clear()
        else:
            processName = newInfo[0]
            iconName = newInfo[1]
            startTime = newInfo[2]
            windowTitle = newInfo[3]
            largeImage = "{}_large".format(iconName)
            print(discordPresence.update(
            details = processName,
            start = startTime,
            large_image = largeImage,
            large_text = processName,
            state = windowTitle))
    except Exception:
        traceback.print_exc()
    time.sleep(10)
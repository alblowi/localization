import requests
import json

LogFileName = 'RSSILogs.txt'
UpdatedFileName = 'RSSI_Location_Logs.txt'
GoogleAPIKey = "AIzaSyBRWGflAn1sJrQZMtK3J2XNOCZC_0Zvq1s"
APIURL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
RequestURL = APIURL + GoogleAPIKey

def UpdateRSSILogsWithLocation():
    with open(LogFileName, 'r') as ReadFileHandler, open(UpdatedFileName, 'w') as WriteFileHandler:
        ReadFileContent = ReadFileHandler.readlines()
        for Line in ReadFileContent:
            ChuncksInLine = Line.split(',')
            print ChuncksInLine


def main():
    UpdateRSSILogsWithLocation()


if __name__ == '__main__':
    main()
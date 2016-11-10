import _mysql as MySQL


class LogParserEngine():

    def __init__(self):
        self.DatabaseHandler = MySQL.connect('localhost', 'root', 'Qwertyui12345678', 'indoor_localization')

    def dump_file(self,FileName):
        CurrentFile = "./logParser/LogFiles/%s" % FileName
        print CurrentFile
        with open(CurrentFile, 'r') as LogFile:
            FileContent = LogFile.readlines()
            print (FileContent)
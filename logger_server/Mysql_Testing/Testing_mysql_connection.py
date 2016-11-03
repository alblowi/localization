import _mysql

DatabaseHandler = _mysql.connect('localhost', 'root', 'Qwertyui12345678', 'LoggerDatabase')
# DatabaseHandler.query("""
# INSERT INTO `RSSILogs` ( `Timestamp`, `MacAddress`, `Longitude`, `Latitude`)
# VALUES ( '121212', '44444', '23232323', '6565656565')
# """)

DatabaseHandler.query("""
SELECT `Longitude`, `Latitude`,`MacAddress`, GROUP_CONCAT(`Timestamp`) FROM `RSSILogs` GROUP BY `LogID`
""")

ResultsSet = DatabaseHandler.store_result()

ResultsRows =  ResultsSet.fetch_row(maxrows=0)

for Row in ResultsRows:
    print Row
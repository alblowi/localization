from __future__ import unicode_literals

from django.db import models

class LogParser(models.Model):
    LogFileID = models.AutoField(primary_key=True)
    LogFileDate = models.DateTimeField(auto_now_add=True)
    LogFileName = models.FileField(upload_to="./logParser/LogFiles/")
    LogFileParsed = models.SmallIntegerField(blank=False, default=0)
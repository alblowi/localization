from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import LogParser
from .serializers import LogParserSerializer
from rest_framework import viewsets
from .parsingEngine.LogParser import LogParserEngine

class LogParserViewSet(viewsets.ModelViewSet):
    queryset = LogParser.objects.all()
    serializer_class = LogParserSerializer
    parser_classes = (FormParser, MultiPartParser)

    def perform_create(self, serializer):
        ParserHandler = LogParserEngine()
        ParserHandler.dump_file(self.request.data.get('LogFileName'))
        serializer.save(LogFileName=self.request.data.get('LogFileName'))

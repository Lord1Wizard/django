import random
import logging
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
logger = logging.getLogger(__name__)

def orel(request):
    logger.info('Orel page started')
    return HttpResponse(random.choice(['орел', 'решка']))


def kubik(request):
    logger.info('Kubik page started')
    return HttpResponse(random.randint(1, 6))


def number(request):
    logger.info('Number page started')
    return HttpResponse(random.randint(0, 100))

import unittest
import fakeObjects
import sys
sys.path.append('C:\\Users\\mundipagg\\Documents\\GitHub\\mundipagg-python-api')

from mundipagg.Gateway import Gateway

def CreateOrder(request):
    gateway = Gateway()
    gateway.CreateOrder(request)


if __name__ == "__main__":
    fakeObjects.newBoletoTransaction()
    fakeObjects.newBuyer()
    CreateOrder(fakeObjects.newCreateOrderRequest())

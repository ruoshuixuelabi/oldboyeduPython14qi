from django.test import TestCase

# Create your tests here.

class A(object):pass

a = A()
a.xxx = 1

class Request(object):pass

request = Request()

request.version = "xx"
request.user
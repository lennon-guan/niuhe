NIUHE WebApi Framework
======

What's NIUHE
------
NIUHE framework is a simple webapi framework, which based on flask

Why we need NIUHE
------
Flask is a great framework. But when we use flask to write our web api service, we find serval problems:
1. The route is tooooo free
2. we should manage our protocols and interfaces manually
3. it's difficult to maintain the api document(s), and to test the api(s)

NIUHE provides some useful features, modules and rules, to make developing web api easier:
1. niuhe.proto provides a simple protocol defining class library, which looks like google protobuf, but in pure python
2. niuhe.flask_ext provides the adaptors from http request to api interface, and some debug pages
3. niuhe.codegen provides a code generator. You can generate your NIUHE based project easily.


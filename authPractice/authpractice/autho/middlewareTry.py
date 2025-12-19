from django.shortcuts import HttpResponse
# ------------------Function Based Middleware------------

# def myMiddi(get_response):
#     print('This is one time Initialization of this middi/ bridge')
#     def myInnerFunction(request):
#         print('Some cool function before view hit any request')
#         response = get_response(request)
#         print('Some cool function after view hit any request and giving response')
#         return response
#     return myInnerFunction

# ----------------------Class Based Middleware-------------------
# class A:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print('This is A time Initialization of this middi/ bridge')
#     def __call__(self,request):
#         print('A function before view hit any request')
#         response = self.get_response(request)
#         print('A function after view hit any request and giving response')
#         return response
# class B:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print('This is B time InitiBlization of this middi/ bridge')
#     def __call__(self,request):
#         print('B function before view hit any request')
#         # response = HttpResponse('Chale jao') --> this will response back to B & A middleware
#         response = self.get_response(request)
#         print('B function after view hit any request and giving response')
#         return response
# class C:
#     def __init__(self,get_response):
#         self.get_response = get_response
#         print('This is C time InitiBlization of this middi/ bridge')
#     def __call__(self,request):
#         print('C function before view hit any request')
#         response = self.get_response(request)
#         print('C function after view hit any request and giving response')
#         return response


#------------------------middlware hooks-----------------
# 1. 
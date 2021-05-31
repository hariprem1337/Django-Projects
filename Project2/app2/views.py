from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    message='''
             <html>
               <body align="center">
                  <h1>
                    <span style="background-color: yellowgreen; height: 20%;">Hello! My name is Hari Prem</span>
                  </h1>
                  <h1>
                    <span style="background-color: burlywood; height: 20%;">Welcome to Django</span>
                  </h1>        
               </body>
             </html> '''
    return HttpResponse(message)


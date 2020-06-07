from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    
    return render( request, 'home.html')
   
    

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    # ------------------------new code------------
    a=0
    b=0
    for i in fulltext:
        a+=1
        if i!=" ":
            b+=1
    character_with_space=a
    character=b


    #----------------------end----------------
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary: 
            worddictionary[word] +=1

        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = True)
    
    return render( request, 'count.html',{ 'text':fulltext, 'count': len(wordlist), 'sortedword':sortedword,'character':character_with_space,'characters':character})


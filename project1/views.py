from django.shortcuts import render
#from django.http import HttpResponse
#from . import modules
from .models import Sstudent
from .models import Dstudent
#from . import Dstudent
#from .templates import *

def say_hello(request):

    #sstudent = Sstudent.objects.get(pk=1)

    #queryset = Dstudent.objects.all()
    queryset1 = Sstudent.objects.all()
    queryset2 = Dstudent.objects.all()


    
    #d = Dstudent(id=2,fullname='aq12i1kdsk',dob='2000-02-01')
    #Dstudent.objects.create(d)
    
    # works
    #Dstudent.objects.create(id=2,fullname='aq12i1kdsk',dob='2000-02-01')

    
    for item in queryset1.iterator():
        vid = item.id
        vfn = item.firstname
        vln = item.lastname
        vdob = item.dob
        vfullname = vfn + ' ' + vln
        print(vid)
        print(vfullname)
        print(vdob)
        
        Dstudent.objects.create(id=vid,fullname=vfullname,dob=vdob)

    # Test below works
    #Dstudent.objects.create(id=2,fullname='aq12i1kdsk',dob='2000-02-01')

    

    #return HttpResponse('Hello World')
    #return render(request, 'templates/hello.html', {'name': 'Mosh', 'sstudent' : list(queryset1)})
    #return render(request, 'templates/hello.html', {'name': 'Mosh', 'dstudent' : list(queryset)})
    return render(request, 'templates/hello.html', {'name': 'Mosh', 'sstudent' : list(queryset1), 'dstudent' : list(queryset2)})
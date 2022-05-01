from cgitb import text
from django.shortcuts import render,redirect
import googletrans
from googletrans import Translator
from .models import Trans
# Create your views here.
def index(req):
    s=0
    d=None
    if req.method == "POST":
        s = req.POST.get("sou")
        lan1 = req.POST.get("lan1")
        lan2 = req.POST.get("lan2")
        t = Translator()
        d = t.translate(s, src=lan1, dest=lan2)
        context = {
                "s":s,
                "d":d.text,
                "lan1" : lan1,
                "lan2" : lan2,
            }
        return render(req, 'trans/index.html', context)
    return render(req, 'trans/index.html')
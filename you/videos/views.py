#coding:utf-8
from django.shortcuts import render

from videos.Meipai import getMiaoPai
import urllib
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.

@csrf_exempt
def getVideo(request):
	print "request",request
	if(request.method=='POST'):
		# url = "pp"
		url = request.POST.get('url',None)
		if len(url)==0:
			return render(request, 'miaopai.html',{'video_url':""})
		video_url = getMiaoPai(url)
		return render(request, 'miaopai.html',{'video_url':video_url})
		pass
	else:
		return render(request, 'miaopai.html',{'video_url':""})
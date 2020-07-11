from builtins import FileNotFoundError

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from django.http import FileResponse, Http404


# Create your views here.

def index(request):
	return render(request,"index.html")

def add(request):

	if request.method == 'POST':

		name = request.POST['name']
		reciver_real = request.POST['email']
		reciver='amiskin140@gmail.com'
		subject = request.POST['subject']
		message = 'From :  '+'['+reciver_real+']' +'\n'+'Subject :  '+ subject +'\n'+ 'Message :  '+ request.POST['message']

		send_mail('Contact From Website', message,settings.EMAIL_HOST_USER,[reciver], fail_silently=False)

		#messages.warning(request, 'Your mail has been send successfully!',extra_tags='alert')
		return render(request, "result.html")

	#return render(request, "index.html")


def pdf_read(request):
	if request.method == 'POST':
		try:
			return FileResponse(open('cv/Akshay_Update_CV.pdf', 'rb'), content_type='application/pdf')
		except FileNotFoundError:
			raise Http404()
	#return render(request,"index.html")



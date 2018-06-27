from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from models import Events, Booked_slot
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage
import csv

def home(request):
	return render(request, 'Homepage.html')
	
	
def log_in(request):
	if request.method=='POST':
		username = request.POST['uname']
		password = request.POST['pword']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			#event = Events.objects.values('event_name').distinct()
			return render(request, 'Booking.html')
		else:
			return render(request, 'Homepage.html', {'err_msg':'Invalid Login'})
	else:
		log_out(request)
		return HttpResponse('Access Denied! Error 2305')
		
def choose(request):
	return render(request,'Booking.html')
		
def book(request,etname):
	if request.user.is_authenticated():
		user=User.objects.get(id=request.user.id)
		if etname=='Clash' and user.first_name=='Clash' or etname=='RC' and user.last_name=='RC':
			if Booked_slot.objects.filter(user=user,evname=etname).exists() is False:
				#q=Events.objects.filter(event_name=etname).values('timing').distinct()
				q=Events.objects.filter(event_name=etname,day='Friday')
				#qcount=Events.objects.filter(event_name=etname,day='Friday').count()
				t=Events.objects.filter(event_name=etname,day='Saturday')
				#tcount=Events.objects.filter(event_name=etname,day='Saturday').count()
				return render(request,'Slots.html',{'q':q,'t':t,'etname':etname})
			else:
				return render(request, 'Booking.html',{'er':'You have already booked a slot for '+etname+' !'})
		else:
			return render(request,'Booking.html',{'er':'Your receipt is not valid for '+etname+' !'})
	else:
		log_out(request)
		return HttpResponse('Logged out!')
	

def final(request,etname,dayn,slotn):
	if request.user.is_authenticated():
			usr=User.objects.get(id=request.user.id)
			q=Events.objects.get(event_name=etname,day=dayn,slotid=slotn)
			if q.count==0:
				#ev=Events.objects.filter(event_name=etname).values('timing').distinct()
				eq=Events.objects.filter(event_name=etname,day='Friday')
				#eqcount=Events.objects.filter(event_name=etname,day='Friday').count()
				et=Events.objects.filter(event_name=etname,day='Saturday')
				#etcount=Events.objects.filter(event_name=etname,day='Saturday').count()
				return render(request,'Slots.html',{'q':eq,'t':et,'etname':etname,'msg':'This slot is exhausted!Try for another slots!'})
			else:
				q.count=q.count-1
				q.save()
				b=Booked_slot.objects.create(user=usr,evname=etname,event=q)
				b.save()
				if usr.email!='none':
					send_mail(
					etname+' Slot Booking Details',
					'Mr/Ms '+usr.username +' you have booked slot for '+ etname +' on '+dayn+' at '+q.timing+'.Please be present.',
					'pisbclash.credenz17@gmail.com',
					[usr.email],
					)
					'''email = EmailMessage('CLash Slot Booking','You have booked slot for '+ etname +' on '+dayn+' at '+q.timing+'.Please be present.', to=['ajaysabale07@gmail.com'])
					email.send()'''
					#evt = Events.objects.values('event_name').distinct()
				return render(request, 'Booking.html', {'er':'Your slot is booked!'})
	else:
		log_out(request)
		return HttpResponse('Logged out!')
	
def log_out(request):
	logout(request)
	return render(request, 'Homepage.html')

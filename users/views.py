from django.shortcuts import render
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def home(request):
	body = "Welcome please register"
	title = "Evaluation System"
	user = request.user
	if request.user.is_authenticated():
		body = "Hello %s" %user
	context = {
		"title": title,
		"body": body,
		"user": user,
	}
	return render(request, "home.html", context)
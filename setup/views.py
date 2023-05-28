from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http.response import HttpResponseRedirect, HttpResponse
from .models import Register,Question,SubmitAnswer
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
import json

def home(request):
    name = request.session.get("quizeapp__name","Guest")
    email = request.session.get("quizeapp__email")
    user_detail = Register.objects.filter(name=name,email=email).exists()
    if user_detail:
        user_detail2 = Register.objects.get(name=name,email=email)
        score = SubmitAnswer.objects.filter(name=name).exists()
        if score:
            score = SubmitAnswer.objects.get(name=name)
            score = score.score
        else:
            score = 0
    else:
        user_detail2 = None
        score = None
    return render(request,'home.html',{"name":name,"ud":user_detail2,"score":score})

def register(request):
    if request.session.get("quizeapp__name") and request.session.get("quizeapp__email") is not None:
        return HttpResponseRedirect(redirect_to='/home/')
    else:
        if request.method == "POST":
            fm = RegisterForm(request.POST)
            
            if fm.is_valid():
                name = fm.cleaned_data['name']
                mobile_no = fm.cleaned_data['mobile_no']
                email = fm.cleaned_data['email']
                city = fm.cleaned_data['city']
                address = fm.cleaned_data['address']
                name_unique = Register.objects.filter(name = name).exists()
                email_unique = Register.objects.filter(email = email).exists()
                if name_unique or email_unique:
                    messages.add_message(request,messages.SUCCESS, 'This Email ID or Username already registered..Use another Email ID or Username..')
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    st = Register.objects.create(name=name,mobile_no=mobile_no,email=email,city=city,address=address)
                    st.save()
                    
                    request.session["quizeapp__name"]= name
                    request.session["quizeapp__email"]=email
                
                    return HttpResponseRedirect("/home/")
        else:
            fm = RegisterForm()
        return render(request,'register.html',{"fm":fm})

def logout(request):
    request.session.flush()
    messages.add_message(request,messages.SUCCESS, 'Your response successfully done!!')
    return HttpResponseRedirect(redirect_to='/')

def startquize(request):
    if request.session.get("quizeapp__email") and request.session.get("quizeapp__name"):
        
        
        questions = Question.objects.all().order_by('-id')
        
        paginator = Paginator(questions,1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        user_name = request.session.get("quizeapp__name")
        score = SubmitAnswer.objects.filter(name=user_name).exists()
        if score:
            score = SubmitAnswer.objects.get(name=user_name)
            score = score.score
        else:
            score = 0
        
        return render(request, 'question.html',{"page_obj":page_obj,"user_name":user_name,"score":score})
    else:
        messages.add_message(request,messages.SUCCESS, 'First register your account and then play quiz!!')
        return HttpResponseRedirect(redirect_to='/')
    
@require_POST
def checkAns(request,pk,ans,user):
    if request.method == 'POST':
        
        question = Question.objects.get(pk=pk)
        if ans == question.answer_hidden:
            message = 'Correct'
            
            user_data = SubmitAnswer.objects.get_or_create(name=user)
            score_in = SubmitAnswer.objects.get(name=user)
            score_in.score += question.point  
            score_in.save() 
        else:
            message = 'False'
            
    ctx = {'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')

def alldone(req):
    if req.method == 'POST':
        
        user_name = req.session.get("quizeapp__name")
        score = SubmitAnswer.objects.filter(name=user_name).exists()
        
        if score:
            score = SubmitAnswer.objects.get(name=user_name)
            score = score.score
        else:
            score = 0
        return render(req,'all_done.html',{"score":score})
    else:
        return HttpResponseRedirect('/')

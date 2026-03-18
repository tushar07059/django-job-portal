from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from Appj.models import JobPost
from django.db.models import Q


# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
job_tittle=[
    "First Job",
    "Second Job",
    "Third Job "
]
job_description=[
    "First Job Description",
    "Second Job Description",
    "Third Job Description",
]

def job_list(request):

    query = request.GET.get('query')
    if query:
        job=JobPost.objects.filter (
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        job=JobPost.objects.all()

    context = {
        "jobs": job,
        "query": query
    }

    return render(request, 'Appj/job_list.html', context)

   
    # job=JobPost.objects.all()
    # context={"jobs":job}
    # return render (request ,'Appj/job_list.html', context)


def hello(request): 
    is_authenticated=True 
    list=["alpha","beta"]
  
    context={"name":"Tushar","age":19,"first_list":list,"is_authenticated":is_authenticated}
    return render(request,"Appj/hello.html",context )


def job_detail(request,id):
       
   # return HttpResponse(f"<h2>We will show you all the available jobs page {id} here</h2>  ")
#   site = "https://google.com"
#   return HttpResponse(f"visit <a href={site}>Google here</a>")
        try:
            if id==0:
             return redirect(reverse('jobs_home'))
            # return_html= f"<h1>{job_tittle[id]}</h1> <h3>{job_description[id]}<h3>"
            job=JobPost.objects.get(id=id)
            context={"job": job }
            return render(request,"Appj/job_detail.html",context)
        except:
            return HttpResponseNotFound("NOT FOUND")
        


# def title_page(request):
#     query = request.GET.get('query')
    
#     if query:
#         jobs = job_tittle.objects.filter(title__icontains=query)
#     else:
#         jobs = job_tittle.objects.all()
    
#     return render(request, 'title.html', {
#         'jobs': jobs,
#         'query': query
#     })

        

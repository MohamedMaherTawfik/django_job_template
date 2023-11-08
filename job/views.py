from django.shortcuts import render
from django.views.generic import CreateView
from .models import job,job_apply
from .forms import jobapplyform
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def job_list(request):
    all_jobs=job.objects.all()
    job_count=all_jobs.count()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 7)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
        
    return render(request,'job/job_list.html',{'jobs':all_jobs,'job_count':job_count})



def job_detail(request,slug):
    Job = job.objects.get(slug=slug)
    return render(request,'job/job_detail.html',{'job':Job})


class Job_apply(CreateView):
    model=job_apply
    success_url="/jobs"
    #fields=['user_name','email','linked_in_profile','github_profile','cv','cover_letter']
    form_class=jobapplyform

    def form_valid(self, form):
       
        slug = self.kwargs['slug']
        Job = get_object_or_404(job, slug=slug)
        job_apply = form.save(commit=False)
        job_apply.job = Job
        job_apply.save()
        
        return super().form_valid(form)
    
    
class Addjob(CreateView):
    model=job
    fields=['title','location','company','salary_start','salary_end','description','vacancy','job_type','experince','category']  
    success_url="/jobs/"  
       
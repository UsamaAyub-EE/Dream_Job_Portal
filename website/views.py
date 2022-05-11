from django.shortcuts import render
from django.http import *
from .models import *
import datetime
# Create your views here.
def index(request):
    return render(request, "index.html")

def add_business_stream(request):
    if request.method == "POST":
        bstream = request.POST.get('bstream')
        BusinessStream(business_stream_name=bstream).save()
        return render(
            request,
            "add_business_stream.html",
            {
                'msg':'Business Stream added!'
            })
    else:
        return render(
            request,
            "add_business_stream.html")

def add_job_type(request):
    if request.method == "POST":
        jobtype = request.POST.get('jobtype')
        JobType(job_type=jobtype).save()
        return render(
            request,
            "add_job_type.html",
            {
                'msg':'Jobtype added!'
            })
    else:
        return render(
            request,
            "add_job_type.html")

def add_company(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        cdes = request.POST.get('cdes')
        url = request.POST.get('url')
        est = request.POST.get('est')
        buss_id = request.POST.get('buss_id')
        password = request.POST.get('password')
        buss_stream = BusinessStream.objects.get(id = buss_id)
        Company(password=password,company_name=cname,company_description=cdes,company_website_url=url,establishment_date=est,business_stream=buss_stream).save()
        return render(
            request,
            "add_company.html",
            {
                'business_streams':BusinessStream.objects.all(),
                'msg':'Company added!'
            }
        )
    else:
        return render(
            request,
            "add_company.html",
            {
                'business_streams':BusinessStream.objects.all(),
            })

def add_job_seeker(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        phone_no = request.POST.get('Phone_no')
        user_ins=User(email=email,password=password,gender=gender,dob=dob,phone_no=phone_no)
        user_ins.save()
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        current_salary = request.POST.get('current_salary')
        currency = request.POST.get('currency')
        JobSeeker(f_name=f_name,l_name=l_name,current_salary=current_salary,currency=currency,user=user_ins).save()
        return render(
            request,
            "job_seeker_login.html",
            {
                'msg':'Sign up successful!'
            }
        )
    else:
        return render(
            request,
            "add_job_seeker.html")

def company_login(request):
    if request.method == "POST":
        company_website_url = request.POST.get('company_website_url')
        password = request.POST.get('password')
        if Company.objects.filter(company_website_url=company_website_url,password=password).exists():
            signed_in_comp = Company.objects.get(company_website_url=company_website_url,password=password)
            return render(
            request,
            "add_job.html",
            {
                'msg':'Login successful!',
                'comp_id':signed_in_comp.id,
                'jobtypes':JobType.objects.all()
            })
        else:
            return render(
            request,
            "company_login.html",
            {
                'msg':'URL or password incorrect!',
            })
    else:
        return render(
            request,
            "company_login.html")

def job_seeker_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email,password=password).exists():
            signed_in_user = User.objects.get(email=email,password=password)
            # signed_in_job_seeker = JobSeeker.objects.get(user = signed_in_user)
            # print('user_id in job_seeker_login :',signed_in_user.user_id)
            return render(
            request,
            "job_seeker_page.html",
            {
                'msg':'Login successful!',
                'user_id':signed_in_user.user_id,
                # 'Fname':signed_in_job_seeker.f_name
            })
        else:
            return render(
            request,
            "job_seeker_login.html",
            {
                'msg':'Email or password incorrect!',
            })
    else:
        return render(
            request,
            "job_seeker_login.html")
def job_seeker_page(request):
    # userid = request.GET.get('user_id')
    # print('user_id in job_seeker_page :',userid)
    # signed_in_user = User.objects.get(user_id = userid)
    # signed_in_job_seeker = JobSeeker.objects.get(user = signed_in_user)
    return render(
            request,
            "job_seeker_page.html",
            {
                'user_id':request.GET.get('user_id'),
                # 'Fname':signed_in_job_seeker.f_name
            })

def apply_for_job(request):
    return render(
            request,
            "apply_for_job.html")

def add_education_detail(request):
    if request.method == "POST":
        degree_certificate_name=request.POST.get('degname')
        major=request.POST.get('major')
        percentage=request.POST.get('percentage')
        cgpa=request.POST.get('cgpa')
        start_date=request.POST.get('startdate')
        completion_detail=request.POST.get('enddate')
        user_id=request.POST.get('user_id')
        print('user_id in job_seeker_page :',user_id)
        signed_in_user = User.objects.get(user_id = user_id)
        EducationalDetail(degree_certificate_name=degree_certificate_name,major=major,percentage=percentage,cgpa=cgpa,start_date=start_date,completion_detail=completion_detail,user=signed_in_user).save()
        return render(
            request,
            "job_seeker_page.html",
            {
                'msg':'Education detail added successfully!',
                'user_id':user_id
            })
    else:
        return render(request, "add_education_detail.html",
            {
                'user_id':request.GET.get('user_id')
            })
def add_experience_detail(request):
    if request.method == "POST":
        start_date=request.POST.get('startdate')
        end_date=request.POST.get('enddate')
        job_title=request.POST.get('title')
        company_name=request.POST.get('cname')
        job_location_city=request.POST.get('city')
        job_location_state=request.POST.get('state')
        job_location_country=request.POST.get('country')
        description=request.POST.get('description')
        user_id=request.POST.get('user_id')
        print('user_id in job_seeker_page :',user_id)
        signed_in_user = User.objects.get(user_id = user_id)
        ExperienceDetail(description=description,job_location_country=job_location_country,start_date=start_date,end_date=end_date,job_title=job_title,company_name=company_name,job_location_city=job_location_city,job_location_state=job_location_state,user=signed_in_user).save()
        return render(
            request,
            "job_seeker_page.html",
            {
                'msg':'Experinece detail added successfully!',
                'user_id':user_id
            })
    else:
        return render(request, "add_experience_detail.html",
            {
                'user_id':request.GET.get('user_id')
            })
def add_job(request):
    if request.method == "POST":
        job_description = request.POST.get('jdes')
        
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        street_address=request.POST.get('street_address')
        zip_code=request.POST.get('zip_code')

        job_loc_ins = JobLocation(zip_code=zip_code,country=country,state=state,city=city,street_address=street_address)
        if JobLocation.objects.filter(zip_code=zip_code,country=country,state=state,city=city,street_address=street_address).exists():
            job_loc_ins = JobLocation.objects.get(zip_code=zip_code,country=country,state=state,city=city,street_address=street_address)
        else:
            job_loc_ins.save()

        jobtype_id = request.POST.get('jobtype')
        jobtype = JobType.objects.get(id = jobtype_id)
        
        comp_id=request.POST.get('comp_id')
        signed_in_comp = Company.objects.get(id = comp_id)
        JobPost(is_active=1,job_type=jobtype,company=signed_in_comp,created_date=datetime.datetime.now(),job_description=job_description,job_location=job_loc_ins).save()
        return render(
            request,
            "add_job.html",
            {
                'jobtypes':JobType.objects.all(),
                'comp_id':signed_in_comp.id,
                'msg':'Job posted!'
            }
        )
    else:
        return render(
            request,
            "add_job.html",
            {
                'jobtypes':JobType.objects.all(),
                'comp_id':request.GET.get('comp_id')
            })

def job_search(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        print('cname is ',cname == '')

        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        street_address=request.POST.get('street_address')

        jobtype_id = request.POST.get('jobtype')
        jobtype = JobType.objects.get(id = jobtype_id)

        jobs = JobPost.objects.filter(job_type=jobtype)

        if cname!='':
            comp_obj = Company.objects.get(company_name=cname)
            jobs = jobs.filter(company=comp_obj)

        locations = 1
        s_locations = 1
        ci_locations = 1
        st_locations = 1
        if country!='':
            locations=JobLocation.objects.filter(country=country)
        if state!='':
            s_locations=JobLocation.objects.filter(state=state)
            if isinstance(locations,int):
                locations = s_locations
            else:
                locations = locations & s_locations
        if city!='':
            ci_locations=JobLocation.objects.filter(city=city)
            if isinstance(locations,int):
                locations = ci_locations
            else:
                locations = locations & ci_locations
        if street_address!='':
            st_locations=JobLocation.objects.filter(street_address=street_address)
            if isinstance(locations,int):
                locations = st_locations
            else:
                locations = locations & st_locations
        
        finaljobs = jobs
        if not isinstance(locations,int):
            finaljobs = 1
            for location in locations:
                temp_jobs = jobs.filter(job_location=location)
                if temp_jobs.exists():
                    if isinstance(finaljobs,int):
                        finaljobs = temp_jobs
                    else:
                        finaljobs = finaljobs | temp_jobs
        # for j in finaljobs:
        #     print(j.job_description)
        return render(
            request,
            "job_search.html",
            {
                'jobs':finaljobs,
                'msg':'Sign up successful!',
                'user_id':request.GET.get('user_id'),
                'jobtypes':JobType.objects.all()
            }
        )
    else:
        return render(
            request,
            "job_search.html",
            {
                'user_id':request.GET.get('user_id'),
                'jobtypes':JobType.objects.all()
            })

def admin_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == '2018ee124@student.uet.edu.pk':
            if password == 'pass':
                return render(
                request,
                "admin_page.html")
        else:
            return render(request,"admin_login.html",
            {
                'msg':'Incorrect credentials'
            })
    else:
        return render(request,"admin_login.html")

def admin_page(request):
    return render(request,"admin_page.html")
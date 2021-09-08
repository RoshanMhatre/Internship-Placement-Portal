from django.db.models.query import EmptyQuerySet
from django.shortcuts import redirect, render
from accounts.models import studentUser, companyUser
from dashboard.models import internshipInfo, placementInfo, Student_placement, Student_internship
from django.contrib.auth.decorators import login_required
# Create your views her


suser = studentUser.objects.all()
cuser = companyUser.objects.all()

iinfo = internshipInfo.objects.all()
pinfo = placementInfo.objects.all()


@login_required(login_url="/stusignin")
def studashboard(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    pObj = placementInfo.objects.all().order_by('company_name', '-pk')
    iObj = internshipInfo.objects.all().order_by('company_name', '-pk')
    return render(request, 'studashboard.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})


@login_required(login_url="/stusignin")
def stuprofile(request):
    cuser = companyUser.objects.all()
    studentuser = studentUser.objects.get(user=request.user)
    if request.method == 'POST' or request.method == 'FILES':
        studentuser.yourname = request.POST["student_name_input"]
        studentuser.branch = request.POST["student_branch_input"]
        studentuser.email = request.POST["student_email_input"]
        studentuser.contact = request.POST["student_phone_input"]
        studentuser.yog = request.POST["student_yog_input"]
        try:
            if request.FILES == "":
                pass
            else:
                studentuser.stuImage = request.FILES["stuChooseImage"]
        except:
            studentuser.save()
    studentuser.save()

    suser = studentUser.objects.all()
    for u in suser:
        if request.user.username == u.username:
            img = u.stuImage
            break
    return render(request, 'stuprofile.html', {'suser': suser, 'cuser': cuser, 'img': img})


@login_required(login_url="/stusignin")
def stuplacement(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    pObj = placementInfo.objects.all().order_by('company_name', '-pk')
    stuPlace = Student_placement.objects.all()
    return render(request, 'stuplacement.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'stuPlace': stuPlace})


@login_required(login_url="/stusignin")
def stuinternship(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    iObj = internshipInfo.objects.all().order_by('company_name', '-pk')
    return render(request, 'stuinternship.html', {'suser': suser, 'cuser': cuser, 'iObj': iObj})


@login_required(login_url="/stusignin")
def stuall(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    pObj = placementInfo.objects.all().order_by('company_name', '-pk')
    iObj = internshipInfo.objects.all().order_by('company_name', '-pk')
    return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})


@login_required(login_url="/comsignin")
def comdashboard(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    id = companyUser.objects.only('id').get(username=request.user.username).id
    iObj = internshipInfo.internship_by_id(id)
    pObj = placementInfo.placement_by_id(id)
    studentIntern = []
    studentPlace = []
    for i in iObj:
        siObj = Student_internship.objects.filter(
            internship_id=i, status=True, pending=True)
        if siObj.exists():
            studentIntern.append(siObj)
    for i in pObj:
        spObj = Student_placement.objects.filter(
            placement_id=i, status=True, pending=True)
        if spObj.exists():
            studentPlace.append(spObj)
    # for item in studentIntern:
    #     for querySet in item:
    #         print(querySet.student_username)
    return render(request, 'comdashboard.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj, 'studentIntern': studentIntern, 'studentPlace': studentPlace})


@login_required(login_url="/comsignin")
def comprofile(request):
    suser = studentUser.objects.all()
    companyuser = companyUser.objects.get(user=request.user)
    if request.method == 'POST' or request.method == 'FILES':
        companyuser.companyemail = request.POST["company_email_input"]
        companyuser.address = request.POST["company_address_input"]
        companyuser.contact = request.POST["company_phone_input"]
        try:
            if request.FILES == "":
                pass
            else:
                companyuser.comImage = request.FILES["comChooseImage"]
        except:
            companyuser.save()
    companyuser.save()
    cuser = companyUser.objects.all()
    for c in cuser:
        if request.user.username == c.username:
            img = c.comImage
            break
    return render(request, 'comprofile.html', {'suser': suser, 'cuser': cuser, 'img': img})


@login_required(login_url="/comsignin")
def complacement(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    pObj = placementInfo.placement_by_id(id)
    return render(request, 'complacement.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'com_name': com_name})


@login_required(login_url="/comsignin")
def cominternship(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    iObj = internshipInfo.internship_by_id(id)
    return render(request, 'cominternship.html', {'suser': suser, 'cuser': cuser, 'iObj': iObj, 'com_name': com_name})


@login_required(login_url="/comsignin")
def comall(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    ids = request.user.id
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    id = companyUser.objects.only('id').get(username=request.user.username).id
    iObj = internshipInfo.internship_by_id(id)
    pObj = placementInfo.placement_by_id(id)
    return render(request, 'comall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj, 'com_name': com_name})


@login_required(login_url="/comsignin")
def createPlacement(request):
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    com_email = companyUser.objects.only('companyemail').get(
        username=request.user.username).companyemail
    com_phone = companyUser.objects.only('contact').get(
        username=request.user.username).contact
    if request.method == 'POST' or request.method == 'FILES':
        company_name = request.POST["company_name"]
        package = request.POST["package"]
        domain = request.POST["domain"]
        cgpa_req = request.POST["cgpa_req"]
        comimg = request.FILES["comimg"]
        company_email = request.POST["company_email"]
        company_phone = request.POST["company_phone"]
        company_website = request.POST["company_website"]
        com_name = companyUser.objects.get(username=request.user.username)
        placement = placementInfo.objects.create(company_name=company_name, package=package, domain=domain, cgpa_req=cgpa_req, comimg=comimg, company_email=company_email, company_phone=company_phone,
                                                 company_website=company_website, company_username=com_name)
        placement.save()
        return redirect("/dashboard/comdashboard")
    return render(request, "createPlacement.html", {'com_name': com_name, 'com_email': com_email, 'com_phone': com_phone})


@login_required(login_url="/comsignin")
def createInternship(request):
    com_name = companyUser.objects.only('companyname').get(
        username=request.user.username).companyname
    com_email = companyUser.objects.only('companyemail').get(
        username=request.user.username).companyemail
    com_phone = companyUser.objects.only('contact').get(
        username=request.user.username).contact
    if request.method == 'POST' or request.method == 'FILES':
        company_name = request.POST["company_name"]
        stipend = request.POST["stipend"]
        domain = request.POST["domain"]
        cgpa_req = request.POST["cgpa_req"]
        comimg = request.FILES["comimg"]
        modeofwork = request.POST["modeofwork"]
        workduration = request.POST["workduration"]
        company_email = request.POST["company_email"]
        company_phone = request.POST["company_phone"]
        company_website = request.POST["company_website"]
        com_name = companyUser.objects.get(username=request.user.username)
        internship = internshipInfo.objects.create(company_name=company_name, stipend=stipend, domain=domain, cgpa_req=cgpa_req, comimg=comimg,
                                                   modeofwork=modeofwork, workduration=workduration, company_email=company_email, company_phone=company_phone,
                                                   company_website=company_website, company_username=com_name)
        internship.save()
        return redirect("/dashboard/comdashboard")
    return render(request, 'createInternship.html', {'com_name': com_name, 'com_email': com_email, 'com_phone': com_phone})


@login_required(login_url="/stusignin")
def regFormPlacement(request):
    if request.method == 'POST':
        pid = request.POST["getpid"]
        student_username = studentUser.objects.get(user=request.user)
        placement_id = placementInfo.objects.get(id=pid)
        studentPlacement = Student_placement.objects.create(
            placement_id=placement_id, student_username=student_username, pending=True)
        studentPlacement.save()
        return redirect(placement_id.regform_link)


@login_required(login_url="/stusignin")
def regFormInternship(request):
    if request.method == 'POST':
        iid = request.POST["getiid"]
        student_username = studentUser.objects.get(user=request.user)
        internship_id = internshipInfo.objects.get(id=iid)
        studentInternship = Student_internship.objects.create(
            internship_id=internship_id, student_username=student_username,  pending=True)
        studentInternship.save()
        return redirect(internship_id.regform_link)


@login_required(login_url="/stusignin")
def search(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    pObj = placementInfo.objects.all().order_by('company_name', '-pk')
    iObj = internshipInfo.objects.all().order_by('company_name', '-pk')
    if request.method == 'GET':
        search = request.GET['search_input']
        iObj = internshipInfo.objects.filter(company_name__icontains=search)
        pObj = placementInfo.objects.filter(company_name__icontains=search)
        if not iObj.exists() and not pObj.exists():
            iObj = internshipInfo.objects.filter(domain__icontains=search)
            pObj = placementInfo.objects.filter(domain__icontains=search)
            return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})
        return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})
    return render(request, 'stuall.html', {'suser': suser, 'cuser': cuser, 'pObj': pObj, 'iObj': iObj})

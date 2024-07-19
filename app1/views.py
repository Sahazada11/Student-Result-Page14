from django.shortcuts import render,redirect
from app1.forms import MarksForm
from app1.models import Marks
# Create your views here.
def index_view(request):
    form=MarksForm()
    return render(request,"app1/index.html",context={"form":form})

def add_view(request):
    if request.method=="GET":
        form=MarksForm()
        return render(request,"app1/add_stud.html",context={"form":form})
    elif request.method=="POST":
        form=MarksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        form=MarksForm()
        return render(request,"app1/add_stud.html",context={"form":form})

def list_view(request):
    marks_data=Marks.objects.all()    
    return render(request,"app1/list_mark.html",context={"marks_data":marks_data})

def edit_view(request,id):
    if request.method=="GET":
        stud=Marks.objects.get(id=id)
        form=MarksForm(instance=stud)
        return render(request,"app1/update_stud.html",context={"form":form})
    elif request.method=="POST":
        stud=Marks.objects.get(id=id)
        form=MarksForm(request.POST,instance=stud)
        if form.is_valid():
            form.save(commit=True)
            return redirect("update")

def search_view(request):
    return render(request,"app1/search.html", context={})

def find_view(request):
    rollno=request.GET.get("rollno")
    try:
        stud=Marks.objects.get(rollno=rollno)
        found=True
        return render(request,"app1/search.html",context={"stud":stud,"found":found})
    except:
        return render(request,"app1/search.html",context={"msg":"Invalid Roll-No"})

def result_view(request):
    mark_qs=Marks.objects.all()
    mark_list=[]
    for stud in mark_qs:
        row=[stud.rollno,stud.name,stud.subject1,stud.subject2,stud.subject3,stud.subject4]
        rs="PASS" if stud.subject1>'40' and stud.subject2>'40' and stud.subject3>'40' and stud.subject4>='40' else "FAIL"
        row.append(rs)
        mark_list.append(row)
    return render(request,"app1/result.html",context={"mark_list":mark_list})


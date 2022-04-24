from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *


class PatListView(ListView):
    queryset = Patient.objects.all()
    template_name = 'Frames/Patientlist.html'
    context_object_name = 'Patient'
    paginate_by = 10


class PatDetailView(DetailView):
    model = Patient
    template_name = 'Frames/Patientdetail.html'


def PatDetail(request, id):
    sid = Raw_video.objects.get(patient=id)
    ex = Ex_video.objects.get(raw_video=sid.id)
    return render(request, 'Frames/Patientdetail.html', {'sid': sid, 'ex': ex})


class ExListView(ListView):
    queryset = Exercise.objects.all()
    template_name = 'Frames/exercise.html'
    context_object_name = 'Exercise'
    paginate_by = 10


def post(request):
    dt = request.POST['patient']
    dat1 = Raw_video.objects.get(patient=dt)
    # dat2 = Ex_video.objects.select_related('raw_video').get(raw_video=dat1.pk)
    # return HttpResponse(dt)
    return render(request, 'result.html', {'raw': dat1, 'dt': dt})


def post2(request):
    dt = request.POST['exercise']
    dat1 = Ex_video.objects.get(exercise=dt)

    #    dat2 = Ex_video.objects.select_related('raw_video').get(raw_video=dat1.pk)
    #    return HttpResponse(dt)
    return render(request, 'result2.html', {'raw': dat1, 'dt': dt})


def Search_id(request, Patient_id):
    q = Patient.objects.get(pk=Patient_id)
    data = q.raw_video_set.get(pk=Patient_id)
    data2 = data.acceleration_set.all
    return render(request, "seacrh_id.html", {"qs": q, "data2": data2})


def Search2_id(request, Exercise_id):
    q = Exercise.objects.get(pk=Exercise_id)
    return render(request, 'search2_id.html', {'raw': q})


def Ground_Truth(request):
    data = Ground_truth.objects.all()
    return render(request, 'Ground_Tracking/Patient_in_Groundtruth.html', {'data': data})


def tracking(request):
    data = Tracking.objects.all()
    return render(request, 'Ground_Tracking/Tracking.html', {'data': data})


def DataSengment(request):
    return render(request, 'Data_set.html')


class FileView(ListView):
    model = Files
    template_name = 'file.html'
    context_object_name = 'files'
    paginate_by = 6

    def get_queryset(self):
        return Files.objects.order_by('-id')


def uploadForm(request):
    return render(request, 'upload.html')


def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'Files Submitted successfully!')
        return redirect('files')
    else:
        messages.error(request, 'Files was not Submitted successfully!')
        return redirect('form')


def detectionview(request):
    detectiondata = Detection.objects.all()
    segmentationdata=Segmentation.objects.all()
    return render(request, 'Data_set.html', {'dataDec': detectiondata,'dataSeg':segmentationdata })

def add_Detection(request):
    return render(request, 'Frames/detection.html')


def adddection(request):
    if request.method == 'POST':
        DataAug = request.POST['DataAug']
        apLeft = request.POST['apLeft']
        apRight = request.POST['apRight']
        mapIou50 = request.POST['mapIou50']
        mapIou75 = request.POST['mapIou75']
        mapIou = request.POST['mapIou']
        paperlink = request.POST['paperlink']

        detection = Detection.objects.create(DataAug=DataAug, apLeft=apLeft, apRight=apRight, mapIou50=mapIou50,
                                             mapIou75=mapIou75, mapIou=mapIou, paperlink=paperlink)
        detection.save()
        return HttpResponseRedirect('/frame/SegmentationDataset')

    else:
        return (request, 'home.html')
    return render(request, 'Frames/detection.html')


class DetectionView(View):
    def get(self, request):
        return render(request, 'Frames/detection.html')
    def post(self, request):
        DataAug = request.POST['DataAug']
        apLeft = request.POST['apLeft']
        apRight = request.POST['apRight']
        mapIou50 = request.POST['mapIou50']
        mapIou75 = request.POST['mapIou75']
        mapIou = request.POST['mapIou']
        paperlink = request.POST['paperlink']

        detection = Detection.objects.create(DataAug=DataAug, apLeft=apLeft, apRight=apRight, mapIou50=mapIou50,
                                             mapIou75=mapIou75, mapIou=mapIou, paperlink=paperlink)
        detection.save()
        messages.success(request, 'Result successfully created')
        return render(request, 'Frames/detection.html')

class SegmentationView(View):
    def get(self, request):
        return render(request, 'Frames/segmentation.html')
    def post(self, request):
        DataAug = request.POST['DataAug']
        apLeft = request.POST['apLeft']
        apRight = request.POST['apRight']
        mapIou50 = request.POST['mapIou50']
        mapIou75 = request.POST['mapIou75']
        mapIou = request.POST['mapIou']
        paperlink = request.POST['paperlink']

        segmentation = Segmentation.objects.create(DataAug=DataAug, apLeft=apLeft, apRight=apRight, mapIou50=mapIou50,
                                             mapIou75=mapIou75, mapIou=mapIou, paperlink=paperlink)
        segmentation.save()
        return render(request, 'Frames/segmentation.html')


class GeneralView(View):
    def get(self, request):
        generaldata = General.objects.all()
        patientdata = Patient.objects.all()
        rawvideodata = Raw_video.objects.all()

        exercisedata=Exercise.objects.all()

        return render(request, 'Frames/General.html',
                      {'generaldata': generaldata, 'patientdata': patientdata,
          'exercisedata': exercisedata, 'rawvideodata':rawvideodata})

    def post(self,request):
        pat_id= request.POST['patient']
        ex_id = request.POST['exercise']
        if(pat_id=="0" and ex_id=='0'):
            generaldata = General.objects.all()
        elif (pat_id=="0" and ex_id!='0'):
            generaldata = General.objects.filter(exercise=ex_id)
        elif (pat_id !="0" and ex_id=='0'):
            generaldata = General.objects.filter(patient=pat_id)
        else:
            generaldata = General.objects.filter(patient=pat_id, exercise=ex_id)
        patientdata = Patient.objects.all()
        exercisedata = Exercise.objects.all()
        ex_id=int(ex_id)
        pat_id=int(pat_id)
        return render(request, 'Frames/General.html',
                      {'generaldata': generaldata, 'patientdata': patientdata, 'exercisedata': exercisedata,'pat_id':pat_id,'ex_id':ex_id})




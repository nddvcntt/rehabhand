from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Patient(models.Model):
    sex_choice = (('Male', 'Male'), ('Female', 'Female'))
    hand_choice = (('Left', 'Left'), ('Right', 'Right'))
    name = models.CharField(max_length=255, verbose_name='Patient name')
    age = models.IntegerField()
    sex = models.CharField(choices=sex_choice, default='Male', max_length=50)
    address = models.CharField(max_length=400)
    weakhand = models.CharField(choices=hand_choice, verbose_name='Weak hand', default='Left', max_length=50)
    stronghand = models.CharField(choices=hand_choice, verbose_name='Strong hand', default='Left', max_length=50)


    def __str__(self):
        return " %s" % (self.name)

    class Meta:
        db_table = 'Patient'
        # Add verbose name
        verbose_name_plural = 'Patients list'

class Raw_video(models.Model):
    choice_camera = (('Head', 'Head'), ('Chest', 'Chest'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    position = models.CharField(choices=choice_camera, default='Head', verbose_name='Camera position', max_length=50)
    nFrames = models.IntegerField()
    name=models.CharField(max_length=255, blank=True, null=True)
    file_path = models.TextField(blank=True, null=True, default=None)
    left_hand_Accelerometer=models.CharField(max_length=255, blank=True, null=True)
    right_hand_Accelerometer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return " %s, %s" % (self.name, self.position)

    class Meta:
        db_table = 'Raw_video'
        # Add verbose name
        verbose_name_plural = 'Raw video'


class Exercise(models.Model):
    name_vn = models.CharField(max_length=255, verbose_name='Vietnamese name')
    name_uk = models.CharField(max_length=255, verbose_name='English name')
    frequency = models.IntegerField()


    # ul = models.IntegerField(choices=choice_limb, default=0)

    def __str__(self):
        return " %s" % (self.name_uk,)

    class Meta:
        db_table = 'Exercise'
        # Add verbose name
        verbose_name_plural = 'Exercise list'


class Ex_video(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    raw_video = models.ForeignKey(Raw_video, on_delete=models.CASCADE)
    file_name=models.CharField(max_length=255, null=True, blank=True)
    frame_start = models.IntegerField()
    frame_stop = models.IntegerField()
    period= models.IntegerField(default=0)
    path = models.TextField(null=True, blank=True)
    patient=models.ManyToManyField('Patient',related_name='ex_video')
    def __str__(self):
        return " %s, %s" % (self.file_name, self.exercise)

    class Meta:
        db_table = 'Ex_video'
        # Add verbose name
        verbose_name_plural = 'Exercise video'


class Seg_video(models.Model):
    ex_video = models.ForeignKey(Ex_video, on_delete=models.CASCADE)
    start = models.TimeField( default=None)
    end = models.TimeField( default=None)
    action=models.IntegerField(default=0)
    th = models.IntegerField(default=0)

    def __str__(self):
        return " %s, %s, %s" % (self.ex_video, self.frame_start, self.frame_stop)

    class Meta:
        db_table = 'Seg_video'
        # Add verbose name
        verbose_name_plural = 'Segment video'


class Ground_truth(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, default=None)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True, default=None)
    frame_start = models.IntegerField(null=True, blank=True, default=None)
    frame_stop = models.IntegerField(null=True, blank=True, default=None)
    path = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return " %s, %s, %s " % (self.frame_start, self.frame_stop, self.path)

    class Meta:
        db_table = 'ground_truth'
        # Add verbose name
        verbose_name_plural = 'Ground_truth'


class Tracking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True, default=None)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True, default=None)
    frame_start = models.IntegerField(null=True, blank=True, default=None)
    frame_stop = models.IntegerField(null=True, blank=True, default=None)
    path = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return " %s, %s, %s " % (self.frame_start, self.frame_stop, self.path)

    class Meta:
        db_table = 'tracking'
        # Add verbose name
        verbose_name_plural = 'Tracking'


class Files(models.Model):
    filename = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='store/pdfs/')
    cover = models.ImageField(upload_to='store/covers/', null=True, blank=True)

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

class Detection(models.Model):
    DataAug = models.CharField(null=True, blank=True,max_length=255)
    apLeft = models.DecimalField(default=0, decimal_places=2, max_digits=4 )
    apRight = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    mapIou50 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    mapIou75 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    mapIou = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    paperlink=models.URLField(null=True, blank=True,max_length=500,default=None)
    def __str__(self):
        return " %s, %s, %s" % (self.DataAug, self.apLeft, self.apRight)

    class Meta:
        db_table = 'Detection'
        # Add verbose name
        verbose_name_plural = 'Detection'

class Segmentation(models.Model):
    DataAug = models.CharField(null=True, blank=True,max_length=255)
    apLeft = models.FloatField(default=0)
    apRight = models.FloatField(default=0)
    mapIou50 = models.FloatField(default=0)
    mapIou75 = models.FloatField(default=0)
    mapIou = models.FloatField(default=0)
    paperlink = models.CharField(null=True, blank=True, max_length=500, default=None)
    # Sensor = models.TextField( null=True, blank=True,default=None )
    def __str__(self):
        return " %s, %s, %s" % (self.DataAug, self.apLeft, self.apRight)

    class Meta:
        db_table = 'Segmentation'
        # Add verbose name
        verbose_name_plural = 'Segmentation'


class General(models.Model):
    hand_choice = (('left', 'left'), ('right', 'right'))
    data=models.CharField(max_length=255)
    dextroushand=models.CharField(max_length=255)
    weekhand = models.CharField(max_length=255)
    timestart=models.CharField(max_length=255)
    timestop=models.CharField(max_length=255)
    path_camera=models.CharField(max_length=1000, default=None)
    path_accelerometor=models.CharField(max_length=1000, default=None)
    ex_hand=models.CharField(choices=hand_choice, default='right',max_length=30)
    patient = models.IntegerField(default=None,null=True )
    exercise= models.IntegerField(default=None,null=True )

    def __str__(self):
        return " %s, %s, %s, %s, %s, %s, %s" % (self.data, self.dextroushand, self.weekhand,self.timestart, self.timestop, self.path_camera, self.path_accelerometor)
    class Meta:
        db_table = 'general'
        # Add verbose name
        verbose_name_plural = ' Bảng Tổng hợp'






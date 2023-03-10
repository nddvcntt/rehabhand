# Generated by Django 4.0.3 on 2022-03-31 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataAug', models.CharField(blank=True, max_length=255, null=True)),
                ('apLeft', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('apRight', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('mapIou50', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('mapIou75', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('mapIou', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('paperlink', models.URLField(blank=True, default=None, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Detection',
                'db_table': 'Detection',
            },
        ),
        migrations.CreateModel(
            name='Ex_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('frame_start', models.IntegerField()),
                ('frame_stop', models.IntegerField()),
                ('period', models.IntegerField(default=0)),
                ('path', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Exercise video',
                'db_table': 'Ex_video',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vn', models.CharField(max_length=255, verbose_name='Vietnamese name')),
                ('name_uk', models.CharField(max_length=255, verbose_name='English name')),
                ('frequency', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Exercise list',
                'db_table': 'Exercise',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='store/covers/')),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('dextroushand', models.CharField(max_length=255)),
                ('weekhand', models.CharField(max_length=255)),
                ('timestart', models.CharField(max_length=255)),
                ('timestop', models.CharField(max_length=255)),
                ('path_camera', models.CharField(default=None, max_length=1000)),
                ('path_accelerometor', models.CharField(default=None, max_length=1000)),
            ],
            options={
                'verbose_name_plural': ' B???ng T???ng h???p',
                'db_table': 'general',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Patient name')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('address', models.CharField(max_length=400)),
                ('weakhand', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='Left', max_length=50, verbose_name='Weak hand')),
                ('stronghand', models.CharField(choices=[('Left', 'Left'), ('Right', 'Right')], default='Left', max_length=50, verbose_name='Strong hand')),
            ],
            options={
                'verbose_name_plural': 'Patients list',
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='Segmentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataAug', models.CharField(blank=True, max_length=255, null=True)),
                ('apLeft', models.FloatField(default=0)),
                ('apRight', models.FloatField(default=0)),
                ('mapIou50', models.FloatField(default=0)),
                ('mapIou75', models.FloatField(default=0)),
                ('mapIou', models.FloatField(default=0)),
                ('paperlink', models.CharField(blank=True, default=None, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Segmentation',
                'db_table': 'Segmentation',
            },
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_start', models.IntegerField(blank=True, default=None, null=True)),
                ('frame_stop', models.IntegerField(blank=True, default=None, null=True)),
                ('path', models.TextField(blank=True, default=None, null=True)),
                ('exercise', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frame.exercise')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frame.patient')),
            ],
            options={
                'verbose_name_plural': 'Tracking',
                'db_table': 'tracking',
            },
        ),
        migrations.CreateModel(
            name='Seg_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(default=None)),
                ('end', models.TimeField(default=None)),
                ('action', models.IntegerField(default=0)),
                ('th', models.IntegerField(default=0)),
                ('ex_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frame.ex_video')),
            ],
            options={
                'verbose_name_plural': 'Segment video',
                'db_table': 'Seg_video',
            },
        ),
        migrations.CreateModel(
            name='Raw_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Head', 'Head'), ('Chest', 'Chest')], default='Head', max_length=50, verbose_name='Camera position')),
                ('nFrames', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file_path', models.TextField(blank=True, default=None, null=True)),
                ('left_hand_Accelerometer', models.CharField(blank=True, max_length=255, null=True)),
                ('right_hand_Accelerometer', models.CharField(blank=True, max_length=255, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frame.patient')),
            ],
            options={
                'verbose_name_plural': 'Raw video',
                'db_table': 'Raw_video',
            },
        ),
        migrations.CreateModel(
            name='Ground_truth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_start', models.IntegerField(blank=True, default=None, null=True)),
                ('frame_stop', models.IntegerField(blank=True, default=None, null=True)),
                ('path', models.TextField(blank=True, default=None, null=True)),
                ('exercise', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frame.exercise')),
                ('patient', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='frame.patient')),
            ],
            options={
                'verbose_name_plural': 'Ground_truth',
                'db_table': 'ground_truth',
            },
        ),
        migrations.AddField(
            model_name='ex_video',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frame.exercise'),
        ),
        migrations.AddField(
            model_name='ex_video',
            name='patient',
            field=models.ManyToManyField(related_name='ex_video', to='frame.patient'),
        ),
        migrations.AddField(
            model_name='ex_video',
            name='raw_video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frame.raw_video'),
        ),
    ]

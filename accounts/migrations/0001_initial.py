# Generated by Django 2.2.2 on 2019-07-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('q1', models.IntegerField(default=0)),
                ('q1ans', models.CharField(max_length=100)),
                ('q2', models.IntegerField(default=0)),
                ('q2ans', models.CharField(max_length=100)),
                ('q3', models.IntegerField(default=0)),
                ('q3ans', models.CharField(max_length=100)),
                ('q4', models.IntegerField(default=0)),
                ('q4ans', models.CharField(max_length=100)),
                ('q5', models.IntegerField(default=0)),
                ('q5ans', models.CharField(max_length=100)),
                ('q6', models.IntegerField(default=0)),
                ('q6ans', models.CharField(max_length=100)),
                ('qattempt', models.IntegerField(default=0)),
                ('qwrong', models.IntegerField(default=0)),
                ('qright', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('pword', models.CharField(max_length=32)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('rollno', models.TextField(max_length=10)),
                ('attempt', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('result', models.IntegerField()),
                ('rhour', models.IntegerField(default=3)),
                ('rminute', models.IntegerField(default=0)),
                ('rsecond', models.IntegerField(default=0)),
                ('commitment', models.BooleanField(default=False)),
            ],
        ),
    ]

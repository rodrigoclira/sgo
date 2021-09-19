from django.db import models

class ProjectType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="nome")

class Project(models.Model):
    name = models.CharField(verbose_name="nome")
    type = models.ForeignKey(ProjectType, on_delete = models.SET_NULL)

class Announcement(models.Model):
    name = models.CharField(verbose_name="nome do edital")
    announcement_data = models.CharField(verbose_name="documentos do edital")

class WorkPlan(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete = models.SET_NULL, blank = True)
    drive_folder = models.URLField(verbose_name="pasta do gdrive")
    start_date = models.DateField(verbose_name="data de início")
    end_data = models.DateField(verbose_name="data de fim")

class Report(models.Model):
    OPTIONS = (("M", "Mensal"), ("P", "Parcial"), ("F", "Final"), ("O", "Outro"))
    type = models.CharField(max_length=1, choices=OPTIONS, blank=False, null=False)

class Request(models.Model):
    pass
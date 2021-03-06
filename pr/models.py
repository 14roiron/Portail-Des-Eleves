
from django.db import models
from django import forms
from trombi.models import UserProfile
from django.core.files import File
import subprocess
import os
from django import forms
from django.forms import ModelForm

class Clip(models.Model):
	titre = models.CharField(max_length=100)
	lien = models.URLField()
	promo = models.IntegerField()
	
	class Meta:
		ordering = ["-promo", "titre"]
		
	def __str__(self):
		return self.titre
	

class Candidat(models.Model):    #C'est la petite zoe qui veut faire de la balancoire mais elle n'y arrive pas. 
    nom = models.CharField(max_length=32)   #Pourquoi 
    nbVotes = models.IntegerField() #Parce qu'elle n'a pas de bras ... merci 13Jougla
    debut_vote = models.DateTimeField()
    fin_vote = models.DateTimeField()
    
    def __str__(self):
        return self.nom  

class Vote(models.Model):
    liste = models.ForeignKey(Candidat)
    eleve = models.ForeignKey(UserProfile, related_name="votes")
    
    def __str__(self):
        return 'vote de ' + self.eleve.user.username + ' pour ' + self.liste.nom
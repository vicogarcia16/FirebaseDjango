from django.shortcuts import render
# Importo las clases render y View 
from django.views.generic import View
# Importo Firebase Admin SDK 
import firebase_admin
# Hacemos uso de credenciales que nos permitirán usar Firebase Admin SDK 
from firebase_admin import credentials
# Importo el Servicio Firebase Realtime Database 
from firebase_admin import db
 
# Create your views here.
class Postres(View):
 
	# Especifico la plantilla o template que usaré 
	template_name = "index.html"
 
	# Llamo al archivo JSON que contiene mi clave privada 
	cred = credentials.Certificate('./') 
 
	# Iniciamos los servicios de Firebase con las credenciales y el nombre de mi proyecto en Firebase 
	firebase_admin.initialize_app(cred, {
	    'databaseURL': ''
	})
 
	# Accedo a la base de datos, específicamente a la tabla 'postres' 
	ref = db.reference('postres') 
	#print(ref.get())
 
	# Llamo los datos que se encuentran en la tabla 'postres' 
	datos = ref.get()
 
	# Envio los datos de la tabla 'postres' a la vista o template 
	def get(self, request):		
		return render(request, self.template_name, { "productos": self.datos})

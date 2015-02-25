######-Listas
@auth.requires_login()
def f_listas():
	response.title = 'Listas'
	response.marca=['Extensões', 'Listas']
	editor = permissao()
	url = URL('admanager', 'listas', 'f_listas_form')

	con = db(Listas).select(orderby=Listas.id)
	
	return response.render("listas/show_listas.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_listas_form():
	response.title = 'Listas'
	response.marca=['Extensões', 'Listas', 'Adiciona Lista']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Listas)
	else:
		form 	=	SQLFORM(Listas, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.numero['_placeholder'] = "exemplo: 01699999999"

	if form.process().accepted:
		redirect(URL('f_listas'))
	else:
		print request.vars

	return response.render("listas/form_listas.html", form=form)


def ajax_listas():
	print request.vars
	if request.vars.tec == 'Departamento':
		con = db(Departamentos.mostrar == True).select(Departamentos.departamento, orderby=Departamentos.departamento)
		#con = con.as_json()
	elif request.vars.tec == 'Ramal':
		con = db(Ramal_virtual.ramal_virtual).select(Ramal_virtual.ramal_virtual, orderby=Ramal_virtual.ramal_virtual)
		#con = con.as_json()
	else:
		con={}

	print con

	return response.json(con)



######-CallBack
@auth.requires_login()
def f_callback():
	response.title = 'CallBack'
	response.marca=['Extensões', 'CallBack']
	editor = permissao()
	url = URL('admanager', 'listas', 'f_callback_form')

	con = db(Callback).select(orderby=Callback.id)
	
	return response.render("listas/show_callback.html",  
					url=url, editor=editor, con=con)

@auth.requires(auth.has_membership('gerenciador') or auth.has_membership('administrador'))
def f_callback_form():
	response.title = 'CallBack'
	response.marca=['Extensões', 'CallBack', 'Adiciona CallBack']
	id_edit	= request.vars['id_edit']
	
	if id_edit is None:
		form 	=	SQLFORM(Callback)
	else:
		form 	=	SQLFORM(Callback, id_edit)

	for input in form.elements():
		input['_class'] = 'form-control'
	form.custom.widget.numero['_placeholder'] = "exemplo: 01699999999"

	if form.process().accepted:
		redirect(URL('f_callback'))

	return response.render("listas/form_callback.html", form=form)

##
##Consultas CSV portabilidade
@auth.requires_login()
def form_consulta_port():
	response.title = 'Consulta Portabilidade'
	response.marca=['Extensões', 'Consulta Portabilidade']
	dict_operadora=''

	if request.vars.param != None:
		dict_operadora = csv_read(request.vars.param)
		
	if request.is_local:
		uploadfolder='/home/fernando/web2py/applications/admanager/upload'
	else:
		uploadfolder='/var/www/web2py/applications/admanager/upload'

	form = SQLFORM.factory(
		Field("arquivo", "upload", uploadfolder=uploadfolder, 
		requires=IS_UPLOAD_FILENAME(extension='csv', error_message=T("arquivo precisa conter formato .CSV")))
	)
	for input in form.elements():
		input['_class'] = 'form-control'

	if form.process().accepted:
		print form.vars['arquivo']
		redirect(URL(vars={'param':form.vars['arquivo']}))

	return response.render("listas/form_consulta_port.html", form=form, dict_operadora=dict_operadora)

@auth.requires_login()
def csv_read(arquivo):
	print 'csv_read'
	import csv, urllib, httplib2
	i=0
	numero=''
	dict_operadora={}
	claro=0 
	tim=0 
	vivo=0 
	oi=0 
	ctbc=0 
	nextel=0
	inexis=0
	if request.is_local:
		uploadfolder='/home/fernando/web2py/applications/admanager/upload'
	else:
		uploadfolder='/var/www/web2py/applications/admanager/upload'

	ati_user='adaldeia'
	ati_pass="#4Ld31A%"
	#ati_url = 'http://lnpcluster.sippulse.com:9091/?ret&num=%s' %(numero)
	h = httplib2.Http('.cache')
	h.add_credentials(ati_user, ati_pass)
	
	caminho = "%s/%s" %(uploadfolder, arquivo)
	cr = csv.reader(open(caminho,"rb"))
	
	for row in cr:
		if i > 0:
			#print row[0]
			ati_url = 'http://lnpcluster.sippulse.com:9091/?ret&num=%s' %(row[0])
			resp = h.request(ati_url, 'GET')[1]
			codigo = resp.split(";")[0]

			if codigo == '55321':
				claro+=1
			elif codigo == '55341':
				tim+=1
			elif (codigo == '55320') or (codigo == '55323') or (codigo == '55315'):
				vivo+=1
			elif (codigo == '55331') or (codigo == '55335') or (codigo == '55314'):
				oi+=1
			elif (codigo == '55377') or (codigo == '55351'):
				nextel+=1
			elif codigo == '55000':
				inexis+=1
		i=i+1

	dict_nome={'claro':claro, 'tim':tim, 'vivo':vivo, 'oi':oi, 'nextel':nextel, 'inexis':inexis}	
	for item in dict_nome:
		if dict_nome[item] !=0:
			dict_operadora[item]=dict_nome[item]
	session.dict_operadora = dict_operadora
	return dict_operadora

@auth.requires_login()
def json_csv():
	print request.vars
 	#dict_operadora = csv_read(request.vars.param)
 	if request.vars.param == 'None': 
 		dict_operadora = {}
 	else:
 		dict_operadora = session.dict_operadora

 	colunas = [{"label":"Operadora","type":"string"},
			{"label":"Quantidade","type":"number"}]

	linhas=[]
	for item in dict_operadora:
		linhas.append({"c":[{"v":item},{"v":dict_operadora[item]}]})


	final ={"rows" : linhas, "cols" : colunas}

	return response.json(final)


@auth.requires_login()
def delete():
	print request.vars
	funcao 	=	request.vars['tabela']
	id_tab	=	request.vars['id_tab']

	if funcao	== "f_callback":
		tabela 	=	Callback.id
		funcao	= 	"f_callback"
	if funcao == "f_listas":
		tabela = Listas.id
		funcao = "f_listas"

	db(tabela == id_tab).delete()
	redirect(URL(funcao))


def mesa():
	ajax_mesa()

	return response.render("listas/mesa.html")

def ajax_mesa():
    import pprint
    from pyajam import Pyajam

    ajam = Pyajam(username='python', password='123456')
    con = ajam.peers()
    dict_final={}
    ramal = db(Ramal_virtual).select(Ramal_virtual.ramal_virtual, Ramal_virtual.ramal_fisico)
    print ramal

    for dado in con:
        for rm in ramal:
            if rm.ramal_fisico == dado['objectname']:
                print dado['objectname']
                dict_final[rm.ramal_virtual]=dado

    return response.json(dict_final)


def read_xml():
	#sem uso
	import requests, urllib2
	from cookielib import Cookie, CookieJar
	from xml.etree.ElementTree import ElementTree

	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	opener.open("http://192.168.100.253:8088/asterisk/mxml?action=login&username=python&secret=123456")
 
	tree = ElementTree(file=opener.open('http://192.168.100.253:8088/asterisk/mxml?action=queuestatus'))
	#print tree
 
	r = tree.getroot()
	#print r
 
	pessoa = r.find('response')
	print pessoa.attrib
 
	a=0
	lista=[]
	fila=[]
	for child in r:
		for var in child:
			if a == 0:
				print var.attrib['message']
				print '>>>>>>>>>>'
				a=a+1
			else:
				evento = var.attrib['event']
				if evento == 'QueueParams':
					if fila == []: #primeira entrada nome da fila
						fila.append(var.attrib['queue'])
						print var.attrib['queue']
						print '>>>>>>>>>>'
					else: #demais entradas noma da fila
						lista.append(fila)
						fila=[]
						fila.append(var.attrib['queue'])
						print var.attrib['queue']
						print '>>>>>>>>>>'
				elif evento == 'QueueMember': #entrada membros da fila
					print var.attrib['name']
					fila.append(var.attrib['name'])
					#print fila
				elif evento == 'QueueStatusComplete': #ultima entrada 
					lista.append(fila)
	#for lin in lista:
	#	lista = lin
 
	return response.json(lista)

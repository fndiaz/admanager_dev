# -*- coding: utf-8 -*-

#########################################################################
## Extras
#########################################################################
import time

def permissao():
	editor = False
	for row in session.auth.user_groups:
		grupo = session.auth.user_groups[row]
		if (grupo == "gerenciador") or (grupo == "administrador"):
			editor = True
	return editor

def escreve_sip_iax():
	ramais = db(db.fisico_sip_iax).select(orderby=db.fisico_sip_iax.usuario)
	sip = open('/aldeia/etc/asterisk/confs/sip_admanager.conf','w')
	iax = open('/aldeia/etc/asterisk/confs/iax_admanager.conf','w')
	ips=db(db.f_parametros).select(db.f_parametros.faixa_ip_interna)[0].faixa_ip_interna

	for ramal in ramais:
		if ramal.tecnologia == 'SIP':
			texto = sip
			print 'escrevendo SIP/%s' %(ramal.usuario)
		if ramal.tecnologia == 'IAX':
			texto = iax
			print 'escrevendo IAX/%s' %(ramal.usuario)
	
		texto.write('[%s]\n' %(ramal.usuario))
		texto.write('type=%s\n' %(ramal.type_f))
		texto.write('host=%s\n' %(ramal.host_f))
		texto.write('secret=%s\n' %(ramal.secret))
		texto.write('context=%s\n' %(ramal.context))
		if ramal.qualify == True:
			texto.write('qualify=yes\n')
		else:
			texto.write('qualify=no\n')
		texto.write('deny=0.0.0.0/0.0.0.0\n')
		if ramal.aut_externa == True:
			texto.write('permit=0.0.0.0/0.0.0.0\n')
		else:
			print ips
			for ip in str(ips).split('\n'):
				if ip != '':
					texto.write('permit=%s\n' %(ip))
		texto.write('disallow=%s\n' %(','.join(ramal.disallow)))
		texto.write('allow=%s\n' %(','.join(ramal.allow)))
		if ramal.nat == True:
			texto.write('nat=yes\n')
		else:
			texto.write('nat=no\n')
		print '--extra--'
		print ramal.extras
		print '--extra--'
		for extra in str(ramal.extras).split('\n'):
			if extra != '':
				texto.write('%s\n' %(extra))
			#else:
			#	print '%s-nulo'%(extra)
		texto.write('\n')
					
	sip.close()
	iax.close()
	commands.getoutput("sudo asterisk -rx 'module reload chan_sip.so'")
	commands.getoutput("sudo asterisk -rx 'module reload chan_iax2.so'")

def dia_mes():
	lista_diames=[]
	for i in range(1,32):
		if i < 10:
			lista_diames.append('0%s' %str(i))
		else:
			lista_diames.append(str(i))
	return lista_diames

def dia_semana():
	dict_diasemana=dias={"mon": "Seg", "tue": "Ter", "wed" : "Qua", "thu" : "Qui", "fri" : "Sex", "sat" : "Sáb", "sun" : "Dom"}
	lista_diasemana=[('mon','Seg'),('tue','Ter'),('wed','Qua'),('thu','Qui'),('fri','Sex'),('sat','Sáb'),('sun','Dom')]
	return dict_diasemana

def peers_fop2():
	arq = open('/usr/local/fop2/buttons.cfg','w')
	#Escrevendo troncos
	troncos = db(Troncos.mostrar == True).select()
	arq.write('####TRONCOS####\n')
	for tronco in troncos:
		arq.write('[%s]\n' %(tronco.dispositivo))
		arq.write('type=trunk\n')
		arq.write('label=%s\n' %(tronco.tronco))
		t_fisicos = db(Troncos_fisicos.id_tronco == tronco.id).select()
		for t_fisico in t_fisicos:
			arq.write('channel=%s\n' %(t_fisico.dispositivo))
		arq.write('\n')

	#Escrevendo ramais
	ramais = db(Ramal_virtual.mesa_fop2 == True).select()
	arq.write('####EXTENSIONS####\n')
	for ramal in ramais:
		arq.write('[%s/%s]\n' %(ramal.tecnologia, ramal.ramal_fisico))
		if ramal.tecnologia == 'QUEUE':
			arq.write('type=queue\n')
		else:
			arq.write('type=extension\n')
		arq.write('extension=%s\n' %(ramal.ramal_virtual))
		arq.write('label=%s\n' %(ramal.nome))
		arq.write('context=ramais\n\n')

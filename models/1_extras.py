##Extras
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
	sip = open('/tmp/sip_admanager.conf','w')
	iax = open('/tmp/iax_admanager.conf','w')
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
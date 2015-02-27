def update_grupo_destinos():
	con = db(Grupo_destinos).select()
	try:
		for dado in con:
			lista=[]
			print dado
			for item in dado.id_destinos:
				print item
				print Destinos[item].tipo_chamada
				lista.append(Destinos[item].tipo_chamada)
			lista = list(set(lista))
			print 'update: %s - %s' %(dado.id, lista)
			db(Grupo_destinos.id == dado.id).update(id_destinos=lista)
	except:
		logger.debug("module:Já Feito")
		return ('Já Feito')

update_grupo_destinos()
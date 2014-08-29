
def credito_automatico():
	logger.debug("module:credito_automatico INICIANDO")
	setvar='ym8wifnYT1etN8la00I3mudao7dA4g2A'

	if setvar == 'ym8wifnYT1etN8la00I3mudao7dA4g2A':
		tipo={'local_fixo': 'Local Fixo', 'local_celular': 'Local Celular', 'ddd_celular': 'DDD Celular', 'ddi': 'DDI', 'ddd_fixo': 'DDD Fixo', '0300': 'Zero Trezentos'}
		dia=db(Parametros).select(Parametros.credito_dia)[0].credito_dia
		if dia == '':
			logger.warning("module:credito_automatico - campo credito_dia vazio")
			logger.debug("module:credito_automatico SAINDO")
			return False
		date = str(datetime.now().replace(day=int(dia)).strftime("%Y-%m-%d") )
		date_now = str(datetime.now().strftime("%Y-%m-%d") )
		print date
		print date_now
		if date == date_now:
			query=(Creditos.id_departamento == Departamentos.id)
			creds=db(query).select()
			for cred in creds:
				query=(Usuariospp.id_departamento == cred.f_creditos.id_departamento)
				usuarios=db(query).select()

				for usr in usuarios:
					if cred.f_creditos.local_fixo != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.local_fixo)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='LOCAL_FIXO')
						logger.debug("module:credito_automatico INSERT LOCAL_FIXO %s:%s" 
							%(usr.nome, int(cred.f_creditos.local_fixo)*60))
					if cred.f_creditos.local_celular != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.local_celular)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='LOCAL_CELULAR')
						logger.debug("module:credito_automatico INSERT LOCAL_CELULAR %s:%s" 
							%(usr.nome, int(cred.f_creditos.local_celular)*60))
					if cred.f_creditos.ddd_fixo != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.ddd_fixo)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='DDD_FIXO')
						logger.debug("module:credito_automatico INSERT DDD_FIXO %s:%s" 
							%(usr.nome, int(cred.f_creditos.ddd_fixo)*60))
					if cred.f_creditos.ddd_celular != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.ddd_celular)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='DDD_CELULAR')
						logger.debug("module:credito_automatico INSERT DDD_CELULAR %s:%s" 
							%(usr.nome, int(cred.f_creditos.ddd_celular)*60))
					if cred.f_creditos.ddi != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.ddi)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='DDI')
						logger.debug("module:credito_automatico INSERT DDI %s:%s" 
							%(usr.nome, int(cred.f_creditos.ddi)*60))
					if cred.f_creditos.f0300 != 0:
						print 'insert'
						Saldos.insert(responsavel=usr.nome, tipo_origem='U', 
						datahora=str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
						tempo=int(cred.f_creditos.f0300)*60, uniqueid='ADMANAGER', 
						tipo='C', tipo_chamada='0300')
						logger.debug("module:credito_automatico INSERT 0300 %s:%s" 
							%(usr.nome, int(cred.f_creditos.f0300)*60))
		else:
			logger.debug("module:credito_automatico - %s != %s" %(date, date_now)) 
			logger.debug("module:credito_automatico SAINDO")	
			return False
	else:
		logger.debug("module:credito_automatico - %s != %s" %(date, date_now)) 
		logger.debug("module:credito_automatico SAINDO")
		return False

	logger.debug("module:credito_automatico SAINDO")
	return True

credito_automatico()
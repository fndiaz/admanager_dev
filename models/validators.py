# -*- coding: utf-8 -*-

#########################################################################
## Funcional
#########################################################################

##Rotas
db.f_rotas.rota.requires = IS_NOT_EMPTY(error_message=T("valor não pode ser nulo"))

db.f_rotas.id_tronco.requires = IS_IN_DB(db, 'f_troncos.id', '%(tronco)s', zero=T('selecione um tronco'), 
					error_message=T("valor inválido"))

db.f_rotas.id_tarifacao.requires = IS_IN_DB(db, 'f_tarifacao.id', '%(tarifacao)s', zero=T('selecione uma tarifacao'), 
					error_message=T("valor inválido"))

db.f_rotas.id_horario.requires = IS_IN_DB(db, 'f_horario.id', '%(horario)s', zero=T('selecione um horário'), 
					error_message=T("valor inválido"))

db.f_rotas.id_empresa.requires = IS_IN_DB(db,'f_empresa.id',"%(empresa)s",
					multiple=True, error_message=T("escolha uma opção"))

db.f_rotas.id_destino.requires = IS_IN_DB(db,'f_destinos.id',"%(destino)s",
					multiple=True, error_message=T("escolha uma opção"))

##Parametros
db.f_parametros.faixa_ip_interna.requires = IS_NOT_EMPTY()


#########################################################################
## Ramais
#########################################################################

#db.fisico_sip_iax.tecnologia.requires = requires=IS_IN_SET(["SIP", "IAX"], zero="SIP")
codecs = ["all", "ulaw", "alaw", "g729", "gsm"]
db.fisico_sip_iax.disallow.requires = IS_IN_SET(codecs, multiple=True)
db.fisico_sip_iax.disallow.default = ["all"]
db.fisico_sip_iax.allow.requires = IS_IN_SET(codecs, multiple=True)
db.fisico_sip_iax.allow.default = ["ulaw", "alaw", "g729"]
db.fisico_sip_iax.qualify.default = True
db.fisico_sip_iax.usuario.requires = IS_NOT_IN_DB(db, 'fisico_sip_iax.usuario')







#########################################################################
## Validadores
#########################################################################

##Agenda
#db.agenda.empresa.requires = IS_NOT_EMPTY(error_message=
#						T("valor não pode ser nulo"))

#db.agenda.telefone.requires = [IS_NOT_EMPTY(error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_NOT_IN_DB(db, 'agenda.telefone', error_message=T("este número está em uso")),
#IS_LENGTH(minsize=9, maxsize=11, error_message=T("o telefone deve conter de 9 a 11 números")),
#IS_MATCH('[0-9]+', error_message=T("somente números"))]
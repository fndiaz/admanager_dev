# -*- coding: utf-8 -*-

#########################################################################
## Tratamento de dados -  DELEÇÂO
#########################################################################

def trata_empresa(funcao, id_tab):
	print '--tratamento empresa--'
	print id_tab
	if not db((Departamentos.id_empresa == id_tab) & (Departamentos.mostrar == True)).isempty():
		print 'existe dept vinculado'
		return False
	if not db(Rotas.id_empresa.like('%|'+id_tab+'|%')).isempty():
		print 'existe rota vinculada'
		return False
	if not db((Troncos.id_empresa == id_tab) & (Troncos.mostrar == True)).isempty():
		print 'existe tronco vinculado'
		return False
	return True
	#return {'status': True, 'tabela': 'tal'}

def trata_departamento(funcao, id_tab):
	print '--tratamento departamento--'
	print id_tab
	if not db(Ramal_virtual.id_departamento == id_tab).isempty():
		print 'existe ramal virtual vinculado'
		return False
	if not db((db.f_usuarios.id_departamento == id_tab) & (Departamentos.mostrar == True)).isempty():
		print 'existe usuario vinculado'
		return False
	return True

def trata_tronco(funcao, id_tab):
	print '--tratamento troncos--'
	print id_tab
	if not db(Rotas.id_tronco == id_tab).isempty():
		print 'existe rota vinculado'
		return False
	if not db(Troncos_fisicos.id_tronco == id_tab).isempty():
		print 'existe tronco fisico vinculado'
		return False
	return True

def trata_destino(funcao, id_tab):
	print '--tratamento destinos--'
	print id_tab
	if not db(Rotas.id_destino.like('%|'+id_tab+'|%')).isempty():
		print 'existe rota vinculado'
		return False
	if not db(Grupo_destinos.id_destinos.like('%|'+id_tab+'|%')).isempty():
		print 'existe grupo destinos vinculado'
		return False

def trata_grupo_destino(funcao, id_tab):
	print '--tratamento destinos--'
	print id_tab
	if not db(db.f_usuarios.id_grupo_destinos == id_tab).isempty():
		print 'existe usuario vinculado'
		return False
	if not db(Ramal_virtual.id_grupo_destinos == id_tab).isempty():
		print 'existe ramal virtual vinculado'
		return False
	return True

def trata_ramal_virtual(funcao, id_tab):
	print '--tratamento ramal virtual--'
	print id_tab
	if not db(Desvios.id_ramalvirtual == id_tab).isempty():
		print 'existe desvio vinculado'
		return False
	if not db(Ddr.id_ramalvirtual == id_tab).isempty():
		print 'existe ddr vinculado'
		return False

def trata_tarifacao(funcao, id_tab):
	print '--tratamento ramal virtual--'
	print id_tab
	if not db(Rotas.id_tarifacao == id_tab).isempty():
		print 'existe rota vinculado'
		return False
	return True

def trata_horario(funcao, id_tab):
	print '--tratamento ramal virtual--'
	print id_tab
	if not db(Rotas.id_horario == id_tab).isempty():
		print 'existe rota vinculado'
		return False
	return True







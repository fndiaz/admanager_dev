# -*- coding: utf-8 -*-

#########################################################################
## Escreve Provisionamento
#########################################################################

def escreve_prov():
	os.system("rm -f /var/www/provisionamento/*.cfg")
	query = (Prov_mac.id_equipamento == Prov_equipamento.id)&\
			(Prov_mac.id_rede == Prov_rede.id) & (Prov_mac.id == Prov_ramal.id_mac)

	con = db(query).select()
	print con
	for dado in con:
		if dado.prov_equipamento.modelo == 'T20':
			status, obs = escreve_t20(dado)
			if status == False:
				return status, obs
		
		if dado.prov_equipamento.modelo == 'SPA2102':
			status, obs = escreve_spa2102(dado)
			if status == False:
				return status, obs
		
		if dado.prov_equipamento.modelo == 'SPA122':
			status, obs = escreve_spa122(dado)
			if status is False:
				return status, obs
		
		if dado.prov_equipamento.modelo == 'PAP2':
			status, obs = escreve_pap2(dado)
			if status is False:
				return status, obs
		if dado.prov_equipamento.modelo == '310HD':
			status, obs = escreve_310hd(dado)
			if status is False:
				return status, obs

	return(True, 'ok')

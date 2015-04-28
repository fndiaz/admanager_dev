import psutil
from pysnmp.entity.rfc3413.oneliner import cmdgen

def especificacoes_json():
	dict_final = {}
	
	dict_final['discos']=discos()
	dict_final['memory']=memoria()
	dict_final['load']=load()
	return response.json(dict_final)

def discos():
	dict_partition={}

	for item in psutil.disk_partitions():
		#verificando uso
		uso = psutil.disk_usage(item.mountpoint)
		temp={}
		#populando temp
		temp['device']=item.device 
		temp['fstype']=item.fstype
		temp['total']=(uso.total /1024) / 1024
		temp['used']=(uso.used /1024) / 1024
		temp['free']=(uso.free /1024) / 1024
		temp['percent']=uso.percent
		#completando dicionario '/'
		dict_partition[item.mountpoint]=temp

	return (dict_partition)

def memoria():
	dict_mem={}
	mem = psutil.virtual_memory()
	temp={}
	temp['total']=	(mem.total /1024) / 1024
	temp['used']=	(mem.used /1024) /1024
	temp['free']=	(mem.free /1024) /1024
	temp['buffers']=(mem.buffers /1024) /1024
	temp['cached']=	(mem.cached /1024) /1024
	temp['percent']=mem.percent
	dict_mem['virtual_memory']=temp

	mems = psutil.swap_memory()
	temp={}
	temp['total']=(mems.total /1024) / 1024
	temp['used']=(mems.used /1024) / 1024
	temp['free']=(mems.free /1024) / 1024
	temp['percent']=mems.percent
	dict_mem['swap_memory']=temp

	return(dict_mem)

def load():
	temp={}
	load = os.getloadavg()
	temp['l1']=load[0]
	temp['l2']=load[1]
	temp['l3']=load[2]

	return(temp)

def chamadas_json():
	num = request.vars.num
	if num is None: num='z'

	##Antigo nao esta em uso####################################
	query=(db.f_bilhetes_chamadas.origem.like ('%'+num+'%'))|\
		  (db.f_bilhetes_chamadas.destino.like ('%'+num+'%'))
	con=db(query).select(Bilhetes.horario, 
						 Bilhetes.origem, 
						 Bilhetes.destino, 
						 Bilhetes.linked_id, 
					     orderby=~Bilhetes.horario, 
					     limitby=(0,10))
	################################################################

	query2=(Rastreamento.origem.like ('%'+num+'%'))|\
		   (Rastreamento.destino.like ('%'+num+'%'))
	con2=db(query2).select(Rastreamento.horario,
						   Rastreamento.origem,
						   Rastreamento.destino,
						   Rastreamento.linked_id,
						   distinct=Rastreamento.linked_id,
						   orderby=~Rastreamento.linked_id|Rastreamento.horario,
						   limitby=(0,10)
						   )
	#debug qtd registros
	soma=0
	for dado in con2:
		soma+=1
	print soma

	return response.json(con2)

def rastreio_json():
	linkedid = request.vars.linkedid

	query=(db.f_rastreamento.linked_id == linkedid)
	con=db(query).select()

	#j = con.as_json()
	return response.json(con)

def rastreio_json2():
	con=db(Rastreamento).select(Rastreamento.linked_id,groupby=Rastreamento.linked_id, limitby=(0,10))

	return response.json(con)


####Khomp
def consulta_khomp():
	#Identifica qtd de ebs
	qtd = gera_snmp('.1.3.6.1.4.1.32624.1.1.0')
	qtd = str(qtd[0][1])

	#Identifica Tipo
	final={}
	for i in range(int(qtd)):
		temp={}
		vart= gera_snmp('.1.3.6.1.4.1.32624.1.2.%s.0' %(str(i+1)) )
		temp['tipo']=str(vart[0][1])
		varse= gera_snmp('.1.3.6.1.4.1.32624.1.3.1.%s.16.0' %(str(i+1)) )
		temp['serial']=str(varse[0][1])
		varsta= gera_snmp('.1.3.6.1.4.1.32624.1.4.6.%s.0' %(varse[0][1]))
		temp['status']=str(varsta[0][1])
	 
		temp_link={}
		if str(vart[0][1]) == '18':
			qtd_link= gera_snmp('.1.3.6.1.4.1.32624.1.3.1.%s.1.0' %(varse[0][1]))
			qtd_link = str(qtd_link[0][1])
			for x in range(int(qtd_link)):
				st_link= gera_snmp('.1.3.6.1.4.1.32624.1.4.1.%s.%s.1.0' %(varse[0][1], str(x+1)))
				temp_link[str(x+1)]= str(st_link[0][1])
			temp['link']=temp_link
	 
		temp_sinal={}	
		temp_ope={}
		temp_stat={}
		if str(vart[0][1]) == '21':
			for y in range(16):
				sn_gsm= gera_snmp('.1.3.6.1.4.1.32624.1.4.5.%s.%s.1.0.0' %(varse[0][1], str(y+1)))
				op_gsm= gera_snmp('.1.3.6.1.4.1.32624.1.4.5.%s.%s.4.1.0' %(varse[0][1], str(y+1)))
				stat_gsm= gera_snmp('.1.3.6.1.4.1.32624.1.4.5.%s.%s.3.1.0' %(varse[0][1], str(y+1)))
				temp_sinal[str(y+1)]= str(sn_gsm[0][1])
				temp_ope[str(y+1)]= str(op_gsm[0][1])
				temp_stat[str(y+1)]= str(stat_gsm[0][1])
			temp['sinal']=temp_sinal
			temp['operadora']=temp_ope
			temp['chstat']=temp_stat
			
		final[str(i+1)]=temp

	print final
	teste={"1": {"status": "1", "tipo": "21", "operadora": {"11": "", "10": "", "13": "", "12": "", "15": "", "14": "", "16": "", "1": "", "3": "", "2": "VIVO", "5": "", "4": "", "7": "", "6": "", "9": "", "8": ""}, "chstat": {"11": "0", "10": "0", "13": "0", "12": "0", "15": "0", "14": "0", "16": "0", "1": "3", "3": "0", "2": "1", "5": "0", "4": "0", "7": "0", "6": "0", "9": "0", "8": "0"}, "sinal": {"11": "255", "10": "255", "13": "255", "12": "255", "15": "255", "14": "255", "16": "255", "1": "73", "3": "255", "2": "76", "5": "255", "4": "255", "7": "255", "6": "255", "9": "255", "8": "255"}, "serial": "54404"}, "2": {"status": "1", "serial": "34460", "link": {"1": "0"}, "tipo": "18"}}
	return response.json(teste)


def gera_snmp(var):
	cmdGen = cmdgen.CommandGenerator()

	errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    		cmdgen.CommunityData('public'),
    		cmdgen.UdpTransportTarget(('192.168.100.253', 161)),
    		var
	)
	return varBinds

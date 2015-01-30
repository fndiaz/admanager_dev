import psutil

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

	query=(db.f_bilhetes_chamadas.origem.like ('%'+num+'%'))|\
		  (db.f_bilhetes_chamadas.destino.like ('%'+num+'%'))

	con=db(query)._select(Bilhetes.horario, 
						 Bilhetes.origem, 
						 Bilhetes.destino, 
						 Bilhetes.linked_id, 
					     orderby=~Bilhetes.horario, 
					     limitby=(0,10))

	query2=(Rastreamento.origem.like ('%'+num+'%'))|\
		   (Rastreamento.destino.like ('%'+num+'%'))
	con2=db(query2)._select(Rastreamento.horario,
						   Rastreamento.origem,
						   Rastreamento.destino,
						   Rastreamento.linked_id,
						   distinct=Rastreamento.linked_id,
						   orderby=~Rastreamento.linked_id|Rastreamento.horario,
						   limitby=(0,10)
						   )

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






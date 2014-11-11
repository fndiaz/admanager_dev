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
		temp['total']=uso.total
		temp['used']=uso.used
		temp['free']=uso.free
		temp['percent']=uso.percent
		#completando dicionario '/'
		dict_partition[item.mountpoint]=temp

	return (dict_partition)

def memoria():
	dict_mem={}
	mem = psutil.virtual_memory()
	temp={}
	temp['total']=mem.total
	temp['used']=mem.used
	temp['free']=mem.free
	temp['buffers']=mem.buffers
	temp['cached']=mem.cached
	temp['percent']=mem.percent
	dict_mem['virtual_memory']=temp

	mems = psutil.swap_memory()
	temp={}
	temp['total']=mems.total
	temp['used']=mems.used
	temp['free']=mems.free
	temp['percent']=mems.percent
	dict_mem['swap_memory']=temp

	return(dict_mem)

def load():
	temp={}
	load = os.getloadavg()
	temp['l1']=load[0]
	temp['l2']=load[1]
	temp['l3']=load[0]

	return(temp)







import os
from xml.dom import minidom


elementos = ['TextView', 'LinearLayout', 'RelativeLayout', 'GridLayout', 'Button', 'ImageButton', 'CheckedBox', 'EditText', 'ImageView']


def percorrePasta(pasta):
	caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	pastas = [pas for pas in caminhos if os.path.isdir(pas)]
	arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
	for p in pastas:
		arquivos = arquivos + percorrePasta(p)
	return arquivos


def filtro(arquivos, extencao):
	return [arq for arq in arquivos if arq.lower().endswith(extencao)]


def attsDoElemento(arquivo, elementos):
	for elemento in elementos:
		arqXml = minidom.parse(arquivo)
		items = arqXml.getElementsByTagName(elemento)
		for item in items:
			print(item.attributes.keys())
	    


def main():
    arquivosXml = filtro(percorrePasta('./'), '.xml')
    for arquivo in arquivosXml:
    	attsDoElemento(arquivo, elementos)    


if __name__ == "__main__":
    main()

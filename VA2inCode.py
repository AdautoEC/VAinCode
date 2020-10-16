import os
from xml.dom import minidom


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
	attributosDoArquivo = []
	arqXml = minidom.parse(arquivo)
	for elemento in elementos:
		items = arqXml.getElementsByTagName(elemento)
		for item in items:
			if item.attributes.getNamedItem('android:paddingTop') != None: print(item.attributes.items())
			#attributosDoArquivo = attributosDoArquivo + list(item.attributes.keys())
	return attributosDoArquivo



def main():
	pasta = './architecture-samples-main/'
	elementos = ['TextView', 'Button', 'ImageButton', 'EditText', 'ImageView', 'CartView', 'BrowserView']
	elementosImg = ['ImageButton', 'Button']
	atributos = ['android:contentDescription', 'android:importantForAccessibility']
	funcoes = ['setContentDescription']

	arquivosXml = filtro(percorrePasta(pasta), '.xml')
	for arquivo in arquivosXml:
		procurados = attsDoElemento(arquivo, elementos)

	arquivosJava = filtro(percorrePasta(pasta), '.java')
	#print('Ocorrencias:', fncProcurados(arquivosJava, funcoes))


if __name__ == "__main__":
    main()

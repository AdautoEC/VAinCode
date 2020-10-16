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
	for elemento in elementos:
		arqXml = minidom.parse(arquivo)
		items = arqXml.getElementsByTagName(elemento)
		for item in items:
			attributosDoArquivo = attributosDoArquivo + list(item.attributes.keys())
	return attributosDoArquivo


def attsProcurados(atributosDoElemento, atributosProcurados):
	procurado = 0
	for attp in atributosProcurados:
		for atte in atributosDoElemento:
			if attp in atte: 
				procurado = procurado+1

	return procurado
		

def fncProcurados(arquivos, funcoesProcuradas):
	ocorrencia = 0
	for arq in arquivos:
		meuArquivo = open(arq, encoding="utf8")
		for linha in meuArquivo:
			linha = linha.strip('\n')
			linha = linha.split()
			for palavra in linha:
				for funcao in funcoesProcuradas:
					if palavra.find(funcao) != -1:
						ocorrencia = ocorrencia + 1
	return ocorrencia


def main():
	pasta = './user-interface-samples-main/'
	elementos = ['TextView', 'Button', 'ImageButton', 'EditText', 'ImageView', 'CartView', 'BrowserView']
	atributos = ['android:contentDescription', 'android:importantForAccessibility']
	funcoes = ['setContentDescription']

	arquivosXml = filtro(percorrePasta(pasta), '.xml')
	for arquivo in arquivosXml:
		for elemento in elementos:
			procurados = attsProcurados(attsDoElemento(arquivo, [elemento]), atributos)
			if procurados != 0: print(arquivo + ':', procurados, "em " + elemento)
	'''for arquivo in arquivosXml:
		procurados = attsProcurados(attsDoElemento(arquivo, elementos), atributos)
		if procurados != 0: print(arquivo + ':', procurados)'''

	arquivosJava = filtro(percorrePasta(pasta), '.java')
	print('Ocorrencias:', fncProcurados(arquivosJava, funcoes))


if __name__ == "__main__":
    main()

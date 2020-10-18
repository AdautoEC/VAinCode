import os
from xml.dom import minidom

pastaProjetos = './Projetos/'

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
	encontrados = []

	for arq in arquivos:
		try:
			meuArquivo = open(arq, encoding="utf8")
			for linha in meuArquivo:
				linha = linha.strip('\n')
				linha = linha.split()
				for palavra in linha:
					for funcao in funcoesProcuradas:
						if palavra.find(funcao) != -1:
							if funcao not in encontrados: encontrados.append(funcao)
							ocorrencia = ocorrencia + 1
		except:
			meuArquivo = open(arq, encoding="ISO-8859-1")
			for linha in meuArquivo:
				linha = linha.strip('\n')
				linha = linha.split()
				for palavra in linha:
					for funcao in funcoesProcuradas:
						if palavra.find(funcao) != -1:
							if funcao not in encontrados: encontrados.append(funcao)
							ocorrencia = ocorrencia + 1

	return encontrados


def analise(pasta):
	elementos = ['TextView', 'Button', 'ImageButton', 'EditText', 'ImageView', 'CartView', 'BrowserView']
	atributos = ['android:contentDescription', 'android:importantForAccessibility']
	funcoes = ['setContentDescription', 'AudioManager', 'MotionEvent', 'Vibrator', 'TextToSpeech']

	print("--------------------------------------------------------------")
	print("Inicio do", pasta)
	print()

	arquivosXml = filtro(percorrePasta(pasta), '.xml')
	for arquivo in arquivosXml:
		for elemento in elementos:
			procurados = attsProcurados(attsDoElemento(arquivo, [elemento]), atributos)
			if procurados != 0: print(arquivo + ':', procurados, "em " + elemento)

	arquivosJava = filtro(percorrePasta(pasta), '.java')
	print('Ocorrencias em', fncProcurados(arquivosJava, funcoes))

	print()
	print("Final do", pasta)
	print("--------------------------------------------------------------")
	print("\n\n")


def main():
	caminhos = [os.path.join(pastaProjetos, nome) for nome in os.listdir(pastaProjetos)]
	projetos = [pas for pas in caminhos if os.path.isdir(pas)]

	for projeto in projetos:
		analise(projeto)

if __name__ == "__main__":
    main()

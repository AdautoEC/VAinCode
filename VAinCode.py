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
	total = 0
	procurado = 0
	for attp in atributosProcurados:
		for atte in atributosDoElemento:
			if attp in atte: 
				procurado = procurado+1
			total = total+1
	return 100*procurado/total if (total != 0) else 0
		


def main():
	elementos = ['TextView', 'LinearLayout', 'RelativeLayout', 'FrameLayout', 'GridLayout', 'Button', 'ImageButton', 'CheckedBox', 'EditText', 'ImageView', 'CartView', 'BrowserView']
	atributos = [':contetDescription', ':importantForAccessibility', ':id', ':accessibilityPaneTitle']

	arquivosXml = filtro(percorrePasta('./'), '.xml')
	for arquivo in arquivosXml:
		print(attsProcurados(attsDoElemento(arquivo, elementos), atributos))


if __name__ == "__main__":
    main()

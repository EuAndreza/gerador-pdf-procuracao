from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from datetime import date

data = date.today()

def geradorPDF(nome,estado_civil,profissao,cpf,rg,rua,bairro,municipio,estado,cep,fone,
	nomePro,estado_civilPro,profissaoPro,cpfPro,rgPro,ruaPro,municipioPro,bairroPro,estadoPro,cepPro,fonePro,
	texto):
	gerador = canvas.Canvas('{}.pdf'.format(nome), pagesize=A4)
	gerador.setFont('Helvetica',12)

	text = texto.split()
	text_line1 = text[:6]
	"""
	#linha superior
	gerador.line(30,820,580,820)
	#linha esquerda
	gerador.line(30,820,30,20)
	#linha inferior
	gerador.line(30,20,580,20)
	#linha direita
	gerador.line(580,820,580,20)


	#quadrado logo
	#linha superior
	gerador.line(250,805,350,805)
	#linha esquerda
	gerador.line(250,805,250,745)
	#linha inferior
	gerador.line(250,745,350,745)
	#linha direita
	gerador.line(350,805,350,745)
	"""
	#titulo
	gerador.drawString(210,730,'PROCURAÇÃO - PESSOA FÍSICA')

	#linha 1
	gerador.drawString(30,700,'ORTOGANTE: ')
	gerador.line(115,700,310,700)
	#adiciona o nome do pdf
	gerador.drawString(120,703,nome)
	gerador.drawString(311,700,', brasileiro(a),')
	gerador.line(385,700,480,700)
	#adiciona o estado civil no pdf
	gerador.drawString(390,703,estado_civil)
	gerador.line(485,700,580,700)
	#adiciona a profissao no pdf
	gerador.drawString(490,703,profissao)
	"""
	#exemplo
	gerador.drawString(385,702,'uniao estavel')
	gerador.drawString(485,702,'tecnico em')
	"""

	#linha 2
	gerador.line(30,670,200,670)
	gerador.drawString(201,670,', portador(a) do CPF n°')
	gerador.line(330,670,435,670)
	#adiciona o cpf no pdf
	gerador.drawString(340,673,cpf)
	gerador.drawString(436,670,', RG n°')
	gerador.line(480,670,580,670)
	#adiciona o rg no pdf
	gerador.drawString(490,673,rg)

	#linha 3
	gerador.drawString(30,640,'residente e domiciliado(a) na (rua, avenida, etc)')
	gerador.line(290,640,530,640)
	#adiciona a rua no pdf
	gerador.drawString(300,643,rua)
	gerador.drawString(531,640,', (bairro)')


	#linha 4
	gerador.line(30,610,190,610)
	#adiciona bairro no pdf
	gerador.drawString(35,613,bairro)
	gerador.drawString(191,610,', municipio')
	gerador.line(250,610,430,610)
	#adiciona municipio no pdf
	gerador.drawString(260,613,municipio)
	gerador.drawString(431,610,', estado')
	gerador.line(480,610,580,610)
	#adiciona estado no pdf
	gerador.drawString(490,613,estado)

	#linha 5
	gerador.drawString(30,580,'CEP')
	gerador.line(60,580,190,580)
	gerador.drawString(70,583,cep)
	gerador.drawString(191,580,', telefone')
	gerador.line(245,580,390,580)
	gerador.drawString(255,583,fone)
	gerador.drawString(391,580,', pelo presente instrumento nomeia')

	#linha 6
	gerador.drawString(30,550,'e constitui como seu(sua) bastante Procurador(a) (Outorgado)')
	gerador.line(365,550,580,550)
	gerador.drawString(375,553,nomePro)

	#linha 7
	gerador.drawString(30,520,'brasileiro(a),')
	gerador.line(100,520,195,520)
	gerador.drawString(110,523,estado_civilPro)
	gerador.line(200,520,450,520)
	gerador.drawString(210,523,profissaoPro)
	gerador.drawString(451,520,', portador(a) do CPF n°')

	#linha 8
	gerador.line(30,490,150,490)
	gerador.drawString(40,493,cpfPro)
	gerador.drawString(151,490,', RG n°')
	gerador.line(195,490,315,490)
	gerador.drawString(205,493,rgPro)
	gerador.drawString(316,490,', residente e domiciliado(a) na (rua, avenida, etc)')

	#linha 9
	gerador.line(30,460,270,460)
	gerador.drawString(40,463,ruaPro)
	gerador.drawString(271,460,', (bairro)')
	gerador.line(320,460,515,460)
	gerador.drawString(330,463,bairroPro)
	gerador.drawString(516,460,', municipio')

	#linha 10
	gerador.line(30,430,150,430)
	gerador.drawString(40,433,municipioPro)
	gerador.drawString(151,430,', estado')
	gerador.line(200,430,330,430)
	gerador.drawString(210,433,estadoPro)
	gerador.drawString(331,430,', CEP')
	gerador.line(370,430,525,430)
	gerador.drawString(380,433,cepPro)
	gerador.drawString(526,430,', telefone')

	#linha 11
	gerador.line(30,400,200,400)
	gerador.drawString(40,403,fonePro)
	gerador.drawString(201,400,', com poderes para representar o outorgante perante (todos os orgãos')

	#linha 12 
	gerador.drawString(30,370,'da administração pública Federal, Estadual,  Distrital e  Municipal,  inclusive perante)  às  Unidades  da')

	#linha 13
	gerador.drawString(30,340,'Receita Federal do Brasil para requerer/solicitar ')
	gerador.line(290,340,580,340)
	gerador.drawString(300,343,' '.join(text_line1))

	#linha 14
	gerador.line(30,310,580,310)

	#linha 15
	gerador.line(30,280,580,280)

	#linha 16
	gerador.line(30,250,280,250)
	gerador.drawString(281,250,',  responsabilizando-se por todos os atos  praticados no')

	#linha 17
	gerador.drawString(30,220,'cumprimento deste instrumento,  cessando  os  efeitos  deste  a  partir  da(o) (extinção do seu objetivo)')

	#linha 18
	gerador.drawString(30,190,'(dia/mês/ano).')

	#linha 19
	gerador.line(100,130,250,130)
	gerador.drawString(110,133,'Recife')
	gerador.line(255,130,310,130)
	gerador.drawString(265,133,str(data.day))
	gerador.drawString(312,130,'de')
	gerador.line(330,130,430,130)
	gerador.drawString(340,133,str(data.month))
	gerador.drawString(432,130,'de')
	gerador.line(450,130,505,130)
	gerador.drawString(460,133,str(data.year))


	#linha 20
	gerador.line(100,100,505,100)
	gerador.drawString(240,85,'(Assinatura do Outorgante)')

	gerador.save()
	print('gerado com sucesso')

nomeOr = input('digite o nome')
estado_civilOr = input('digite o estado civil')
profissaoOr = input('digite a profissão')
cpfOr = input('digite o cpf')
rgOr = input('digite o rg')
ruaOr = input('digite a rua')
bairroOr = input('digite o bairro')
municipioOr = input('digite o municipio')
estadorOr = input('digite o estado')
cepdOr = input('digite o cep')
foneOr = input('digite o telefone')


nomePro = input('digite o nome do Procurador')
estado_civilPro = input('digite estado civil do procurador')
profissaoPro = input('digite a profissao do Procurador')
cpfPro =input('digite o cpf do Procurador')
rgPro = input('digite o rg do Procurador')
ruaPro = input('digite a rua do Procurador')
bairroPro = input('digite o bairro do Procurador')
municipioPro = input('digite o municipio do Procurador')
estadoPro = input('digite o estado do Procurador')
cepPro = input('digite o cep do Procurador')
fonePro = input('digite o telefone do Procurador')

texto = input('digite o texto')


geradorPDF(nomeOr,estado_civilOr,profissaoOr,cpfOr,rgOr,ruaOr,bairroOr,municipioOr,estadorOr,cepdOr,foneOr,
	nomePro,estado_civilPro,profissaoPro,cpfPro,rgPro,ruaPro,bairroPro,municipioPro,estadoPro,cepPro,fonePro,texto)
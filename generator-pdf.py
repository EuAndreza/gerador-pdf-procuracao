from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

canvas = canvas.Canvas("gera.pdf", pagesize=A4)
canvas.setFont('Helvetica',12)
"""
#linha superior
canvas.line(30,820,580,820)
#linha esquerda
canvas.line(30,820,30,20)
#linha inferior
canvas.line(30,20,580,20)
#linha direita
canvas.line(580,820,580,20)


#quadrado logo
#linha superior
canvas.line(250,805,350,805)
#linha esquerda
canvas.line(250,805,250,745)
#linha inferior
canvas.line(250,745,350,745)
#linha direita
canvas.line(350,805,350,745)
"""
#titulo
canvas.drawString(210,730,'PROCURAÇÃO - PESSOA FÍSICA')

#linha 1
canvas.drawString(30,700,'ORTOGANTE: ')
canvas.line(115,700,310,700)
canvas.drawString(311,700,', brasileiro(a),')
canvas.line(385,700,480,700)
canvas.line(485,700,580,700)
"""
#exemplo
canvas.drawString(385,702,'uniao estavel')
canvas.drawString(485,702,'tecnico em')
"""

#linha 2
canvas.line(30,670,200,670)
canvas.drawString(201,670,', portador(a) do CPF n°')
canvas.line(330,670,435,670)
canvas.drawString(436,670,', RG n°')
canvas.line(480,670,580,670)

#linha 3
canvas.drawString(30,640,'residente e domiciliado(a) na (rua, avenida, etc)')
canvas.line(290,640,530,640)
canvas.drawString(531,640,', (bairro)')

#linha 4
canvas.line(30,610,190,610)
canvas.drawString(191,610,', municipio')
canvas.line(250,610,430,610)
canvas.drawString(431,610,', estado')
canvas.line(480,610,580,610)

#linha 5
canvas.drawString(30,580,'CEP')
canvas.line(60,580,190,580)
canvas.drawString(191,580,', telefone')
canvas.line(245,580,390,580)
canvas.drawString(391,580,', pelo presente instrumento nomeia')

#linha 6
canvas.drawString(30,550,'e constitui como seu(sua) bastante Procurador(a) (Outorgado)')
canvas.line(365,550,580,550)

#linha 7
canvas.drawString(30,520,'brasileiro(a),')
canvas.line(100,520,195,520)
canvas.line(200,520,450,520)
canvas.drawString(451,520,', portador(a) do CPF n°')

#linha 8
canvas.line(30,490,150,490)
canvas.drawString(151,490,', RG n°')
canvas.line(195,490,315,490)
canvas.drawString(316,490,', residente e domiciliado(a) na (rua, avenida, etc)')

#linha 9
canvas.line(30,460,270,460)
canvas.drawString(271,460,', (bairro)')
canvas.line(320,460,515,460)
canvas.drawString(516,460,', municipio')

#linha 10
canvas.line(30,430,150,430)
canvas.drawString(151,430,', estado')
canvas.line(200,430,330,430)
canvas.drawString(331,430,', CEP')
canvas.line(370,430,525,430)
canvas.drawString(526,430,', telefone')

#linha 11
canvas.line(30,400,200,400)
canvas.drawString(201,400,', com poderes para representar o outorgante perante (todos os orgãos')

#linha 12 
canvas.drawString(30,370,'da administração pública Federal, Estadual,  Distrital e  Municipal,  inclusive perante)  às  Unidades  da')

#linha 13
canvas.drawString(30,340,'Receita Federal do Brasil para requerer/solicitar ')
canvas.line(290,340,580,340)

#linha 14
canvas.line(30,310,580,310)

#linha 15
canvas.line(30,280,580,280)

#linha 16
canvas.line(30,250,280,250)
canvas.drawString(281,250,',  responsabilizando-se por todos os atos  praticados no')

#linha 17
canvas.drawString(30,220,'cumprimento deste instrumento,  cessando  os  efeitos  deste  a  partir  da(o) (extinção do seu objetivo)')

#linha 18
canvas.drawString(30,190,'(dia/mês/ano).')

#linha 19
canvas.line(100,130,250,130)
canvas.line(255,130,310,130)
canvas.drawString(312,130,'de')
canvas.line(330,130,430,130)
canvas.drawString(432,130,'de')
canvas.line(450,130,505,130)

#linha 20
canvas.line(100,100,505,100)
canvas.drawString(240,90,'(Assinatura do Outorgante)')

canvas.save()
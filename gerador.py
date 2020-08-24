#from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


canvas = canvas.Canvas("gerador1.pdf", pagesize=A4)
#canvas.setLine(.27)
canvas.setFont('Helvetica',12)

canvas.drawString(210,750,'PROCURAÇÃO PARTICULAR')
canvas.drawString(30,720,'Por este instrumento de procuração, eu,')
nome = 'andreza'
canvas.drawString(280,723,nome)

#linha apos o nome
canvas.line(250,720,580,720)

canvas.drawString(30,690, 'nascido(a) em ')
dia = '06'
mes = '09'
ano = '1998'
canvas.drawString(110,690, '____/____/____ ,')	
canvas.drawString(113,690,dia)
canvas.drawString(150,690,mes)
canvas.drawString(170,690,ano)

#linha após a data de nascimento
canvas.line(205,690,580,690)

mes1 = 'setembro '
dia1 = 'seis '
ano1= 'mil novecentos e noventa e oito'
canvas.drawString(210,693,dia1)
canvas.drawString(240,693,mes1)
canvas.drawString(300,693,ano1)

canvas.drawString(30,660,'(nacionalidade)(estado civil) portador(a) da célula de identidade RG nº:' )

#linha apos o RG
canvas.line(410,660,580,660)

rg = '12.345.678-9'
canvas.drawString(420,663,rg)

canvas.drawString(30,630,'inscrito(a) no CPF/MF sob nº:')

#linha apos cpf
canvas.line(190,630,390,630)
cpf = '000.000.000-00'
canvas.drawString(200,633,cpf)
#canvas.line(ponto de partida da linha,posição do ponto de partida da linha,ponto final da linha,posição do ponto final da linha)

canvas.drawString(395,630,', residente e domiciliado(a) na, ')
canvas.line(30,600,410,600)
canvas.drawString(415,600,'(rua,avenida,praça,etc e nº)')

canvas.line(30,570,470,570)
canvas.drawString(475,570,'(bairro)')

canvas.line(30,540,470,540)
canvas.drawString(475,540,'(cidade)')

canvas.drawString(30,510,'(estado - UF) (CEP) (TELEFONE) nomeio e constituo meu (minha) bastante procurador(a) o(a) Sr.(a)')

canvas.line(30,480,180,480)
canvas.drawString(185,480,'(nome)')
canvas.line(230,480,380,480)
canvas.drawString(385,480, 'nascido(a) em')
canvas.drawString(470,480,'____/____/____')

canvas.line(30,450,210,450)
canvas.drawString(215,450,'(nacionalidade) (estado civil) portador(a) da cédula de identidade')

canvas.drawString(30,420,'RG nº:')
canvas.line(70,420,250,420)
canvas.drawString(255,420,'inscrito(a) no CPF/MF sob nº:')
canvas.line(420,420,570,420)

canvas.drawString(30,390,'residente e domiciliado(a) na,')
canvas.line(190,390,400,390)
canvas.drawString(405,390,'(rua, avenida, praça, etc e nº)')

canvas.line(30,360,470,360)
canvas.drawString(475,360,'(bairro)')

canvas.line(30,330,470,330)
canvas.drawString(475,330,'(cidade)')

canvas.drawString(30,300,'(estado - UF) (CEP) (telefone) a quem confiro os mais amplos, gerais e limitados poderes')

canvas.drawString(30,270,'para: tratar, requer, assinar papéis, documentos, concordar ou não com o que se faça')

canvas.drawString(30,240,'necessário junto à FUNDAÇÃO PROCON-TAL ESTADO para o bom e fiel cumprimento do presente mandato.')

canvas.drawString(290,180,'Tal estado, ____ de _______________ de _____.')

canvas.line(200,120,400,120)
canvas.drawString(220,90,'Assinatura do(a) consumidor(a)')
canvas.save()
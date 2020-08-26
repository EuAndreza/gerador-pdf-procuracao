from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

canvas = canvas.Canvas("gera.pdf", pagesize=A4)
canvas.setFont('Helvetica',12)

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

#titulo
canvas.drawString(225,730,'PROCURAÇÃO PARTICULAR')

#linha 1
canvas.drawString(42.25,715,'Por este instrumento de procuração, eu,')
canvas.line(260,715,580,715)

#linha 2
canvas.drawString(30,700, 'nascido(a) em ____/____/____ ,')	
canvas.line(205,700,580,700)

#linha 3
canvas.drawString(30,685,'(nacionalidade)(estado civil) portador(a) da célula de identidade RG nº:' )
canvas.line(410,685,580,685)

#linha 4
canvas.drawString(30,670,'inscrito(a) no CPF/MF sob nº:')
canvas.line(190,670,410,670)
canvas.drawString(415,670,', residente e domiciliado(a) na, ')

#linha 5
canvas.line(30,655,425,655)
canvas.drawString(430,655,'(rua,avenida,praça,etc e nº)')

#linha 6
canvas.line(30,640,280,640)
canvas.drawString(285,640,'(bairro)')
canvas.line(330,640,530,640)
canvas.drawString(535,640,'(cidade)')

#linha 7 
canvas.drawString(30,625,'(estado - UF)')
canvas.line(105,625,220,625)
canvas.drawString(225,625, '(CEP)')
canvas.line(260,625,375,625)
canvas.drawString(380,625,'(TELEFONE)')
canvas.line(455,625,580,625)
canvas.drawString(30,610,' nomeio e constituo meu (minha) bastante procurador(a) o(a) Sr.(a)')


canvas.save()
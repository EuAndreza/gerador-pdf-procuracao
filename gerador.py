from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


canvas = canvas.Canvas("gerador1.pdf", pagesize=letter)
#canvas.setLine(.27)
canvas.setFont('Helvetica',12)

canvas.drawString(210,750,'PROCURAÇÃO PARTICULAR')
canvas.drawString(30,720,'Por este instrumento de procuração, eu,')
nome = 'andreza'
canvas.drawString(280,723,nome)
canvas.line(250,720,580,720)
canvas.drawString(30,690, 'nascido(a) em ')
dia = '06'
mes = '09'
ano = '1998'
canvas.drawString(110,690, '____/____/____')	
canvas.drawString(113,690,dia)
canvas.drawString(150,690,mes)
canvas.drawString(170,690,ano)
canvas.line(250,720,580,720)

canvas.save()
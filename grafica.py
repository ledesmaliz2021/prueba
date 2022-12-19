from matplotlib import pyplot
trabajo=("Python con Niños","Programación con Scratch","Comunidad STEM","Acompañamiento de Pasantias")
slices=(50,70,60,30)
color=('blue','green','yellow','red')
pyplot.pie(slices,colors=color,labels=trabajo,autopct='%1.1f%%')
pyplot.axis('equal')
pyplot.title('Mis actuales trabajos como instructora')
pyplot.show()
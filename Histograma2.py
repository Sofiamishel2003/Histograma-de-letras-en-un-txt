from tkinter import*
from tkinter import messagebox, filedialog
v=Tk()
v.geometry("800x920")
v.title("Reto 1")
v.configure(bg="thistle")
titulo=Label(v, text="Programa Histograma", font=("Arial 12 bold"))
titulo.place(x=300, y=10)
l=Label(v, text="Ingrese su archivo:", bg="thistle")
l.place(x=5,y=90)
texto= StringVar()
c1=Entry(v,width=35, state=DISABLED,textvariable=texto)
c1.place(x=130,y=90)
t1=Button(v,width=10, state=DISABLED,text="Letra")
t1.place(x=0,y=140)
t2=Button(v,width=10, state=DISABLED,text="Frecuencia")
t2.place(x=80,y=140)
t3=Button(v,width=10, state=DISABLED,text="Frec. Relativa")
t3.place(x=160,y=140)
canva=Canvas(v, width=500, height=500, bg="white")
canva.place(x=260,y=140)
global total
total=0
global maxi
maxi=0
# Abrir y crear 
def abrir():
        rutatotal= filedialog.askopenfilename(filetypes=(("Archivo de texto","*.txt"),),title="Seleccionar un lugar para guardar")
        texto.set(rutatotal)
        file=open(rutatotal, "r", encoding="utf-8")
        linea=file.readlines()
        file.close() 
#definición para hacer la busqueda
def dobusqueda():
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(27):
        busqueda(letras[i],i+1)
    print(maxi)
    to1=Button(v,width=10, state=DISABLED,text="Total")
    to1.place(x=0,y=896)
    to2=Button(v,width=10, state=DISABLED,)
    to2.place(x=80,y=896)
    to3=Button(v,width=10, state=DISABLED,text=(str(round(total,4))))
    to3.place(x=160,y=896)
#definición de busqueda con parametros
def busqueda(letra,yl):
    global total 
    global maxi
    try:
        file= open(c1.get(), "r", encoding="utf-8")
        lineas= file.readlines()
        acu=0
        cont=0
        for linea in lineas:
            linea=linea.lower()
            for i in linea:
                if(i=="á"):
                    i="a"
                if(i=="é"):
                    i="e"
                if(i=="í"):
                    i="i"
                if(i=="ó"):
                    i="o"
                if(i=="ú" or i=="ü"):
                    i="ú"
                if (i  in "abcdefghijklmnñopqrstuvwxyz"):
                    cont=cont+1 
                if(i==letra):
                    acu=acu+1
        if(maxi<acu):
            maxi=acu
        fr=acu/(cont)
        total=total+fr
        letrita=Button(v,width=10, state=DISABLED,text=letra)
        letrita.place(x=0,y=140+(27*yl))
        frecuencia=Button(v,width=10, state=DISABLED,text=(str(acu)))
        frecuencia.place(x=80,y=140+(27*yl))
        relativa=Button(v,width=10, state=DISABLED,text=(str(round(fr,4))))
        relativa.place(x=160,y=140+(27*yl))
        canva.create_rectangle(50+(13*yl)+yl-10,450,(50+(13*yl)+13)+yl-10,450-((acu/(maxi))*400),fill="skyblue")
        nombre4=Label(v,text=letra, bg="white")
        nombre4.place(x=303+(14*yl),y=600, width=9)
        file.close() 
    except:
        messagebox.showerror("ERROR","ARCHIVO VACIO O NO SELECCIONO UNO")
canva.create_line(50,450,50,50,fill="red")
canva.create_line(50,450,450,450,fill="red")
bt1= Button(v, text="Abrir/Crear", command=abrir)
bt1.place(x=390,y=85)
bt2= Button(v, text="Busqueda", command=dobusqueda)
bt2.place(x=390,y=745) 
v.mainloop()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Reforzar los conocimeintos de archivos
#Lenguaje: python
#Net Framewor: 4.5
#Recursos: visual studio
#Descripción: Desarrollar un programa que pueda abrir/crear un archivo y escribir y leer el archivo
#Ultima modificación 19/01/2021
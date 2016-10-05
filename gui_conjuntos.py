#-*- encoding: utf-8 -*-
#Credits to gui_form: Pedro Jefferson
#Github: 1pedro
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import conjuntos

class Janela(Gtk.Window):
    def __init__(self):
        
        #Janela Principal
        Gtk.Window.__init__(self, title="Álgebra de Conjuntos")
        Gtk.Window.set_size_request(self,500,400)
        Gtk.Window.set_resizable(self,False)
        Gtk.Window.modify_bg(self,Gtk.StateType.NORMAL,Gdk.color_parse("#cccccc"))
        #Grid_total
        self.grid_total = Gtk.Grid()
        self.add(self.grid_total)
        self.grid1 = Gtk.Grid()
        self.grid1 = Gtk.Grid(column_homogeneous=False,column_spacing=10,row_spacing=10)
        #Texto e box de escolha para a Operação
        self.combo = Gtk.ComboBoxText()
        self.label_combo = Gtk.Label(label="Operação: ")
        self.label_combo.set_halign(Gtk.Align.END)
        self.grid1.attach(self.label_combo,1,2,1,1)
        self.combo.insert(0,"0", "União (A U B)")
        self.combo.insert(1,"1", "Interseção (A ∩ B)")
        self.combo.insert(2,"2", "Diferença (A - B)")
        self.combo.insert(3,"3", "Diferença Simétrica (A  △ B)")
        self.combo.insert(4,"4", "Complementar (Ac)")
        self.combo.set_halign(Gtk.Align.START)
        self.grid1.attach(self.combo, 2,2,1,1)
        #Texto e Campo de entrada do Conjunto A
        self.label_conjuntoA = Gtk.Label(label="  Conjunto A: ")
        self.label_conjuntoA.set_halign(Gtk.Align.END)              
        self.grid1.attach(self.label_conjuntoA,1,4,1,1)
        self.entry_conjuntoA = Gtk.Entry()
        self.entry_conjuntoA.set_max_length(100)
        self.entry_conjuntoA.set_width_chars(50)            
        self.entry_conjuntoA.set_halign(Gtk.Align.FILL)
        self.grid1.attach(self.entry_conjuntoA, 2,4,1,1)
        self.entry_conjuntoA.set_text("1,2,3")
        #Texto e Campo de entrada do conjunto B
        self.label_conjuntoB = Gtk.Label(label="  Conjunto B: ")
        self.label_conjuntoB.set_halign(Gtk.Align.END)              
        self.grid1.attach(self.label_conjuntoB,1,6,1,1)
        self.entry_conjuntoB = Gtk.Entry()
        self.entry_conjuntoB.set_max_length(100)
        self.entry_conjuntoB.set_width_chars(50)            
        self.entry_conjuntoB.set_halign(Gtk.Align.FILL)
        self.grid1.attach(self.entry_conjuntoB, 2,6,1,1)
        self.entry_conjuntoB.set_text("4,5,6")
        #Botão de Resultado
        self.button = Gtk.Button(label="Ver Solução")
        self.button.set_halign(Gtk.Align.START)
        self.grid1.attach(self.button,2,12,2,2)
        self.button.connect("clicked", self.button_clicked)
        #Texto de Resultado / Conjunto Solução
        self.label_solucao = Gtk.Label(label=" ")
        self.label_solucao.set_halign(Gtk.Align.START)              
        self.grid1.attach(self.label_solucao,2,18,1,1)
        #Espaçamento das grids
        self.grid1.set_row_spacing(30)
        self.box3 = Gtk.Box()
        #Colocando a Grid1 e box3 na grid principal
        self.grid_total.set_row_spacing(20)
        self.grid_total.attach(self.grid1, 0,3,2,1)
        self.grid_total.attach(self.box3, 0,9,1,1)

    def button_clicked(self, widget):
        operacao  = self.combo.get_active_text()
        conjunto_a = self.entry_conjuntoA.get_text()
        conjunto_b = self.entry_conjuntoB.get_text()

        conjunto_a = conjunto_a.split(',')
        conjunto_b = conjunto_b.split(',')
        resultado = []

        if(operacao == "União (A U B)"):
            resultado = conjuntos.uniao(conjunto_a, conjunto_b)     
        elif(operacao == "Interseção (A ∩ B)"):
            resultado = conjuntos.intersecao(conjunto_a, conjunto_b) 
        elif(operacao == "Diferença (A - B)"):
            resultado = conjuntos.diferenca(conjunto_a, conjunto_b)  
        elif(operacao == "Diferença Simétrica (A  △ B)"):
            resultado = conjuntos.difSimetrica(conjunto_a, conjunto_b)
        elif(operacao == "Complementar (Ac)"):
            resultado = conjuntos.diferenca(conjunto_b, conjunto_a)  

        try:
            resultado = [float(i) for i in resultado]
            resultado = conjuntos.ordenaVetor(resultado)
            resultado = ", ".join(str(x) for x in resultado)
            resultado = "[" + resultado + "]"
            self.label_solucao.set_text(resultado)
        except:
            self.label_solucao.set_text("Por favor, insira elementos válidos nos dois conjuntos!\n\nEx: 1,2,3,4,5")

        if(operacao == None):
            self.label_solucao.set_text("Escolha uma operação!")
        elif(resultado == "[]"):
            self.label_solucao.set_text("[ ] ou ø")
        
#Inicialização da aplicação
win = Janela()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

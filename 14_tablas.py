#!/usr/bin/env python
from gi.repository import Gtk
class BasicTreeViewExample:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_title("Ejemplo sobre un a columna")
        self.window.set_size_request(500, 300)

        self.lista = Gtk.TreeStore(str, str)
	# se aniaden los datos alas columnas
        self.lista.append(None, ["Ubuntu","Gnome"])
        self.lista.append(None, ["Linux Mint", "Gnome shell"])
        self.lista.append(None, ["Fedora", "KDE"])
        self.lista.append(None, ["ArchLinux","Gnome"])
        self.lista.append(None, ["Manriva", "Hnome shell"])
        self.lista.append(None, ["Debian", "Gnome"])
        self.lista.append(None, ["Lula","XFE"])
        self.lista.append(None, ["Gentoo","LXE"])
        self.lista.append(None, ["Pupi","Unity"])


        self.treeview = Gtk.TreeView(self.lista)
        # se crean lostitulos de las columnas
        self.titulo_columna = Gtk.TreeViewColumn('Distribuciones linux')
	self.titulo_columna1 = Gtk.TreeViewColumn('Escritorios')
        # se aniaden las colimnas ala vista de arbol
        self.treeview.append_column(self.titulo_columna)
        self.treeview.append_column(self.titulo_columna1)

        # se crean las celdas
        self.cell = Gtk.CellRendererText()
	self.cell2 = Gtk.CellRendererText()

        # se empaquetan las columnas
        self.titulo_columna.pack_start(self.cell, True)
        self.titulo_columna1.pack_start(self.cell2, True)
	
	#Hacer que se muestre el texto de cada columna
        self.titulo_columna.add_attribute(self.cell, 'text', 0)
        self.titulo_columna1.add_attribute(self.cell2, 'text', 1)

        self.treeview.set_search_column(0)
	#Dar propiedad reordenable a cada columna
        self.titulo_columna.set_sort_column_id(0)
	self.titulo_columna1.set_sort_column_id(0)

        self.treeview.set_reorderable(True)#Activar la propiedad reordenble

        self.window.add(self.treeview)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

def main():
    Gtk.main()

if __name__ == "__main__":
    tvexample = BasicTreeViewExample()
    main()

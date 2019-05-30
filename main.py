#-*-coding: utf-8-*-
#!/usr/bin/local/python3

import pymysql
from os import system
from Coffices import Coffice
from cmysql import Cmysql

class Menu():

	def __init__ (self):
		self.oficina = Coffice()

			
	def insertar(self):
		system("clear")
		print ("*****************************************************************")
		print ("                     INSERTAR CLASSICMODELS                  ")
		print ("*****************************************************************")

		idOffice = input("Digite el identificador a insertar: ")
		if self.oficina.controlar_id(idOffice) != True:
		
			if self.oficina.consultar_id(idOffice) == False:
				print ("\n")
				
				print ("*****************************************************************")
				ciudad = input("Digite la nueva ciudad: ")
				telefono = input("Digite el nuevo telefono: ")
				direccion1 = input("Digite la nueva direccion 1: ")

				if self.oficina.insertar_datos(idOffice, ciudad, telefono, direccion1) == True:
				

					print ("*****************************************************************")
					print ("Los datos se insertaron correctamente")
					print ("*****************************************************************")
					input()
					print ("\n")

				else:
					print ("*****************************************************************")
					print ("ERROR - Los datos  no se pudieron insertar")
					print ("*****************************************************************")
					input()
				
			else:
				print ("*****************************************************************")
				print ("ERROR - La oficina ya existe")
				print ("*****************************************************************")
				input()

		else:
			print ("*****************************************************************")
			print ("ERROR - El identificador a buscar se encuentra vacio.")
			print ("*****************************************************************")
			input()
		
	def leer(self):
		system("clear")
		print ("*****************************************************************")
		print ("                     VISUALIZAR CLASSICMODELS                  ")
		print ("*****************************************************************")
		
		idOffice = input("Digite el identificador del campo a visualizar: ")
		if self.oficina.controlar_id(idOffice) != True:
			
			if self.oficina.consultar_id(idOffice) != False:
				print ("\n")
				print ("****************************************************************")
				self.oficina.mostrar_datos(idOffice)
				print ("*****************************************************************")
				input()

			else:
				print ("*****************************************************************")
				print ("ERROR - La oficina no existe")
				print ("*****************************************************************")
				input()
		else:
			print ("*****************************************************************")
			print ("ERROR - El identificador a buscar se encuentra vacio.")
			print ("*****************************************************************")
			input()
		
	def modificar(self):
		print ("*****************************************************************")
		print ("                     MODIFICAR CLASSICMODELS                  ")
		print ("*****************************************************************")

		idOffice = input("Digite el identificador del campo a modificar: ")
		if self.oficina.controlar_id(idOffice) != True:
			
			if self.oficina.consultar_id(idOffice) != False:
				print ("\n")
				print ("****************************************************************")
				self.oficina.mostrar_datos(idOffice)
				print ("*****************************************************************")
				input()
				ciudad = input("Digite la nueva ciudad: ")
				telefono = input("Digite el nuevo telefono: ")
				direccion1 = input("Digite la nueva direccion 1: ")

				if self.oficina.controlar_datos(ciudad, telefono, direccion1) == True:
					print ("*****************************************************************")
					print ("ERROR - Hay campos vacios. No se pueden agregar los datos.")
					print ("*****************************************************************")
					input()

				else:
					self.oficina.modificar_datos(idOffice, ciudad, telefono, direccion1)
					
					print ("*****************************************************************")
					self.oficina.mostrar_datos(idOffice)
					print ("*****************************************************************")
					print ("Los datos se modificaron correctamente")
					print ("*****************************************************************")
					input()
					print ("\n" )
				
			else:
				print ("*****************************************************************")
				print ("ERROR - La oficina no existe")
				print ("*****************************************************************")
				input()

		else:
			print ("*****************************************************************")
			print ("ERROR - El identificador a buscar se encuentra vacio.")
			print ("*****************************************************************")
			input()
		
	def eliminar(self):
		print ("*****************************************************************")
		print ("                      ELIMINAR DATOS                  ")
		print ("*****************************************************************")
		idOffice = input("Digite el identificador del campo a eliminar: ")
		if self.oficina.controlar_id(idOffice) != True:
		
			if self.oficina.consultar_id(idOffice) != False:
				print ("\n")
				print ("****************************************************************")
				self.oficina.mostrar_datos(idOffice)
				print ("*****************************************************************")
				input()

				self.oficina.eliminar_datos(idOffice)
				print ("****************************************************************")
				print ("¡La oficina se elimino correctamente!")
				print ("****************************************************************")
				input()
								
			else:
				print ("****************************************************************")
				print ("¡La oficina no existe!")
				print ("****************************************************************")
				input()

		else:
			print ("*****************************************************************")
			print ("ERROR - El identificador a buscar se encuentra vacio.")
			print ("*****************************************************************")
			input()
		
	def listar(self):
		self.oficina.listar()
		input("")

	def encabezado_almacen(self):
		system("clear")
		print ("***********************************")
		print ("***********************************")
		print ("******                      *******")
		print ("******    CLASSICMODELS     *******")
		print ("******                      *******")
		print ("******                      *******")
		print ("***********************************")
		print ("***********************************")
		print ("***********************************")
		print ("           MENU PRINCIPAL          ")
		print ("***********************************")
		print ("***********************************")
		print (" 1. CREATE                       **")
		print (" 2. READ                         **")
		print (" 3. UPDATE                       **")
		print (" 4. DELETE                       **")
		print (" 5. LIST                         **")
		print (" 6. EXIT                         **")
		print ("***********************************")
		print ("***********************************")
			
	def menu_principal(self):
		while True:
			self.encabezado_almacen()
			try:
				op = int((input("DIGITE SU OPCION: ")))
				print ("***********************************")

				if op == 1:
					self.insertar()

				elif op == 2:
					self.leer()

				elif op == 3:
					self.modificar()

				elif op == 4:
					self.eliminar()
						
				elif op == 5:
					self.listar()
						
				elif op == 6:
					break


			except ValueError:
				print ("*******************************************")
				print ("ERROR - La opcion debe estar entre 1 y 6.")
				print ("*******************************************")
				input()

if __name__== '__main__':
	classicmodels = Menu()
	classicmodels.menu_principal()
	

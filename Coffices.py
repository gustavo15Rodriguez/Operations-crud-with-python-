from cmysql import *

class Coffice( Cmysql ):


	def consultar_id(self, idOffice):
		
		self.idOffice = idOffice	
		cnn,crs = self.conectar()   
		sSQL = "SELECT * FROM offices where officeCode = %s"
		try:
			crs.execute( sSQL % self.idOffice )
			results = crs.fetchall()

			for row in results:
			
				if self.idOffice == row["officeCode"]:
					return True

			return False
		
		except crs.InternalError() as error:
			code, message = error.args
			print("ERROR: ", code, message)
			
		finally:
			cnn.close()

	def mostrar_datos(self, idOffice):
		self.idOffice = idOffice
		if self.consultar_id(self.idOffice) == True:
			cnn,crs = self.conectar()   
			sSQL = "SELECT * FROM offices where officeCode = %s"
			try:
				crs.execute( sSQL % self.idOffice )
				results = crs.fetchall()
				print("ID\tCIUDAD\tTELEFONO\tDIRECCION 1\tDIRECCION 2\tESTADO\tPAIS\tCODIGO POSTAL\tTERRITORIO\t")
				for row in results:

					print( "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ( row["officeCode"], row["city"], row["phone"], row["addressLine1"], row["addressLine2"], row["state"], row["country"], row["postalCode"], row["territory"] ))
		
			except crs.InternalError() as error:
				code, message = error.args
				print("ERROR: ", code, message)
			
			finally:
				cnn.close()


	def modificar_datos(self, idOffice, ciudad, telefono, direccion1):
		self.idOffice = idOffice
		self.ciudad = ciudad
		self.telefono = telefono
		self.direccion1 = direccion1

		cnn,crs = self.conectar()   
		sSQL = "UPDATE offices SET city = '%s', phone = '%s', addressLine1 = '%s' WHERE officeCode = '%s'"
		try:
			print("ID\tCIUDAD\tTELEFONO\tDIRECCION 1")

			crs.execute( sSQL % (self.ciudad, self.telefono, self.direccion1, self.idOffice)  )
			cnn.commit()
			return True 

		except crs.InternalError() as error:
			code, message = error.args
			print("ERROR: ", code, message)
			
		finally:
			cnn.close()

	def listar( self, iduser = None ):    
		cnn,crs = self.conectar()   
		sSQL = "SELECT * FROM offices"

		try:
			crs.execute( sSQL )
			results = crs.fetchall()
			print("ID\tCIUDAD\tTELEFONO\tDIRECCION 1\tDIRECCION 2\tESTADO\tPAIS\tCODIGO POSTAL\tTERRITORIO\t")

			for row in results:
				print( "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % ( row["officeCode"], row["city"], row["phone"], row["addressLine1"], row["addressLine2"], row["state"], row["country"], row["postalCode"], row["territory"] ))

		except crs.InternalError() as error:
			code, message = error.args
			print("ERROR: ", code, message)
		finally:
			cnn.close()  


	def eliminar_datos(self, idOffice):
		self.idOffice = idOffice
		cnn,crs = self.conectar()   
		sSQL = "DELETE FROM offices WHERE officeCode = '%s'"
	
		try:
			crs.execute( sSQL % self.idOffice )
			cnn.commit()

			return True

		except crs.InternalError() as error:
			code, message = error.args
			print ("ERROR: ",code, message)

		finally:
			cnn.close()

	def insertar_datos(self, idOffice, ciudad, telefono, direccion1):
		self.idOffice = idOffice
		self.ciudad = ciudad
		self.telefono = telefono
		self.direccion1 = direccion1

		cnn,crs = self.conectar()   
		sSQL = "INSERT INTO offices VALUES('%s','%s','%s','%s', 'NO.23-114', 'CA', 'Brasil', '3254', 'N/A')"
		try:
			crs.execute( sSQL % (self.idOffice, self.ciudad, self.telefono, self.direccion1))
			results = cnn.commit()
			return True 

		except crs.InternalError() as error:
			code, message = error.args
			print("ERROR: ", code, message)
			
		finally:	
			cnn.close()

	def controlar_datos(self,ciudad, telefono, direccion1):
		self.ciudad = ciudad
		self.telefono = telefono
		self.direccion1 = direccion1
		lista = []
		
		try:
			lista.append(self.ciudad)
			lista.append(self.telefono)
			lista.append(self.direccion1)

			for i in range(len(lista)):
				if lista[i] == "" or lista[i] == " ":
					return True

				return False

		except ValueError:
			print("ERROR... ")

	def controlar_id(self, idOffice):
		self.idOffice = idOffice
		lista_id = []
		
		try:
			lista_id.append(self.idOffice)

			for i in range(len(lista_id)):
				if lista_id[i] == "" or lista_id[i] == " ":
					return True

				return False

		except ValueError:
			print("ERROR... ")


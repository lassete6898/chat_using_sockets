import socket
import threading
import sys
import pickle
import os

class Servidor():
	print("Que puerto quiere usar ")
	def __init__(self, host=socket.gethostname(), port = input()):
		self.clientes = []
		self.sock = socket.socket()
		self.sock.bind((str(host), int(port)))
		self.sock.listen(20)
		self.sock.setblocking(False)

		aceptar = threading.Thread(target=self.aceptarC)
		procesar = threading.Thread(target=self.procesarC)
		
		print("_____Hilo que acepta mensajes iniciado en modo DAEMON")
		aceptar.daemon = True
		aceptar.start()

		print("_____Hilo que procesa mensajes iniciado en modo DAEMON")
		procesar.daemon = True
		procesar.start()
		
		host_ip = socket.gethostbyname(host)

		print("Su ip actual es : ",host_ip)

		while True:
			msg = input('<< SALIR = 1 >>\n')
			if msg == '1':
				print("**** TALOGOOO *****")
				self.sock.close()
				sys.exit()
			else:
				pass

	def broadcast(self, msg, cliente):
		for c in self.clientes:
			try:
				if c != cliente:
					c.send(msg)
			except:
				self.clientes.remove(c)

	def aceptarC(self):
		while True:
			try:
				conn, addr = self.sock.accept()
				print(f"\nConexion aceptada via {conn}\n")
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def procesarC(self):
		print("Procesamiento de mensajes iniciado")
		while True:
			if len(self.clientes) > 0:
				for c in self.clientes:
					try:
						data = c.recv(32)
						if data:
							self.broadcast(data,c)
					except:
						pass

s = Servidor()
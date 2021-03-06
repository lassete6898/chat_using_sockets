import threading
import sys
import socket
import pickle
import os

class Cliente():

	def __init__(self, host=input("Introduzca la ip del servidor ? "), port=input("Introduzca el puerto del servidor ? ")):
		self.sock = socket.socket()
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		print('Hilo con PID = ',os.getpid())
		print('Total de hilos activos = ', threading.active_count())

		while True:
			msg = input('\nEscriba texto ? ** Enviar = ENTER ** Salir Chat = 1 \n')
			if msg != '1' :
				self.enviar(msg)
			else:
				print(" **** TALOGOOO  ****")
				self.sock.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.sock.recv(32)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()

		
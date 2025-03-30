import socket  #Esta línea importa el módulo socket, que proporciona acceso a la interfaz de red de bajo nivel de Python.

ip = input("Introduce la IP: ")  #Se agrega la dirección IP a escanear

try: #El comando TRY intenta ejecutar el bloque de código que sigue. Si ocurre un error, se pasa al bloque EXCEPT.
    nombre = socket.gethostbyaddr(ip)
    print("El nombre del host es:", nombre[0])
except socket.herror:
    print("No se pudo resolver el nombre del host")

with open("puertos_abiertos.txt", "w") as archivo:
    for i in range(1, 65536):  #Busca en todos los puertos desde 1 hasta 65536.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crea un nuevo socket utilizando IPv4 y TCP
        s.settimeout(0.1)  #Establece un tiempo de espera de 0.1 segundos para la conexión
        
        if s.connect_ex((ip, i)) == 0:  #Intenta conectarse al puerto i de la IP anotada al principio
            mensaje = f"Puerto {i} abierto\n"
            print(mensaje, end="")  #Entrega los puertos abiertos en la consola
            archivo.write(mensaje)  #Anota los resultados en el archivo txt
        
        s.close()  #Cierra la conexión del socket

print("Escaneo finalizado")  #Imprime un mensaje indicando que el escaneo ha terminado

#tener Flask instalado pip install flask

#Crear un directorio llamado pdfs en la misma carpeta que el proyecto

# Formulario debe tener un atributo enctype="multipart/form-data" para permitir la carga de archivos. 

<form action="/subir_pdf" method="POST" enctype="multipart/form-data">
  <input type="file" name="archivo">
  <input type="submit" value="Subir archivo">
</form>

#enlace para descargar el archivo PDF. Este enlace debe apuntar a la ruta /descargar_pdf/nombre_archivo

<a href="/descargar_pdf/mi_archivo.pdf">Descargar archivo</a>

#Ejecuta el servidor Flask python app.py



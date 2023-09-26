
# PibasTechLinked (BETA)
A script used for connecting automatically using Python and Selenium (along with google apis) with everyone on the community of PibasTech 



 ## Requerimientos:

 - [Python](https://www.python.org)
 - [ChromeDriver](https://community.chocolatey.org/packages/chromedriver) (Yo lo utilice con Chocolatey) 
  Tiene que coincider con la version de tu Chrome Browser si queres que funcione
 - [Credenciales de Google API](https://console.cloud.google.com/apis/) (Spreadsheet y Drive, habra que generarlas y agregarlas al path de este directorio)

 - Una cuenta de LinkedIn :D



 ### Pasos:

 1. Instalar lo mencionado arriba
 2. Instalar requerimientos de python 
 3. Correr el primer script [PrimerScript](./gettingMails.py), esto devuelve un csv con todos los LinkedIns del Spreadsheet

 4. Correr el [SegundoSript](./partSelenium.py), esto recorre cada script y conecta con cada uno de los linkedin. Es necesario agregar el email y contraseña de la cuenta

 CUIDADO, LinkedIn a veces pide verificar que no seas robot, tenes 15 segundos para pasar la verificacion jaja



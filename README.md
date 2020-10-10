# Climatronic 3000
[![Generic badge](https://img.shields.io/badge/version-3.09.10-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-2-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  


## Table of contents
* [Acerca del proyecto](#acerca-del-proyecto)
* [Como empezar](#como-empezar)
  * [Prerequisitos](#prerequisites)
  * [Installation](#installation)
* [Uso](#uso)





# Acerca del proyecto
Basicamente este proyecto tiene como objetivo utilizar peticiones a openwehather map, para proveer de información acerca del clima en diferentes ciudades.
Este consta de una carpeta src, que contine todo el código legible,interpretable y ejecutable, a su vez una carpeta 
```
resources
```

dicha carpeta contiene 4 carpetas y un archivo .mp3, es importante saber que de manipular 

```
Documentacion
```
Contine un PDF escrito en LaTex, sobre todo lo que necesitas saber sobre el programa: Costos, funcionamientos, Desarrollo y aquello que hoy no lo parece pero en el futuro de su mantenimiento y revisión será muy necesario


```
dataset
```
Los efectos pueden generar daños a la ejecución general del programa pues contiene los archivos .csv que permiten obtener las peticiones de aquellos datos que se desean.

```
greeting
```
Contiene archivos de texto, que permiten a la voz saludar de forma  casi impredecible, pueden manipularse, pero recuerde que cualquier frase escrita ahí, podría ser Leída por el alto parlante

```
tones
```
Incluye la cortinilla de entrada para anunciar la entrada de la voz, de modificarlo, deberá ser una archivo por el mismo nombre, recomendamos un archivo .mp3 con una duración <=10 sec, pues será reproducido antes de cada anuncio

```
speaking.mp3
```
Recomendamos no manipularlo durante la ejecución del programa, pues ahí se encuentra la voz, sin embargo antes de la ejecución del programa y tras finalizar, puede ser utilizado como cualquier archivo de extensión .mp3

# Como empezar
Primero que nada, es necesario mencionar que se encuentra escrito en Python, bajo las versiones superiores o iguales a Python 3.8, por ello es recomendable actualizar a la versión de Python más reciente a tu ordenador, de lo contrario podrían ocurrir algunas fallas, y  de igual manera recomendamos ejecutar en ordenadores con Sistema Operativo GNU LINUX en cualquiera de sus versiones. 
Asimismo es necesario instalar algunas bibliotecas extras, no es necesario que te preocupes por instalar de forma correcta cada una de ellas, gracias a un script de auto-instalación


## Prerequisitos
* Verifica utilizar una versión superior a Python 3.6 :
```
python --version
```
> `Python 3.8+` is adviced  

  Nota, en algunos distros de Linux, lo correras como:  
  ```
  python3 --version
  ```


* Tu puedes revisar si tu tienes instalado PyPI así como Python 
  Disponible en el siguiente artículo
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

## Instalación
1. Clona el repositorio
```
git clone https://github.com/IanGarciaUnam/climatronic_3000.git
```
3. Verifica la instalación de los paquetes con nuestro instalador
  ```
  bash Tarea01/src/install_librarys.sh
  ```
  Se instalará
  * `gTTS`
  * `playsound`
  * `pandas`
  * `keyboard`
  * `googletrans`
 4. Tras instalar el bash ejecutara las pruebas unitarias, deberá aparecer la leyenda
 ```
 OK
 ```
 lo cual significa que se encuentra correcto




# Uso

Solo deberás ejecutar
```
bash Tarea01/src/launcher.sh
```
ó 
```
python3 Tarea01/src/Menu.py
```


# Desarrollado por:
#### David Hernández Urióstegui | No. de Cuenta: 420003708   <-> Ian Israel García Vázquez | No. de Cuenta: 317097364

[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=iangarcia@ciencias.unam.mx)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=Dhdezu@ciencias.unam.mx)





---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#climatronic-3000)

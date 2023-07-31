# PragmaBot ES
## ¡Hola!
Bienvenido a nuestro sistema de PragmaBot. Estamos encantados de tenerte aquí y esperamos brindarte toda la ayuda que necesitas.

## Descripción general del sistema
PragmaBot es una aplicación inteligente que utiliza una base de datos MongoDB para obtener el contexto necesario para sus interacciones. Está diseñado para brindar asistencia y generar alertas ante errores, advertencias o actividades inusuales.

El sistema se encuentra alojado en la nube y hace uso de tecnologías como AWS Lambda y CloudFront para garantizar la escalabilidad y disponibilidad del servicio. Gracias a esta infraestructura cloud, el bot puede manejar un gran número de solicitudes de manera eficiente.

## Requerimientos recomendados
- **Python 3.10.6 con WSL**: Recomendamos utilizar Python 3.10.6 en un entorno de Subsistema de Windows para Linux (WSL) para garantizar la compatibilidad y el rendimiento óptimo.

A continuación, te proporcionamos algunos enlaces que te ayudarán a instalar WSL en caso de que no lo tengas configurado y estés en un entorno Windows:

- [Guía de instalación de WSL en Windows](https://docs.microsoft.com/es-es/windows/wsl/install)

## Instalación de dependencias
Para instalar las dependencias necesarias, simplemente ejecuta el siguiente comando en tu entorno de desarrollo con Python:

```bash
python 3 -m venv venv
source /venv/bin/activate 
# A partir de este punto, deberás de ver un (venv) a la izquierda de la terminal
pip install -r requirements.txt
```
Este comando instalará automáticamente todas las librerías y módulos especificados en el archivo "requirements.txt", lo que permitirá que el sistema funcione sin problemas y dejando todas las dependencias de este proyecto aisladas en un ambiente virtual.

¡Gracias por utilizar nuestro Asistente Bot! Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en preguntar.

# PragmaBot EN

## Hello!
Welcome to our PragmaBot system. We are delighted to have you here and look forward to providing you with all the assistance you need.

## System Overview
PragmaBot is an intelligent application that uses a MongoDB database to obtain the necessary context for its interactions. It is designed to provide assistance and generate alerts for errors, warnings, or unusual activities.

The system is hosted in the cloud and makes use of technologies such as AWS Lambda and CloudFront to ensure scalability and availability of the service. Thanks to this cloud infrastructure, the bot can handle a large number of requests efficiently.

## Recommended Requirements
- **Python 3.10.6 with WSL**: We recommend using Python 3.10.6 in a Windows Subsystem for Linux (WSL) environment to ensure compatibility and optimal performance.

Below are some links to help you install WSL if you do not have it configured and are using a Windows environment:

- [WSL Installation Guide for Windows](https://docs.microsoft.com/en-us/windows/wsl/install)

## Installing Dependencies
To install the necessary dependencies, simply execute the following command in your Python development environment:

```bash
python 3 -m venv venv
source /venv/bin/activate 
# From this point, you should see a (venv) at the left of the terminal
pip install -r requirements.txt
```
This command will automatically install all the libraries and modules specified in the "requirements.txt" file, allowing the system to function smoothly, also, I'll create a virtual environment to separate the dependencies of this project with the others.

Thank you for using our Assistant Bot! If you have any questions or need further assistance, feel free to ask.
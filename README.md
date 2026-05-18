# Análisis de Ventas - TP Git, GitHub, Jira y Google Colab

## Descripción

Este proyecto corresponde al Trabajo Práctico de Organización Empresarial de la Tecnicatura Universitaria en Programación de la UTN.

El objetivo del trabajo es aplicar gestión colaborativa mediante Jira, control de versiones con Git y GitHub, y ejecución técnica desde Google Colab.

## Escenario elegido

Escenario B: Análisis de Ventas de una Pequeña Empresa.

## Integrantes

- Santiago Joaquin Diaz tomando los 3 roles.

## Roles de trabajo

- P1 - Líder y Organizador: inicialización del repositorio y estructura de carpetas.
- P2 - Desarrollador Técnico: desarrollo del script de análisis de ventas.
- P3 - Revisor y QA: revisión de documentación, seguridad y Pull Request.

## Estructura del repositorio

datos/
scripts/
resultados/
README.md
.gitignore

## Dataset utilizado

Se utilizó un dataset de ventas en formato CSV, almacenado en la carpeta `datos/`.

El archivo principal es:

datos/sales_sample_2024.csv

## Script principal

El análisis se ejecuta mediante el archivo:

scripts/analisis_datos.py

## Resultados generados

El script genera archivos dentro de la carpeta `resultados/`:

- resumen_ventas.csv
- ventas_por_mes.csv
- grafico_ventas_mensuales.png

## Instrucciones de ejecución en Google Colab

Clonar el repositorio:

git clone https://github.com/JoakuGit/TP_GestionColaborativa_OE

Ingresar a la carpeta del proyecto:

cd TP_GestionColaborativa_OE

Ejecutar el script:

python scripts/analisis_datos.py

## Trazabilidad con Jira

Los commits del proyecto se vinculan con las tareas de Jira mediante el ID del issue.

Ejemplo:

OETPGIT-5: Agregar script de análisis de ventas

## Buenas prácticas aplicadas

- Uso de ramas de trabajo.
- Commits trazables con Jira.
- Organización en carpetas.
- Uso de `.gitignore`.
- Ejecución reproducible desde Google Colab.
- Generación automática de resultados.

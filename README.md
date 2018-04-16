---
title: 'Práctica 1: Web scraping'
author: "Mercy Pinargote"
date: "April 16, 2018"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

## Descripción

El conjunto de datos generado como parte de esta actividad práctica reúne diferentes características de prospectos que han aplicado a la universidad de Nueva York entre los años 2012 y 2018. Algunas de las variables que se recogen en el conjunto de datos son el género, estado, tipo de escuela, GPA, SAT, si es atleta.

## Miembros del equipo 

La actividad ha sido realizada de manera individual por Mercy Pinargote.

## Ficheros del código fuente 
.	src/main.py: punto de entrada al programa. Inicia el proceso de scraping. 
.	src/scraper.py: contiene la implementación de la clase StudentsScraper cuyos métodos generan el conjunto de datos a partir de la base de datos online CollegeData.

## Recursos

.	Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data
.	Simon Munzert, Christian Rubba, Peter Meißner, Dominic Nyhuis. (2015). Automated Data Collection with R: A Practical Guide to Web Scraping and Text Mining. John Wiley & Sons.
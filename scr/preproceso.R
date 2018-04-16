setwd("C:/MERCY UOC/Tipologia y Ciclo de los Datos/Web-Scraping/csv")
aplicantes <- read.table("Students.csv", 
                             header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)
aplicantes <-na.omit(aplicantes)
write.csv(aplicantes.completo, file = "aplicantes_clean.csv")
# Plantilla para el Pre Procesado de Datos
# Importar el dataset
dataset = read.csv('Data.csv')
#dataset = dataset[, 2:3]

# Dividir los datos en conjunto de entrenamiento y conjunto de test
# install.packages("caTools")
library(caTools)
set.seed(123)
# Split genera un vector en base a la variable dataset$Purchased con un ratio de 0.8 en la separación de los datos
# En el vector todos los datos TRUE corresponden a los pertenecientes al ratio y FALSE los que deben quedar afuera
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# subset divide la BD según el vector split definido anteriormente
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

# Escalado de valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])
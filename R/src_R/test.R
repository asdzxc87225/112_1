my_vector <- 1:10
print(my_vector)
print(mean(my_vector))

my_matrix <- matrix(1:9, nrow = 3, ncol =3)
print(my_matrix)

odd_sequence <- seq(0, 20, by=2)
print(odd_sequence)

data <- read.csv("data.csv")
head(data,5)

my_list <- list(
                fruits = c("Apple","Banana","Orange"),
                prices = c(1.0,0.8,1.2),
                organic = c(TRUE,FALSE,TRUE)
                )
print(my_list)

library(ggplot2)
df <- data.frame(Fruit = my_list$fruits, Price = my_list$prices)
ggplot(df, aes(x = Fruit, y = Price)) + geom_point()


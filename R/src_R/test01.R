sales_data <- read.csv("../data/data.csv")
print(sales_data)

summary(sales_data$Sales)
max(sales_data$Sales)
min(sales_data$Sales)

library(ggplot2)
ggplot(sales_data, aes(x = Date, y = Sales))+
  geom_line()+
  labs(x = "月份",y="銷售額")

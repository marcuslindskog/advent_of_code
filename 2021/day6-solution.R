library(tidyverse)
library(data.table)

#Star 1

fish <-c(4,1,4,1,3,3,1,4,3,3,2,1,1,3,5,1,3,5,2,5,1,5,5,1,3,2,5,3,1,3,4,2,3,2,3,3,2,1,5,4,1,
         1,1,2,1,4,4,4,2,1,2,1,5,1,5,1,2,1,4,4,5,3,3,4,1,4,4,2,1,4,4,3,5,2,5,4,1,5,1,1,1,4,5
         ,3,4,3,4,2,2,2,2,4,5,3,5,2,4,2,3,4,1,4,4,1,4,5,3,4,2,2,2,4,3,3,3,3,4,2,1,2,5,5,3,2,
         3,5,5,5,4,4,5,5,4,3,4,1,5,1,3,4,4,1,3,1,3,1,1,2,4,5,3,1,2,4,3,3,5,4,4,5,4,1,3,1,1,4,
         4,4,4,3,4,3,1,4,5,1,2,4,3,5,1,1,2,1,1,5,4,2,1,5,4,5,2,4,4,1,5,2,2,5,3,3,2,3,1,5,5,5,4,
         3,1,1,5,1,4,5,2,1,3,1,2,4,4,1,1,2,5,3,1,5,2,4,5,1,2,3,1,2,2,1,2,2,1,
         4,1,3,4,2,1,1,5,4,1,5,4,4,3,1,3,3,1,1,3,3,4,2,3,4,2,3,1,4,1,5,3,1,1,5,3,2,
         3,5,1,3,1,1,3,5,1,5,1,1,3,1,1,1,1,3,3,1)

for (day in 1:80){
  fish <- fish - 1
  fish <- c(fish, rep(8, sum(fish == -1)))
  fish[fish == -1] <- 6
}

(nr_fish <- length(fish))

#Star2
fish <-c(4,1,4,1,3,3,1,4,3,3,2,1,1,3,5,1,3,5,2,5,1,5,5,1,3,2,5,3,1,3,4,2,3,2,3,3,2,1,5,4,1,
         1,1,2,1,4,4,4,2,1,2,1,5,1,5,1,2,1,4,4,5,3,3,4,1,4,4,2,1,4,4,3,5,2,5,4,1,5,1,1,1,4,5
         ,3,4,3,4,2,2,2,2,4,5,3,5,2,4,2,3,4,1,4,4,1,4,5,3,4,2,2,2,4,3,3,3,3,4,2,1,2,5,5,3,2,
         3,5,5,5,4,4,5,5,4,3,4,1,5,1,3,4,4,1,3,1,3,1,1,2,4,5,3,1,2,4,3,3,5,4,4,5,4,1,3,1,1,4,
         4,4,4,3,4,3,1,4,5,1,2,4,3,5,1,1,2,1,1,5,4,2,1,5,4,5,2,4,4,1,5,2,2,5,3,3,2,3,1,5,5,5,4,
         3,1,1,5,1,4,5,2,1,3,1,2,4,4,1,1,2,5,3,1,5,2,4,5,1,2,3,1,2,2,1,2,2,1,
         4,1,3,4,2,1,1,5,4,1,5,4,4,3,1,3,3,1,1,3,3,4,2,3,4,2,3,1,4,1,5,3,1,1,5,3,2,
         3,5,1,3,1,1,3,5,1,5,1,1,3,1,1,1,1,3,3,1)

n_days <- 256
f <- data.table(fish = fish)
days <- data.table(day = 1:n_days, new_fish = 0)

for (day in 1:n_days){
  f$fish <- f$fish - 1
  days$new_fish[day] <- sum(f$fish == -1)
  f$fish[f$fish == -1] <- 6
}

for(rows in 1:nrow(days)){
  day_n <- days$new_fish[rows]
  if(rows+9 <= nrow(days)){
    days$new_fish[rows+9] <- days$new_fish[rows+9] +day_n
  }
  k <- 1
  while(rows +9 + k*7 <= nrow(days)){
    days$new_fish[rows +9 + k*7] <- days$new_fish[rows +9 + k*7 ] +day_n
    k <- k+1
  }
  
}
(n_fish <- length(fish) + sum(days$new_fish))

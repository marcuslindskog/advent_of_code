library(tidyverse)
depths <- read_csv("day1-input.txt", col_names = FALSE) %>%
  unlist(use.names = FALSE)

#Star 1
sum <- 0

for (dep in 2:length(depths)) {
  if (depths[dep] > depths[dep-1]) {
    sum = sum+1
  }
}

print(sum)


#Star 2
sum <- 0

for (dep in 3:(length(depths)-1)){
  w1 <- depths[dep-2] + depths[dep-1] + depths[dep]
  w2 <- depths[dep-1] + depths[dep] + depths[dep+1]
  
  if (w2 > w1) {
    sum = sum+1
  }
  
}

print(sum)

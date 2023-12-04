library(tidyverse)

#Star 1
pos <- read_csv("day7-input.txt", col_names = FALSE) %>%
  unlist(., use.names=FALSE)

max_pos <- max(pos)
min_pos <- min(pos)

dist <- tibble(align_pos = min_pos:max_pos, fuel = 0)

for(positions in min_pos:max_pos){
  dist$fuel[dist$align_pos == positions] <- sum(abs(pos - positions))
  
}

dist %>%
  slice_min(fuel, n = 1)


#Star 2
pos <- read_csv("day7-input.txt", col_names = FALSE) %>%
  unlist(., use.names=FALSE)

max_pos <- max(pos)
min_pos <- min(pos)

dist <- tibble(align_pos = min_pos:max_pos, fuel = 0)

for(positions in min_pos:max_pos){
  dist$fuel[dist$align_pos == positions] <- sum((abs(pos - positions)*(abs(pos - positions) + 1)/2))
}


dist %>%
  slice_min(fuel, n = 1)

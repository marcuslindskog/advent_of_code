library(tidyverse)

#Star 1
data_points <- read_csv("day5-input.txt") %>%
  mutate(vert = ifelse(x1==x2, 1, 0),
         hori = ifelse(y1==y2, 1, 0),
         straight = ifelse(vert == 1 | hori == 1, 1, 0)) %>%
  filter(straight == 1)

dot_grid = matrix(rep(0, 1000*1000), byrow = TRUE, nrow = 1000)

for (rows in 1:nrow(data_points)) {
  dot_grid[data_points$y1[rows]:data_points$y2[rows],data_points$x1[rows]:data_points$x2[rows]] = dot_grid[data_points$y1[rows]:data_points$y2[rows],data_points$x1[rows]:data_points$x2[rows]] +1
}

(dangerous_points <- sum(dot_grid >= 2))



#Star 2
data_points <- read_csv("day5-input.txt") %>%
  mutate(vert = ifelse(x1==x2, 1, 0),
         hori = ifelse(y1==y2, 1, 0),
         straight = ifelse(vert == 1 | hori == 1, 1, 0)) %>%
  filter(straight == 0)

for (rows in 1:nrow(data_points)) {
  y <- data_points$y1[rows]:data_points$y2[rows]
  x <- data_points$x1[rows]:data_points$x2[rows]
  for (point in 1:length(y)) {
    dot_grid[y[point],x[point]] = dot_grid[y[point],x[point]] +1
  }
  
}

(dangerous_points <- sum(dot_grid >= 2))

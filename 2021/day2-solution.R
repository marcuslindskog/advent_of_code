#Star 1
library(tidyverse)

boat_positions <- read_csv("day2-input.txt", col_names = FALSE) %>%
  rename(direction = X1, step = X2) %>%
  group_by(direction) %>%
  summarise(sum_dir = sum(step))

multip <- boat_positions$sum_dir[boat_positions$direction == "forward"] * 
  (boat_positions$sum_dir[boat_positions$direction == "down"] -
     boat_positions$sum_dir[boat_positions$direction == "up"])

print(multip)

#Star 2
boat_positions_s2 <- read_csv("day2-input.txt", col_names = FALSE) %>%
  rename(direction = X1, step = X2) %>%
  mutate(aim = 0, horizontal = 0, depth = 0)

aim <- 0
horizontal <- 0
depth <- 0

for(steps in 1:nrow(boat_positions_s2)){

  if (boat_positions_s2$direction[steps] == "down") {
  aim <- aim + boat_positions_s2$step[steps]
  boat_positions_s2$aim[steps] <- aim
   
  }else if (boat_positions_s2$direction[steps] == "up") {
    aim <- aim - boat_positions_s2$step[steps]
    boat_positions_s2$aim[steps] <- aim
    
  }else {
    horizontal <- horizontal + boat_positions_s2$step[steps]
    boat_positions_s2$horizontal[steps] <- horizontal
    
    depth <- depth + aim*boat_positions_s2$step[steps]
    boat_positions_s2$depth[steps] <- depth
    
    boat_positions_s2$aim[steps] <- aim
   
 }
    
    
}

final <- horizontal*depth

print(final)

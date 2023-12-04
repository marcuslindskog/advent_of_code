library(tidyverse)

#Star 1
diagnostics <- read_csv("day3-input.txt", col_names = FALSE) %>%
  select(-X13) %>%
  summarise_all(mean) %>%
  unlist(., use.names=FALSE)

gamma <- strtoi(paste(as.numeric(diagnostics > .5), collapse =""), base=2)
epsilon <-  strtoi(paste(as.numeric(diagnostics < .5), collapse =""), base = 2)

answer <- gamma*epsilon

print(answer)



#Star 2

ogr_filtering <- read_csv("day3-input.txt", col_names = FALSE) %>%
  select(-X13) %>%
  filter(X1 == as.numeric(mean(X1)>= .5)) %>%
  filter(X2 == as.numeric(mean(X2)>= .5)) %>%
  filter(X3 == as.numeric(mean(X3)>= .5)) %>%
  filter(X4 == as.numeric(mean(X4)>= .5)) %>%
  filter(X5 == as.numeric(mean(X5)>= .5)) %>%
  filter(X6 == as.numeric(mean(X6)>= .5)) %>%
  filter(X7 == as.numeric(mean(X7)>= .5)) %>%
  filter(X8 == as.numeric(mean(X8)>= .5)) %>%
  filter(X9 == as.numeric(mean(X9)>= .5)) %>%
  filter(X10 == as.numeric(mean(X10)>= .5)) %>%
  filter(X11 == as.numeric(mean(X11)>= .5)) %>%
  filter(X12 == as.numeric(mean(X12)>= .5)) %>%
  unlist(., use.names=FALSE)

OGR <- strtoi(paste(ogr_filtering, collapse =""), base=2)

co2_filtering <- read_csv("day3-input.txt", col_names = FALSE) %>%
  select(-X13) %>%
  filter(X1 != as.numeric(mean(X1)>= .5))%>%
  filter(X2 !=  as.numeric(mean(X2)>= .5))%>%
  filter(X3 !=  as.numeric(mean(X3)>= .5)) %>%
  filter(X4 !=  as.numeric(mean(X4)>= .5)) %>%
  filter(X5 !=  as.numeric(mean(X5)>= .5)) %>%
  filter(X6 !=  as.numeric(mean(X6)>= .5)) %>%
  filter(X7 !=  as.numeric(mean(X7)>= .5)) %>%
  filter(X8 != as.numeric(mean(X8)>= .5)) %>%
  filter(X9 != as.numeric(mean(X9)>= .5)) %>%
  unlist(., use.names=FALSE)

co2 <- strtoi(paste(co2_filtering, collapse =""), base=2)

life_support <- OGR*co2
print(life_support)

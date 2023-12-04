library(tidyverse)
source("day8-functions.R")

#Star 1
codes <- read_delim("day8-input.txt", delim = "|", col_names = FALSE) %>%
  select(X2) %>%
  mutate(X2 = str_trim(X2,"left"))%>%
  separate(X2, c("D1", "D2", "D3", "D4"), sep = " ") %>%
  mutate_all(~str_count(.)) %>%
  mutate_all(~.%in% c(2, 3, 4, 7)) %>% 
  pivot_longer(D1:D4, names_to = "string") %>%
  summarise(n_digits = sum(value))

(answer_s1 <- codes$n_digits[1])

#Star 2
codes <- read_delim("day8-input.txt", delim = "|", col_names = FALSE) %>%
  mutate(X1, X2 = str_trim(X2,"left"))

codes$value <- 0

for(rows in 1:nrow(codes)){
  inp <- unlist(strsplit(codes$X1[rows], " "))
  code <- unlist(strsplit(codes$X2[rows], " "))
  value <- find_digits(inp, code)
  codes$value[rows] <-value
}

(answer_s2 <- sum(codes$value))




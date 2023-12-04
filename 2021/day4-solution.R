library(tidyverse)

#Star 1
draws <- read_csv("day4-input-1.txt", col_names = FALSE) %>%
  unlist(., use.names = FALSE)

boards <- read_table("day4-input-2.txt", col_names = FALSE) %>%
  mutate(board = rep(1:100,each =5),
         row = rep(1:5, 100))



board_to_check <- boards

for (draw in draws) {
  
  board_to_check <- board_to_check %>%
   mutate_at(c("X1", "X2", "X3", "X4", "X5"), ~ifelse(. == draw, 1000, .)) %>%
   mutate(row_sum = rowSums(.[1:5]))
    
  if (sum(board_to_check$row_sum == 5000) != 0) {
    winning_spot <- board_to_check %>%
      filter(row_sum == 5000)
    
    winning_board <- board_to_check %>%
      filter(board == winning_spot$board[1])
    break
  }
  
 check_cols <- board_to_check %>%
    group_by(board) %>%
    summarize_at(c("X1", "X2", "X3", "X4", "X5"), sum) %>%
    pivot_longer(-board, names_to = "column", values_to = "col_sum") %>%
   slice_max(col_sum, n =1)
 
  if (check_cols$col_sum == 5000) {
    winning_board <-board_to_check %>%
      filter(board == check_cols$board[1])
    break
  }

}

final_score<- sum(as.matrix(winning_board %>%
  select(X1:X5) %>%
  mutate_all(~ifelse(. == 1000, NA, .))), na.rm=TRUE) * draw

print(final_score)

#Star 2

draws <- read_csv("day4-input-1.txt", col_names = FALSE) %>%
  unlist(., use.names = FALSE)

boards <- read_table("day4-input-2.txt", col_names = FALSE) %>%
  mutate(board = rep(1:100,each =5),
         row = rep(1:5, 100))

board_to_check <- boards
winning_boards <- numeric(0)

for (draw in draws) {
  
  board_to_check <- board_to_check %>%
    filter(!(board %in% winning_boards)) %>%
    mutate_at(c("X1", "X2", "X3", "X4", "X5"), ~ifelse(. == draw, 1000, .)) %>%
    mutate(row_sum = rowSums(.[1:5]))
  
 check_rows <- board_to_check %>%
    group_by(board) %>%
    summarize(max_row_sum = max(row_sum)) %>%
    filter(max_row_sum == 5000)
    
    winning_boards <- c(winning_boards, check_rows$board)

  check_cols <- board_to_check %>%
    filter(!(board %in% winning_boards)) %>%
    group_by(board) %>%
    summarize_at(c("X1", "X2", "X3", "X4", "X5"), sum) %>%
    pivot_longer(-board, names_to = "column", values_to = "col_sum") %>%
    group_by(board) %>%
    summarize(max_col_sum = max(col_sum)) %>%
      filter(max_col_sum == 5000)
  
    winning_boards <- c(winning_boards, check_cols$board)
    
    if (length(winning_boards) == 100) {
      print(draw)
      break
    }
  
}


final_score_s2 <- sum(as.matrix(board_to_check %>%
                              select(X1:X5) %>%
                              mutate_all(~ifelse(. == 1000, NA, .))), na.rm=TRUE) * draw
print(final_score_s2)

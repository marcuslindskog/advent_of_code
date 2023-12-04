
find_digits <- function(inp, code){
  nchar(inp)
  
  digits <- rep(NA, 10)
  
  #Clear shots
  #1
  digits[which(nchar(inp) == 2)] <- 1
  
  #4
  digits[which(nchar(inp) == 4)] <- 4
  
  #7
  digits[which(nchar(inp) == 3)] <- 7
  
  #8
  digits[which(nchar(inp) == 7)] <- 8
  
  #Using identified
  candidates<- lapply(strsplit(inp[which(nchar(inp) == 6)], ""), unlist)
  one <- unlist(strsplit(inp[which(nchar(inp) == 2)],""))
  four <- unlist(strsplit(inp[which(nchar(inp) == 4)],""))
  #0, 9, 6
  
  
  numbers <- 1:3
  #6
  for(k in numbers){
    if(sum(candidates[[k]] %in% one) == 1){
      six <- paste(candidates[[k]], collapse ="")
      k_six <- k
      break
    }
  }
  digits[inp == six] <- 6
  
  #9
  for(k in numbers){
    if(sum(candidates[[k]] %in% four) == 4){
      nine <- paste(candidates[[k]], collapse ="")
      k_9 <- k
      break
    }
  }
  digits[inp == nine] <- 9
  
  #0
  zero <- paste(candidates[[numbers[!numbers %in% c(k_six, k_9)]]], collapse ="")
  digits[inp == zero] <- 0
  
  #5, 2, 3
  candidates<- lapply(strsplit(inp[which(nchar(inp) == 5)], ""), unlist)
  
  numbers <- 1:3
  
  #3
  for(k in numbers){
    if(sum(candidates[[k]] %in% one) == 2){
      three <- paste(candidates[[k]], collapse ="")
      k_three <- k
      candidates[k] <- NA
      break
    }
  }
  digits[inp == three] <- 3
  
  
  #5
  for(k in numbers){
    if(sum(candidates[[k]] %in% four) == 3){
      five <- paste(candidates[[k]], collapse ="")
      k_five <- k
      break
    }
  }
  digits[inp == five] <- 5
  
  #2
  two <- paste(candidates[[numbers[!numbers %in% c(k_three, k_five)]]], collapse ="")
  digits[inp == two] <-2
  
  fun <- function(string){
    paste(str_sort(unlist(strsplit(string, ""))), collapse = "")
    
  }
  
  code_digits <- rep(NA, length(code))
  
  for(digit in 1:length(code)){
    code_digits[digit] <- digits[which(paste(str_sort(unlist(strsplit(code[digit], ""))), collapse = "") ==  sapply(inp,fun))]
  }
  
  code_digits <- as.numeric(paste(code_digits, collapse = ""))
  
  
  return(code_digits)
}
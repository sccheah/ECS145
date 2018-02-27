# constructor for 'ascendNums'
makeAscendNums <- function(x) {
  
  # take difference element-wise of vector excluding first element and vec excluding last element
  y <- x[-1] - x[-length(x)]    
  
  # if there are any elements of y < 0, stop() bc it a decreasing vector
  if (any(y < 0)){
    stop("not nondecreasing")
  }
  
  # if there are any elements of y <= 0, then it is not strictly increasing
  if (any(y <= 0)){
    attr(x, 'strictAscend') <- FALSE
  }
  else {
    attr(x, 'strictAscend') <- TRUE
  }

  # make x a class of 'ascendNums'
  class(x) <- 'ascendNums'
  
  # return instance of class 'ascendNums'
  return (x)
}

# overload print to just show values
#'print.ascendNums' <- function (x) {
#  print (as.vector(x))
#}

# Overload '+' operator
'+.ascendNums' <- function(x, y) {
 
  # make sure both instances are of class 'ascendNums' 
  if ((class(x) != 'ascendNums') || (class(y) != 'ascendNums')) {
    stop("An object is not an instance of class \'ascendNums\'.")
  }
  
  # keep track of x and y index
  x_index <- 1
  y_index <- 1
  
  # result vector that we will return as an instance of class ascendNums
  result <- c(rep(0), length(x) + length(y))
  
  # iterate through the length of the two vectors we want to combine
  for (i in 1:(length(x) + length(y))) {
    # if we are done with x vector and not done with y, then automatically append y element
    if (x_index > length(x) && y_index <= length(y)) {
      result[i] <- y[y_index]
      y_index <- y_index + 1
    }
    # else if we are done with y vector and not done with x, then automatically append x element
    else if(x_index <= length(x) && (y_index > length(y))) {
      result[i] <- x[x_index]
      x_index <- x_index + 1
    }
    # else, perform comparison
    else {
      if (x[x_index] <= y[y_index]){
        result[i] <- x[x_index]
        x_index <- x_index + 1
      }
      else {
        result[i] <- y[y_index]
        y_index <- y_index + 1
      }
    }
  }
  
  # return instance of makeAscendNums
  return (makeAscendNums(result))
}

# overload '[<-'() to report error;
'[<-.ascendNums' <- function(x, i, value) {
  # method to make it perform as normal assignment
  # x <- as.vector(x)
  # x[i] <- value
  # return (makeAscendNums(x))
  
  stop("read-only")
}







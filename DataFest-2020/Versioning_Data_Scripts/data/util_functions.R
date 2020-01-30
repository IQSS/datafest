# Small script snipplets that can be brief
# examples for programming or demonstrations


# Print Hello World
hello_world <- function() {
  myString <- "Hello, World!"
  print (myString)
}


# Monte Carlo Pi
montecarloPi <- function(trials) {
  count = 0
  for(i in 1:trials) {
    if((runif(1,0,1)^2 + runif(1,0,1)^2) < 1) {
      count = count + 1
    }
  }
  return((count*4) / trials)
}


# Estimate Pi
est.pi <- function(n){
  
  # drawing in  [0,1] x [0,1] covers one quarter of square and circle
  # draw random numbers for the coordinates of the "dart-hits"
  a <- runif(n,0,1)
  b <- runif(n,0,1)
  # use the pythagorean theorem
  c <- sqrt((a^2) + (b^2) )
  
  inside <- sum(c<1)
  #outside <- n-inside
  
  pi.est <- inside/n*4
  
  return(pi.est)
}


# Square function
square_it <- function(x){
  sq <- x*x
  return(sq)
}


# Anscombe's quartet
anscombes_quartet <- {
    library(Tmisc)

    # Load the data and look at it
    data(quartet)
    str(quartet)

    # Compute simple statistics for each
    library(dplyr)
    quartet %>% 
      group_by(set) %>% 
      summarize(mean(x), sd(x), mean(y), sd(y), cor(x,y))

    # Visualize the data
    library(ggplot2)
    ggplot(quartet, aes(x, y)) + 
      geom_point() + 
      geom_smooth(method = lm, se = FALSE) + 
      facet_wrap(~set)
}

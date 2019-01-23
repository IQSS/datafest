Sys.setenv(R_MAKEVARS_USER="~/.R/Makevars")
library(rstan)
golf_data <- read.csv("golf_data.csv")
dat <- with(golf_data, list(obs = nrow(golf_data), feet = feet, 
                            tries = tries, made = made, mu = 1 / 15))
model1 <- stan_model("golf1.stan")
post1 <- sampling(model1, data = dat, refresh = 0)
print(post1, pars = "beta")
mat_post1 <- as.matrix(post1)

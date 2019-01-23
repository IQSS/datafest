data {
  int<lower = 0> obs;           // number of levels of feet from hole
  vector<lower = 0>[obs] feet;  // distance to hole, measured in feet
  int<lower = 0> tries[obs];    // number of puts at each level of feet
  int<lower = 0> made[obs];     // number of puts made at each level of feet
  real<lower = 0> mu;           // expected value of beta
}
parameters { real<lower = 0> beta; }    // sensitivity of success probability
transformed parameters {
  vector[obs] prob = exp(-beta * feet); // success probability function
}
model {
  made ~ binomial(tries, prob); // ex-ante beliefs about data
  beta ~ exponential(1 / mu);   // ex-ante beliefs about beta
}
generated quantities { // calculates things for subsequent model comparison
#include /log_lik.stan
}

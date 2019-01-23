data {
  int<lower = 0> obs;           // number of levels of feet from hole
  vector<lower = 0>[obs] feet;  // distance to hole, measured in feet
  int<lower = 0> tries[obs];    // number of puts at each level of feet
  int<lower = 0> made[obs];     // number of puts made at each level of feet
  real<lower = 0> r;            // radius of the golf ball (in feet)
  real<lower = 0> R;            // radius of the hole (in feet)
}
transformed data { 
  vector[obs] num = asin((R - r) * inv(feet)); // numerator
}
parameters { 
  real<lower = 0> sigma_degrees;
}
transformed parameters {
  real sigma = sigma_degrees * pi() / 180;     // now in radians
  vector[obs] prob = 2 * Phi(num / sigma) - 1; // Phi() is std normal CDF
}
model {
  made ~ binomial(tries, prob);   // ex-ante beliefs about data
  sigma_degrees ~ exponential(1); // ex-ante beliefs about sigma_degrees
}
generated quantities {
#include /log_lik.stan
}

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
  real<lower = 0> sigma_distance;
}
transformed parameters {
  real sigma_1 = sigma_degrees * pi() / 180;     // now in radians
  vector[obs] prob = (2 * Phi(num / sigma_1) - 1);
  for (i in 1:obs) {
    real denom = sigma_distance^(feet[i] + 1);
    prob[i] *= Phi(2 / denom) - Phi(-1 / denom);
  }
}
model {
  made ~ binomial(tries, prob);   // ex-ante beliefs about data
  sigma_degrees ~ exponential(1); // ex-ante beliefs about sigma_degrees
  sigma_distance ~ exponential(0.3); // ex-ante beliefs about sigma_distance
}
generated quantities {
#include /log_lik.stan
}

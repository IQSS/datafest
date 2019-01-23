  vector[sum(tries)] log_lik; // ex-ante log-probability of the result of each putt
  {
    vector[obs] log_prob = log(prob);
    int pos = 1;                               // indexing in Stan starts with 1
    for (n in 1:obs) {
      real log_prob_n = log_prob[n];           // index once, use repeatedly
      real log_comp_n = log1m_exp(log_prob_n); // log1m_exp(x) := log(1 - exp(x))
      for (m in 1:made[n]) {                   // successful putts
        log_lik[pos] = log_prob_n;
        pos += 1;
      }
      for (t in 1:(tries[n] - made[n])) {      // failured putts
        log_lik[pos] = log_comp_n;
        pos += 1;
      }
    }
  }

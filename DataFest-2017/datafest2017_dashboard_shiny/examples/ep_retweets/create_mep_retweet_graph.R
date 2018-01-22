# ---------------------------
# Create network graph from MEP retweets by party group
# Christopher Gandrud
# ---------------------------

# Load required packages
library(rio)
library(dplyr)
library(igraph)
library(networkD3)

# Set working directory. Change as needed.
setwd('~/Dropbox/FlexShinyDataFest/datafest2017_dashboard_shiny/examples/ep_retweets/')

# Import edgelist
full_data <- import('retweets.csv')

# Randomly select 100 retweets
#sub_data <- full_data[runif(n = 1000, min = 1, max = nrow(full_data)), ]
sub_data <- subset(full_data, origMepName %in% c('Nigel FARAGE', 'Martin SCHULZ',
                                                 'Guy VERHOFSTADT'))

el <- sub_data[, c('origMepGroupShort', 'retweetMepGroupShort')] %>% as.matrix

# Create graph from edgelist
mep_graph <- graph_from_edgelist(el, directed = FALSE) 

mep_wt <- cluster_optimal(mep_graph)
mep_membership <- membership(mep_wt)

E(mep_graph)$weight <- 1
mep_graph <- simplify(mep_graph, edge.attr.comb=list(weight="sum"))



mep_graph_networkD3 <- igraph_to_networkD3(mep_graph, group = mep_membership)
mep_graph_networkD3$weight <- E(mep_graph)$weight


forceNetwork(Links = mep_graph_networkD3$links, Nodes = mep_graph_networkD3$nodes, 
             Source = 'source', Target = 'target', NodeID = 'name', 
             Group = 'group',
             legend = TRUE)




plot(mep_graph)

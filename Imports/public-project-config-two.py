[NEAT]
fitness_criterion     = max
fitness_threshold     = 0.6666666666
pop_size              = 10
reset_on_extinction   = False

[DefaultGenome]
# node activation options
activation_default      = relu
activation_mutate_rate  = 0.0
activation_options      = relu

# node aggregation options
aggregation_default     = sum
aggregation_mutate_rate = 0.4
aggregation_options     = sum max

# node bias options
bias_init_mean          = 0.0
bias_init_stdev         = 1.0
bias_max_value          = 30.0
bias_min_value          = -30.0
bias_mutate_power       = 0.5
bias_mutate_rate        = 0.8
bias_replace_rate       = 0.3

# genome compatibility options
compatibility_disjoint_coefficient = 2.0
compatibility_weight_coefficient   = 0.5


# connection add/remove rates
conn_add_prob           = 0.8
conn_delete_prob        = 0.5

# connection enable options
enabled_default         = True
enabled_mutate_rate     = 0.01

feed_forward            = True
initial_connection      = full_nodirect

# node add/remove rates
node_add_prob           = 0.5
node_delete_prob        = 0.3

# network parameters
num_hidden              = 1
num_inputs              = 3
num_outputs             = 1

# node response options
response_init_mean      = 1.0
response_init_stdev     = 0.0
response_max_value      = 2.0
response_min_value      = -2.0
response_mutate_power   = 0.0
response_mutate_rate    = 0.0
response_replace_rate   = 0.0

# connection weight options
weight_init_mean        = 0.0
weight_init_stdev       = 0.01
weight_max_value        = 5
weight_min_value        = -5
weight_mutate_power     = 0.05
weight_mutate_rate      = 0.8
weight_replace_rate     = 0.3

[DefaultSpeciesSet]
compatibility_threshold = 2.5

[DefaultStagnation]
species_fitness_func = max
max_stagnation       = 20
species_elitism      = 2

[DefaultReproduction]
elitism            = 2
survival_threshold = 0.2
import math

class UpperBoundCalculator():
    def __init__(self, num_agents):
        self.num_agents = num_agents

    def sum_range_calc(self, num_agents):
        if num_agents%4==0:
            return (num_agents-4)/4, 'A'
        elif (num_agents-2)%4==0:
            return (num_agents-2)/4, 'B'
        elif (num_agents-1)%4==0:
            return (num_agents-1)/4, 'C'
        elif (num_agents-3)%4==0:
            return (num_agents-3)/4, 'D'
    
    def sum_formula_lookup_calc(self, sum_type, num_agents, value):
        if sum_type=='A':
            result = ((3*num_agents) - (4*value))/math.factorial((2*value))/math.factorial(num_agents - (2*value))
            return result
        if sum_type=='B':
            result = ((3*num_agents) - (4*value) - 2)/math.factorial((2*value) + 1)/math.factorial(num_agents - (2*value) - 1)
            return result
        if sum_type=='C':
            result = ((num_agents) + (4*value) - 1)/math.factorial((2*value))/math.factorial(num_agents- (2*value))
            return result
        if sum_type=='D':
            result = ((num_agents) + (4*value) - 1)/math.factorial((2*value) + 1)/math.factorial(num_agents- (2*value) - 1)
            return result
        
    def result_calc(self, prod_type, sum, num_agents):
        if prod_type=='A':
            result = 1/(2+(sum*2*(math.pow(math.factorial(num_agents/2),2))/num_agents))
            return 1-result
        if prod_type=='B':
            result = 1/(2+(sum*2*(math.pow(math.factorial(num_agents/2),2))/num_agents))
            return 1-result
        if prod_type=='C':
            result = 1/(sum*num_agents*(math.pow(math.factorial((num_agents - 1)/2),2))/(num_agents - 1))
            return 1-result
        if prod_type=='D':
            result = 1/(sum*num_agents*(math.pow(math.factorial((num_agents - 1)/2),2))/(num_agents - 1))
            return 1-result
    
    def get_upper_bound(self):
        sum_range, sum_type = self.sum_range_calc(self.num_agents)
        sum_range = int(sum_range) + 1
        sum = 0

        for j in range(sum_range):
            sum+=self.sum_formula_lookup_calc(sum_type, self.num_agents, j)

        result = self.result_calc(sum_type, sum, self.num_agents)
        return result
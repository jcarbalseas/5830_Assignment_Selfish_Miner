# import random

# #alpha: selfish miners mining power (percentage),
# #gamma: the ratio of honest miners choose to mine on the selfish miners pool's block
# #N: number of simulations run
# def Simulate(alpha,gamma,N, seed):
    
#     # DO NOT CHANGE. This is used to test your function despite randomness
#     random.seed(seed)
  
#     #the same as the state of the state machine in the slides 
#     state=0
#     # the length of the blockchain
#     ChainLength=0
#     # the revenue of the selfish mining pool
#     SelfishRevenue=0

#     #A round begin when the state=0
#     for i in range(N):
#         r=random.random()
#         if state==0:
#             #The selfish pool has 0 hidden block.
#             if r<=alpha:
#                 #The selfish pool mines a block.
#                 #They don't publish it. 
#                 state=1
#             else:
#                 #The honest miners found a block.
#                 #The round is finished : the honest miners found 1 block
#                 # and the selfish miners found 0 block.
#                 ChainLength+=1
#                 state=0

#         elif state==1:
#             #The selfish pool has 1 hidden block.
#             if r<=alpha:
#                 #The selfish miners found a new block.
#                 #Write a piece of code to change the required variables.
#                 #You might need to define new variable to keep track of the number of hidden blocks.
#             else:
#                 #Write a piece of code to change the required variables.

#         elif state==-1:
#             #It's the state 0' in the slides (the paper of Eyal and Gun Sirer)
#             #There are three situations! 
#             #Write a piece of code to change the required variables in each one.
#             if r<=alpha:

#             elif r<=alpha+(1-alpha)*gamma:

#             else:


#         elif state==2:
#             #The selfish pool has 2 hidden block.
#             if r<=alpha:

#             else:
#                 #The honest miners found a block.

#         elif state>2:
#             if r<=alpha:
#                 #The selfish miners found a new block

#             else:
#                 #The honest miners found a block

#     return float(SelfishRevenue)/ChainLength


# """ 
#   Uncomment out the following lines to try out your code
#   DON'T include it in your final submission though.
# """

# """
# #let's run the code with the follwing parameters!
# alpha=0.35
# gamma=0.5
# Nsimu=10**7
# seed = 100
# #This is the theoretical probability computed in the original paper
# print("Theoretical probability :",(alpha*(1-alpha)**2*(4*alpha+gamma*(1-2*alpha))-alpha**3)/(1-alpha*(1+(2-alpha)*alpha)))
# print("Simulated probability :",Simulate(alpha,gamma,Nsimu, seed))
# """

import random

def Simulate(alpha, gamma, N, seed):
    random.seed(seed)
  
    state = 0        # Initial state
    ChainLength = 0  # Length of the blockchain
    SelfishRevenue = 0  # Revenue of the selfish mining pool
    
    hidden_blocks = 0  # To keep track of hidden blocks held by selfish miners
    
    for i in range(N):
        r = random.random()
        
        if state == 0:
            # State 0: Selfish pool has 0 hidden blocks
            if r <= alpha:
                # Selfish miners mine a block and keep it hidden
                state = 1
            else:
                # Honest miners found a block
                ChainLength += 1
                state = 0

        elif state == 1:
            # State 1: Selfish pool has 1 hidden block
            if r <= alpha:
                # Selfish miners found another block, now have 2 hidden
                hidden_blocks = 2
                state = 2
            else:
                # Selfish miners lose their hidden block to honest miners
                state = 0

        elif state == -1:
            # State -1: Selfish pool has 0 hidden blocks, honest miners found a block
            if r <= alpha:
                # Selfish miners found a block
                ChainLength += 1
                SelfishRevenue += 1
                state = 0
            elif r <= alpha + (1 - alpha) * gamma:
                # Honest miners found a block, selfish miners publish 1 hidden block
                ChainLength += hidden_blocks
                SelfishRevenue += hidden_blocks * gamma
                state = 0
                hidden_blocks = 0
            else:
                # Honest miners found a block, selfish miners lose all hidden blocks
                ChainLength += hidden_blocks
                state = 0
                hidden_blocks = 0

        elif state == 2:
            # State 2: Selfish pool has 2 hidden blocks
            if r <= alpha:
                # Selfish miners found a block
                ChainLength += 2
                SelfishRevenue += 2
                state = 3
            else:
                # Honest miners found a block
                ChainLength += 2
                state = 1

        elif state > 2:
            if r <= alpha:
                # Selfish miners found a block
                ChainLength += state + 1
                SelfishRevenue += state + 1
                state += 1
            else:
                # Honest miners found a block
                ChainLength += state
                state -= 1

    return float(SelfishRevenue) / ChainLength

# Uncomment the following lines to test the function
"""
alpha = 0.35
gamma = 0.5
Nsimu = 10**7
seed = 100

print("Theoretical probability :", (alpha*(1-alpha)**2*(4*alpha+gamma*(1-2*alpha))-alpha**3)/(1-alpha*(1+(2-alpha)*alpha)))
print("Simulated probability :", Simulate(alpha, gamma, Nsimu, seed))
"""


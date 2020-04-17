#!/usr/bin/python

import argparse

def find_max_profit(prices):
# set current price to index 0 this is the pointer
    curr_min_price = prices[0] 
#set current max profit which to start is going to be index 1 - index 0     
    curr_max_profit = prices[1] - curr_min_price
#loop over prices starting at index1, curr min price is index0     
    for i in range(1, len(prices)):
        
    # compare the prices if it's less set it to current price   
        if prices[i] < curr_min_price:
        #lowest price gets set to current min price
            curr_min_price = prices[i]
        #if the difference betweeen the current min price and the next 
        # price is greater than the current max profit       
        elif prices[i] - curr_min_price > curr_max_profit:             
        # set it as the current max profit
            curr_max_profit = prices[i] - curr_min_price
            
            
    return curr_max_profit     

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
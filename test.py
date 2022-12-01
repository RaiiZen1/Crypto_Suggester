# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr
import Bitcoin_address_suggester.viz_v2 as viz


#antoine's address for testing

addresses=[]
 
addresses = sgstr.suggest('3QQdfAaPhP1YqLYMBS59BqWjcpXjXVP1wi')

print('addresses = ',addresses)
print('Possible addresses are ',list(addresses.keys()))

viz.plot_from_first('3QQdfAaPhP1YqLYMBS59BqWjcpXjXVP1wi', addresses)


"""
chances of errors:
    new innovative wallet anonymity method to better anonymize the person
"""

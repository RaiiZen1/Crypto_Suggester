# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr
import Bitcoin_address_suggester.viz_v2 as viz


#antoine's address for testing

addresses=['32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp',    #OK
           '3HsVXJadDZFRwQCfVFNHeornRkmZaVcDzP',
           '37ASdZj1gC3qKS1vLMLDQS2MdZTdYN1Kbi',
           '3GARffqjDk5LgfCUhx3L6nCk7dVEwEPUaN']
 
suggested_addresses = sgstr.suggest('3QQdfAaPhP1YqLYMBS59BqWjcpXjXVP1wi').keys()
print(suggested_addresses)

viz.plot_from_first('3QQdfAaPhP1YqLYMBS59BqWjcpXjXVP1wi', suggested_addresses)


"""
chances of errors:
    new innovative wallet anonymity method to better anonymize the person
"""

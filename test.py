# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr
import Bitcoin_address_suggester.viz_v2 as viz


#antoine's xpub address for testing

addresses=['32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp',    #First
           '3HsVXJadDZFRwQCfVFNHeornRkmZaVcDzP',    #OK
           '37ASdZj1gC3qKS1vLMLDQS2MdZTdYN1Kbi',
           '3GARffqjDk5LgfCUhx3L6nCk7dVEwEPUaN']

    
print(sgstr.suggest('32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp'))
viz.plot_from_first('32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp')
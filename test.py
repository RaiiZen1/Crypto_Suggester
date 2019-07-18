# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr
import Bitcoin_address_suggester.viz_v2 as viz


#antoine's xpub address for testing

"""
addresses=['32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp',    #OK
           '3HsVXJadDZFRwQCfVFNHeornRkmZaVcDzP',
           '37ASdZj1gC3qKS1vLMLDQS2MdZTdYN1Kbi',
           '3GARffqjDk5LgfCUhx3L6nCk7dVEwEPUaN']

addresses = ['3LoynermEyTjSx6aFTSVCCcu1CjHgHD6B8', #A
              '3GMBMYvQBJ5VJkHxYmsGnhZEvgGSfHX14v', #B
              '14RSprohFSLf6jud6ghW4ckhg5Jx5NaSzF', #A first
              '14ct44kH5yVPdvCkZMPtCEyhZiuWRmfSys'] #B first"""

addresses = ['3J51RsAJBHs2wf1sYRusjwkST7pu1RSZZd',  #B
  '1H5FB4fDZWM4fbLWS1uj9yNkV2kQyvHR9V',#A
  '19Em3MS2PggEoEzUhyWbh6hycFAzTFCYm8', #A
  '1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7']#A first
    
#addresses = sgstr.suggest('1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7').keys()
viz.plot_from_first('1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7')
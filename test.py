# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:08:41 2019

@author: Admin
"""

import Bitcoin_address_suggester.get_possible_addr as sgstr

addresses=['32e3ns2dTfx5ogMYhm5UPnqsUYvu2vHGJp',    #OK
           '3HsVXJadDZFRwQCfVFNHeornRkmZaVcDzP',
           '37ASdZj1gC3qKS1vLMLDQS2MdZTdYN1Kbi',
           '3GARffqjDk5LgfCUhx3L6nCk7dVEwEPUaN']

addresses = ['3LoynermEyTjSx6aFTSVCCcu1CjHgHD6B8', #A
              '3GMBMYvQBJ5VJkHxYmsGnhZEvgGSfHX14v', #B
              '14RSprohFSLf6jud6ghW4ckhg5Jx5NaSzF', #A first
              '14ct44kH5yVPdvCkZMPtCEyhZiuWRmfSys'] #B first

addresses = ['1KfbMRm3RaNgST7aDCDxdxUH9coNxoxsTx',  #B
  '15samGwmfwYobjxRi6akvKWDUhLVjJjUnF',#A
  '19Em3MS2PggEoEzUhyWbh6hycFAzTFCYm8', #A
  '1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7']#A first
    
print(suggest('1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7'))
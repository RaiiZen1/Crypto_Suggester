# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:48:53 2019

@author: Admin

initial try


source all : bp_petkanic

"""


from Bitcoin_address_suggester.blockchain_API import blockexplorer as blk
import Bitcoin_address_suggester.heuristics
import csv




def rem_dup(lis):
    """
    returns the same list without duplicate
    """
    new_lis = []
    for l in lis:
        if l not in new_lis:
            new_lis+=[l]
    return new_lis

def get_addresses_from_tx(lis):
    """
    get list of addresses from outputs/inputs P.s. outputs and inputs are list of 
    Output and Input Object from Blockchain API respectively
    """
    ret = []
    for l in lis:
        ret+=[l.address]
    return ret

    

def get_listed_transaction(addr):#an addr object
    """
    returns a list of [[addresses in the input],
                       [addresses in the output],
                       boolean if input,
                       transaction object from blockchain api]
    """
    txs = blk.get_address(addr).transactions
    list_trans = []
    for tx in txs:
        inp = get_addresses_from_tx(tx.inputs)
        out = get_addresses_from_tx(tx.outputs)
        input_ = False
        for each_in in tx.inputs: #check if the given address is in the input
            if each_in.address == addr:
                input_ = True
        
        list_trans+=[(inp, out, input_, tx)]
    return list_trans
    
    

def derive(addr):
    transactions = get_listed_transaction(addr) # [(input_address, 
                                                #  output_address,
                                                #  bool_input, tx_hash)]
    multi_input = []
    shadow = []
    change = []
    
    for trans in transactions:
        multi_input+=heuristics.check_multi_input(addr, trans[0], trans[1], trans[2]) #check only if input
        shadow+=heuristics.check_shadow(addr, trans[0], trans[1], trans[3] ,trans[2]) #check for datecreation
        change+=heuristics.check_change(addr, trans[0], trans[3] ,trans[2])
        
    multi_input , shadow, change= rem_dup(multi_input), rem_dup(shadow), rem_dup(change)
    dic = {}
    for m in multi_input:
        dic[m] = ['multi_input']
    for m in shadow:
        if m not in dic.keys():
            dic[m] = ['shadow']
        else:
            dic[m] += ['shadow']
    for m in change:
        if m != addr:
            if m not in dic.keys():
                dic[m] = ['change']
            else:
                dic[m] += ['change']
    return dic


def suggest(a, max_ = 5):
    dic = derive(a)
    old = {}
    while len(dic.keys())<max_:
        new = []
        for b in dic.keys():
            new += [derive(b)]
        for n in new:
            dic = {**dic, **n}
        if old == dic:
            return dic
        else:
            old = dic
    return dic
    





#print(suggest('1KTMbDyDANDT9FDzsxuDn4tMo6omJf6Vt7'))
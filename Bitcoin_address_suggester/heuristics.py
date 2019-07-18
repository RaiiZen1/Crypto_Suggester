# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:56:12 2019

@author: Admin
"""

from Bitcoin_address_suggester.blockchain_API import blockexplorer as blk

def get_earliest_tx(addr):
    """
    get the earliest transaction from an address
    return a Transaction object
    """
    addr = blk.get_address(addr)
    out = addr.transactions[0]
    for tx in addr.transactions[1:]:
        if out.time>tx.time:
            out = tx
    return out
    

def get_minimum_output(tx):
    """
    given a transaction object
    return an output object with the minimum output
    """
    m = tx.outputs[0]
    for out in tx.outputs:
        if m.value >out.value:
            m=out
    return m
    
def get_minimum_input(tx):
    """
    given a transaction object
    return an input object with the minimum input
    """
    m = tx.inputs[0]
    for inp in tx.inputs:
        if m.value >inp.value:
            m=inp
    return m


def check_multi_input(addr, tx_ins, tx_outs, input_tx=True):
    """
    if 2 or more addresses take part as an input in a transaction , can be considered 
    as one entity
    """
    if input_tx == True and 4 >len(tx_ins) > 1:
        out = []
        for inp_addr in tx_ins:
            if inp_addr != addr:
                out+= [inp_addr]
        return out #return a list of multi input other than addr
    return []

def check_shadow(addr, tx_ins, tx_outs, tx, input_tx=True):
    """
    if the time of the earliest transaction of an address is very close to the time 
    of the transaction, then it is considered as shadow address 
    i.e. belongs to the same entity
    the shadow address needs to be an output
    """
    time = tx.time
    out = []
    if input_tx == False:
        return []
    else:
        for tx_out in tx_outs:
            try:
                first = get_earliest_tx(tx_out) #return a transaction object
                if abs(first.time - time) < 10: #10 is chosen arbitrary
                    out += [tx_out]
            except:
                pass
        return out
            
        
def check_change(addr, tx_ins, tx, input_tx=True):
    """
    if minimum value of an output is smaller than the minimum of the input
    then that output is a change address i.e. belongs to the same entity
    This heuristics is based on the assumption that wallets doesn't spend
    unspent transactions carelessly
    
    we added an extra limit of the outputs, otherwise it can output a 
    false positive due to a coin join transaction or exchange
    """
    min_out = get_minimum_output(tx) #return an output object
    min_in = get_minimum_input(tx)  #return an input object
    
    if input_tx == False:
        return [] 
    else:
        if min_out.value < min_in.value and len(tx.outputs)<3: 
            return [min_out.address]
        else:
            return []
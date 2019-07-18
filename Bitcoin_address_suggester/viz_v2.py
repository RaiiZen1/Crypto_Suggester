# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:38:13 2019

@author: Admin

network visualizing with bfs

"""

import networkx as nx
from blockchain_API import blockexplorer as blk
import csv
import pandas as pd

"""
users = {}

def get_email(id_):
    ""
    given an ID get the email of that person
    ""
    return emails[int(id_)]
    

with open('user-address.csv', newline='') as cs:
    reader = csv.DictReader(cs)
    df = pd.read_csv('user-email.csv')
    emails = pd.Series(df.email.values,index=df.id).to_dict()
    for row in reader:
        if 'antoine' not in get_email(row['id_user']) and 'emile' not in get_email(row['id_user']): #for test
            if row['id_user'] not in users.keys():
                users[row['id_user']] = [row['address']]
            else:
                users[row['id_user']] += [row['address']]"""
                
#---------------------

def is_input(addr, tx):
    """
    check whether an address is an input in a given transaction
    return a boolean value True if it is an input
    """
    for inp in tx.inputs:
        if inp.address == addr:
            return True
    return False

def is_subset(lis, target):
    """
    check whether the lis is a subset of target
    """
    return set(lis).issubset(target)

def total_address_in_tx(tx):
    """
    get the total number of addresses included in a transaction
    """
    return len(tx.inputs)+len(tx.outputs)

def is_valid(addr):
    """
    given an address we check whether it is an exchange address by the
    heuristics that if there exist a transaction from that address that 
    uncludes more than 20 addresses we can say it is an exchange
    """
    txs =  blk.get_address(addr).transactions
    for tx in txs:
        if  total_address_in_tx(tx)>20:
            return False
    return True

def rem_dup_and_addr(lis, addr):
    """
    given a list and an address, remove duplicates and the address from thelist
    """
    new_lis = []
    for l in lis:
        if l not in new_lis and l != addr:
            new_lis+=[l]
    return new_lis

def get_details_from_address(address):
    """
    return edges, labels, nodes on a format of NetworkX
    """
    edges= []
    labels = {}
    nodes = []
    addr = blk.get_address(address)
    i=0
    for tx in addr.transactions:
        i+=1
        if len(tx.inputs) > 6:
            print('coinjoin transaction possibility with {} inputs'.format(len(tx.inputs)))
        if is_input(address, tx):
            for inp in tx.inputs:
                for outp in tx.outputs:
                    edges+=[[inp.address, outp.address]]
                    labels[(inp.address , outp.address)]=str(i)
                    nodes += [inp.address, outp.address]
                    if inp.address in addresses:
                        print('{} address found as input!'.format(inp.address))
                    if  outp.address in addresses:
                        print('{} address found as output!'.format(outp.address))
    return edges, labels, rem_dup_and_addr(nodes, address)



def next_depth(addr):
    """
    with an input address get all the output addresses when the 
    addr is an input to extend the network / graph
    """
    try:
        address = blk.get_address(addr)
        lis = []
        for tx in address.transactions:
            if is_input(addr, tx):
                for each_outp in tx.outputs:
                    if is_valid(each_outp.address):
                        lis+= [each_outp.address]
        if len(lis) < 5:
            return lis
        else:
            print('total number of recepient sent from {} is {}'.format(addr, len(lis)))
            return lis
    except:
        return []
    
    
def plot_from_first(addr, d=4):
    print('First address is {}'.format(addr))
    current =[addr]
    G = nx.DiGraph()
    G.add_nodes_from(current)
    depth = 0
    while (depth<d) and len(G.nodes())<100: 
        next_depth_list = []
        for each_addr in current:
            next_depth_list += next_depth(each_addr)
            try:
                edges, labels, nodes = get_details_from_address(each_addr)
                G.add_nodes_from(nodes)
                G.add_edges_from(edges)
                print(depth)
            except:
                print('enter')
                pass
        current = next_depth_list
        depth += 1
    print(" {}/{} Addresses found!".format(len(set(addresses).intersection(set(G.nodes()))),len(addresses) ))
    G.add_nodes_from(addresses)
    colors = []
    for node in G.nodes():
        if node == addr:
            colors += ['g']
        elif node in addresses:
            colors += ['b']
        else:
            colors += ['r']
    pos = nx.spring_layout(G,k=0.5,iterations=20)
    nx.draw(G, pos, node_color=colors, 
                                with_labels=False, alpha = 0.5)
    


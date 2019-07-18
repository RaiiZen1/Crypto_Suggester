# Cryptio_bitcoin_API

## Motivation:
With the ever increasing interest in using **bitcoin** as currency, The bitcoin market has been more and more alive 
also wallet providers has been more creative in ways to make the identity of their client more *anonymous* (*pseudo-anonymous*).
With that being said there is no possible deterministic approach to cluster addresses in the bitcoin blockchain, however many research has been 
done on the probabilistic approach to this problem. I have collected papers and it is available as reference in this repo under resources folder
This project is an open project and is open to any suggestion and contribution.

To summarize my research, there are several well known behaviour characteristics of crypto wallets that **GENERALLY** can help us guess 
whether 2 addresses are owned or derived from the same wallet. These characteristics are packed into heuristics that analyzes a transaction
and can determine from the addresses that took part in this transaction which are change addresses and which are actual recipients addresses.

The heuristics that I used in the algorithm is :

	-*Multi-input heuristics*
	-*Shadow heuristics*
	-*Change heuristics*

The list is not strictly unchangable, other honorable mentions for the heuristics that i have not implemented can be *Address format* Heuristics 
and as this is an open project , feel free to make your own heuristics and play around with it

**1. Multi Input**

Most papers include the heuristics **_Multi input_** which says *if 2 or more addresses is an input in one same transaction, 
it is safe to assume that the 2 addresses belong to the same wallet*, but due to the wallets advancements such as coinjoin transaction, 
this heuristics can easily become irrelevant

**2. Shadow**

Some papers also include the **_Shadow heuristics_** which says *if the time of the earliest transaction of an address is very close to the time of the 
transaction, then it is considered as shadow address* 
i.e. belongs to the same entity the shadow address needs to be an output

**3. Change**

**_Change Heuristics_** also is one of the most popular heuristics out there. It says that if *minimum value of an output is smaller than the minimum of the 
input then that output is a change address* (i.e. belongs to the same entity)
This heuristics is based on the assumption that wallets doesn't spend unspent transactions carelessly
we also added an extra limit for the number of outputs, otherwise it can output a false positive due to a coin join transaction or exchange addresses

## Dependencies:
	-Blockchain API(No need to install)
	-networkx (for visualization)
	-python3 (Have not tested for python2)

## Practical tutorial

# 1.Installation

Installing this shouldn't be hard, you **do not** need to install blockchain in your pyhton since we have a copy of the api in the repo. 
I did this because the full blockchain API has other features such as wallets, createwallet, exchangerates, etc. which are not really useful for 
our goal. Do refer to the blockexplorer api from blockchain [documentation](https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md)
for some of the notation we will use or if you want to go deeper into the code.
with that being said, all you left to do is to fork this repo and make sure you have python networkx library for the visualization which should already be
in the python package.

# 2.




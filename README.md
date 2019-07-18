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

###1. Multi Input

	Most papers include the heuristics **_Multi input_** which says *if 2 or more addresses is an input in one same transaction, 
it is safe to assume that the 2 addresses belong to the same wallet*, but due to the wallets advancements such as coinjoin transaction, 
this heuristics can easily become irrelevant

## Dependencies:
	-Blockchain API(No need to install)
	-networkx (for visualization)


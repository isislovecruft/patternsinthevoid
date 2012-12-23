Title: Some Ideas For Darknet Implementation, Encryption, and Integration
Date: 2011-04-05 23:19
Author: Admin
Category: Anarchism, Technology
Tags: algorithms, crypto-anarchism, cryptography, cyberfeminism, darknet, darknet integration, decentralized social networks, encryption, freenet, fuzzy logic, i2p, p2p, sinkstoring, small-world models

Notes on Reading [Private Communication Through a Network of Trusted
Connections: The Dark Freenet][] (click for .pdf)

I learned that data encryption within a Freenet (not necessarily dark)
is often restricted to two types: CHKs and SSKs (6). As a basic measure
against profiling and traffic analysis, documents are relegated to set
sizes -- 32kb for CHKs (Content Hash Key, a type of symmetric
cryptographic key generation in which the data includes the means of
generating the key) and 1kb for SSKs (Signed Subspace Key, i.e. ain
information publisher has an asymmetric key-pair used to sign documents
within a free(/dark)net subspace. Any larger documents are split up into
smaller ones to maintain this size imperative. Also, as anyone who has
used any type of P2P net has experienced, search functions within the
network are limited, but I just learned the reason why: directories
aren't plaintext, but are (usually) MD5 hashes of locations. So, unless
you know the precise location of the document or information you're
trying to access, and thus can generate the matching MD5 hash, you can't
even discover that the directory is there. Kind of like how you can't
access an .onion site unless you already know the address. This was
making my brain itch a little bit, but I'm good now.

Fuzzy Logic Operations within Computerized Social Networks applied to
Darknet Operations:[![][]][]

"Instead [of Stanley Milgram's small-world model], we use a method which
draws off the small world models of Jon Kleinberg. The routing we
perform is purely greedy: at each step, the desirability of the
neighbors is ordered by the proximity of their identities to the route
key K (seen as floating point number between 0 and 1 with periodic
boundary). The question then becomes one of trying affect the randomized
assignment of identities such that this becomes an efficient way of
routing. For routing to be efficient Kleinberg’s results show that
certain relation between the frequency of connections of different
lengths (with respect to the identities) must be present, so our goal is
to, to the degree that it is possible, assign identities so that this
holds. The method we have chosen for doing this is a development of that
described in ["Distributed routing in small-world networks" by O.
Sandberg]." (7)

Basically, the propinquity of your friend Miss X to her friend Sir Y's
node which contains the data you're attempting to access, this proximity
is systematized via a fuzzy logic operator which outputs between a range
of [0,1], 0 representing no connections to the desired node, and 1
representing the desired node. Thus, an informational subgraph is
overlayed onto the subgraph of the world's social network which contains
the portion of your social network connected to the darknet.

[caption id="" align="alignleft" width="450" caption="Fuzzy Logic
Explained!"][![][1]][][/caption]

Sorry for the fuzzy logic geek out...I thought it was a cool application
in informational network analysis.

"In our implementation nodes start upon joining the network with
randomly selected identities seen as numbers between 0 and 1. These
identities are then switched between the nodes using the simulated
annealing like method first explored in [29], which causes nodes that
are in some sense close in the network topology to also have nearby
identities. (It is only when this property holds that greedy routing
makes sense in anything but the final step.) The use of random
positions, rather than fixed points in a grid, makes our model slightly
different than the Kleinberg model that is the basis of previous
analysis of this method, but similar continuum models have been
previously studied in [15] and [14]. Nodes at a constant rate initiate
random walks, which terminate after a fixed number of steps (current
six, which simulation indicates is enough even in a large network). When
the walk terminates, the node at which it was started and that at which
it ended attempt to switch identities, which will happen with a
probability specified by the algorithm. Ideally, one would hope to be
able to assign the identities so that every step in a route for K brings
us to a node whose identity is closer to K than the last, until we have
found the best node on the network. In practice, this may not always be
possible, but we still use this as heuristic to show us when to
terminate a route. Currently the route continues until it has reached a
maximal Hops-To-Live (HTL), which is motivated by attempting to balance
a thorough search while limiting resource usage." (7-8)

"Several enhancements to the basic algorithm described in [29] which
could lead to better results have been suggested. Knowing the identity
of ones neighbors’ neighbors is known to improve the performance of
routing in Kleinberg type networks [24] by allowing nodes to route to
the neighbor whose neighbors identities best match the query. Knowing
the identities of neighbor’s neighbors reveals something about the
surrounding network, but does not tell one who they are, so the basic
principle of only revealing oneself to trusted peers remains. Another
performance enhancement that we use is for nodes to be aware of which
documents are present in their neighbor’s cache, by for instance
neighbors passing Bloom filters [4] summarizing the contents of their
cache to each other. A combination of both these techniques can greatly
increase the number of successful searches and decrease the query
length." (8)

One enhancement to this system which I can conceive of would be the
application of hash tags to identities. For instance, when searching on
the darknet for a document, e.g. Kropotkin's Conquest of Bread, your
node would analyze the hash tags of your friends' friends identities
according to the likelihood of them having the document. So, for
instance, you're searching for Conquest of Bread, and you route on the
darknet to your friend Miss X's node. Miss X has two friends on the
darknet, whose identities are invisible to you, but the hash tag
descriptions of them are not. One of these friends has a tag identifying
them as a Democrat, meaning the likelihood of their node containing the
Conquest of Bread is low, say a 5% chance, and so they have an assigned
value of .05 . Miss X's other friend is an Anarchist, and so their
likelihood is high, say 80%, and so they have a value of .80. Now I
realise that the data stored on your node is not directly determined by
you, but by what information is most commonly accessed on the darknet.
However, there should still be some way to either 1) control what data
is stored, or 2) apply hash tags for the type of data which has been
pseudo-randomly stored. I'm not in a position to be creating a darknet
right now, so anyone wanting to use this idea (if it's even at all
feasible) should feel welcome to do so.

Alright, I read further and realized I'm behind on the times. A very
similar idea has already been implemented, called sinkstoring: "...each
node keeps two seperate caches of data. One is a short term cache where
all data that the node transfers is stored temporarily until it pushed
out by other data. The other is meant to keep data longer by storing
only inserted data that matches the nodes identity. The strategy used to
populate this second cache, which we have dubbed sinkstore, is this: A
node will attempt to place the document corresponding to a key K in its
store if it is better located at the node, given its identity, than to
that of any of its neighbors. For example, in the configuration shown in
Figure 1, the node with identity 0.49 is a sink for K = 0.50: its
current identity is closer to that value than any of its neighbors
identities - if the query was an insert, the node with current identity
0.49 would store it." (8)

One of the problems with darknets is the availabilty of trusted peers to
new users. If each new user only knew one person already connected to
the darknet, the resulting network would take on a tree formation, and
the routing process would fail entirely. A possible solution to this
could be integration of darknets with emerging decentralized social
networking platforms, such as Appleseed and Diaspora, so that when users
sign up for an account on the social network they are automatically
integrated with a darknet system. If this were applied, new users
shouldn't have trouble connecting to multiple trusted peers. Again,
someone please steal my ideas -- that's what they're for.

Plus points to the authors of "Private Communication Through a Network
of Trusted Connections: The Dark Freenet" for their excellent gender
politics in using "she" wherever third person gender neutral pronouns
would have been syntactically ambiguous. \<3

  [Private Communication Through a Network of Trusted Connections: The
  Dark Freenet]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/04/Private-Communication-Through-a-Network-of-Trusted-Connections-The-Dark-Freenet.pdf
  []: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/04/darknet-2.jpg
    "darknet 2"
  [![][]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/04/darknet-2.jpg
  [1]: http://imgs.xkcd.com/comics/cat_proximity.png
    "http://xkcd.com/231/"
  [![][1]]: http://xkcd.com/231/

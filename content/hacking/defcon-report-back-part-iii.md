Title: Defcon Report Back, Part III
Date: 2011-08-10 18:45
Author: isis agora lovecruft
Category: hacking
Tags: anonymity, certificate authority, cryptography, defcon

Sunday 7th August, 2011, Defcon 19, Las Vegas

## Whitfield Diffie & Moxie Marlinspike

It was nice to hear my friend Moxie talk with another admirable
cryptographer, Whitfield Diffie, *a la*
[Diffie-Hellman key exchange](https://www.rsa.com/rsalabs/node.asp?id=2248).
I hope, if Mr. Diffie should happen to read this, that he shall excuse
my link to RSA laboratories. However, it was regrettable to have so
many time burglars during the Q&A pretending to ask questions while
actually egotistically talking about obscure research they once did,
or posing artificial problems for [Moxie's](https://thoughtcrime.org)
[Covergence project](http://convergence.io) (a P2P replacement for the
current Certificate Authority structure, the former of which bears
similarities to the PGP/GPG web-of-trust structure).  Commenting on
his project, at one point, Moxie said, "I believe that Certificate
Authorities and politicians are incredibly similar. That is, I believe
that trust in either should expire and and be replaced on a
second-to-second basis." Oh, Moxie. I think you just made every other
crypto-anarchist on the planet fall in love with you. ♥Ⓐ

## Cipherspaces & Darknets

[Adrian "Irongeek" Crenshaw](http://www.irongeek.com/)'s talk,
"*Cipherspaces/Darknets: An Overview of Attack Strategies*", was
incredibly basic. I was disappointed to waste my hour listening to
essentially the exact same talk I gave at Evergreen State College in
Olympia, Washington, on anonymity networks.  Snore. I did learn one
new thing, namely that Firefox can be configured to mitigate DNS
leakage while using Tor by going into the about:config and setting
network.proxy.socks\_remote\_dns to true.

Cryptographic Oracles
---------------------

[Daniel Crowley](http://twitter.com/dan_crowley)
gave a talking [on defeating various cryptographic
schemes using oracles](https://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Crowley-Cryptographic-Oracles.pdf).
Crowley, who is adorable and has an excellent
surname, gave a brief overview of cryptographic terms and ideas, and
then delved into encryption and decryption oracles. An oracle is
essentially any data which is leaked from a cryptographic scheme. So,
for example, if I send multiple queries to a database which uses
encryption, I can get a good idea of how that encryption is occurring
based on the server's responses to manipulated queries such as "aaaa"
"aaaabbbbaaaabbbb" "ababab" etc. At one point during Crowley's demo,
which sadly didn't work as expected, Crowley was using the encrypted
data from a cookie to make SQL injections on a website's encrypted
database. The attack was supposed to result in a page which read "I have
a crush on Moxie Marlinspike...shh!" but, again, it didn't work during
the live demo. As I said earlier, Moxie, every crypto-anarchist and
cipherpunk on the planet is in love with you.

The next talk was on the use of PLCs in the prison system. I'm going to
devote an entire post to discussing this, later, when I'm already in a
bad mood, because that talk made me sick to my stomach with some of the
things I realized. And the presenters' compliance with government
agencies and sociopathic lust to put other human's in cages was
absolutely disgusting. Fuck them.

Title: Tor Bridge Distribution & OONI's Data Collector
Date: 2013-04-28 13:38
Author: isis agora lovecruft
Category: hacking
Tags: China, OONI, Tor, Censorship
Status: draft


Last week, I went to China, for the first -- and possibly the last --
time. 

Later, when I feel like complaining, I'll blog about the negative things, like
the evidence that someone had broken into mine and another Tor developer's
hotel room. As well as the tale of being followed by multiple plainclothes
people through the streets of Kowloon, again with another Tor developer, down
alleys, in and out of cabs, through electronic stores where I loudly and openly
bought tiny audio/video devices to bug myself and the hotel room with. This is
the first time I've ever worn a wire (I know, *they all say that*, right?): it
doens't feel right. I felt the compulsion to warn people who walked up and
started talking to me before they spoke. And even then I still felt dirty and
creepy.

When I started officially working on things for the
[Tor Project](https://torproject.org) last year, I'd imagined that the world
was like a map in an RPG, and that there were a lot of dark, hazy spots that
needed filling in. I worried that if my legal name was publicly attached to Tor
that places like China, Iran, and Syria would always remain dark spots. The
idea that I might be prevented from seeing experiencing those cultures and
regions firsthand, that I would not be able to see the homelands of people I
wanted to empower, merely because a (*corrupt* would be redundant) government
had gotten wise to some name I don't answer to -- it seemed daunting, and a bit
heartbreaking.

![kowloon-1](|filename|../images/2013/04/kowloon-1.jpg)

I've been thinking a lot more about borders lately. Ashamed as I am to admit it
(it's not like I was ever *in favour* of having borders), until now I've held a
very privileged perspective on them. Sure, borders suck. Got it. Yep, people
should be allowed to work wherever they want. Freedom of association, right?
And yet it had never occurred to me: that an invisible line drawn in the sand
could keep you away from your home, or that an arbitrary date on a slip of
paper could decide how long you were permitted to see someone you loved.

After living in Germany and France for precisely the number of days my tourist
visa would allow (Oops. I'd been counting, and thought I was still a week
under. I should probably script that.), I took off for Hong Kong, where
[OpenITP](https://openitp.org) had generously offered me a travel grant to
attend
[the third Censorship Circumvention Summit](http://openitp.org/?q=node/32). Jumping
from France to China to somewhere-undetermined-that-is-not-Schengen definitely
presented some interesting security challenges, since I had to take *all of the
things* I own with me. (It all fits in a backpack, so it's not a space/money
issue, it's a 
> "%&$#@! I'm carrying devices which normally have access to thousands of
> computers, including some Tor Project infrastructure and repositories, and I
> have to keep them safe from a government that is going to hate me more than
> the United States, while eating nothing but plain rice *and* travelling
> 24,671 kilometers?!"
<br>issue.</br>

Since part of this security setup involved not connecting to anything while
inside China, I tried as best as I could to remove network capability from my
laptop, including recompiling my kernel with most of the CONFIG_[\*NET|IP\*]
settings disabled. Without internet and only IRL people to talk to, I got bored
pretty fast (*kidding!* ♡ ) and resorted to pen and paper technology, because I
had some ideas on Tor bridge distribution regarding a system for having clients
connect to a bridge Distributor, and the Distributor authenticating the clients
or requiring a valid Proof-of-Work computation. If the authcheck or PoW doesn't
pass, the Distributor should instruct an OONI Data Collector node to connect to
the client, to scan for censorship events (*I wonder if we can actually get a
network vantage point from the DPI boxes?* :D ), else if the client check
passes, the Distributor should instruct a Tor Bridge to connect to the client.

Here are [my notes](|filename|../images/2013/04/bdb-and-ooni.jpg).

Obviously, the Distributors are going to get blocked, but if we were to use
something like David Fifield's FlashProxy, with it's Facilitator as our
Distributor (notice how all these words are oh-so-cleverly suffixed with
*Tor*...), to contact the Distributor through a "normal" browser, the client
should still be able to compute the auth/PoW and the Bridge or OONI Collector
connect back to them. The Proof-of-Work should be necessary for protecting the
Facilitator/Distributor from getting blocked, as well as significantly increase
the cost of scanning for bridges.

![kowloon-nathan-rd](|filename|../images/2013/04/kowloon-nathan-rd.jpg)

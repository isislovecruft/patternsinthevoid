Title: Defcon Report Back, Part II
Date: 2011-08-09 02:47
Author: isis
Category: Technology
Tags: asterisk, botnet, Defcon, dual-tone multi-frequency, GreyDragon, GreyWolf, keygen, linux, moshi moshi, password cracking, RAFT, reverse engineering, sip-to-pstn, smart fuzzing, voip botnet, web fuzzing

Saturday 6^th^ August 2011, Defcon 19, Las Vegas

 Smartfuzzing
-------------

I missed [Smartfuzzing the Web: Carpe Vestra Foramina][], by Nathan
Hamiel et. al., which I had wanted to attend. I went through the pdf of
the presentation just now, and I wouldn't exactly call it smartfuzzing,
but I did note the cleverness of the presenters' idea to use wordlists
comprised of words taken from the robots.txt file of websites for
fuzzying purposes. Their new tool, [RAFT][], is being released soon,
though it is currently available as an svn checkout.

Creating Cracks and Keygens for .NET Applications
-------------------------------------------------

The first presentation I attended was [Hacking .Net Applications][] by
[Jon McCoy][]. He detailed the extensive uses of his GreyWolf and
GreyDragon tools, including the production of cracks, keygens, and
malware. [GreyWolf][], which is currently in Beta, is a reverse
engineering tool which allows extraction of source code from .dll files,
and [GreyDragon][GreyWolf] is a .NET injection tool. It was astounding
how little actual security is put into authentication of enterprise
applications. The funniest use of GreyDragon was an instance in the demo
in which McCoy altered a Boolean string controlling a password check
from var a=true to var a!=true, which meant that only wrong passwords
would allow access to the program. He was also able to extract source
code from .dlls, find the security and authentication mechanisms, and
then create a keygen for the demonstrated program – a commercial
keylogger – within five minutes.

VoIP Botnetting
---------------

The presentation which might possibly rank as the most impressive was
[Sounds Like Botnet][] by [Itzik Kotler and Iftach Ian Amit][], on VoIP
botnetting. The idea is that certain networks which do not allow active
connections to the outside internet usually do allow VoIP traffic, and
these packets are not often paid much attention. Basically, SIP (Session
Initiation Protocol) is quite similar to HTTP and has little security
built in. SIP supports TSL, but even with this type of encryption
enabled the traffic can be easily sniffer. What this means is that SIP
traffic can easily transverse firewalls, and SIP-to-PSTN (Public Service
Telephony Network, a.k.a. standard telephone lines) can be used to relay
commands to botnetted machine within a closed network, or a network
which does not allow internet access.

Researchers Kotler and Amit used an [Asterisk][] server hosted in the
cloud as the Command-and-Control (C&C). Conference calls were used to
link botnetted boxes together and issue commands from the botmaster,
which also allows for more anonymous direction of the botnet with
conference call bridge numbers. [Moshi Moshi][], an open source VoIP
botnet, was used to communicate with the botnet using Text-to-Speech
engines for output to the botmaster and DTMF tones for input. DTMF
stands for Dual-Tone Multi-Frequency signalling, and, if you remember
the adventures of phreaker Captain Crunch and his 2600Hz whistle tones
which allowed for free telephone calls, you've basically got the idea.
With DTMF, standard keyboard inputs are mapped to certain tonal
frequencies, and when a machine with such translation software
installed, complete binary files and commands can be sent over the wire
through music. Seriously. You make techno music out of a binary file,
play it to your zombies, and they execute the binary. Fucking awesome.
So, the botmaster calls into the conference call on the server, and
receives Text-to-Speech information on the number of machines connected.
During the demo, when the presenters called into the Asterisk server,
they were greeted with a robotic voice saying, "There are currently two
others in this conference room." Next, they played a .wav file of DTMF
tones, and the machines went off to do their bidding.

I really, really, really want Botnet to become a new EBM subgenre.
Really badly.

  [Smartfuzzing the Web: Carpe Vestra Foramina]: https://raft.googlecode.com/files/Smartfuzzing_The_Web_BlackHatUSA_2011.pdf
  [RAFT]: https://code.google.com/p/raft/
  [Hacking .Net Applications]: http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-McCoy-Hacking-Net.pdf
  [Jon McCoy]: http://digitalbodyguard.com/
  [GreyWolf]: http://digitalbodyguard.com/Programs.html
  [Sounds Like Botnet]: http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Kotler-Amit-Sounds-Like-Botnet.pdf
  [Itzik Kotler and Iftach Ian Amit]: http://security-art.com/
  [Asterisk]: https://www.asterisk.org/
  [Moshi Moshi]: https://code.google.com/p/moshimoshi/

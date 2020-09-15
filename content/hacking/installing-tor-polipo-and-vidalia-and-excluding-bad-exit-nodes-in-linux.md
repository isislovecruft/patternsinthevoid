Title: Installing Tor, Polipo, and Vidalia, and Excluding Bad Exit Nodes, in Linux
Date: 2011-06-21 20:15
Author: isis agora lovecruft
Category: hacking
Tags: .onion, anonymity, Bad Apple Attack, Excluding Bad Exit Nodes, linux, Polipo, Setting Up a Tor Relay, Tor, Tor Hidden Services, Vidalia
Status: hidden

**EDITED 1 September 2011:** I STRONGLY SUGGEST THAT YOU FOLLOW
DOCUMENTATION ON THE TOR PROJECT'S WEBSITE, AND IF THAT DOESN"T WORK
THEN ASK FOR HELP IN \#TOR ON IRC.OFTC.NET. I do not have time to write
security howtos, or keep old ones up to date. My apologies, friends.

This is a reference how-to for troubleshooting [Tor][], [Polipo][], and
[Vidalia][] installations and configurations in [Debian][]/[Ubuntu][]
based Linux. Specifically, this is for setting up a [Tor relay][] and
using the Vidalia GUI to configure Tor to skip known bad exit nodes.
However, these instructions can be used to set up Tor for client
(non-relay) use, and the instructions to skip known bad exit nodes still
apply. I am frequently asked to help people with Tor, and so I'm putting
this up for reference.

~~Follow the [steps at the Tor Project page][] for Tor and Polipo
installation. When the installation instructions tell you to move to
step two and install Polipo, skip this part if you are using Ubuntu
10.04 (lucid) or newer. The reason for this is that the apt-get manager
automatically detects Polipo as a dependency and installs it for you.
However, you will have to [configure Polipo][]. Take this [*sample
configuration file for Vidalia with Tor*][], and put copy/paste it into
your current polipo config file (usually at either /etc/polipo/config or
\~/.polipo). Continue through steps three through five on that page to
Torify your browser and applications, and [set up Tor as a relay][].~~

~~Next, you'll want to install the Vidalia GUI.~~

**UPDATE, 1 September 2011:** Installing Vidalia now automatically
installs both Tor and Polipo, and configures them for you, so you only
need the following instructions for getting Vidalia. (If you're running
a Tor relay, you'll still want to head over to the Tor Project website
and follow their current configuration instructions for Tor and Polipo.)

Normally, I'd say fuck GUIs -- they needlessly complicate matters. But
in this case, it's important because it makes editing the torrc (the Tor
configuration file) easier on-the-fly. Which you'll want to be doing to
avoid the known bad exit nodes. And, trust me, you really want to avoid
those nodes. I'll explain what those are in a minute. For instance,
there's a node called "NSAFortMeade". Um, yeah. Good job, guys, on not
making it obvious. /facepalm

Alright, to install the Vidalia GUI, you'll need to add these lines to
your repository sources file (usually located in /etc/apt/sources.list):

          deb http://ppa.launchpad.net/adnarim/ubuntu gutsy main      deb-src http://ppa.launchpad.net/adnarim/ubuntu gutsy main

Then do:

          sudo apt-get update      sudo apt-get install vidalia

~~Next, you'll want to remove Tor from the startup scripts. This is
important because Vidalia and Tor may be working fine right now, but
next time you restart your computer, Tor will start automatically, and
then Vidalia will try to start another instance of Tor, which will cause
it to break.~~

~~To remove all Tor processes from all startup scripts, use the
command:~~

     $ sudo update-rc.d -f tor remove

There you go; Vidalia should now start with Alt+F2 then type "vidalia"
in the run prompt. Vidalia should automatically start an instance of
Tor. If it complains that Tor is already running, you'll want to
manually stop Tor (see the useful commands section at the bottom of this
page), then restart Vidalia.

Okay, now for configuring Tor *not to use* those bad exit nodes. I'm
going to give a brief explanation of what those are and why you'll want
to avoid them now. For those of you who aren't new to Tor, skip ahead a
little bit.

Basically, for those of you new to Tor, your traffic is going to route
through several other computers, called nodes, in the Tor network before
going to the destination (website, remote fileserver, etc.). Usually,
your traffic will go through a chain of three nodes. This chain will
change every ten minutes or so. Tor uses onion encryption, which is
exactly like it sounds --  like an onion. The first node can "see" the
first layer of the onion, which contains information on who you are and
which other node to second your information to; however, it cannot see
what information you have requested. The second node can "see" the
second layer of the onion, which doesn't say much of anything; the
second node cannot see who you are, nor can it see what information you
are requesting. The last node, called the exit node, can see what
information has been requested, but it doesn't know who requested it.
The connection between the exit node and the internet is, by default,
plaintext, unless you have requested an encrypted/secure webpage (which
is why it is important to use [HTTPS Everywhere][]). This means that, if
the people running the exit node which your traffic is currently routed
though are dirty, no-good, evil, malicious baddies, they can implement
what is known as the [Bad Apple Attack][] to discover your true IP
address. It is also possible for the baddies running a bad exit node to
alter your traffic, which is called [packet injection][]. Those evil
baddies can also do other things, like phish for your passwords, spoof
webpages to steal credentials, etc. Long story short, it's a good idea
to avoid these nodes.

Thankfully, there's a [.onion site][] (that means it's a [Tor Hidden
Service][] -- a website hosted anonymously via the Tor network and only,
or [mostly only][], viewable through Tor). So, with Tor running, direct
a new tab of your browser to [InspecTor][]. Check the boxes for nodes
you want to exclude, depending on your level of paranoia. I'd recommend,
at bare minimum, checking the boxes for Known Bad Nodes, Nodes With
Strange Exit Policies, and Nodes Running Critical Versions of Tor. I'd
also recommend checking the box to identify nodes based on their
fingerprint. Click the button to generate the ExcludeNodes list. A new
page will come up with the list of nodes in a text box. Select all, and
copy.

In the Vidalia GUI, click the Settings button, then navigate to the
Advanced tab. In the second box down, click the Edit Current Torrc
button. Paste the list of nodes to exclude from InspecTor into this
file, make sure the Apply All button is selected, and the Save Settings
box is checked. Hit OK.

There you are. If you have [Torbutton][] installed in Firefox, you can
now surf the internet (pseudo)anonymously, without worrying about the
NSA and other baddies sniffing your traffic.

If you have questions or problems, email me at
isis agora lovecruft(at)patternsinthevoid(dot)net, and I will do my best to help. My
public GPG key can be found [here][], if you wish to send me an
encrypted email. To head back to the Basic Security pages, [click
here][].

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Commands of General Help

    $ lsb_release -c                 //displays the codename of the running Ubuntu version$ /etc/debian_version            //displays the codename of the running Debian version$ ss -anl | grep 9050            //checks which service is running on a specific port,                                 //in this case, port:9050, the standard port for Tor$ sudo /etc/init.d/tor stop      //stops Tor$ sudo /etc/init.d/polipo stop   //stops Polipo$ sudo /etc/init.d/tor start     //starts Tor$ sudo /etc/init.d/polipo start  //starts Polipo$ sudo /etc/init.d/tor restart   //I think you get the idea$ sudo update-rc.d -f tor remove //removes all instances of Tor from the startup scripts

 

  [Tor]: https://www.torproject.org/index.html.en
  [Polipo]: http://www.pps.jussieu.fr/%7Ejch/software/polipo/
  [Vidalia]: https://torproject.org/projects/vidalia
  [Debian]: http://www.debian.org/
  [Ubuntu]: http://www.ubuntu.com/
  [Tor relay]: http://195.234.10.45/
  [steps at the Tor Project page]: https://www.torproject.org/docs/debian.html.en
  [configure Polipo]: https://www.torproject.org/docs/tor-doc-unix.html.en#polipo
  [*sample configuration file for Vidalia with Tor*]: https://gitweb.torproject.org/torbrowser.git/blob_plain/HEAD:/build-scripts/config/polipo.conf
  [set up Tor as a relay]: https://www.torproject.org/docs/tor-doc-relay.html.en
  [HTTPS Everywhere]: https://www.eff.org/https-everywhere/
  [Bad Apple Attack]: http://search.yahoo.com/r/_ylt=A0oGdVvgRwFOiBgA6eRXNyoA;_ylu=X3oDMTByZ3RtN3J1BHNlYwNzcgRwb3MDMgRjb2xvA3NrMQR2dGlkAw--/SIG=12kk6c8up/EXP=1308728384/**https%3A//db.usenix.org/events/leet11/tech/full_papers/LeBlond.pdf
  [packet injection]: http://security-freak.net/packet-injection/packet-injection.html
  [.onion site]: http://en.wikipedia.org/wiki/.onion
  [Tor Hidden Service]: https://www.torproject.org/docs/hidden-services.html.en
  [mostly only]: http://tor2web.org/
  [InspecTor]: http://xqz3u5drneuzhaeo.onion/users/badtornodes/
  [Torbutton]: https://www.torproject.org/torbutton/
  [here]: http://www.patternsinthevoid.net/isis agora lovecruft_pgp_public_key.html
  [click here]: http://www.patternsinthevoid.net/security.html

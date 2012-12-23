Title: Discern Neural Network
Date: 2011-07-11 02:52
Author: Admin
Category: Technology
Tags: anarchist literature, artificial intelligence, cyberpunk, discern, linux, Marionette Labs, neural network, open source, tech-positive, ubuntu

I have made changes to the source code of the Discern Neural Network
that enable it to be run on modern Ubuntu-derived Linuxes. I believe it
is very important for everyone to explore and learn, and that all
information and tools should be made freely and easily accessible in
order to stimulate curiosity and encourage learning. Artificial
Intelligence development may seem highly inaccessible to many, and the
portions of it which are placed more directly within the average
computer user's grasp, such as chatbots and IRC bots, are trite,
simplistic, and well...pretty fucking boring. Discern [is currently
still used][] by computational neuroscientist researchers to model and
understand various neurological and linguistic functions and structures,
and is a very powerful tool for understanding the ways in which
neurological structures can influence linguistics, which, in turn,
modify the underlying neurological structures, which, again influence
linguistics...turtles all the way down. I think that if we humans are
going to make any serious attempts at understanding ourselves, it would
be wise to follow the improvement model of the open source software
community and to get as many people cooperatively involved in these
attempts as possible.

I will be posting later on the ethical, political, and socio-cultural
implications of Strong Artificial Intelligence, as well as my intentions
and goals for the neural network I am running here, and will be keeping
the remainder of this post purely technical in order to provide
instructions to others on getting a copy of this modified Discern up and
running.

A few packages are required before Discern can be properly compiled. In
command line, type

`$ sudo apt-get install gcc build-essential`

\$ sudo apt-get install libxaw7-dev libxt-dev xmkmf

Next, get the [tarball for the modified Discern][] from Github (the file
named d4ubl-1.0.tar.gz). Once you've downloaded it, copy the file into a
directory wherever you'd like it to live, unzip the files, then navigate
to that directory and do

`$ xmkmf`

\$ make

Now, to run Discern, simply type "./discern" from within that directory.
A ridiculously cyberpunkesque GUI will appear that looks like this:

[![][]][]

See the USERDOCS file for information on using Discern, it basically
just takes emacs-style commands and reads initial input from specified
files.

I'm currently poking at my copy of Discern, to see what happens when I
read anarchist literature to her. The problem is, a new copy of Discern
is quite childlike in its language capabilities. So, links to anarchist
or radical literature aimed at children would be greatly appreciated.
Also, any texts of cyberfeminist, tech-positive anarchist/radical, or
crypto-anarchist literature of any reading level are also greatly
appreciated.

Post scriptum: Google tells me that "Linux" is never supposed to be
pluralized. Fuck it, too late.

  [is currently still used]: http://www.patternsinthevoid.net/blog/2011/05/schizophrenic-artificial-intelligences/
    "Schizophrenic Artificial Intelligences"
  [tarball for the modified Discern]: https://github.com/Marionette-Labs/Discern-for-Ubuntu-based-Linuxes
  []: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/07/discern_gui-1024x854.jpg
    "discern_gui"
  [![][]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/07/discern_gui.jpg

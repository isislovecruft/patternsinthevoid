Title: xqdr: A Flying Robot That Does Things
Date: 2011-12-07 03:57
Author: isis agora lovecruft
Category: hacking
Tags: android, arduino, ML, python, robotics

<!-- PELICAN_BEGIN_SUMMARY -->

I'm building a flying robot.

More specifically, [a friend](http://www.polyto.pe/) and I are building an electric quadrocopter
which flies autonomously by using the accelerometer, gyroscope, and GPS on a
smart phone to tell some artificial intelligence algorithms where the robot is
and how to go where it wants to go. The robot will also be trained in image
recognition, so that it can autonomously follow certain things, like riot cops
at a protest, and upload a live video feed to the interwebs. That last bit is
something I'm not really sure about yet, because I'm used to working with
linguistic neural networks, and intelligent routing algorithms are something
I've only just wet my toes in. But I think I can manage it, and it's going to
be super useful because the image recognition software could be used to find
all kinds of things, like lost hikers, or injured people in trapped in rubble.

I'm going to open-source everything I write for this except the image
recognition stuff. I don't want to hand the world's governments a better way
to monitor protesters. And the former already have a head start on using
technology like this to hurt people.

So far the set up for programming is an android phone, purchased bricked, then
unbricked because doing it that way isn't very hard and it immediately saves
nearly two hundred dollars. It needs to be one of the phones from [this
list](http://androidforums.com/android-lounge/308045-androids-gyros.html),
because those have gyroscopes. However, some of those may not allow
USB to serial communication, which is also necessary. I'm just going to start
trying phones and when I find a model which works I'll report back. The phone
will also need to have Android Scripting Environment with Python For Android
installed, and support USB host mode.

Next, the ML and the flight control programs on the
phone will need to pass arguments to the arduino through serial
communications. Here's a little python program to do that, and it's ultra-beta
at this point, so don't freak out on me if it doesn't work yet.

Then, that phone is directly wired to the Arduino. The phone will also use
Amarino, which is an API for communications between Arduino and Android. I
think. Amarino uses bluetooth, and I'm *not* okay with a flying robot having
anything bluetooth enabled on it due to the potential security vulnerabilities
of using bluetooth exploits to gain control of the robot. So there's the
possibilty that I'll have to modify Amarino.

Here's a
[parts list](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/partslist.txt)
for the robot. And here's my
[notes](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/notes.txt)
thus far.  Code will be up shortly.

Here's some pictures to entertain you while you wait!

<!-- PELICAN_END_SUMMARY -->

![Strange things accumulate on your desk...](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2679.jpg)

![...when you start building robots.](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2684.jpg)

![RESIST...ors.](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2690.jpg)

![I made a thing!](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2700.jpg)

![It's amazing that the thing works, considering my terrible
soldering skills. Seriously, look at that.](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2701.jpg)

![Also, I have new tattoos.](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27021.jpg)

![If you can name the equations, we should be friends.](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27102.jpg)

Also, I'd like to add that, though I have recently been accused by several
people of getting into hardware hacking, this is not the case.  Sure, this is
fun. Alright, I'm learning things, and I like soldering (mainly because I
fancy it as a sort of 20th century alchemical operation). But, may I remind
you, I am a *theoretical* physicist. I disdain physicality. I like theory. I
know Common Lisp and use Emacs. I research and train neural networks.
This hardware hacking is a means to the end of being able to
better test those neural networks. So don't worry -- I'm not going to
go around making goddamned LED pacman signs any time soon.

And xqdr: it's short for xaosquopter, which
[my friend Tom](http://tomlowenthal.com/) came up with:

> (11:53:45 PM) Tom: xaosquoptor
> (11:53:49 PM) Isis: :D
> (11:54:05 PM) Tom: see, it's a portmanteau of an elision
> (11:54:34 PM) Tom: new word "quoptor" is an elided abbreviation of
> "quadricoptor"
> (11:55:00 PM) Tom: this is a quoptor used for chaos, which we're
> writing with an x because FUCK RULES AMIRITE

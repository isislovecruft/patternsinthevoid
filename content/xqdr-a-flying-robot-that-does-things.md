Title: xqdr: A Flying Robot That Does Things
Date: 2011-12-07 03:57
Author: Admin
Category: Anarchism, Technology
Tags: Anarchism, android, arduino, artificial intelligence, general relativity, hacking, occupy movement, python, robotics, xqdr

I'm building a flying robot.

More specifically, [a friend][] and I are building an [electric
quadrocopter][] which flies autonomously by using the accelerometer,
gyroscope, and GPS on a smart phone to tell some artificial intelligence
algorithms where the robot is and how to go where it wants to go. The
robot will also be trained in image recognition, so that it can
autonomously follow certain things, like riot cops at a protest, and
upload a live video feed to the interwebs. That last bit is something
I'm not really sure about yet, because I'm used to working with
linguistic neural networks, and intelligent routing algorithms are
something I've only just wet my toes in. But I think I can manage it,
and it's going to be super useful because the image recognition software
could be used to find all kinds of things, like lost hikers, or injured
people in trapped in rubble.

I'm going to opensource everything I write for this except the image
recognition stuff. I don't want to hand the world's governments a better
way to monitor protesters. And the former already have a head start on
using technology like this to hurt people.

So far the set up for programming is an android phone, purchased
bricked, then unbricked because doing it that way isn't very hard and it
immediately saves nearly two hundred dollars. It needs to be one of the
phones from [this list][], because those have gyroscopes. However, some
of those may not allow USB to serial communication, which is also
necessary. I'm just going to start trying phones and when I find a model
which works I'll report back. The phone will also need to have Android
Scripting Environment with Python For Android installed.

Next, the artificial intelligences and the flight control programs on
the phone will need to pass arguments to the arduino through serial
communications. Here's a little python program to do that, and it's
ultra-beta at this point, so don't freak out on me if it doesn't work
yet. (Actually, I'm going to have to put in on a GitHub, so hold your
horses. Apparently, WordPress wisely considers .py files a security
concern.)

Then, that phone is directly wired to the Arduino. The phone will also
use Amarino, which is an API for communications between Arduino and
Android. I think. Amarino uses bluetooth, and I'm *not* okay with a
flying robot having anything bluetooth enabled on it due to the
potential security vulnerabilities of using bluetooth exploits to gain
control of the robot. So there's the possibilty that I'll have to modify
Amarino.

Here's a [parts list][] for the robot. And here's my [notes][] thus far.
Code will be up shortly.

Here's some pictures to entertain you while you wait!

[caption id="attachment\_1081" align="aligncenter" width="614"
caption="Strange things accumulate on your desk..."][![][]][][/caption]

 

[caption id="attachment\_1082" align="aligncenter" width="614"
caption="...when you start building robots."][![][1]][][/caption]

[caption id="attachment\_1083" align="aligncenter" width="614"
caption="RESIST...ors."][![][2]][][/caption]

[caption id="attachment\_1084" align="aligncenter" width="614"
caption="I made a thing!"][![][3]][][/caption]

[caption id="attachment\_1085" align="aligncenter" width="614"
caption="It's amazing that the thing works, considering my terrible
soldering skills. Seriously, look at that."][![][4]][][/caption]

[caption id="attachment\_1088" align="alignleft" width="262"
caption="Also, I have new tattoos."][![][5]][][/caption]

[caption id="attachment\_1089" align="alignright" width="277"
caption="If you can name the equations, we should be
friends."][![][6]][][/caption]

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Also, I'd like to add that, though I have recently been accused by
several people of getting into hardware hacking, this is not the case.
Sure, this is fun. Alright, I'm learning things, and I like soldering
(mainly because I fancy it as a sort of 20th century alchemical
operation). But, may I remind you, I am a *theoretical* physicist. I
disdain physicality. I like theory. I know Common Lisp and use emacs. I
research and train artificial intelligences. This hardware hacking is a
means to the end of being able to better test those artificial
intelligences. So don't you worry -- I'm not going to go around making
goddamned LED pacman signs any time soon.

And xqdr: it's short for xaosquopter, which [my friend Tom][] came up
with:

> (11:53:45 PM) Tom: xaosquoptor
>
> (11:53:49 PM) Isis Lovecruft: :D
>
> (11:54:05 PM) Tom: see, it's a portmanteau of an elision
>
> (11:54:34 PM) Tom: new word "quoptor" is an elided abbreviation of
> "quadricoptor"
>
> (11:55:00 PM) Tom: this is a quoptor used for chaos, which we're
> writing with an x because FUCK RULES AMIRITE

  [a friend]: http://www.polyto.pe/
  [electric quadrocopter]: http://hackerspaces.org/wiki/OccuCopter
  [this list]: http://androidforums.com/android-lounge/308045-androids-gyros.html
  [parts list]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/partslist.txt
  [notes]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/notes.txt
  []: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2679-1024x768.jpg
    "IMG_2679"
  [![][]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2679.jpg
  [1]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2684-1024x768.jpg
    "IMG_2684"
  [![][1]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2684.jpg
  [2]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2690-1024x768.jpg
    "IMG_2690"
  [![][2]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2690.jpg
  [3]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2700-1024x768.jpg
    "IMG_2700"
  [![][3]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2700.jpg
  [4]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2701-1024x768.jpg
    "IMG_2701"
  [![][4]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_2701.jpg
  [5]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27021-768x1024.jpg
    "IMG_2702"
  [![][5]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27021.jpg
  [6]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27102-768x1024.jpg
    "IMG_2710"
  [![][6]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/12/IMG_27102.jpg
  [my friend Tom]: http://tomlowenthal.com/

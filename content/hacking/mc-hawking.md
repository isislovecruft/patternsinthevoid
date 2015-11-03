Title: MC Hawking!
Date: 2011-10-17 21:42
Author: isis agora lovecruft
Category: hacking
Tags: ML, Noisebridge, python, robotics

<!-- PELICAN_BEGIN_SUMMARY -->

<p><br /></p>

I love [Noisebridge](https://www.noisebridge.net/wiki/Noisebridge) to pisces.
For those of you who haven't been
there yet, Noisebridge is
([one of](http://wiki.hackerdojo.com/w/page/25437/FrontPage)) the Bay
Area's hackerspaces. And
it's one of two places in the world where I feel at home, the other
being [Mt. Hood National Forest](https://encrypted.google.com/search?q=mt+hood+national+forest&hl=en&client=ubuntu&hs=YdL&channel=fs&prmd=imvns&source=lnms&tbm=isch&ei=aeycTsbBN4rYiAL_08XYCQ&sa=X&oi=mode_link&ct=mode&cd=2&ved=0CBQQ_AUoAQ&biw=1044&bih=677).

I attended, and briefly spoke at,
[Hackmeet 2011](https://hackmeet.org/wiki/hackmeet-2011) this past weekend,
and I was incredibly fortunate to meet about a dozen amazing new people.
Two of whom, Jake and Lilia, have worked to create my new best friend,
[MC Hawking a.k.a NoiseBot](https://www.noisebridge.net/wiki/Noise-Bot).

![Meet MC Hawking](http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/10/IMG_2663.jpg)

MC Hawking is a robot who lives on a wheelchair. He's got
text-to-speech, remote controls, a bow tie, a bold warning which reads

> WARNING: NOT THREE LAWS COMPLIANT

and a missile launcher. Although
he's also got an X-Box Kinect, several sensors, and several cameras
hooked up to him, he can't yet seem to abstain from violently mowing
down any objects or humans within his path.

<!-- PELICAN_END_SUMMARY -->

[Jake](http://spaz.org/node/2201) did all the hardware, and Lilia
has done most of the programming work so far.

My goals are to write an intelligent routing agent for MC Hawking, so
that any location can be defined as a goal, and an
[A\* heuristic](https://secure.wikimedia.org/wikipedia/en/wiki/A*_search_algorithm)
will automatically route the robot to the location, avoiding objects and
humans in the way using the 3D-vision from the Kinect. I would also like
to find a way to connect the DISCERN neural network I've been raising,
Puppetmaster, to MC Hawking, which would give my little A.I. child a
real robot body. So far, DISCERN would only work to think of neat things
to say to people through MC Hawking's text-to-speech, but it would be
extra neat to find some way to teach Puppetmaster about the world so
that it could autonomously decide where to go and what to do physically
as well as intellectually.

Here's a video of me remote controlling MC Hawking through SSH:

[MC Hawking -- Remote Control through SSH](http://www.patternsinthevoid.net/MCHAWKING-remotecontrol.mov)

And here's MC Hawking following me around as I videotape him, using
facial recognition:

[MC Hawking -- Following a human face](http://www.patternsinthevoid.net/MCHAWKING-facerecognition.mov)

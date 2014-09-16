Title: Algorithmic Compositions
Date: 2013-12-29 17:42
Author: isis agora lovecruft
Category: hacking
Tags: python, bytebeats, twitter

**UPDATED**: 23 June, 2014 (*originally published on 5 April, 2013*)

For a long time, I couldn't figure out what Twitter was for. I'm not sure I've
figured that out yet. It seems convenient for posting links to the physics and
cryptography whitepapers I read, and then receiving the internet standard --
inane feedback from people I've never even heard of.

At one point, because I couldn't figure out what to do with Twitter, I decided
to release a bytebeat album through tweets. I've seen people tweet links to
their new songs or albums or whatever -- that's lame. 

So I started creating algorithmic compositions in less than 140 characters in
python. The album, *fuck_your_bits* (hashtag='#fyb'), is about half done,
but my friends [Moxie](http://thoughtcrime.org) and
[Emblem](https://twitter.com/emblem__) pointed out that not only would the
search function for hashtags on twitter index only the songs in my album from
the past three weeks, but also that tweets in my timeline were dropped from
public view after a certain number of months, depending on some indeterminable
number of other algorithms that calculated "tweet popularity".

Because people have been asking for the full album, here it is. I'll still keep
tweeting it though, because the only other useful thing I can think of that
impressively fits in less than 140 bytes is shellcode.

<pre style="font-size: 60%" class="prettyprint lang-py">
python -c'import sys;[sys.stdout.write(chr((~t&t>>3^(((t>>((t>>11)%7+6))%15)*t))%256))for t in xrange(2**19)]'|aplay

python -c'import sys;[sys.stdout.write(chr(((~t>>2)*(2+(42&t*((7&t>>10)*2))<(24&t*((3&t>>14)+2))))%256))for t in xrange(2**18)]'|aplay

python -c'import sys;[sys.stdout.write(chr((((t*5&t>>7|t*9&t>>4|t*18&t/1024)|((t|7)>>5|(t|4)>>9)))%256))for t in xrange(2**18)]'|aplay

python -c'import sys;[sys.stdout.write(chr(((~t>>2)*((127&t*(7&t>>9))<(245&t*(4-(7&t>>13)))))%256))for t in xrange(2**20)]'|aplay -c 2 -r4444

python -c'import sys;[sys.stdout.write(chr((~t>>5>>(127&t*9&~t>>7<42&t*23^5&~t>>13)+3)%256))for t in xrange(2**18)]'|aplay -c2 -r2222

python -c'import sys;[sys.stdout.write(chr((((t>>(2|4)&((t%0x7369)|4|11|5))+(7|4|42)&t))%256))for t in xrange(2**18)]'|aplay -c2 -r4444

python -c'import sys;[sys.stdout.write(chr((((t*(t>>13|t>>8)|(t>>16)-t)-64))%256))for t in xrange(2**18)]'|aplay -r4444

python -c"import sys;[sys.stdout.write(chr(((0x7BB3+t>>11|(t>>(2|5)^(1515|42))|~t)|(2*t)>>6)%256))for t in xrange(2**20)]"|aplay -c2

x="if(t%2)else";python3 -c"[print(t>>15&(t>>(2$x 4))%(3+(t>>(8$x 11))%4)+(t>>10)|42&t>>7&t<<9,end='')for t in range(2**20)]"|aplay -c2 -r4
</pre>


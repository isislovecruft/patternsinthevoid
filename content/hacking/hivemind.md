Title: Hivemind
Date: 2011-12-14 15:31
Author: isis agora lovecruft
Category: hacking
Tags: botnet, C, digital security, hacking, hivemind, IRC, python, text-based RPGs

So I hacked together this IRC bot to play oldschool text-based RPGs with
multiple people in an IRC channel. The
[RPGs are pre-written][http://www.ifarchive.org/indexes/if-archiveXgamesXzcode.html]
and are run by a Z-Machine interpreter called
[Frotz][http://frotz.sourceforge.net/], which runs on a server somewhere, and
commands to Frotz are piped to stdin through a python program called
[pexpect][http://www.noah.org/python/pexpect/].

I'm not going to say which channel this thing is is, because it's hella
insecure (Frotz uses multiple uses of strcpy(), wtf?!), but I will say that
while looking into pexpect I found some old 1990s botnet C&C software when I
totally wasn't expecting it. Check out this file,
[hive.py][http://patternsinthevoid.net/hive.py.txt], which comes with pexpect!
So oldschool!

For some reason, this made me really happy.

 ♥Ⓐ

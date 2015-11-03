Title: Depression Has Infinite Recursion
Date: 2011-12-19 03:03
Author: isis
Category: hacking
Tags: i thought robots weren't supposed to have emotions

<pre class="prettyprint lang-py">
#!/usr/bin/env/ python

def do_nothing():
    while depressed is True:
        do_nothing()
    print "you are still depressed"

if __name__ == "__main__":
    depressed = True
    do_nothing()
</pre>

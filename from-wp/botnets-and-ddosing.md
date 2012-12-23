Title: Botnets and DDoSing
Date: 2011-09-02 15:52
Author: Admin
Category: Technology
Tags: botnet, cloudflare, DDoS, hacking, hailstorm, radical designs, Tor

I was recently the Distributed Denial of Service (DDoS) target of a
known Chinese botnet. Why some random Chinese botmaster decided to
target me, I have no clue. Fortunately, the attack didn't really do any
damage because I use [CloudFlare][]. Which is awesome (and free!). It
made it slightly more difficult for me to update my blog, and I ended
having to go into Wordpress though the frontend after tunneling to the
server over the [Tor][] network. But, due to CloudFlare, my sight stayed
up throughout the entire attack, which lasted several days. Take that,
Chinese hackers!

I mostly wanted to say that I just tested a new web server stress
analyzer, called [Hailstorm][], made by some of my friends over at
[Radical Designs][]. It's basically a website (with a pretty UI!) that
you tell to go to your website, and it attempts to DDoS your website,
and then gives you a bunch of pretty graphs and charts on what happened.
I set the concurrent threads to their highest setting at 1000, and the
maximum requests to the highest setting at 5000. I gave Hailstorm the
highest bandwidth requests I could muster, like some of my music files
and artwork. My site didn't flinch. Not one bit. I even Hailstormed this
site several times within a period of a few minutes. Nothing.

So, Hailstorm, you didn't really tell me anything. You should allow your
maximum requests and concurrent thread settings to go *way* higher. I
guess if you did tell me anything, you told me that that Chinese botnet
was a giant scary monster of a botnet. Which told me, in turn, that
CloudFlare is an even more giant monster, albeit less scary. Thanks,
Hailstorm and CloudFlare, for teaching me things!

And, fuck you, Chinese botmaster.

  [CloudFlare]: https://www.cloudflare.com/
  [Tor]: https://torproject.org/
  [Hailstorm]: http://hailstorm.radicaldesigns.org/
  [Radical Designs]: http://radicaldesigns.org/

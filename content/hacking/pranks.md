Title: Pranks
Date: 2012-06-28 07:42
Author: isis agora lovecruft
Category: hacking
Tags: censorship detection, cryptography, javascript, MPOTR, python, reverse engineering, rio de janeiro, Tor

So, while I'm busy researching away, hard at work [reverse engineering
proprietary network monitoring software][], and trying to devise methodologies
[for detecting all][] the various and newly-emerging means for technological
censorship that the world's government seem to be
[oh][]-[so][]-[peachy][]-[keen][] on developing (the [State Department
recently mentioned our research][] in their daily briefing), my friend
[Nadim][] gets to sit around, playing with crypto, doing things like
implementing the [Anubis cipher][] [for Javascript][] and inventing [music
sharing services with 80s-retro aesthetics][].

And then, he invents [Cryptocat][]. Some of you might have heard of it.  It's
[OTR][], in your browser, as client-side Javascript, and we're hoping to build
it into the Tor Browser Bundle someday. But...that OTR business...I don't
know. It's so *nineties*. And Ian Goldberg recently published a new paper [on
multi-party off-the-record messaging][], but it hasn't been implemented
anywhere yet. Cryptocat is supposed to have multi-party encrypted messaging
support soon, and Nadim was going back and forth on the spec -- there were
some open questions, for example, whether or not the static asymmetric keypair
was necessary given that the each chat was already an in-browser session.

(Cryptonerd tangent: I argue that the static keypair is still necessary due to
Alice and Bob still needing to authenticate to each other with new ephemeral
keypairs when Charlie joins the chat session. Calculation of the session ID
*sid*(i), and thus the group key *gk*(i) for participants *P*(i) depends on
the ephemeral public key {E(Y,i) | Y ∈ *P*(i)} of each participant, ergo to
add to or remove from *P*(i) a new *sid*(i) must be derived, and one should
never reuse E(i). Second, if a user wants to have multiple sids at the same
time, or exit one chat and then join another, assuming that Cryptocat allows
that and that it is done all in the same browser tab, then obviously for the
same reason as before they will need both static and ephemeral keypairs.)

So, myself and some other people involved with Tor, and stuff and crypto
and stuff, took to sending messages to Nadim in all sorts of fanciful
and prankish ways, just to say "IMPLEMENT MPOTR." Notes under the hotel
room door in Brazil; late night phone calls; sharpie on his face after
diving over a conference room table to tackle him. That sort of thing.

Then! I got bored doing some thing where I do something that involves a
computer. And I wrote [this][]:

<pre class="prettyprint lang-sh">
#!/bin/bash
###############################################################
# kaepora
# -------
# Sends an email to @kaepora about implementing MPOTR.
# Requires 'dict' and 'fortune-mod', mutt as your configured
# mail client, and some sort of MTA.
#
# @author isis agora lovecruft Agora Lovecruft, 0x2cdb8b35
# @date 11 June 2012
###############################################################

. ~/.bashrc

TO="nadim@nadim.cc"
FUTURE=`/usr/games/fortune`
FUTURE_FIRST=${FUTURE:0:1}
FUTURE_LAST=${FUTURE:1}
FUTURE="${FUTURE_FIRST,,}$FUTURE_LAST"
FUTURE=${FUTURE%%?[-][-]*}

set -- junk $FUTURE; shift

if [[ "$#" -gt "10" ]] ; then
    SUBJECT="When you implement mpOTR, "`/bin/echo ${@:1:10}`"..."
    shift 10
    BODY="...""$@"
else
    SUBJECT="When you implement mpOTR, $@"
fi
BODY="$BODY"`/usr/bin/whoami`"@"`/bin/hostname`":~$ dict implement
"`/usr/bin/dict implement`"
"`/usr/bin/whoami`"@"`/bin/hostname`":~$ dict mpOTR
"`/usr/bin/dict mpOTR 2>&1`""

echo "${BODY}" | mutt -s "${SUBJECT}" ${TO}
</pre>

Which, short explanation, sends a fancy email to Nadim about how he
needs to IMPLEMENT MPOTR.

And then I tweeted this:

![kaepora-mean-tweet](|filename|../images/kaepora-mean-tweet.jpg)

Which grabs the above script and puts it in the user's crontab so that
the email goes out daily (and each day it's a different email).

I don't actually know how many people crontabbed it. I'm hoping not many,
because I didn't really program any undo button on the little botnet. I
dunno. Twitter. I just wasn't expecting people to read my feed, let alone
click links.

But now, Nadim's just about done IMPLEMENTING MPOTR, so I feel bad. Now
there's [this][1]:

<pre class="prettyprint lang-sh">
#!/bin/bash
###############################################################
# kaepora (nice version)
# ----------------------
# Sends an email to @kaepora to say thanks for implementing 
# MPOTR.  Requires 'fortune-mod', mutt as your configured mail 
# client, a default install of python>=2.5 and some sort of MTA.
#
# @author isis agora lovecruft Agora Lovecruft, 0x2cdb8b35
# @date 28 June 2012
###############################################################

. $HOME/.bashrc

TO="nadim@nadim.cc"
ALSO="isis agora lovecruft@patternsinthevoid.net"
FUTURE=`/usr/games/fortune -e science computers`
FUTURE_FIRST=${FUTURE:0:1}
FUTURE_LAST=${FUTURE:1}
FUTURE="${FUTURE_FIRST,,}$FUTURE_LAST"
FUTURE=${FUTURE%%?[-][-]*}

set -- junk $FUTURE; shift

if [[ "$#" -gt "10" ]] ; then
    SUBJECT="Because you implemented mpOTR, "`/bin/echo ${@:1:10}`"..."
    shift 10
    BODY="...""$@"
else
    SUBJECT="Because you implemented mpOTR, $@"
fi

BODY_SCRIPT=$HOME/scripts/geo-kaepora

if [[ -z $BODY_SCRIPT ]] ; then
    if [[ -z $HOME/.geo-kaepora ]] ; then
        wget -O $HOME/.geo-kaepora http://www.patternsinthevoid.net/geo-kaepora
        chmod +x $HOME/.geo-kaepora
    fi

    BODY_SCRIPT=$HOME/.geo-kaepora
fi

BODY="$BODY"`$BODY_SCRIPT`""
echo "${BODY}" | mutt -s "${SUBJECT}" ${TO}

## Just to be fair this time...
echo "${BODY}" | mutt -s "${SUBJECT}" ${ALSO}
</pre>

Which downloads and calls [this ridiculous python script][]:

<pre class="prettyprint lang-py">
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################################################################################
# geo-kaepora
# -----------------------
# Prints a random abstract geometrical shape as ascii art!
# Makes a pretty!
# Tells a story written by an AI!
#
# @author Isis Agora Lovecruft, 0x2cdb8b35
# @version 0.0.1
# @date 28 June 2012
#________________________________________________________________________________
# Changelog:
# ----------
# v0.0.1: For kaepora! <(A)3
#         Thanks for being awesome and implementing mpOTR!
#################################################################################

from os import path
from random import choice
from simplejson import loads
from urllib2 import urlopen
from urlparse import urlparse, urlunparse

import socket


class InvalidURL(Exception):
    pass

class SafemnAPI():
    def __init__(self):
        self.URL_SHORTEN = "http://safe.mn/api/?url=%s&format=json"

    def shorten(self, url):
        try:
            url = urlunparse(urlparse(url))
            response = urlopen(self.URL_SHORTEN % url)
            json = response.read()
            json_decode = loads(json)
            url = json_decode.get('url', None)
            if url is None:
                raise InvalidURL
            return url
        except Exception, e:
            raise e

class ForKaepora():

    def __init__(self):
        pass

    @staticmethod
    def print_a_shape(self):
        shapes = []
        shapes.append("""
                                    ,_-=(!7(7/zs_.
                                 .='  ' .`/,/!(=)Zm.
                   .._,,._..  ,-`- `,\ ` -` -`\\7//WW.
              ,v=~/.-,-\- -!|V-s.)iT-|s|\-.'   `///mK%.
            v!`i!-.e]-g`bT/i(/[=.Z/m)K(YNYi..   /-]i44M.
          v`/,`|v]-DvLcfZ/eV/iDLN\D/ZK@%8W[Z..   `/d!Z8m
         //,c\(2(X/NYNY8]ZZ/bZd\()/\7WY%WKKW)   -'|(][%4.
       ,\\i\c(e)WX@WKKZKDKWMZ8(b5/ZK8]Z7%ffVM,   -.Y!bNMi
       /-iit5N)KWG%%8%%%%W8%ZWM(8YZvD)XN(@.  [   \]!/GXW[
      / ))G8\NMN%W%%%%%%%%%%8KK@WZKYK*ZG5KMi,-   vi[NZGM[
     i\!(44Y8K%8%%%**~YZYZ@%%%%%4KWZ/PKN)ZDZ7   c=//WZK%!
    ,\y\YtMZW8W%%f`,`.t/bNZZK%%W%%ZXb*K(K5DZ   -c\\/KM48
    -|c5PbM4DDW%f  v./c\[tMY8W%PMW%D@KW)Gbf   -/(=ZZKM8[
    2(N8YXWK85@K   -'c|K4/KKK%@  V%@@WD8e~  .//ct)8ZK%8`
    =)b%]Nd)@KM[  !'\cG!iWYK%%|   !M@KZf    -c\))ZDKW%`
    YYKWZGNM4/Pb  '-VscP4]b@W%     'Mf`   -L\///KM(%W!
    !KKW4ZK/W7)Z. '/cttbY)DKW%     -`  .',\y)K(5KW%%f
    'W)KWKZZg)Z2/,!/L(-DYYb54%  ,,`, -\-/y(((KK5WW%f
     \M4NDDKZZ(e!/\7vNTtZd)8\Mi!\-,-/i-v((tKNGN%W%%
     'M8M88(Zd))///((|D\tDY\\KK-`/-i(=)KtNNN@W%%%@%[
      !8%@KW5KKN4///s(\Pd!ROBY8/=2(/4ZdzKD%K%%%M8@%%
       '%%%W%dGNtPK(c\/2\[Z(ttNYZ2NZW8W8K%%%%YKM%M%%.
         *%%W%GW5@/%!e]_tZdY()v)ZXMZW%W%%%*5Y]K%ZK%8[
          '*%%%%8%8WK\)[/ZmZ/Zi]!/M%%%%@f\ \Y/NNMK%%!
            'VM%%%%W%WN5Z/Gt5/b)((cV@f`  - |cZbMKW%%|
               'V*M%%%WZ/ZG\+5((+)L'-,,/  -)X(NWW%%%
                    `~`MZ/DZGNZG5(((\,    ,t\\Z)KW%@
                       'M8K%8GN8\5(5///]i!v\K)85W%%f
                         YWWKKKKWZ8G54X/GGMeK@WM8%@
                          !M8%8%48WG@KWYbW%WWW%%%@
                            VM%WKWK%8K%%8WWWW%%%@`
                              ~*%%%%%%W%%%%%%%@~
                                 ~*MM%%%%%%@f`
                                     '''''

    """)
        shapes.append("""
                     _______
                    / _____ \
              _____/ /     \ \_____
             / _____/  311  \_____ \
       _____/ /     \       /     \ \_____
      / _____/  221  \_____/  412  \_____ \
     / /     \       /     \       /     \ \
    / /  131  \_____/  322  \_____/  513  \ \
    \ \       /     \       /     \       / /
     \ \_____/  232  \_____/  423  \_____/ /
     / /     \       /     \       /     \ \
    / /  142  \_____/  333  \_____/  524  \ \
    \ \       /     \       /     \       / /
     \ \_____/  243  \_____/  434  \_____/ /
     / /     \       /     \       /     \ \
    / /  153  \_____/  344  \_____/  535  \ \
    \ \       /     \       /     \       / /
     \ \_____/  254  \_____/  445  \_____/ /
      \_____ \       /     \       / _____/
            \ \_____/  355  \_____/ /
             \_____ \       / _____/
                   \ \_____/ /
                    \_______/

    """)
        shapes.append("""
    +------+.      +------+       +------+       +------+      .+------+
    |`.    | `.    |\     |\      |      |      /|     /|    .' |    .'|
    |  `+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+'  |
    |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
    +---+--+.  |   +-+----+ |     +------+     | +----+-+   |  .+--+---+
     `. |    `.|    \|     \|     |      |     |/     |/    |.'    | .'
       `+------+     +------+     +------+     +------+     +------+'

       .+------+     +------+     +------+     +------+     +------+.
     .' |    .'|    /|     /|     |      |     |\     |\    |`.    | `.
    +---+--+'  |   +-+----+ |     +------+     | +----+-+   |  `+--+---+
    |   |  |   |   | |    | |     |      |     | |    | |   |   |  |   |
    |  ,+--+---+   | +----+-+     +------+     +-+----+ |   +---+--+   |
    |.'    | .'    |/     |/      |      |      \|     \|    `. |   `. |
    +------+'      +------+       +------+       +------+      `+------+

       .+------+     +------+     +------+     +------+     +------+.
     .' |      |    /|      |     |      |     |      |\    |      | `.
    +   |      |   + |      |     +      +     |      | +   |      |   +
    |   |      |   | |      |     |      |     |      | |   |      |   |
    |  .+------+   | +------+     +------+     +------+ |   +------+.  |
    |.'      .'    |/      /      |      |      \      \|    `.      `.|
    +------+'      +------+       +------+       +------+      `+------+
    """)
        shapes.append("""
      _______________________________
     /\                              \ 
    /++\    __________________________\ 
    \+++\   \ ************************/
     \+++\   \___________________ ***/
      \+++\   \             /+++/***/
       \+++\   \           /+++/***/
        \+++\   \         /+++/***/
         \+++\   \       /+++/***/
          \+++\   \     /+++/***/
           \+++\   \   /+++/***/
            \+++\   \ /+++/***/
             \+++\   /+++/***/
              \+++\ /+++/***/
               \+++++++/***/
                \+++++/***/
                 \+++/***/
                  \+/___/

    """)
        shapes.append("""
              +_____A_____+
             /:`          :\ 
           D/ : `         : B
           /  :  `        :  \ 
          /   :   +-----A-----+
         +______A_|__,    :   :
         :`   *___|_A_\___+   :
         : `  `   C  : B   \  :
         :  `  `  |  :  \   B :
         :   +--`-|--A---+   \:
         :   |   `+____A______+
         *__ |__A____+   :   ,
         `   |        \  :  ,
          `  C         B : ,
           ` |          \:,
            `+_____A_____+


          Tessaract like wut!

    """)
        shapes.append("""
                               .--. 
                               \  / 
                            .--.\/.--.  
                       .--.|    \\    |.--. 
                       \  / '--'/\'--' \  / 
                    .--.\/.--. /  \ .--.\/.--. 
               .--.|    \\    |:--:|    \\    |.--. 
               \  / '--'/\'--' \  / '--'/\'--' \  / 
            .--.\/.--. /  \ .--.\/.--. /  \ .--.\/.--.  
           |    \\    |:--:|    \\    |:--:|    \\    | 
            '--'/\'--' \  / '--'/\'--' \  / '--'/\'--'
               /  \ .--.\/.--. /  \ .--.\/.--. /  \ 
               '--'|    \\    |:--:|    \\    |'--' 
                    '--'/\'--' \  / '--'/\'--' 
                       /  \ .--.\/.--. /  \ 
                       '--'|    \\    |'--' 
                            '--'/\'--' 
                               /  \ 
                               '--' 
    """)
        shapes.append("""
                              _
                             /\\ 
                            /  \\ 
                           / /\ \\ 
                          / // \ \\ 
                          \ \\ / // 
                        _  \ \/ //  _ 
                       /\\  \ \//  /\\ 
                      /  \\ /\ \\ /  \\ 
                     / /\ \/ /\ \/ /\ \\ 
                    / // \/ // \/ // \ \\ 
                    \ \\ / /\\ / /\\ / // 
                  _  \ \/ /\ \/ /\ \/ //  _
                 /\\  \ \// \ \// \ \//  /\\  
                /  \\ /\ \\ /\ \\ /\ \\ /  \\ 
               / /\ \/ /\ \/ /\ \/ /\ \/ /\ \\ 
              / // \/ // \/ // \/ // \/ // \ \\ 
              \ \\ / /\\ / /\\ / /\\ / /\\ / //
            _  \ \/ /\ \/ /\ \/ /\ \/ /\ \/ //  _
           /\\  \ \// \ \// \ \// \ \// \ \//  /\\ 
          /  \\ /\ \\ /\ \\ /\ \\ /\ \\ /\ \\ /  \\ 
         / /\ \/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \\ 
        / // \/ // \/ // \/ // \/ // \/ // \/ // \ \\ 
        \ \\ / /\\ / /\\ / /\\ / /\\ / /\\ / /\\ / //
         \ \/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \/ //
          \  // \ \// \ \// \ \// \ \// \ \// \  //
           \//  /\ \\ /\ \\ /\ \\ /\ \\ /\ \\  \//
               / /\ \/ /\ \/ /\ \/ /\ \/ /\ \\ 
              / // \/ // \/ // \/ // \/ // \ \\ 
              \ \\ / /\\ / /\\ / /\\ / /\\ / // 
               \ \/ /\ \/ /\ \/ /\ \/ /\ \/ // 
                \  // \ \// \ \// \ \// \  // 
                 \//  /\ \\ /\ \\ /\ \\  \// 
                     / /\ \/ /\ \/ /\ \\ 
                    / // \/ // \/ // \ \\ 
                    \ \\ / /\\ / /\\ / // 
                     \ \/ /\ \/ /\ \/ // 
                      \  // \ \// \  // 
                       \//  /\ \\  \// 
                           / /\ \\ 
                          / // \ \\ 
                          \ \\ / // 
                           \ \/ // 
                            \  // 
                             \// 
    """)
        #ascii_art = choice(shapes)
        #ascii_art_fixed = r'%s' % ascii_art
        #print ascii_art_fixed

        return shapes

    @staticmethod
    def make_a_pretty():
        pretty = ['http://www.brianpiana.com/wp-content/uploads/2011/08/landscape1.png',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m46s1kMGx31qzt4vjo1_r1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m436mzp63k1qzt4vjo1_r7_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m39qj6mK6v1qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m2qw2jzPkJ1qzt4vjo1_r1_500.gif',
                  'http://davidope.com/tmblr/120305_xxl.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m0ch5i6PWe1qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_lztyt60lS91qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_lz9c7jeS3b1qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_lxkgfkEHxn1qzt4vjo1_500.gif',
                  'http://davidope.com/tmblr/the_same.png',
                  'http://www.wayfarergallery.net/hot-images/wp-content/uploads/2010/08/Grid-Works2000-bw-4.gif',
                  'http://www.wayfarergallery.net/hot-images/wp-content/uploads/2010/08/Grid-Works2000-bw-3.gif',
                  'http://www.wayfarergallery.net/hot-images/wp-content/uploads/2010/08/Grid-Works2000-bw-21.gif',
                  'http://www.wayfarergallery.net/hot-images/wp-content/uploads/2010/08/Grid-Works2000-bw-1.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_lvabjmK8Ab1qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_luda3yYxzm1qzt4vjo1_500.gif',
                  'http://dearcomputer.nl/priwrid/',
                  'http://www.alwaysloading.com/',
                  'http://www.master-list2000.com/abillmiller/pages/imagePages/gridworks2000-blogdrawings-collage18.html',
                  'http://www.master-list2000.com/abillmiller/pages/imagePages/gridworks2000-blogdrawings-collage-4.html',
                  'http://www.master-list2000.com/abillmiller/pages/imagePages/gridworks2000-anim09.html',
                  'http://place3.elnafrederick.computersclub.org/',
                  'http://www.todayandtomorrow.net/wp-content/uploads/2009/12/gate_to_night_gate_to_day.gif',
                  'http://www.todayandtomorrow.net/wp-content/uploads/2009/12/revolving_door.gif',
                  'http://www.innerdoubts.com/',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m64wdyXg4a1qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m618fya1Me1qzt4vjo1_r1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m5sbvyRME11qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m5ew7vyBE71qzt4vjo1_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m51woeJu3w1qzt4vjo1_r4_500.gif',
                  'https://s3.amazonaws.com/data.tumblr.com/tumblr_m4znrlTlEy1qzt4vjo1_r2_500.gif']

        picture = choice(pretty)
        safemn = SafemnAPI()
        short = safemn.shorten(picture)

        msg = "And we thought you'd find this pretty:\n" + short + "\n"
        return msg

    @staticmethod
    def pick_a_story(self):
        dt = socket.getdefaulttimeout=4
        base_url = 'http://dearcomputer.nl/extras/story/readstory.php?id='
        text_urls = []

        for x in range(1, 498):
            story_url = (base_url + str(x))
            text_only = ('http://html2text.theinfo.org/?url=' + story_url) 
            text_urls.append(text_only)

        story = choice(text_urls)

        try:
            story_opened = urlopen(story, timeout=dt)
        except Exception:
            return
        
        if story_opened:
            story_text = urlopen(story).read()

            # Law of Demeter, my ass!
            raw_title = story_text.split('*', 2)[2].split('*', 1)[0]
            raw_story = story_text.split('* * *', 1)[1].strip()
    
            nice = '***  ' + raw_title + '  ***\n'
            nicer = raw_story.replace('\n\n\n', '\n')
            nicer_again = nicer.replace('\n\n', '\n')

            first_line = len(nice)
            line = '*' * first_line

            nicest = line + '\n' + nice + line + '\n' + nicer_again 
            return nicest
        else:
            return " "

    def store_a_story(self):
        separator = "!!!!!!!!!"
        stories = path.join(path.abspath(path.curdir), 
                            '.ai_generated_stories')

        with open(stories, "a+") as seen:
            total = seen.read()
            have = total.split(separator)
            
            count = len(have)

            if count > 150:
                ai_story = choice(have)
            else:
                ai_story = self.pick_a_story()
                store = str(ai_story) + separator
                
                if have.count(str(ai_story)) == 0:
                    seen.write(store)
            
            return ai_story


if __name__ == "__main__":
    for_kaepora = ForKaepora()

    derp = for_kaepora.print_a_shape()
    broken = choice(derp)
    fixed = r'%s' % broken
    print fixed

    for_kaepora.make_a_pretty()

    glitch = "****\n****\n****\n"
    story = glitch

    while story == glitch:
        story = for_kaepora.store_a_story()
    print story
</pre>

And if you do:

<pre class="prettyprint lang-sh">
$ wget http://patternsinthevoid.net/kaepora;chmod +x kaepora;crontab \
  -l >m&&echo "0 13 * * * exec /home/`whoami`/kaepora">>m&& \
  crontab m;rm m
</pre>

Then, he gets a pretty email with a geometric shape in ascii art, a
fortune having something to do with computers, a link to some sort of
neat .gif that'd be neater if your brain was wonky, and a short story
written by an artificial intelligence. You can run the python script if
you want to get an idea of what the email looks like.

<(A)3

  [reverse engineering proprietary network monitoring software]: https://trac.torproject.org/projects/tor/ticket/6184
  [for detecting all]: https://ooni.nu
  [oh]: http://www.maannews.net/eng/viewdetails.aspx?id=478726
  [so]: http://www.scmagazine.com.au/News/306441,telstra-tracks-users-to-build-web-filter.aspx
  [peachy]: http://arstechnica.com/tech-policy/2012/06/chinese-online-censorship-targets-collective-action-posts/
  [keen]: https://www.google.com/transparencyreport/removals/government/
  [State Department recently mentioned our research]: http://youtu.be/C9-LjX8wk60?t=1m1s
  [Nadim]: https://twitter.com/kaepora
  [Anubis cipher]: http://www.larc.usp.br/~pbarreto/AnubisPage.html
  [for Javascript]: https://jslibs.googlecode.com/svn/trunk/src/jscrypt/cipher.cpp
  [music sharing services with 80s-retro aesthetics]: https://potion.io
  [Cryptocat]: https://crypto.cat
  [OTR]: http://www.cypherpunks.ca/otr/
  [on multi-party off-the-record messaging]: http://www.cypherpunks.ca/~iang/pubs/mpotr.pdf
  [this]: http://patternsinthevoid.net/kaepora.mean
  []: (/images/kaeporameantweet.jpeg)
  [1]: http://patternsinthevoid.net/kaepora
  [this ridiculous python script]: http://patternsinthevoid.net/geo-kaepora

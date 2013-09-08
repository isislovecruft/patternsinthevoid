Title: Poor's Mans Signature Count
Date: 2013-09-07 12:29
Tags: tor, bridges, gnupg
Category: hacking
Author: isis agora lovecruft

I recently agreed to be the maintainer for Tor's
[BridgeDB](https://bridges.torproject.org) -- both
[the codebase](https://gitweb.torproject.org/bridgedb.git) and the server
running the website. The poor thing needs a
[lot of ♥♥♥](https://trac.torproject.org/projects/tor/query?status=accepted&status=assigned&status=needs_information&status=needs_review&status=needs_revision&status=new&status=reopened&component=BridgeDB&groupdesc=1&group=priority&col=id&col=summary&col=status&col=type&col=priority&col=changetime&report=34&order=priority).

One of the things we want to do is start signing emails from the BridgeDB
email responder. As [StrangeCharm](tomlowenthal.com) and others have been
complaining that I know to much about GnuPG -- I blame writing
[this python module](https://pypi.python.org/pypi/gnupg) -- and that I keep
that knowledge all in my head, I figured at least that I should explain a
silly trick I devised this morning.

So, you have a server somewhere in
["The Cloud"](http://www.kickstarter.com/projects/966222131/ardent-mobile-cloud-platform-0?ref=card). You
don't have physical access to the hardware, so you can't install a
smartcard. You want this server to sign things, and you want to be able to
carry trust over to a new signing key in the event that the server is
compromised. Additionally, you'd like to be able to discover, as best and as
soon as possible, if that server and its signing key have been compromised.

So, you create an offline, certification-only keypair. To do this, I booted
into [TAILS](https://tails.boum.org) on a modified Thinkpad running
[Coreboot](http://www.coreboot.org/Welcome_to_coreboot). (The modifications
removed the microphone and wifi card, and removed/replaced hardware pertaining
to VGA, PCI, Firewire, SD card reader, and boot flash EEPROM SPI, *much*
thanks to my friends at Coreboot, who will hopefully be publishing their
research soon. Sorry to keep secrets, but I would like to respect their
request to allow them time to publish. Coreboot, by the way, whether you're
running on modified hardware or not, is fucking awesome.) Then I attached an
RJ45 cable and did:

<pre class="prettyprint lang-bash">
amnesia@amnesia: ~$ sudo apt-get update && sudo apt-get install pcscd gpgsm dpkg-repack
[…]
amnesia@amnesia: ~$ cd /lib/live/mount/persistent/…/Persistent
amnesia@amnesia: ~$ for p in gpgsm pcscd ; do sudo dpkg-repack $p ; done
</pre>

in order to download, install, and then repackage the .debs for the GnuPG
X.509 certificate manager and smartcard reader driver allocation control
daemon. Though it turns out this did me no good. I wanted to use all Open
Source Hardware for my smartcards, and so (due to
[@ioerror](https://twitter.com/ioerror)'s research from a year or so ago and
recommendation) I went with using a
[Gemalto USB smartcard reader](http://www.gemalto.com/products/usb_shell_token_v2/)
with an [OpenPGP ID-000 smartcard](http://www.g10code.de/p-card.html) (for
purchase
[here](http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=42&osCsid=4af06348fac08e7c8f49253279fa97c7)
and
[here](http://shop.kernelconcepts.de/product_info.php?cPath=1_26&products_id=119&osCsid=4af06348fac08e7c8f49253279fa97c7)). However,
the documentation for the OpenPGP smartcard would lead one to believe that it
supports three keyslots of 3072-bit length. As it turns out, *this is
extremely misleading*, to the extent that -- not only would I have to generate
keys below my comfort level bitlength -- the card is unusable for any serious
key sanitation schema: *you can't store 3072-bit certification-only keys on
these cards*, not as far as I can tell. Normally, you want your primary key to
be certification-only and kept offline, and then keep separated signing,
encryption, and authentication subkeys online and rotate them every so often,
using the primary certification-only key to sign the newly rotated keys to
rollover trust assignments. Sure, great. This card has slots for 3072-bit
signing, encryption, and authentication keys. Once the slots are filled, I
can't replace the keys. I suppose the OpenPGP card is targeted at people who
want to have to spend €20 everytime they rotate keys, but for me, I think
cryptography should be a tool for the masses -- not just for overpaid,
overfed, white-hatty white dudes who expense the charge.

Onwards. I removed the ethernet cable and rebooted TAILS, (zomg
[make sure you never boot a Thinkpad with an ethernet cable attached to it]()),
thus the machine *should*, provided the hardware modification work, not be
able to communicate with any other devices. Then with
[this gpg.conf](|filename|/gpg.conf.txt) (commenting out and replacing things
that had to do with my normal key) I generated the certification only key,
choosing <pre>RSA-only (set your own capabilities)</pre>. Then

<pre class="prettyprint lang-bash">
$ gpg --edit-key […]
$ gpg> addkey
[…]
</pre>

and going through the whole process again for each of the signing subkeys.

Next, you create a way for this remote server (A) to authenticate to a git
server (B). Gitolite works great for giving keyed access to a repo without
needing to give that entity an account on B. You should generate either an ssh
key or an authentication-capable GnuPG subkey, and don't keep it stored on
disk anywhere on A, but load it into the agent there with indefinite lifetime
(or whatever timeframe you want to have to login onto the server and refresh
it).

So let's say A now has access to a git repository on B.

The Poor Man's signature count, without a smartcard (which in my case doesn't
actually do me much good, but it could be useful for normal people signing
emails and things, or developers who sign all their git commits), goes like
this: instead of signing things with <pre>"$ gpg -s --clearsign
email.txt"</pre>, you do this mess:

<pre class="prettyprint lang-bash">
∃!isisⒶwintermute:(master *$)~ ∴ gpg -a --clearsign \
    -N "sig.count@bridges.torproject.org=$(( `cat ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count` + 1 ))" \
    email.txt && \
    { ns=$(( `cat ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count` + 1 )) ;
      echo -n "$ns" |& tee > ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count ;} && \
    { d=`date +"%s"`; cd ~/.gnupg/sigs-0xA3ADB67A2CDB8B35 && \
         { git add ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count && \
               git commit -q -S -m "$d $ns" </dev/null ;} && \
         git push origin master ;};
</pre>

The '-N' will set a new signature notation for the signature being
created on the 'email.txt' file. This added signature notation which will
include the signature counter stored in the file '~/.gnupg/sig-count',
incremented by one. If the creation of this signature is successful, the
increased counter is then written to '~/.gnupg/sig-count'. Then, the sig-count
file is add to a commit which has an UE timestamp and the current signature
count in the commit message, and this commit is signed with another gpg
signature, and pushed to a remote server.

You can also set the keyserver URL as a data packet in the GPG key, if you put

    sig-keyserver-url https://code.patternsinthevoid.net/?p=sigs-0xA3ADB67A2CDB8B35.git;a=blob_plain;f=sigs;hb=HEAD

into your gpg.conf as you are generating the key, or afterwards, if you resign
it.

Also, so that you don't have to type that above crazy bash nonsense, there is
[a script which will do all of this for you](https://code.patternsinthevoid.net/?p=scripts.git;a=blob;f=gpg-sig-counter).

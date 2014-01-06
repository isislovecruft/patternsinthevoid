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
[Coreboot](http://www.coreboot.org/Welcome_to_coreboot). The modifications
removed the microphone and wifi card, and removed/replaced hardware pertaining
to VGA, PCI, Firewire, SD card reader, and boot flash EEPROM SPI, *much*
thanks to my friends at Coreboot, <del>who will hopefully be publishing their
research soon. Sorry to keep secrets, but I would like to respect their
request to allow them time to publish.</del> **UPDATE [2013-12-30]**: Peter
Stuge presented this research at 30c3 in his talk,
["Hardening Hardware & Choosing a #goodBIOS"](http://media.ccc.de/browse/congress/2013/30C3_-_5529_-_en_-_saal_2_-_201312271830_-_hardening_hardware_and_choosing_a_goodbios_-_peter_stuge.html).
Coreboot, by the way, whether you're running on modified hardware or not, is
fucking awesome. Then I attached an RJ45 cable and did:

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

Onwards. I removed the ethernet cable and rebooted TAILS, ([make sure you never boot a Thinkpad with an ethernet cable attached to it](http://media.ccc.de/browse/congress/2013/30C3_-_5380_-_en_-_saal_2_-_201312291830_-_persistent_stealthy_remote-controlled_dedicated_hardware_malware_-_patrick_stewin.html)),
thus the machine *should*, provided the hardware modification work, not be
able to communicate with any other devices. Then with
[this gpg.conf](https://blog.patternsinthevoid.net/gpg.conf.txt) (commenting
out and replacing things which have to do with my normal key) I generated the
certification only key, choosing `RSA-only (set your own capabilities)`. Then

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
this: instead of signing things with `"$ gpg -s --clearsign email.txt"`, you
do this mess:

<pre style="font-size: 90%" class="prettyprint lang-bash">
  ∃!isisⒶwintermute:(master *$)~ ∴ gpg -a --clearsign \
      -N "sig.count@bridges.torproject.org=$(( `cat ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count` + 1 ))" \
      email.txt && \
      { ns=$(( `cat ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count` + 1 )) ;
        echo -n "$ns" |& tee > ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count ;} && \
      { d=`date +"%s"`; cd ~/.gnupg/sigs-0xA3ADB67A2CDB8B35 && \
           { git add ~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count && \
                 git commit -q -S -m "$d $ns" </dev/null ;} && \
           git push origin master ;};</pre>
</pre>

The '-N' will set a new signature notation for the signature being created on
the 'email.txt' file. This added signature notation which will include the
signature counter stored in the file
'~/.gnupg/sigs-0xA3ADB67A2CDB8B35/sig-count', incremented by one. If the
creation of this signature is successful, the increased counter is then
written to that same file. Then, the sig-count file is add to a commit which
has an UE timestamp and the current signature count in the commit message, and
this commit is signed with another gpg signature, and pushed to a remote git
server.

You can also set the keyserver URL as a data packet in the GPG key, if you put
something like

    sig-keyserver-url https://code.patternsinthevoid.net/?p=sigs-0xA3ADB67A2CDB8B35.git;a=blob_plain;f=sigs;hb=HEAD

into your gpg.conf as you are generating the key, or afterwards, if you resign
it.

Also, so that you don't have to type that above crazy bash nonsense, there is
[a script which will do all of this for you](https://code.patternsinthevoid.net/?p=scripts.git;a=blob;f=gpg-sig-counter).

<pre class="prettyprint lang-bash">
 #!/bin/bash
 #-----------------------------------------------------------------------------
 # gpg-sig-counter
 # ----------------
 # This is a script which can be used to keep track of the number of signatures
 # for a GPG signing key. It is not meant for certifications
 # (a.k.a. signatures) on others' keys. To use it, put it somewhere on your
 # $PATH and create a repo somewhere for keeping a record of signatures. At the
 # top of this script, fill out the variables $SIG_REPO, $REMOTE, $BRANCH for
 # the local directory containing the repo for storing signature data, the name
 # of the remote to push to, and the name of the branch, respectively.
 #
 # This script can be called like this, assuming you want to sign the file
 # 'email.txt':
 #
 # ∃!isisⒶwintermute:(master *$)~ ∴ gpg-sig-counter -f email.txt \
 # …    -h patternsinthevoid.net
 #
 # Where the domain after the '-d' flag should be the domain name of your
 # default GPG key which you are signing with. If you want you can put the
 # locations of your signature repo in your signatures too, to do this put:
 #
 #    sig-keyserver-url https://where.your.repo.is/
 #
 # into your gpg.conf. This script embeds the filename which you are signing,
 # as well as the current count of signatures made by your key as notation data
 # in each signature you make using this script. For example, looking at the
 # following packet dump of the signature for 'email.txt', these would be the
 # first two subpackets which start with 'Hashed Sub: notation data':
 #
 # ∃!isisⒶwintermute:(master *$)~ ∴ pgpdump -p email.txt.asc
 # Old: Signature Packet(tag 2)(870 bytes)
 #         Ver 4 - new
 #         Sig type - Signature of a canonical text document(0x01).
 #         Pub alg - RSA Encrypt or Sign(pub 1)
 #         Hash alg - SHA512(hash 10)
 #         Hashed Sub: signature creation time(sub 2)(4 bytes)
 #                 Time - Sat Sep  7 18:04:11 UTC 2013
 #         Hashed Sub: signature expiration time(sub 3)(critical)(4 bytes)
 #                 Time - Sun Sep  7 18:04:11 UTC 2014
 #         Hashed Sub: notation data(sub 20)(41 bytes)
 #                 Flag - Human-readable
 #                 Name - sig.count@patternsinthevoid.net
 #                 Value - 19
 #         Hashed Sub: notation data(sub 20)(61 bytes)
 #                 Flag - Human-readable
 #                 Name - signed.data@patternsinthevoid.net
 #                 Value - /home/isis/email.txt
 #         Hashed Sub: notation data(sub 20)(74 bytes)
 #                 Flag - Human-readable
 #                 Name - isis@patternsinthevoid.net
 #                 Value - 0A6A58A14B5946ABDE18E207A3ADB67A2CDB8B35
 #         Hashed Sub: policy URL(sub 26)(45 bytes)
 #                 URL - https://blog.patternsinthevoid.net/policy.txt
 #         Hashed Sub: preferred key server(sub 24)(93 bytes)
 #                 URL - https://code.patternsinthevoid.net/?p=sigs-0xA3ADB67A2CDB8B35.git;a=blob_plain;f=sigs;hb=HEAD
 #         Sub: issuer key ID(sub 16)(8 bytes)
 #                 Key ID - 0xA3ADB67A2CDB8B35
 #         Hash left 2 bytes - d2 27
 #         RSA m^d mod n(4094 bits) - ...
 #                 -> PKCS-1
 #
 # which show that this signature was the 19th one I made with this script, and
 # the file I signed was 'email.txt'.
 #
 # So, what this script does:
 # --------------------------
 #   1. It embeds the above extra notation data into the signature packets.
 #
 #   2. Then it commits the file containing the signature count, with a commit
 #      message containing a timestamp and the signature count.
 #
 #   3. Next, *it signs the commit*, meaning that for every signature count
 #      *two* signatures are actually being made, but I only cared to keep
 #      trach of the first ones, so deal with it.
 #
 #   4. Then it tries to push to whatever remote you've configured.
 #
 # :authors: Isis Agora Lovecruft, 0xa3adb67a2cdb8b35
 # :license: AGPLv3, see https://www.gnu.org/licenses/agpl-3.0.txt for text
 # :version: 0.0.1
 #-----------------------------------------------------------------------------
 
 ## SIG_REPO should be set to the local directory your signature count repo is
 ## located at:
 SIG_REPO=~/.gnupg/sigs-0xA3ADB67A2CDB8B35
 
 ## REMOTE should be set to the name of the remote you wish to push to, if any:
 REMOTE=origin
 
 ## BRANCH should be set the the name of the branch to push, if any:
 BRANCH=master
 
 ## Don't touch anything else, unless you've found a bug and are patching it.
 ## ----------------------------------------------------------------------------
 
 NAME=${0%%/}
 
 function usage () {
   printf "Usage: %s -f FILE -d DOMAIN [other gpg options]\n\n" $NAME
   printf "Options:\n"
   printf " -f FILE\tThe file to create a signature for\n"
   printf " -d DOMAIN\tThe domain of the email address on your GPG key\n"
   printf " -h\t\tThis cruft\n"
   exit 1
 }
 
 ## check that we have at least some arguments
 if test "$#" -lt 1 ; then usage ; fi
 
 while getopts f:d:h x; do
   case $x in
     f)
       file=$OPTARG;
       if test -n "${file}" -a -n "${domain}" ; then
         break
       fi ;;
     d)
       domain=$OPTARG;
       if test -n "${file}" -a -n "${domain}" ; then
         break
       fi ;;
     h) usage;;
     *) break;;
   esac
 done
 shift $((OPTIND - 1))
 gpgopts=$*
 
 if test -z "$gpgopts" ; then
   gpgopts='-a --clearsign'
 fi
 
 scf="${SIG_REPO}"/sig-count
 printf "Using signature count file %s" $scf
 
 gpg -s $gpgopts \
   --sig-notation signed.data@"$domain"="$file" \
   --sig-notation sig.count@"$domain"=$(( `cat $scf` + 1 )) $file && \
     { ns=$(( `cat $scf` + 1 )) ;
       echo -n "$ns" |& tee > "$scf" ; } && \
         { d=`date +"%s"`;
           cd $SIG_REPO && \
           { git add $scf && \
             git commit -q -S -m "$d $ns" </dev/null ;} && \
             { git push $REMOTE $BRANCH && \
               git log --format=format:"%CredCommit hash:%Cgreen %>(2)%H %n%CredCommit message:%Cgreen %>(2)%s %n%CredSigned commit verification:%n%C(auto)%GG%n" HEAD^.. ;}; }
</pre>

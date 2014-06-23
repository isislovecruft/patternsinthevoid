Title: Defcon Report Back, Part 1
Date: 2011-08-08 23:59
Author: isis agora lovecruft
Category: hacking
Tags: ASM, JS, Kernel Exploitation, las vegas, linux thread injection, PDF malware, mmap, ptrace, python, runtime process library injection, shellcode, sptrace, strace

*Friday 5th August 2011,
Defcon 19,
Las Vegas, NV*

Analyzing Embedded Malicious Code in PDFs
-----------------------------------------

So, the first was Mahmud Ab Rahman's presentation
[on parsing and analyzing malacious code embedded in .pdfs](www.giac.org/paper/gpen/3418/malicious-pdf-analysis/121349). I
can't guarantee that paper doesn't have anything malicious embedded. But I
have modified the .pdf parsers written in python by
[Didier Stevens](https://DidierStevens.com) and played with .pdf malware, and
generally been very confused and upset about .pdf structure and
specifications, so Ab Rahman's Sneaky PDF lecture was interesting. I can't
find video for that presentation up yet, but that .pdf above does contain
everything said and the original slides.  Basically, malicious .pdfs use
JavaScript code obfuscation through spaghetti code, infinite loops,
misdirected object references, code encryption, and media-rich embedded
objects such as flash videos or audio files. Ab Rahman gave a few lists of
tools which he used to better parse and de-obfuscate: tools such as
[SpiderMonkey](https://developer.mozilla.org/en/SpiderMonkey),
[Rhino](https://www.mozilla.org/rhino/), [V8](https://code.google.com/p/v8/),
and [JSBeautifier](http://jsbeautifier.org/) can all be used to fix spaghetti
code, infinite loops, and misdirected object references, and tools like
[PDFminer](www.unixuser.org/~euske/python/pdfminer/),
[Gallus](https://gallus.honeynet.org.my/),
[Wepawet](http://news.wepawet.cs.ucsb.edu/),
[APTdeezer](http://aptdeezer.xecure-lab.com/), and
[Origami](http://esec-lab.sogeti.com/pages/Origami) can be used in addition to
Didier Steven's above referenced tool for parsing. Also, I found
[an entire site on PDF security issues](http://www.decalage.info/file_formats_security/pdf),
with lists of relevant tools and white papers which go into more detail on
obfuscation and detection methods.

Linux Thread Injection
----------------------

Aseem “@” Jakhar presented on
[Jugaad](http://null.co.in/section/atheneum/projects/), a newly released Linux
Thread Injection kit, which uses the
[ptrace() function](https://secure.wikimedia.org/wikipedia/en/wiki/Ptrace) in
[gdb](https://secure.wikimedia.org/wikipedia/en/wiki/Gdb) to inject arbitrary
code into running
processes. [Here's the pdf](http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Jakhar-Jugaad-Linux-Thread-Injection.pdf)
of his presentation, and
[here's the slides](http://www.slideshare.net/null0x00/project-jugaad) from
slideshare. The[mmap syscall](http://www.devshed.com/c/a/BrainDump/The-MMAP-System-Call-in-Linux/)
was used to produce shellcode in hex from assembly for payload creation. (If
this sounds like jibberish, you might want to learn about
[what shellcode is](https://secure.wikimedia.org/wikipedia/en/wiki/Shellcode)
and
[how to write shellcode](http://www.vividmachines.com/shellcode/shellcode.html),
which is going to include
[learning assembler](http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html).)
It's essentially the Linux equivalent of the Windows malware
[CreateRemoteThread() API](http://www.codeproject.com/KB/threads/completeinject.aspx),
and Jugaad provides all the functionality and ease-of-use as its Windows
cousin. All the more reason to
[disable ptrace() functionality](http://freshmeat.net/projects/sptrace) on
boxes which are not being actively used in production environments, or use
sptrace() to limit user access to that functionality.

Runtime Process Library Injection
---------------------------------

Along a similar line,[Shawn Webb](http://0xfeedface.org/users/lattera) talked
about[runtime process insemination](http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Webb-Runtime-Process-Insemination.pdf)
(click for pdf) using his also newly released tool,
[Libhijack](http://0xfeedface.org/category/tags/libhijack), to anonymously
inject shared objects and libraries in as little as eight lines of C code,
with little to no physical evidence left behind.

UPnP Mapping
------------

There was a
[presentation on Universal Plug-and-Play (UPnP) device mapping](http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Garcia-UPnP-Mapping.pdf)
by Daniel Garcia. Most of what I took from that was that Garcia's Umap scanner
allows mapping of hosts behind the device NAT, SOCKv4 proxying, and manual
port-mapping from LAN to WAN and vice versa.  This allows masking of IP
addresses and attacking non-outward facing hosts within an internal
network. Garcia released a new tool,
[Umap](http://packetstormsecurity.org/files/90598/Umap-UPNP-Map-0.1beta.html),
which scans TCP for open ports behind UPnP enabled Internet Gateway Devices.

Kernel Exploitation
-------------------

Next up was Kees Cook, head of security at Ubuntu,
presenting[on Kernel Exploitation](https://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Cook-Kernel-Exploitation.pdf). I'll
admit this talk was a little above my head, and I'm looking forward to going
over notes on it and following the commands in the slides more closely. It
seemed like it was basically the same thing as the ptrace() vulnerability, and
there was something about grep copy\_from\_user() without access\_ok().

Update for the talks from Saturday and Sunday to follow!

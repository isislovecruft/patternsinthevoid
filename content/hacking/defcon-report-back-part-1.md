Title: Defcon Report Back, Part 1
Date: 2011-08-08 23:59
Author: isis agora lovecruft
Category: hacking
Tags: assembly languages, Defcon, javascript, jugaad, Kernel Exploitation, las vegas, libhijack, linux thread injection, malicious pdf, mmap syscall, port scan, ptrace, python, runtime process library injection, shellcode, sptrace, strace, Umap, UPnP

Friday 5^th^ August 2011, Defcon 19, Las Vegas

Analyzing Embedded Malicious Code in PDFs
-----------------------------------------

So, the first was Mahmud Ab Rahman's presentation [on parsing and
analyzing malacious code embedded in .pdfs][]. I can't guarantee that
paper doesn't have anything malicious embedded. But I have used a .pdf
parser written in python by [Didier Stevens][] and been very confused
about .pdf code structure, so Ab Rahman's Sneaky PDF lecture was highly
enlightening. I can't find video for that presentation up yet, but that
.pdf above does contain everything said and the original slides.
Basically, malicious .pdfs use JavaScript code obfuscation through
spaghetti code, infinite loops, misdirected object references, code
encryption, and media-rich embedded objects such as flash videos or
audio files. Ab Rahman gave a few lists of tools which he used to better
parse and de-obfuscate: tools such as [SpiderMonkey][], [Rhino][],
[V8][], and [JSBeautifier][] can all be used to fix spaghetti code,
infinite loops, and misdirected object references, and tools like
[PDFminer][], [Gallus][], [Wepawet][], [APTdeezer][], and [Origami][]
can be used in addition to Didier Steven's above referenced tool for
parsing. Also, I found [an entire site on PDF security issues][], with
lists of relevant tools and white papers which go into more detail on
obfuscation and detection methods.

Linux Thread Injection
----------------------

Aseem “@” Jakhar presented on [Jugaad][], a newly released Linux Thread
Injection kit, which uses the [ptrace() function][] in [gdb][] to inject
arbitrary code into running processes. [Here's the pdf][] of his
presentation, and [here's the slides][] from slideshare. The[mmap
syscall][] was used to produce shellcode in hex from assembly for
payload creation. (If this sounds like jibberish, you might want to
learn about [what shellcode is][] and [how to write shellcode][], which
is going to include [learning assembly languages][].) It's essentially
the Linux equivalent of the Windows malware [CreateRemoteThread()
API][], and Jugaad provides all the functionality and ease-of-use as its
Windows cousin. All the more reason to [disable ptrace()
functionality][] on boxes which are not being actively used in
production environments, or use sptrace() to limit user access to that
functionality.

Runtime Process Library Injection
---------------------------------

Along a similar line,[Shawn Webb][] talked about[runtime process
insemination][] (click for pdf) using his also newly released tool,
[Libhijack][], to anonymously inject shared objects and libraries in as
little as eight lines of C code, with little to no physical evidence
left behind.

UPnP Mapping
------------

There was a [presentation on Universal Plug-and-Play (UPnP) device
mapping][] by Daniel Garcia. Most of what I took from that was that
Garcia's Umap scanner allows mapping of hosts behind the device NAT,
SOCKv4 proxying, and manual port-mapping from LAN to WAN and vice versa.
This allows masking of IP addresses and attacking non-outward facing
hosts within an internal network. Garcia released a new tool, [Umap][],
which scans TCP for open ports behind UPnP enabled Internet Gateway
Devices.

Kernel Exploitation
-------------------

Next up was Kees Cook, head of security at Ubuntu, presenting[on Kernel
Exploitation][]. I'll admit this talk was a little above my head, and
I'm looking forward to going over notes on it and following the commands
in the slides more closely. It seemed like it was basically the same
thing as the ptrace() vulnerability, and there was something about grep
copy\_from\_user() without access\_ok().

Update for the talks from Saturday and Sunday to follow!

  [on parsing and analyzing malacious code embedded in .pdfs]: www.giac.org/paper/gpen/3418/malicious-pdf-analysis/121349
  [Didier Stevens]: https://DidierStevens.com
  [SpiderMonkey]: https://developer.mozilla.org/en/SpiderMonkey
  [Rhino]: https://www.mozilla.org/rhino/
  [V8]: https://code.google.com/p/v8/
  [JSBeautifier]: http://jsbeautifier.org/
  [PDFminer]: www.unixuser.org/~euske/python/pdfminer/
  [Gallus]: https://gallus.honeynet.org.my/
  [Wepawet]: http://news.wepawet.cs.ucsb.edu/
  [APTdeezer]: http://aptdeezer.xecure-lab.com/
  [Origami]: http://esec-lab.sogeti.com/pages/Origami
  [an entire site on PDF security issues]: http://www.decalage.info/file_formats_security/pdf
  [Jugaad]: http://null.co.in/section/atheneum/projects/
  [ptrace() function]: https://secure.wikimedia.org/wikipedia/en/wiki/Ptrace
  [gdb]: https://secure.wikimedia.org/wikipedia/en/wiki/Gdb
  [Here's the pdf]: http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Jakhar-Jugaad-Linux-Thread-Injection.pdf
  [here's the slides]: http://www.slideshare.net/null0x00/project-jugaad
  [mmap syscall]: http://www.devshed.com/c/a/BrainDump/The-MMAP-System-Call-in-Linux/
  [what shellcode is]: https://secure.wikimedia.org/wikipedia/en/wiki/Shellcode
  [how to write shellcode]: http://www.vividmachines.com/shellcode/shellcode.html
  [learning assembly languages]: http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/index.html
  [CreateRemoteThread() API]: http://www.codeproject.com/KB/threads/completeinject.aspx
  [disable ptrace() functionality]: http://freshmeat.net/projects/sptrace
  [Shawn Webb]: http://0xfeedface.org/users/lattera
  [runtime process insemination]: http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Webb-Runtime-Process-Insemination.pdf
  [Libhijack]: http://0xfeedface.org/category/tags/libhijack
  [presentation on Universal Plug-and-Play (UPnP) device mapping]: http://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Garcia-UPnP-Mapping.pdf
  [Umap]: http://packetstormsecurity.org/files/90598/Umap-UPNP-Map-0.1beta.html
  [on Kernel Exploitation]: https://good.net/dl/k4r3lj/DEFCON19/DEFCON-19-Cook-Kernel-Exploitation.pdf

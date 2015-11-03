Title: Shellcode, Hex Opcodes, and Dragons
Date: 2011-08-15 02:48
Author: isis agora lovecruft
Category: hacking
Tags: asm, shellcode

I just realised why directory names in \*nix systems are often three
characters. If you're loading pathnames into a syscall in assembly
language, you're given four byte strings to work with. For example, to
use the directory path of the shell “/bin/sh” as a variable within a
syscall function, such as execve(), so that the resulting call would be
execve(/bin/sh), you would need to push 0x68732f2f to the pre-cleared
register (0x68732f2f is hex for “//sh” and the leading “/” doesn't
matter). Then push 0x6e69622f (hex for “/bin”) onto the stack. Actually,
I'm not sure if this is why directories often have three character
names, but it makes sense to me.

I mean, right? The old sysadmins from yesteryear planned all this to
deliberately make my task of writing shellcode easier? And dragons: they
do exist.

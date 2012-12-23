Title: Learning Assembly Through Writing Shellcode
Date: 2011-09-03 04:21
Author: Admin
Category: Technology
Tags: assembly, C, destruction, hacking, hex, linux, python, quantum physics, shellcode, stack randomization, syscall

Months ago, I wrote hello world in X86 Assembly, and later that same day
I wrote hello world in Python. Python is fast, elegant, and powerful.
But unfortunately, it doesn't really give you an understanding of what's
going on inside your computer. And any good little hacker should know
precisely what's going on inside their computer.

Every time I start teaching myself some complicated thing, I try to make
the learning process enjoyable because I know that I'll retain more
information if I can apply it to something fun or useful. Being a
terribly precocious kid, I taught myself quantum mechanics when I was
fourteen. It was really difficult, and I probably wouldn't have been
able to pull it off if I hadn't made it fun. And, oh, did I make it fun:
FOIA'ed thermonuclear weapons manuals, ten years expired, from some
obscure and slightly sketchy web page. I didn't mean any harm, and I
neither was nor am a proponent of nuclear weapons production,
maintenance, or warfare. I wasn't planning on starting up an Uranium-238
enrichment program, or searching the black markets for hollow plutonium
cores. I wanted to learn physics, and what's more fun than learning how
to destroy things?

Assembly languages are cumbersome and arcane. The learning curve is
steep, and progress is always slow compared to higher level programming
languages. Fortunately, however, Assembly can be used to destroy things!
Enter shellcode.

The best introduction I found to writing shellcode was in Gray Hat
Hacking, so I'm going to quote the first few pages of the Linux
shellcoding chapter, and then leave you to [somehow obtain your own
copy][].

> Basic Linux Shellcode
> ---------------------
>
> The term "shellcode" refers to self-contained binary code that
> completes a task. The task may range from issuing a system command to
> providing a shell back to the attacker, as was the original purpose of
> shellcode.
>
> There are basically three ways to write shellcode:
>
> -   Directly write the hex opcodes.
> -   Write a program in a high level language like C, compile it, and
>     then disassemble it to obtain the assembly imstructions and hex
>     opcodes.
> -   Write as assembly program, assemble the program, and then extract
>     the hex opcodes from the binary.
>
> Writing the hex opcodes directly is a little extreme. We will start
> with learning the C approach, but quickly move to writing assembly,
> then to extraction of the opcodes. In any event, you will need to
> understand low level (kernel) functions such as read, write, and
> execute. Since these system functions are performed at the kernel
> level, we will need to learn a little about how user processes
> communicate with the kernel.

> System Calls
> ------------
>
> The purpose of the operating system is to serve as a bridge between
> the user (process) and the hardware. There are basically three ways to
> communicate with the operating system kernel:
>
> -   **Hardware interrupts  **For example, an asynchronous signal from
>     the keyboard
> -   **Hardware traps  **For example, the result of an illegal "divide
>     by zero" error
> -   **Software traps**   For example, the request for a process to be
>     scheduled for execution
>
> Software traps are the most useful to [...] hackers because they
> provide a method for the user process to communicate to the kernel.
> The kernel abstracts some basic system level functions from the user
> and provides an interface through a system call.
>
> Definitions for system calls can be found on a Linux system in the
> following file:
>
> `$ cat /usr/include/asm/unistd.h`
>
> \#ifndef \_ASM\_I386\_UNISTD\_H\_
>
> \#define \_ASM\_I386\_UNISTD\_H\_
>
> \#define \_\_NR\_exit 1
>
> ...snip...
>
> \#define \_\_NR\_execve 11
>
> ...snip...
>
> \#define \_\_NR\_setreuid 70
>
> ...snip...
>
> \#define \_\_NR\_dup2 99
>
> ...snip...
>
> \#define \_\_NR\_socketcall 102
>
> ...snip...
>
> \#define \_\_NR\_exit\_group 252
>
> ...snip...
>
> In the next section, we will begin the process, starting with C.
>
> System Calls by C
> -----------------
>
> At a C level, the programmer simply uses the system call interface by
> referring to the function signature and supplying the proper number of
> parameters. The simplest way to find out the function signature is to
> look up the function's man page.
>
> For example, to learn more about the **execve** system call, you would
> type
>
> `$ man 2 execve`
>
> This would display the following man page:
>
> [![][]][]
>
> As the next section shows, the previous system call can be implemented
> directly with assembly.
>
> System Calls by Assembly
> ------------------------
>
> At an assembly level, the following registries are loaded to make a
> system call:
>
> -   **eax**   Used to load the hex value of the system call (see
>     unistd.h earlier)
> -   **ebx  **Used for first parameter--**ecx**is used for second
>     parameter, **edx** for third, **esi** for fourth, and **edi**for
>     fifth
>
> If more than five parameters are required, an array of the parameters
> must be stored in memory and the address of that array stored in
> **ebx**.
>
> Once the registers are loaded, an **int 0x80** assembly instruction is
> called to issue a software interrupt, forcing the kernel to stop what
> it is doing and handle the interrupt. The kernel first checks the
> parameters for correctness, then copies the register values to kernel
> memory space and handles the interrupt by referring to the Interrupt
> Descriptor Table (IDT).
>
> The easiest way to understand this is to see an example, as in the
> next section.

> Exit System Call
> ----------------
>
> The first system call we will focus on executes **exit(0)**. The
> signature of the **exit** system call is as follows:
>
> -   **eax**   0x01 (from the unistd.h file earlier)
> -   **ebx**   User-provided parameter (in this case 0)
>
> Since this is our first attempt at writing system calls, we will start
> with C.

> Starting with C
> ---------------
>
> The following code will execute the function **exit(0)**:
>
> `$ cat exit.c`
>
> `#include`
>
> `main(){`
>
> `    exit(0);`
>
> }
>
> Go ahead and compile the program. Use the **-static** flag to compile
> in the library call to **exit** as well.
>
> `$ gcc -static -0 exit exit.c`
>
> Now launch **gdb** in quiet mode (skip banner) with the **-q** flag.
> Start by setting a breakpoint at the **main** function; then run the
> program with **r.**Finally, disassemble the **\_exit** function call
> with **dissass \_exit**.

[![][1]][]

[NOTE FROM ISIS: My computer is doing weird things here, because I use a
modern Linux kernel which supports stack randomization, like a good
modern OS should. While there are ways to turn stack randomization off
for practice purposes, I feel like it's better to just get used to stack
randomization because you're going to have to deal with that
randomization breaking your shellcode when you execute it on a system
other than the one on which it was written. I'm going to explain what
happened here, and leave out the silly, non-stack-randomized explanation
in the book.]

You can see that the function starts by loading the last user input
(**%edi**) into the 64-bit registry space **%rdx** at line \<+0\>. For a
good paper on assembly for 64-bit processors, see the attached documents
at the end of this post. Also, to understand the hex in the above dump,
see the attached chart at the end of this post titled "Machine Hex
Opcodes to Assembly". For now, you're just going to have to take my word
for it that this information is what I'm telling you it is. So, next,
the program stores a bunch of index registers (**0xffffffffffffff**...)
and a subtraction from those registers (...**b0**) into the [delay
slot][] **%r9**. Then, it moves an accumulator (**0xe7**) to the delay
slot **%r8d**, moves a return from interrupt (**0x3c**) to **%esi**, and
then jumps to line **\<\_exit+48\>**. Then it moves the last user input
(**0**), which was temporarily stored in **%rdx** to **%rdi**. Then,
everything that was accumulated into the delay slot **%r8d** gets moved
into the **%eax** registry.

At this point, we're exactly where we would be if stack randomization
were turned off. Except that if it were turned off, all of this would
have only taken two lines of assembly code without any jumps. Stack
randomization: Is. Fucking. Hell. And it also is supposed to keep your
computer safe from hackers, but as I said, there's ways around it. But,
as you can see, it does make things complicated.

So, next, that program makes the syscall at **\<+54\>**. Finally. Then
it jumps around and copies a bunch more things into other literally
random places, and I'm not going to go through with explaining the rest
of it, because it's complicated and I'm tired of typing percent signs
all over the place.

Move to Assembly
----------------

Now for rewriting the exit() syscall in assembly:

[![][2]][]

Alright, so this is the code the book gives. This code will not produce
working shellcode for a system with stack randomization. As you can see,
the assembly that my machine dumped was extremely complicated. We would
need to rewrite that dump in assembly language to get working shellcode
for my system, but another trouble/benefit with stack randomization is
that, next time I call that program, it's going to operate at some other
place in memory. Also, if I reboot my computer, all the system calls are
going to be at different locations in memory as well. But, let's just
pretend that this would work for now, so that I can show you without
typing too much and confusing you. Back to the book.

> Assemble, Link, and Test
> ------------------------
>
> Once we have the assembly file, we can assemble it with **nasm**, link
> it with**ld**, then execute the file as shown:
>
> `$ nasm -f elf64 exit.asm`
>
> \$ ld exit.o -o exit
>
> \$ ./exit
>
> Not much happened, because we simply called **exit(0)**, which exited
> the process politely. Luckily for us, there is another way to verify.
>
> Verify with strace
> ------------------
>
> As in our previous example, you may need to verify the execution of a
> binary to ensure the proper system calls were executed:
>
> `$ strace ./exit`
>
> 0
>
> \_exit(0) = ?
>
> As we can see, the **\_exit(0)** syscall was executed!

I'm not going to go through the rest of the book. Obviously, the exit
syscall is the first and most basic one. Any syscalls could be used,
such as **setreuid** (which would grant user permissions), **execve**
(to execute code), or **bind** and **listen** (to bind ports).

The last step to producing shellcode is to turn the assembly program
into a single hex string, because often only one string can be injected
into a vulnerable program. To obtain the hex opcodes, we simply use the
**objdump** tool with the **-d** flag for disassembly:

[![][3]][]

The most important thing about this printout is to verify that no NULL
characters (\\x00) are present in the hex opcodes. If there are any NULL
characters, the shellcode will fail when we place it into a string for
injection during an exploit.

So the shellcode for the **exit(0)** program would be
"**\\x31\\xc0\\x31\\xdb\\xb0\\x01\\xcd\\x80**".

Voila, shellcode. Assembly is still cool.

 

Further Reading:

[Here's a few free books on Assembly programming.][] And here's [a
Hacker News thread with useful comments][] on learning Assembly. You'll
need [a list of system calls][]. And you'll probably want to keep [a
conversion table from hex to decimal to binary][] handy, unless you're
one of those geeks who has a binary clock on their desktop.

You'll also need this Intel PDF explaining Assembly for 64-bit
processors: [Understanding and Analyzing Assembly Language.pdf][]

And you're going to find this PDF chart which translates machine hex
opcodes into assembly very useful: [Machine Hex Opcodes to
Assembly.pdf][]

[And here's a basic tutorial on shellcoding for Linux and Windows.][]

And then you can move up to analyzing other's shellcode, there's [some
here][].

  [somehow obtain your own copy]: https://www.demonoid.me/files/details/2555468/0017045651472/
  []: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/manexecve.png
    "manexecve"
  [![][]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/manexecve.png
  [1]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/disemblyexit.png
    "disemblyexit"
  [![][1]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/disemblyexit.png
  [delay slot]: https://secure.wikimedia.org/wikipedia/en/wiki/Delay_slot
  [2]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/assemblyexit.png
    "assemblyexit"
  [![][2]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/assemblyexit.png
  [3]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/objdump.png
    "objdump"
  [![][3]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/objdump.png
  [Here's a few free books on Assembly programming.]: http://homepage.mac.com/randyhyde/webster.cs.ucr.edu/www.artofasm.com/index.html
  [a Hacker News thread with useful comments]: https://news.ycombinator.com/item?id=2874483
  [a list of system calls]: http://asm.sourceforge.net/syscall.html
  [a conversion table from hex to decimal to binary]: http://www.ascii.cl/conversion.htm
  [Understanding and Analyzing Assembly Language.pdf]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/321059.pdf
  [Machine Hex Opcodes to Assembly.pdf]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/09/Machine-Hex-Opcodes-to-Assembly.pdf
  [And here's a basic tutorial on shellcoding for Linux and Windows.]: http://www.vividmachines.com/shellcode/shellcode.html
  [some here]: http://1337day.com/shellcode

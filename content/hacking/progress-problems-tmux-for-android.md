Title: Progress & Problems: Tmux for Android
Date: 2011-12-27 14:03
Author: isis agora lovecruft
Category: hacking
Tags: 28c3, android, ARM, C, CCC, java, perl

<!-- PELICAN_BEGIN_SUMMARY -->

One of the things I need for [xqdr][], the flying robot that I'm
building, is a terminal multiplexer, like [screen][] or [tmux][]. I use
tmux, personally, and jeepers wouldn't it be neat to have it run
natively on my phone so that I don't have to use ConnectBot to an
outside server and then do "tmux attach"?

Fortunately (or so I thought when starting this project), tmux is
written entirely in C. This turned out to be difficult, and so I'll
outline how I did it.

The Android kernel uses a slimmed down version of standard C libraries
(libc.so), called bionic. This is where all the allowed calls are
stored. It's possible to either:

Surprisingly, I attempted the second option first. *This was insane.* I
had to [compile a compiler to compile a compiler to compile a
compiler][] to [compile a shared object library through a perl
wrapper][] to compile the code. I think I made it through all the
compiling compilers parts, and then my [finished compiler][] crapped all
over its pants.

<!-- PELICAN_END_SUMMARY -->

It was at this point that I decided to check my phone, and I realised
that CyanogenMod7 already has a shared object library for standard C.
(It's at /system/lib/libc.so). There is the possibility that I could use
this pre-ARM-compiled library, bundle it with tmux, and then use
[Android][] [NDK][] to compile tmux for ARM. This would also necessitate
creating a .JNI makefile for the frontend, which includes [a trivial
amount of Java to wrap the native code][].

I'll update when I finish or fuck myself over, but right now I'm getting
on brutal series of international flights for [Chaos Computer Club][]'s
[28C3][] in Berlin, and my connection is slower than liberal reformist
tactics are at creating a freer society.

♥Ⓐ

  [xqdr]: http://www.patternsinthevoid.net/blog/2011/12/xqdr-a-flying-robot-that-does-things/
    "xqdr: A Flying Robot That Does Things"
  [screen]: http://en.wikipedia.org/wiki/GNU_Screen
  [tmux]: http://tmux.sourceforge.net/
  [compile a compiler to compile a compiler to compile a compiler]: https://gist.github.com/1518816
  [compile a shared object library through a perl wrapper]: http://plausible.org/andy/agcc
  [finished compiler]: https://github.com/jsnyder/arm-eabi-toolchain
  [Android]: http://developer.android.com/sdk/ndk/index.html
  [NDK]: http://mindtherobot.com/blog/452/android-beginners-ndk-setup-step-by-step/
  [a trivial amount of Java to wrap the native code]: http://mobile.tutsplus.com/tutorials/android/ndk-tutorial/
  [Chaos Computer Club]: http://www.ccc.de/en/
  [28C3]: http://events.ccc.de/congress/2011/wiki/Welcome

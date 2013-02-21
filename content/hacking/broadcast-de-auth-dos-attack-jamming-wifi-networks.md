Title: Broadcast De-auth DOS Attack: Jamming WiFi Networks
Date: 2011-05-07 13:52
Author: isis agora lovecruft
Category: hacking
Tags: DOS, packet injection, wifi jamming

The following may or may not be illegal to practice on networks not
owned by the broadcaster. As such, it is purely for informational and
educational purposes.

I'm certainly not the first to discover this, by any means. It's
incredibly simple, and there's no way to defend against it. This type of
attack uses aireplay-ng to broadcast streaming de-authorization packets
to any client on a given wireless network, or networks. Put simply, it
effectively "jams" WiFi networks. If you're within radio range of the
network access point, you stream the de-auth packets to boot everyone
off the network. If you keep streaming this, it becomes a Denial of
Service attack because they can't reconnect to the network while you're
jamming it.

To do this, you need a wireless card which supports packet injection and
monitoring, and simply the aircrack-ng suite of tools. The command for
it is

    airplay-ng --death 0 -a [BSSID of victim network access point] mon0

There's no way to defend against this type of attack, but the victim(s)
could triangulate your position using the frequency strength of your
broadcast. So, if you're going to do this, use rollerskates.

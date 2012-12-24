Title: Best. Game. Ever.
Date: 2011-07-29 00:17
Author: isis
Category: Chaos Theory, Game Theory, Technology
Tags: artificial intelligence, cellular automata, chess, combinatorial game theory, game complexity, game of go, game of life, game theory, gliders, golly, heuristics, John Horton Conway, Manhattan Project, neuroscience, particle physics, shannon's number, turing complete, von Neumann

I used to be really into a good 'ol game of chess. I still am, I
suppose. But it got old. There's only so many possibilities --
[Shannon's number][] gives the lower bound to be only 10^3^, to be
precise, and [the upper bound has been calculated][] at less than
2^155^, which is less than 10^46.7^. That's factoring in all possible,
legal moves, and factoring out invalid or illegal moves. It doesn't
factor in that human players are not the most logical creatures and
their playing can quickly become predictable. I mean, if you take a look
at game theory, in "Guess Two Thirds of the Average" as played in the
general population,[it's statistically shown that humans do not think
beyond three logical iterations][]. Chess is grand, and a good match is
always appreciated. But it just got old after a while.

Lately, I've been really into playing Go. Go is amazing, and I still
suck at it. I could probably waste my life away learning Go strategy,
and still not master the game. To compare it with chess, the [maximum
number of legal moves in Go][] is 2.08168199382×10^170^, more than 130
orders of magnitude higher. That's also more than double [the amount of
particles in the universe][]. While super chess computers, such as Deep
Blue, can beat World Champion chess players, [young children can often
beat even the best Go computers][]. However, as artificial intelligence
continually develops to higher levels,[that trend is beginning to
change][], which makes a computer's aptitude for the game a useful
measurement of its capability for human-like thought.

From [the Wired Science article on Go-playing AIs][that trend is
beginning to change]:

> Faced with such extraordinary complexity, our brains somehow find a
> path, navigating the possibilities using mechanisms only dimly
> understood by science. Both of the programs that have recently
> defeated humans used variations on mathematical techniques originally
> developed by Manhattan Project physicists to coax order from pure
> randomness.
>
> Called the [Monte Carlo method][], it has driven computer programs to
> defeat ranking human players six times in the last year. That’s a far
> cry from chess, the previous benchmark of human cognitive prowess, in
> which Deep Blue played Garry Kasparov to a panicked defeat in 1997,
> and Deep Fritz trounced Vladimir Kramnik in 2006. To continue the golf
> analogy, computer Go programs beat the equivalents of Chris Couch
> rather than Tiger Woods, and had a multi-stroke handicap. But even six
> victories was inconceivable not too long ago, and programmers say it
> won’t be long before computer domination is complete.
>
> There is, however, an asterisk to the programs’ triumphs. Compared to
> the probabilistic foresight of our own efficiently configured
> biological processor — sporting 10^15^ neural connections, capable of
> 10^16^ calculations per second, times two — computer Go programs are
> inelegant. They rely on what Deep Blue designer Feng-Hsiung Hsu
> [called][] the “substitution of search for judgment.” They crunch
> numbers.
>
> “People hoped that if we had a strong Go program, it would teach us
> how our minds work. But that’s not the case,” said [Bob Hearn][], a
> Dartmouth College artificial intelligence programmer. “We just threw
> brute force at a program we thought required intellect.”
>
> If only we knew what our own brains were doing.
>
> Inasmuch as human *Go* prowess is understood, it’s explained in terms
> of pattern recognition and intuition. “When there are groups of stones
> arranged in certain ways, you can build visual analogies that work
> very well. You can think, ‘This configuration radiates influence to
> that part of the board’ — and it turns out it’s a useful concept,”
> said Hearn. “The revolutionary people in the field have an intuitive
> sense, and can look at things completely differently from other
> people.”
>
> Image-based neuroscience supports this explanation, albeit vaguely.
> When University of Minnesota researchers led by cognitive scientist
> Michael Atherton [scanned the brains][] of people playing chess and
> compared them to [*Go*-playing brains][], they found heightened
> activation in the *Go* players’ parietal lobes, a region responsible
> for processing spatial relationships. But these observations,
> said[Atherton][], were rudimentary. “The higher-level stuff, we didn’t
> figure out,” he said.
>
> In a more recent brain-scanning study, Japanese researchers
> [compared][] professional and amateur *Go* players as they
> contemplated opening- and end-stage moves. Both displayed parietal
> lobe activity. During the end stages, however, professionals had
> extremely high activity in their precuneus and cerebellum regions,
> where the brain integrates a sense of space with our bodies and
> motions.
>
> Put another way, professionals fuse their consciousness into the
> decision tree of the game.
>
> Go players have an ability “to think creatively and prune the search
> tree in an aesthetic sense,” said Atherton. “They have a feel for the
> game.”
>
> Artificial intelligence researchers historically tried to harness this
> pattern-based approach, however poorly understood, to their Go
> programs. It wasn’t easy. “When I’ve talked to *Go* professionals
> about how they come to their decisions, it’s been difficult for them
> to describe why a move is right,” said Doshay at UCSC, who designed a
> Go computer program called [SlugGo][]. “*Go* is a game of living
> things, and you talk about it that way, as if the patterns might be
> alive.”
>
> But if turning cryptic statements from *Go* masters into working
> algorithms for determining the statistical health of game patterns was
> impossible, there didn’t seem to be any other way of doing it. “It was
> possible to sidestep the cognitive issues by throwing brute force at
> chess,” said Hearn, “but not at *Go*.”
>
> Compared to the challenge posed to a Go program, Deep Blue’s
> computations — possible moves in response to a move, carried 12 cycles
> into the future — are back-of-the-napkin scribblings. “If you look at
> the game trees, there’s about 30 possible moves you can make from a
> typical position. In *Go*, it’s about 300. Right away, you get
> exponential scaling,” said Hearn.
>
> With every anticipated move, the possibilities continue to scale
> exponentially — and unlike chess, where captured pieces are counted
> immediately, *Go* territory can switch hands until the game’s end.
>
> Running a few branches down the tree is useless: take one step, and it
> needs to be pursued, exponential scale by scale, until the game end.
>
> According to Doshay, the number of *Go*’s end-states — 10^171^ — is
> almost inconceivably smaller than the 10^1100^ different ways of
> getting there. Without patterns to eliminate whole swaths of choices
> from the outset, computers simply can’t cope with it, at least not
> within time frames contained by the universe’s remaining existence.
> But to Doshay, guiding computers with human-rules patterns was wrong
> from the beginning.
>
> “If you want computers to do something well, you concentrate on the
> ways computers do things well,” he said. “Computers can generate
> enormous quantities of random numbers very rapidly.”
>
> Enter the Monte Carlo method, named by its Manhattan Project pioneers
> for the casinos where they gambled. It consists of random simulations
> repeated again and again until patterns and probabilities emerge: the
> characteristics of an atomic bomb explosion, phase states in quantum
> fields, the outcome of a *Go* game. Programs like [MoGO][] and [Many
> Faces][] simulate random games from start to finish, over and over and
> over again, with no concern for figuring out which of any given move
> is best.
>
> “At first, I was dismissive,” said Hearn. “I didn’t think there was
> anything to be gained from random playouts.” But the programmers had
> one extra trick: they crunched the accumulated statistics, too. Once a
> few million random games are modeled, probabilities take form. Thus
> informed, the programs devote extra processing power to promising
> branches, and less power to less-promising alternatives.
>
> The resulting game style looks human, but aside from a few rough human
> heuristics, the patterns articulated by our intuitions are
> unnecessary. “The surprising, mysterious thing to me is that these
> algorithms work at all,” said Hearn. “It’s very puzzling.”
>
> Puzzling it might be, but the game is almost over. Hearn and others
> say that, having started to beat human professionals, Monte
> Carlo-based programs will only get better. They’ll incorporate the
> results of earlier games to their heuristic arsenal, and within a few
> years — a couple decades at the most — be able to beat our best.
>
> What is the larger significance of this? When computers finally
> triumphed at chess, the world was shocked. To some, it seemed that
> human cognition was less special than before. But to others, the
> competition is an illusion. After all, behind every machine is the
> hand that made it.
>
> “There’s a strong tendency in humans to have a conceit about how far
> we’ve advanced,” said Doshay. “But we’ve only really started
> programming computers.”

While Go can be used to measure the intellectual capacity of artificial
intelligences, it can also be used to study self-replicating systems.
The British mathematician Conway, while studying von Neumann's
algorithms for self-replicating machines, invented [the Game of Life][],
a cellular automata, with a Go board. The rules are incredibly simple:

1.  Any live cell with fewer than two live neighbours dies, as if caused
    by under-population.
2.  Any live cell with two or three live neighbours lives on to the next
    generation.
3.  Any live cell with more than three live neighbours dies, as if by
    overcrowding.
4.  Any dead cell with exactly three live neighbours becomes a live
    cell, as if by reproduction.

[![][]][]Conway's Game of Life, interestingly enough,[is also Turing
complete][]. And it's where the "hacker emblem" comes from. Not to
mention, and pardon if I digress, that you can make lobsters which shit
spaceships. It is the absolute hands-down no-buts definition of fun.

There are plenty of Life emulators, but the one I'd recommend is
[Golly][], which is cross-platform and supports the HashLife algorithms.
There's also [plenty][] [of][] [already][] [discovered][] neat patterns
like gliders, and spaceships, and whatnot that you can copy/paste into
Golly to get you started. And, to use game theory terms, it's a
zero-player game, which is fancy words meaning it only takes initial
input patterns and then the game plays itself from there. Which means,
you don't need friends to play it. Which, in my case, makes it the best
game ever.

  [Shannon's number]: https://secure.wikimedia.org/wikipedia/en/wiki/Shannon_number
  [the upper bound has been calculated]: http://homepages.cwi.nl/~tromp/chess/chess.html
  [it's statistically shown that humans do not think beyond three
  logical iterations]: http://www.patternsinthevoid.net/blog/2011/06/game-theory-anarchism-ii-how-information-can-smash-the-state/
  [maximum number of legal moves in Go]: https://secure.wikimedia.org/wikipedia/en/wiki/Go_and_mathematics
  [the amount of particles in the universe]: http://www.strangehorizons.com/2001/20010402/biggest_numbers.shtml
  [young children can often beat even the best Go computers]: http://www.usgo.org/resources/whatisgo.html
  [that trend is beginning to change]: http://www.wired.com/wiredscience/2009/03/gobrain/
  [Monte Carlo method]: http://en.wikipedia.org/wiki/Monte_Carlo_method
  [called]: http://www.spectrum.ieee.org/print/5552
  [Bob Hearn]: http://www.dartmouth.edu/%7Erah/
  [scanned the brains]: http://www.ncbi.nlm.nih.gov/pubmed/12589885
  [*Go*-playing brains]: http://www.ncbi.nlm.nih.gov/pubmed/12589886
  [Atherton]: http://www.tc.umn.edu/%7Eathe0007/
  [compared]: http://cat.inist.fr/?aModele=afficheN&cpsidt=16711741
  [SlugGo]: http://senseis.xmp.net/?SlugGo
  [MoGO]: http://senseis.xmp.net/?MoGo
  [Many Faces]: http://www.smart-games.com/manyfaces.html
  [the Game of Life]: https://secure.wikimedia.org/wikipedia/en/wiki/Conway%27s_Game_of_Life
  []: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/07/Gospers_glider_gun.gif
    "Gospers_glider_gun"
  [![][]]: http://www.patternsinthevoid.net/blog/wp-content/uploads/2011/07/Gospers_glider_gun.gif
  [is also Turing complete]: http://www.igblan.free-online.co.uk/igblan/ca/
  [Golly]: http://golly.sourceforge.net/
  [plenty]: http://home.interserv.com/~mniemiec/objtype.htm
  [of]: http://members.tip.net.au/~dbell/
  [already]: http://entropymine.com/jason/life/#collections
  [discovered]: http://www.radicaleye.com/lifepage/patterns/contents.html

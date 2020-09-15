Title: Implementing As-Safe-As-Possible, Misuse-Resistant Cryptographic Libraries: Part I
Date: 2020-09-14 16:01
Modified: 2020-09-14 16:01
Tags: cryptography
Category: hacking
Author: isis agora lovecruft

<!-- Image: /static/images/2015/12/card.jpeg -->

<!-- PELICAN_BEGIN_SUMMARY -->

Over the years, I've discovered many techniques in learning how to design
as-safe-as-possible, misuse-resistant cryptographic libraries for some fairly
complex primitives, which I'd like to share in the hopes that we can continue to
progress the state-of-the-art in cryptography towards greater safety at
decreased cost to both cryptographers and security engineers.  Time permitting,
I hope to eventually turn this into a series of posts.

The typestate pattern is one I've greatly appreciated but didn't have a name for
before reading [this article](http://cliffle.com/blog/rust-typestate/).  I
highly recommend reading it, and I won't be reviewing it in detail here.  The
tl;dr is that you encode your state machine into a type system, such that invalid
state changes are caught at compile time rather than runtime.

<!-- PELICAN_END_SUMMARY -->

Take, for example, this stubbed out implementation of a two-round distributed
key generation protocol.

<pre class="prettyprint lang-rust">
use curve25519_dalek::ristretto::RistrettoPoint;
use curve25519_dalek::scalar::Scalar;

pub struct Commitment(pub(crate) RistrettoPoint);
pub struct SecretKeyShard(pub(crate) Vec&lt;Scalar&gt;);
pub struct PublicKeyShard(pub(crate) Scalar);
pub struct ProofOfKnowledgeOfSecretKeyShard(pub(crate) Scalar, pub(crate) Scalar);

impl ProofOfKnowledgeOfSecretKeyShard {
    /// Prove in zero-knowledge a secret key.
    pub fn prove(
        secret: &SecretKeyShard
    ) -> ProofOfKnowledgeOfSecretKeyShard {
        // ...
    }

    /// Verify a proof of knowledge of a secret key.
    pub fn verify(
        &self,
    ) -> Result<(), ()> {
        // ...
    }
}

pub struct DistributedKeyGeneration {};

impl DistributedKeyGeneration {
    /// Generate a shard of the eventual shared secret, and form some
    /// commitments and a zero-knowledge proof regarding those secrets, in order
    /// to prevent rogue-key attacks, and send the commitments and proof to the
    /// other participants for checking.
    pub fn round_one_init(
    ) -> (SecretKeyShard, ProofOfKnowledgeOfSecretKeyShard, Vec&lt;Commitment&gt;) {
        // ...
    }

    /// Check the commitments and proofs that were sent by the other participants.
    pub fn round_one_finish(
        proofs: &Vec&lt;ProofOfKnowledgeOfSecretKeyShard&gt;,
    ) -> Result<(), ()> {
        for proof in proofs.iter() {
            proof.verify()?;
        }
        // ...
    }

    /// Each participant uses their secret shard to evaluate a different shard
    /// of the eventual shared public key, which they send to each respective
    /// participant.
    pub fn round_two_init(
        secret: &SecretKeyShard,
    ) -> Vec&lt;PublicKeyShard&gt; {
        // ...
    }

    /// Verify the public shards received from the other participants, aborting
    /// on failure, then compute our long-lived signing key and a proof of its
    /// correctness.
    pub fn round_two_finish(
        secret: &SecretKeyShard,
        public_shards: &Vec&lt;PublicKeyShard&gt;,
        commitments: &Vec&lt;Commitment&gt;,
    ) -> Result<(), ()> {
        // ...
    }
}
</pre>

It's already doing better than many cryptographic APIs I've seen in the wild:

* Rather than passing around blobby arrays of bytes, it's at least using the
  type system to do basic things, like ensuring that pieces of the secret key
  shards are kept separate and treated differently to the public key shards,
  even though they share the same underlying mathematical objects.

* It has basic documentation, stating what actions — outside the scope of this
  cryptographic library — should be done with the return values.  (E.g. "send
  the commitments and proof to the other participants for checking".)

* It attempts to use intuitive naming for types and variables, rather than
  condensing things in to nearly indecipherable acronyms, or — even worse —
  using inexplicable¹ single-letter function/variable names.

¹ IMHO it's okay to use single-letter variable names when mirroring the names
used in a paper, and leaving comments to make it clear what the object actually
is, however in all likelihood this isn't code that should be exposed to a
security engineer.

So how could it be better?

This is precisely where the typestate pattern shines.  The above code would
allow a developer to do:

<pre class="prettyprint lang-rust">
let (secret, nipk_of_secret, commitments) = DistributedKeyGeneration::round_one();

send_to_participants(nipk_of_secret, commitments);

let public = DistributedKeyGeneration::round_two_init(&secret);
</pre>

Depending on the specifics of the protocol, skipping the call to
`DistributedKeyGeneration::round_one_finish()` allows for a
[rogue-key attack](https://eprint.iacr.org/2018/417), where a rogue participant
creates a crafted public key shard which negates the contribution to a signature
from the targeted other participant(s).

Let's see instead how this known attack could be eliminated entirely <i>by
making it discoverable at compile-time</i>.

<pre class="prettyprint lang-rust">
use curve25519_dalek::ristretto::RistrettoPoint;
use curve25519_dalek::scalar::Scalar;

pub struct Commitment(pub(crate) RistrettoPoint);
pub struct SecretKeyShard(pub(crate) Vec&lt;Scalar&gt;);
pub struct PublicKeyShard(pub(crate) Scalar);
pub struct ProofOfKnowledgeOfSecretKeyShard(pub(crate) Scalar, pub(crate) Scalar);

impl ProofOfKnowledgeOfSecretKeyShard {
    /// Prove in zero-knowledge a secret key.
    pub fn prove(
        secret: &SecretKeyShard
    ) -> ProofOfKnowledgeOfSecretKeyShard {
        // ...
    }

    /// Verify a proof of knowledge of a secret key.
    pub fn verify(
        &self,
    ) -> Result<(), ()> {
        // ...
    }
}

pub type DistributeKeyGenerationState = DistributedKeyGenerationRound1;

pub struct DistributedKeyGenerationRound1 {
    pub(crate) secret_shards: SecretKeyShard,
    pub proof: ProofOfKnowledgeOfSecretKeyShard,
    pub commitments: Vec&lt;Commitment&gt;,
}; 

impl DistributedKeyGenerationRound1 {
    /// Generate a shard of the eventual shared secret, and form some
    /// commitments and a zero-knowledge proof regarding those secrets, in order
    /// to prevent rogue-key attacks, and send the commitments and proof to the
    /// other participants for checking.
    pub fn init(
    ) -> DistributedKeyGenerationRound1 {
        // ...
    }

    /// Check the commitments and proofs that were sent by the other participants.
    /// Only progress to round 2 if the verifications passed.
    pub fn progress(
        &self,
        proofs: &Vec&lt;ProofOfKnowledgeOfSecretKeyShard&gt;,
    ) -> Result<DistributedKeyGenerationRound2, ()> {
        for proof in proofs.iter() {
            proof.verify()?;
        }

        // ...

        Ok(DistributedKeyGenerationRound2a{ secret_shards: self.secret_shards.clone() }
    }
}

pub struct DistributedKeyGenerationRound2a {
    pub(crate) secret_shards: SecretKeyShard,
}

impl DistributedKeyGenerationRound2a {
    /// Each participant uses their secret shard to evaluate a different shard
    /// of the eventual shared public key, which they send to each respective
    /// participant.
    pub fn progress(
        &self,
    ) -> DistributedKeyGenerationRound2b {
        // ...
    }
}

pub struct DistributedKeyGenerationRound2b {
    pub(crate) secret_shards: SecretKeyShard,
    pub public_shards: Vec&lt;PublicKeyShard&gt;,
}

impl DistributedKeyGenerationRound2b {
    /// Verify the public shards received from the other participants, aborting
    /// on failure, then compute our long-lived signing key and a proof of its
    /// correctness.
    pub fn finish(
        &self,
    ) -> GroupPublicKey {
        // ...
    }
}

pub struct GroupPublicKey(pub RistrettoPoint);
</pre>

With these changes, the code of a security developer would likely look more like
this:

<pre class="prettyprint lang-rust">
let state = DistributedKeyGeneration::init();

let proofs = collect_proofs_from_other_participants();

let state = state.progress(&proofs)?.progress();

send_public_shards_to_other_participants(state.public_shards);

let group_public_key = state.progress();
</pre>

If any of the state machine update functions are ever called without the correct
context, the compiler catches the mistake, thus enforcing safety against
cryptographic attacks before they occur.

This is, albeit, a pretty trivial and simple toy example.  There are many other
things we could do with a decent type system to improve this code, including but
not limited to:

* Providing a `RoundTwo` trait for genericising over the two typestates in the
second round of the protocol.

* Using the [the sealed design pattern](https://rust-lang.github.io/api-guidelines/future-proofing.html#sealed-traits-protect-against-downstream-implementations-c-sealed)
to prevent third parties from creating further implementations of valid
`RoundTwo` states.

* Avoiding repeated `clone()`/`copy()` of data in the state machine (e.g. the
`secret_shards` which get copied multiple times in the above example) by abusing
yet another empty trait which is implemented for all typestates to store the
actual state in a heap-allocated pointer (e.g. `Box<ActualState>`) which is
copied instead.

If you'd like to see a more complex example of these design patterns all put
together, I have
[a rough draft implementation](https://github.com/isislovecruft/ed25519-dalek/blob/9e44fb1c6e060bce9e54480ce1c7387d13c17b75/src/state.rs)
of the MSDL protocol from
["Compact Multi-Signatures for Smaller Blockchains"](https://eprint.iacr.org/2018/483)
by Boneh, Drijvers, and Neven.

<!--

further post ideas:
* two sets of documentation, or documentation in general, eg. never write a
  doctext you're not okay with someone copy-pasting

-->

# Gravit Project Historical Register

Draft 0.2, 9 November 2026. Maintained by the Gravit Open Network Foundation.

**Rule of this register.** A date appears only where a public source exists. "Idea → artefact" means the artefact develops the idea, not that the idea is fully realised. Changes to this file are made by pull request; earlier versions stay in the history.

## A. Dated milestones

| Date | Event | Source |
|---|---|---|
| 2015 | Decipial Foundation, six decentralized principles | https://decipial.org |
| 2026-03-17 | gravit-research: research, drafts, simulations | GitHub repository creation date |
| 2026-04-24 | gravit-dwf-poc (capital markets) | GitHub |
| 2026-05-23 | gravit-epistemic-verifier | GitHub |
| 2026-05-30 | gravit-core, gravit-spec, partner proofs of concept | GitHub |
| 2026-06-25 | gravit-grover | GitHub |
| 2026-07-13 | graviteron: proposed unit of verifiable trust | GitHub |
| 2026-10-09 | verifier: reference implementation in Python and Rust | GitHub |
| 2026-10-13 | history-keeper, gravit-verifier-service | GitHub |
| 2026-11-01 | draft-gravit-graviteron-00 at the IETF | IETF Datatracker |
| 2026-11-07 | 100 million cases, Python and Rust, zero differences | verifier/reports/difftest-2026-11-07 |
| 2026-11-09 | Gravit Education: manifesto and four school lessons | https://gravit.world/manifest/ |

## B. From idea to artefact

| Early idea | What exists today | Status |
|---|---|---|
| "We do not assert truth; we develop methods for testing it" | Manifesto *Purpose, values, integrity* | published |
| Trust coefficient, trust mass | θ (theta) in GEVP and the evidence admission rules of the verifier | in decision rules; a general formula remains research |
| A unit of trust ("grav") | **Graviteron**: weight of independent signed evidence in decibans, 21 vectors, IETF draft | proposed standard, not a recognised unit |
| "Ten repetitions are not ten confirmations" | Verifier rule against aggregation laundering; independence evidence in the registry; IETF AUDIT proposal | implemented and proposed |
| Claim graphs, provenance | Provenance in evidence records; history-keeper (append-only log of claims) | partial |
| Verification loops, circular proof | Exclusion of dependent evidence in the verifier | partial; loop taxonomy not published |
| Invariant test suite | 60 golden vectors; differential test of 100 million cases | published |
| Security and attack model | Sybil tests, forged and replayed signatures, adversarial Ed25519 signatures | in the test suites |
| Loop passport | Signed decision records and receipts | close analogue; no separate standard |
| Claim graph exchange (CGXP) | GEVP (IETF) exchanges decisions | decisions yes, graphs not yet |
| Gravit Engine | verifier, verifier-service, eval-pack | reference implementation exists |
| Trust field theory | simulations in gravit-research | hypothesis; no formal model or experiment yet |
| Trust topology, trust singularity | none | concept |
| Education framework | https://gravit.world/lessons/ (four modules, three languages) | school level started |

## C. Open problems

1. A rigorous specification of a trust coefficient and its relation to the Graviteron.
2. Calibration of θ on real data; robustness against Sybil attacks.
3. Which evidence suffices to show that sources are independent.
4. A taxonomy of verification loops and detection of circular proof in claim graphs.
5. Trust field theory: a formulation with a testable prediction.
6. Exchange of claim graphs between independent nodes on top of GEVP.

Contributions, corrections and objections are welcome as issues or pull requests.

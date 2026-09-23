---
layout: single
title: "Engineering Better Gene-Therapy Vectors"
permalink: /research/gene-therapy-vectors/
author_profile: true
---

<p class="project-back"><a href="/research/">← All research</a></p>

*The core of my independent program: designing the delivery vehicles that carry gene therapies into the body — and making them precise, safe, and manufacturable.*

---

## The Problem

To treat a genetic disease, we need to deliver a working gene into the right cells. The most successful tool for this is the **AAV** — a harmless virus, stripped of its own genes, repurposed as a microscopic delivery truck. AAVs are behind several approved gene therapies today.

But the trucks we have are blunt instruments. Natural AAVs don't home in on the tissues we care about, so treating a large organ like muscle requires **enormous doses** — hundreds of trillions of particles per kilogram of body weight. At those doses, the vector floods the liver and other organs it was never meant to reach, which has caused severe, sometimes fatal, side effects in clinical trials. High doses are also extraordinarily expensive to manufacture, and many patients are excluded because their immune system already recognizes the virus.

**The goal of my work is to redesign the truck** so it delivers its cargo to the right place at a fraction of the dose — safer, cheaper, and available to more patients.

---

## My Approach: Design Instead of Trial-and-Error

For years, better vectors were found mostly by chance — making millions of random variants and fishing out the rare ones that worked. That process is slow, hard to interpret, and optimizes for only one property at a time.

I took a different route: **design the vector on purpose.** I combine what we know about how viruses enter cells with computational modeling and artificial intelligence, so that each new vector is a deliberate hypothesis rather than a lucky find.

<div class="pipeline-steps" data-aos="fade-up">
  <div class="pipeline-step">
    <div class="step-num">1</div>
    <div class="step-body"><strong>Find the doorway.</strong> I identified a specific "receptor" — a molecular doorknob called integrin αVβ6 — that is abundant on muscle, scarce in the liver, and conserved across species. Aiming the vector at this doorway redirects it to muscle.</div>
  </div>
  <div class="pipeline-step">
    <div class="step-num">2</div>
    <div class="step-body"><strong>Design the key.</strong> Using structural modeling, I grafted the natural "key" that fits this doorway onto the surface of the vector — while making sure the redesigned vector could still be produced at scale.</div>
  </div>
  <div class="pipeline-step">
    <div class="step-num">3</div>
    <div class="step-body"><strong>Let AI expand the search.</strong> I then added protein-AI models — the same family of methods behind modern language models, trained on protein sequences instead of text — to propose and rank thousands of improved designs, optimizing several properties at once.</div>
  </div>
  <div class="pipeline-step">
    <div class="step-num">4</div>
    <div class="step-body"><strong>Test at massive scale, then validate.</strong> We tag each candidate with a unique molecular "barcode," test millions together in a single experiment, and read out which ones win — before validating the best in cell and animal models.</div>
  </div>
</div>

---

## What We Achieved: The LICA Vector Family

This strategy produced a family of engineered vectors we call **LICA** (Linked-Integrin-Complex AAV).

- **LICA1**, the first-generation design, delivered its cargo to muscle just as well as the best existing vectors while sending far less to the liver — the cleanest muscle-versus-liver targeting of any vector we tested. It worked not only in mice but also in **non-human primates**, a crucial step toward the clinic.
- At a dose about **twenty times lower** than those used in current muscular dystrophy trials, LICA1 restored muscle function and reduced damage in two different disease models.
- The **AI-designed second generation — LICA3 and LICA4** — went further, efficiently reaching both **skeletal muscle and the heart**, while remaining easy to manufacture. These vectors are now advancing in preclinical programs.

Together, this work established a new principle: that gene-therapy vectors can be **rationally designed and AI-optimized**, rather than stumbled upon — and that doing so can make treatment dramatically safer.

---

## Where It's Going

I am now extending this platform in several directions, all aimed at matching the vector to the biology of each disease:

- **Muscle *and* heart together** — because many muscular dystrophies also cause heart failure, tuning vectors to treat both at once.
- **Reaching muscle stem cells** — so that gene edits are *durable*, carried forward as muscle renews itself, rather than fading over time.
- **Crossing into the brain** — engineering vectors that slip across the blood-brain barrier through a natural transport route, to treat neurological diseases without invasive surgery.
- **Decoding the vector surface** — a long-term effort to map how every part of the vector's surface controls its behavior, turning vector design into a fully predictive science.

This program is supported by an **ANR young-investigator grant** (AAV-SkEdit), a **DIM BioConvS doctoral grant** (ENGAGE-Heart), and the **POC'UP** technology-transfer grant, and is protected by several patent families now used in academic and industrial collaborations.

---

<p style="font-size:0.85rem;color:var(--color-muted-stone);"><strong>Key publications:</strong> Vu Hong et al., <em>Nature Communications</em> (2024); Petat, Suel, …, Richard &amp; Vu Hong, preprint (2026, under revision at <em>Molecular Therapy</em>). <a href="/publications/">See all →</a></p>

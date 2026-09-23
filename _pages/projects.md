---
layout: single
title: "Projects"
permalink: /projects/
author_profile: true
---

<div class="project-list">

<div class="project-card">
  <div class="project-card__meta">
    <span class="project-tag">Computer Vision</span>
    <span class="project-tag">Histology</span>
    <span class="project-tag">Python</span>
  </div>
  <h2 class="project-card__title">
    <a href="/projects/f2fmatcher/">F2FMatcher: Fiber-to-Fiber Matching Across Histological Stains</a>
  </h2>
  <p class="project-card__desc">
    Matching individual muscle fibers across serial tissue sections stained with different protocols is a fundamental bottleneck in quantitative histology. F2FMatcher solves this with a three-stage AI pipeline — a variational autoencoder that encodes Cellpose flow fields into compact fiber embeddings, a pairwise neural classifier (F1 ≈ 0.944), and a geometry-aware propagation algorithm that achieves 50–95% match coverage on sections of 2,000–3,500 fibers. Released under MIT license with pre-trained models included.
  </p>
  <a href="/projects/f2fmatcher/" class="project-card__link">Read more →</a>
</div>

<div class="project-card">
  <div class="project-card__meta">
    <span class="project-tag">Protein AI</span>
    <span class="project-tag">Language Models</span>
    <span class="project-tag">Open Source</span>
  </div>
  <h2 class="project-card__title">
    <a href="https://huggingface.co/avuhong" target="_blank">AAV Protein Language Models</a>
  </h2>
  <p class="project-card__desc">
    A pair of openly released AI models for gene-therapy vector design. <strong>AAVesm2</strong> is a "reader" — it turns a capsid sequence into a numerical fingerprint used to predict how the vector will behave. <strong>PiccoviralesGPT</strong> is a "writer" — a generative model that proposes new, realistic capsid sequences to expand the space of candidates worth testing. Together they let us design and rank vectors computationally, before touching the bench.
  </p>
  <a href="https://huggingface.co/avuhong" target="_blank" class="project-card__link">View on Hugging Face →</a>
</div>

<div class="project-card">
  <div class="project-card__meta">
    <span class="project-tag">Gene Therapy</span>
    <span class="project-tag">AAV Engineering</span>
    <span class="project-tag">Platform</span>
  </div>
  <h2 class="project-card__title">
    <a href="/research/gene-therapy-vectors/">The LICA Vector Platform</a>
  </h2>
  <p class="project-card__desc">
    A family of engineered AAV vectors — the delivery vehicles of gene therapy — designed to reach muscle, heart, and brain precisely and at low, safer doses. Built by combining structural design with AI, and protected by several patent families, LICA vectors are now advancing in preclinical programs and partnerships across Europe and the US.
  </p>
  <a href="/research/gene-therapy-vectors/" class="project-card__link">Read more →</a>
</div>

</div>

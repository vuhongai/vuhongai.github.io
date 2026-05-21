---
layout: single
title: "F2FMatcher: Fiber-to-Fiber Matching Across Histological Stains"
permalink: /projects/f2fmatcher/
author_profile: true
---

<p class="project-back"><a href="/projects/">← Projects</a></p>

<div class="project-hero">
  <div class="project-hero__tags">
    <span class="project-tag">Computer Vision</span>
    <span class="project-tag">Histology</span>
    <span class="project-tag">Deep Learning</span>
    <span class="project-tag">Python</span>
    <span class="project-tag">MIT License</span>
  </div>
  <p class="project-hero__links">
    <a href="https://github.com/vuhongai/F2FMatcher" target="_blank" rel="noopener">GitHub Repository</a>
  </p>
</div>

---

## What It Does

Serial histological sections from the same tissue block are routinely stained with different protocols — immunofluorescence for protein localization, Sirius Red for fibrosis, H&E for morphology — yet identifying the *same fiber* across stains has historically required manual annotation, limiting throughput to a handful of fibers per experiment.

F2FMatcher automates this: given two images from serial sections stained differently, it finds corresponding muscle fibers between them and quantifies staining intensity in matched regions. On typical sections of 2,000–3,500 fibers it achieves **50–95% match coverage** with a classifier F1 of approximately **0.944**.

---

## How It Works

The pipeline runs in eight sequential stages:

<div class="pipeline-steps">

<div class="pipeline-step">
<span class="step-num">1</span>
<div class="step-body">
<strong>Image I/O</strong> — Converts CZI (Zeiss) files to PNG and rescales both images to a common reference resolution.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">2</span>
<div class="step-body">
<strong>Cellpose Segmentation</strong> — Fine-tuned Cellpose models segment individual fibers and produce per-pixel flow fields encoding fiber shape and boundary.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">3</span>
<div class="step-body">
<strong>ROI Cropping</strong> — 256 × 256 pixel crops are extracted around each fiber centroid in both images.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">4</span>
<div class="step-body">
<strong>VAE Embedding</strong> — A variational autoencoder (<em>SharedMultiHeadVAE</em>) encodes 128 × 128 flow field representations into compact <strong>256-dimensional latent vectors</strong>, one per fiber, capturing shape independently of staining color.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">5</span>
<div class="step-body">
<strong>Pairwise Classification</strong> — A binary neural classifier concatenates embeddings from two fibers (one from each image) and outputs a match-probability score for every cross-image pair.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">6</span>
<div class="step-body">
<strong>Geometry-Aware Matching</strong> — Classifier scores are combined with spatial signatures (Wasserstein distance of k-NN vectors). Seed pairs are validated by triangle geometry and then propagated iteratively through neighboring fibers until convergence. An affine fill step recovers remaining ROIs.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">7</span>
<div class="step-body">
<strong>Output Generation</strong> — Paired fiber labels and overlay PNG visualizations are written to disk.
</div>
</div>

<div class="pipeline-step">
<span class="step-num">8</span>
<div class="step-body">
<strong>Quantification</strong> — Staining intensity is measured in matched fiber regions across both images.
</div>
</div>

</div>

---

## Model Architecture

### VAE — SharedMultiHeadVAE

The encoder progressively downsamples flow field crops through convolutional layers to produce 256-dimensional latent vectors. The decoder reconstructs three outputs simultaneously: `flow_x`, `flow_y`, and region masks. The training loss combines reconstruction error, KL divergence (β = 0.001), and a latent consistency penalty.

### Pairwise Classifier

A fully-connected network with dropout takes a 512-dimensional input (two concatenated 256-d embeddings) and outputs a single match probability. Validation F1 ≈ **0.944**.

### Matching Algorithm

| Stage | Method |
|---|---|
| Cost matrix | Classifier logits + Wasserstein spatial similarity |
| Seed selection | Top-scoring pairs filtered by triangle geometry (side lengths & angles) |
| Propagation | Iterative neighbor expansion, stops when < 0.25% new pairs per iteration |
| Fill | Affine transform estimated from seed matches → remaining ROIs matched |

---

## Installation

```bash
conda env create -f environment.yml
conda activate fibermatcher
pip install -e .
```

Pre-trained models are included in the repository — no separate download required.

---

## Usage

**Single pair:**

```bash
f2fmatcher run-pipeline \
    --img1 TAG01 --img2 TAG01 \
    --source1 /path/to/imgs1 \
    --source2 /path/to/imgs2 \
    --cp-model-1 "CP_AV_Laminin_Dia_Qua_TA_AxioScan10X" \
    --output /path/to/output
```

**Batch processing** uses parameter files that define image lists and Cellpose model assignments.

**Training from scratch:**

```bash
# Train the VAE
f2fmatcher train-vae --config configs/default.yaml

# Train the pairwise classifier
f2fmatcher train-classifier --config configs/default.yaml
```

---

## Performance

| Metric | Typical value |
|---|---|
| Fibers per image | 2,000 – 3,500 |
| Match coverage | 50 – 95% |
| Classifier F1 (validation) | ≈ 0.944 |
| Propagation iterations | 10 – 20 |

---

## Code & License

Source code is organized under `src/f2fmatcher/` with modules for CLI, I/O, segmentation, VAE, classification, matching, analysis, visualization, and utilities. Released under the **MIT License**.

<a href="https://github.com/vuhongai/F2FMatcher" target="_blank" rel="noopener" class="project-card__link">View on GitHub →</a>

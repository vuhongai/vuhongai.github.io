---
layout: single
title: "Research"
permalink: /research/
author_profile: true
hide_page_title: true
---

<div class="hero-section" data-aos="fade-up" style="padding-bottom:0.5rem;">
  <h1 class="hero-name" style="font-size:2.4rem;">Research</h1>
  <p class="hero-affiliation">Predictive engineering of gene-therapy vectors and the immune barriers that limit them.</p>
</div>

My independent research program at Genethon operates at the interface of **protein engineering, artificial intelligence, and translational gene therapy**. It is organised along two complementary lines that share a common foundation in computational protein design:

1. **AAV capsid engineering** — transforming vector development from empirical selection into a predictive, multi-parameter engineering discipline.
2. **Targeted protein degradation** — a host-directed strategy that removes the antibodies which block gene therapy and drive autoimmune disease.

Capsid engineering acts on the vector; protein degradation acts on the host environment. Pursued together, they address both sides of the central obstacle to systemic gene therapy — reaching the right cells, and evading the immune system that opposes delivery.

---

## AAV capsid engineering

Capsid engineering has historically relied on three strategies, each with intrinsic limits. **Directed evolution** explores large libraries but selects along a single functional axis, systematically eliminating variants with balanced advantages and optimising efficacy without safety. **Rational design** introduces defined receptor interactions under structural constraints — as in our LICA1/3/4 vectors — but samples only a narrow region of sequence space. **Machine learning** offers predictive design but is limited by datasets that diversify a single capsid region. These converge on a common gap: no framework combines simultaneous diversification of multiple variable regions, parallel measurement of multiple functional properties, and computational integration of the two.

My program is built on an integrated platform that closes this gap (Patent PCT/EP2024/082609).

### A predictive, multi-parameter engineering platform

**Rationale.** Many clinically decisive vector properties — receptor engagement, neutralising-antibody escape, manufacturability — are governed by the combined topology of several surface loops, and cannot be captured by diversifying one variable region at a time.

**Objective.** To jointly optimise tissue targeting, manufacturability, and immune evasion by (i) simultaneously diversifying multiple capsid variable regions (VRs) within one backbone while preserving VR–barcode linkage, (ii) profiling millions of barcoded variants in parallel — measuring vector delivery (DNA) and productive expression (RNA), production yield, affinity-purification compatibility, tissue tropism, and antibody escape as independent variables, and (iii) training interpretable deep-learning models that generalise these sequence–function relationships, including inter-VR epistasis, into unexplored sequence space. An AI-optimised LICA1 library already raised the proportion of viable capsids above 75%, providing the high-quality datasets that power the disease-adapted programs below.

### Disease-adapted LICA vectors: coordinated muscle–heart delivery

**Rationale.** Many neuromuscular and cardiac disorders — Duchenne muscular dystrophy (in which cardiomyopathy is now a leading cause of death), sarcoglycanopathies, laminopathies, Emery-Dreifuss dystrophy — require coordinated correction of both skeletal and cardiac muscle. The goal is not maximal transduction of one tissue, but tuning the cardiac-to-skeletal delivery ratio to disease anatomy. Our LICA3/4 vectors established that this coordinated optimisation is feasible.

**Objective.** To identify the capsid sequence features that control cardiac-to-skeletal partitioning and to optimise this ratio predictively — using in silico evolution driven by our screening-trained models as fitness oracles, then validating candidates across human iPSC-derived cardiomyocytes and myotubes, mouse models, and non-human primates. *Supported by the ENGAGE-Heart doctoral project (DIM BioConvS, 2025–2028).*

### Durable gene editing: dual myofiber–muscle stem cell targeting

**Rationale.** Current AAV vectors transduce post-mitotic myofibers efficiently but reach muscle stem cells (MuSCs) poorly. If MuSCs remain uncorrected, regenerated fibers carry the original defect and therapeutic benefit erodes under the chronic degeneration–regeneration seen in DMD, sarcoglycanopathies, and dysferlinopathies. Our data suggest LICA capsids can access the MuSC compartment, possibly via αVβ1.

**Objective.** To engineer a dual-tropism capsid — combined with a promoter active in both quiescent MuSCs and mature myofibers — that enables durable single-AAV gene editing sustained across repeated regenerative cycles. *Core of the AAV-SkEdit project (ANR JCJC, 2026–2029).*

### Brain-targeted delivery via the transferrin receptor

**Rationale.** The blood–brain barrier (BBB) severely limits CNS gene therapy: natural serotypes such as AAV9 cross poorly, forcing high systemic doses and peripheral toxicity. The most advanced engineered solution, BI-hTFR1, binds only human TfR1 and shows no activity in wild-type mice, so its preclinical evaluation depends entirely on humanised knock-in animals.

**Objective.** To engineer AAV9 capsids, co-diversified at VR4 and VR8, that engage transferrin receptor 1 (TfR1) **across human and mouse** for receptor-mediated BBB transcytosis — enabling direct validation in the existing repertoire of neurological disease models (Alzheimer's disease, myotonic dystrophy type 1, Pompe disease) while retaining human-relevant receptor interactions. *In collaboration with Prof. Hervé Le Stunff (Université Paris-Saclay, CNRS UMR 9197).*

### Decoding the full capsid sequence–function landscape

**Rationale.** The programs above each diversify only two of the ten capsid variable regions. The rules connecting the complete capsid surface to the full spectrum of vector properties remain largely unknown — the most consequential barrier to turning AAV engineering into a predictive science.

**Objective.** To decode, then design. Using a library diversified across all ten VRs (already built and pre-enriched), profile it across manufacturability, cross-species tropism, intracellular trafficking, and immunogenicity, and interpret it with deep learning to produce residue-, VR-, and epistasis-level maps of functional determinants. These principles will then drive the rational design of universal, manufacturable, immune-evasive vectors for muscle, liver, and brain — a closed-loop *design–build–test–learn* framework transferable to other vectors and protein-engineering problems.

---

## Targeted protein degradation

**Rationale.** Antibodies pose a dual challenge. In gene therapy, pre-existing neutralising antibodies exclude 30–60% of patients from systemic treatment and post-treatment immunity prevents re-administration. Beyond gene therapy, pathogenic IgGs are direct disease drivers in autoimmune conditions such as myasthenia gravis. Existing IgG-lowering strategies act non-selectively (FcRn antagonists), transiently and immunogenically (bacterial IdeS), or only partially (Seldegs) — none combines antigen specificity with catalytic, irreversible elimination.

Building on the protein-design expertise developed for capsid engineering, I designed synthetic bifunctional proteins that harness the cation-independent mannose-6-phosphate receptor (CI-M6PR / IGF2R) to route target IgGs to complete lysosomal degradation — a LYTAC-inspired mechanism distinct from recycling inhibition or extracellular cleavage (Patent EP25306380.4).

### Global IgG degradation to overcome humoral barriers

**Objective.** To develop IgG degraders (Iggd) that lower circulating anti-AAV antibodies enough to enable vector transduction in seropositive patients and restore eligibility for re-administration. Our lead candidate **Iggd8** drives rapid, efficient lysosomal IgG degradation with broad cross-species recognition, outperforms IdeS in restoring AAV transduction *in vitro*, and substantially reduces circulating IgG within 24 hours *in vivo*. This axis is developed in direct synergy with immune-evasive capsid engineering, pairing host-directed antibody depletion with vector-directed immune evasion.

### Selective autoantibody degradation in myasthenia gravis

**Rationale.** Myasthenia gravis (~20,000 patients in France) is a prototypic IgG-mediated autoimmune disease; ~85% of patients carry pathogenic anti-acetylcholine-receptor (AChR) IgGs. All current IgG-lowering therapies deplete pathogenic and protective antibodies alike.

**Objective.** To reprogram the degradation technology from global to **antigen-specific** clearance by replacing its generic IgG-binding module with AI-designed epitope-mimetic mini-proteins that reproduce the main immunogenic region of the AChR α1 subunit — selectively capturing and degrading pathogenic anti-AChR IgGs while sparing protective immunity. If validated, this establishes a generalisable paradigm for any antibody-mediated autoimmune disease with a defined antigen. *In collaboration with the Le Panse laboratory (INSERM UMR 974, Institut de Myologie, Paris).*

---

## Collaborations

The LICA vectors and the protein-degradation platform are deployed with academic and industrial partners across Europe and the US:

| Partner | Institution | Focus |
|---|---|---|
| Denis Furling | Sorbonne Université, INSERM UMR-S 974 | Myotonic dystrophy type 1 — LICA1 / LICA3 |
| Peter L. Jones | University of Nevada · Renogenyx (US) | Facioscapulohumeral muscular dystrophy (FSHD) — LICA1 / LICA3 |
| Eric Hajduch | Sorbonne Université, INSERM UMR-S 1166 | Type 2 diabetes & insulin resistance — LICA3 / AAV8 |
| Hervé Le Stunff | Université Paris-Saclay, CNRS UMR 9197 | Brain-targeted capsid — microglia & hypothalamus |
| Nathalie Neyroud | Sorbonne Université, INSERM UMR-S 1166 | Brugada syndrome — LICA3 |
| Francesca Rochais | Neocor Therapeutics (France) | Cardiac fibrosis — LICA3 |
| Jocelyn Laporte | IGBMC (France) | Muscle-directed nanoparticle delivery |
| Rozen Le Panse | Sorbonne Université, INSERM U974 | Selective autoantibody degradation — myasthenia gravis (Iggd8) |

I welcome new academic collaborations and industrial licensing discussions — [get in touch](mailto:avuhong@genethon.fr).

---

## Supervision & management

**Research engineers** — Nathalie Bourg-Alibert (2025–present), Eva Petat (2023–present), Laurence Suel (2021–present), Alejandro Arco Hierves (2022–2023).

**PhD students**

- **Thu Trang Dao** (2026–2029, co-supervisor) — *Synthetic immunobiology for the targeted degradation of autoantibodies in autoimmune myasthenia.*
- **Farasoa Razafinome** (2025–2028, co-director, 50%) — *Engineering next-generation AAV vectors for versatile gene therapy applications in heart diseases.*
- **Corentin Azzoun** (2025–2028, co-director, 25%) — *AAV gene therapy approaches for Duchenne muscular dystrophy.*

**Master's students** — Duc Thien Nguyen (M1, 2026), Teimurazi Gochitashvili (M2, 2022), Carolina Pacheco Algalan (M2, 2022), Grégoire Davignon (M2, 2020), Clara Mendes (M2, 2020), Nicolas Sandoval Villegas (M2, 2019).

*All positions at Genethon · Université Paris-Saclay · INSERM Integrare UMR-S 951.*

---

<p style="font-size:0.85rem;color:var(--color-muted-stone);">
  See the underlying work on the <a href="/publications/">publications page</a>, and the funding and IP behind it under <a href="/awards/">awards &amp; grants</a>.
</p>

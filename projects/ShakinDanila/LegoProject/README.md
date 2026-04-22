# LEGO DUPLO Sorting Machine

Automated system for sorting LEGO DUPLO bricks by type using computer vision.

---

## Overview

The project implements a hardware-software complex capable of identifying LEGO DUPLO bricks on a conveyor belt and routing them to designated bins without human intervention. A camera captures each brick as it passes; a neural network classifies it in real time; the sorting mechanism deflects it into the correct container.

The system addresses a practical problem: manual sorting of bulk LEGO sets is slow, error-prone, and labour-intensive. This solution reduces sorting time by an estimated order of magnitude and produces a machine-readable Bill of Materials (BOM) as a by-product, enabling inventory tracking and set completion analysis.

---

## Architecture

```
Android App  ──HTTP──►  Raspberry Pi 5 (inference server)
                              │
                    ┌─────────┴──────────┐
                    │                    │
               YOLO v11            Arduino Uno × 4
               (classifier)       (motor controllers)
                                        │
                          ┌─────────────┼──────────────┐
                        Conveyor     Servo          IR Sensors
                         Belt      (deflector)
```

| Component | Quantity | Role |
|-----------|----------|------|
| Raspberry Pi 5 | 1 | Central controller, runs inference server, exposes HTTP API |
| Arduino Uno | 4 | Low-level motor and servo control via UART/USB |
| Conveyor motors | 3 | Belt drive, consistent feed rate |
| Servo MG996R | 1 | Deflector gate, routes brick to target bin |
| IR sensors | 4 | Brick presence detection, trigger capture |
| Android device | 1 | Operator UI, displays classification results and BOM |

**Conveyor geometry:** V-groove at 45° centres bricks laterally before the camera zone. Belt speed ~30 cm/s; camera field of view 20 × 20 cm; sorting window 5–8 cm.

---

## Machine Learning Pipeline

### Dataset

- ~2 000 labelled photographs of LEGO DUPLO bricks
- Sources: own captures under controlled lighting + synthetic renders from 3D models
- Annotation format: bounding box + class label (brick type)
- Augmentation: rotation, brightness jitter, background substitution

### Model

**YOLOv11** — chosen for real-time single-pass detection and classification. Training target: ≥ 80% mAP on the validation split, rising to ≥ 95% after full dataset expansion.

Inference runs on Raspberry Pi 5; the model is exported to ONNX for deployment. The Android app sends a JPEG frame via HTTP POST and receives a JSON response containing detected class, confidence, and part ID.

### BOM Generation

Each classification event writes a record to a local database:
```
{ part_id, part_name, colour, quantity, timestamp }
```
The accumulated records form a Bill of Materials exportable as JSON or CSV, compatible with LEGO's own part taxonomy.

---

## Performance

| Metric | Value |
|--------|-------|
| Throughput | 1 brick / 5 s |
| Per minute | 12 bricks |
| Per hour | 720 bricks |
| Per 8-hour shift | 5 760 bricks |

---

## Current Status

The repository is at the **initial stage**. The following has been completed:

- [x] Technical specification finalised
- [x] Component list and budget approved (~79 500 RUB)
- [x] 3D model of the machine (Blender)
- [x] Reference image set for DUPLO bricks collected
- [x] LEGO brick ID dictionary prepared (`Lego_bricks.xlsx`)
- [ ] Dataset labelling and augmentation
- [ ] YOLOv11 training and validation
- [ ] Raspberry Pi inference server
- [ ] Arduino motor control firmware
- [ ] Android application
- [ ] End-to-end integration and field testing

**Timeline:** February 2 – April 30, 2026 (4 sprints).

---

## Skills Applied in This Project

The following Claude Code skills are used across the development lifecycle. Skills marked *(planned)* are not yet invoked but defined for upcoming phases.

### `/tz` — Technical Specification

Generates structured TZ documents from informal descriptions. Used to formalise hardware requirements, define acceptance criteria per sprint, and produce the component specification table.

### `/plan` — Project Calendar

Produces a sprint-by-sprint calendar with hour estimates per role. Used to allocate effort across ML engineer, embedded developer, and Android developer tracks.

### `/ocenka` — Complexity Assessment

Evaluates project difficulty across five axes: technical complexity, scope, uncertainty, integrations, and team. Used at project kickoff to identify the ML pipeline and hardware integration as the highest-risk areas.

### `/pdf-to-md` — Document Conversion *(planned)*

Converts datasheets (Arduino pinouts, RPi GPIO reference, servo specs) from PDF to Markdown for inline reference during development.

### `/preza` — Presentation Generation *(planned)*

Generates Reveal.js HTML slide decks from project notes. Planned for Sprint 4 final demo and academic defence.

### `/img` — Image Generation *(planned)*

Generates synthetic training data: brick renders on varied backgrounds, different lighting conditions, orientations. Supplements the physical photo dataset.

### `/klientu` — Client Communication *(planned)*

Converts informal progress updates into professional reports suitable for academic supervisors and course reviewers.

---

## How Claude Code Accelerates Development

Claude Code is used as an active development partner across three dimensions:

**1. Architecture and design.** At the outset, Claude Code analysed the sorting problem and proposed the current architecture: separating inference (Python on RPi) from motor control (C++ on Arduino) and exposing a clean HTTP boundary between hardware and UI. This decomposition reduced integration risk substantially.

**2. Code generation and review.** Claude Code writes and reviews:
- YOLOv11 training scripts (dataset loading, augmentation pipeline, export to ONNX)
- Arduino firmware for conveyor timing and servo deflection logic
- Raspberry Pi API server (Flask/FastAPI endpoint receiving frames, returning JSON)
- Android HTTP client and BOM display UI

**3. Structured documentation.** TZ, component lists, sprint plans, and this README were produced with Claude Code skills (`/tz`, `/plan`). This keeps documentation consistent with the code and eliminates the gap between specification and implementation.

The workflow is: describe intent in plain language → Claude Code produces a concrete artefact (code, document, or diagram) → developer reviews and refines. Iteration cycles that would take hours are compressed to minutes.

---

## Repository Structure

```
LegoProject/
├── README.md           ← this file
├── ml/                 ← dataset, training scripts, model weights
├── firmware/           ← Arduino C++ sketches (conveyor, servo, sensors)
├── server/             ← Raspberry Pi inference server (Python)
├── android/            ← Android application
└── docs/               ← TZ, BOM schema, sprint reports
```

*(Directories will be populated as development progresses.)*

---

## References

- [YOLOv11 Documentation](https://docs.ultralytics.com)
- [Raspberry Pi 5 Datasheet](https://datasheets.raspberrypi.com/rpi5/raspberry-pi-5-product-brief.pdf)
- [Arduino Uno R3 Reference](https://docs.arduino.cc/hardware/uno-rev3/)
- [LEGO Part Taxonomy](https://rebrickable.com/parts/)

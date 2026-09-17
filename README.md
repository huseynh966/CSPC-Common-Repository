# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course.
Each practical lives under `PW<n>/Lab <X>/`.

## Setup

Create and activate the environment for a given lab:

```bash
conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc
```

Run the tests for a lab from inside its folder:

```bash
cd "PW<n>/Lab <X>"
pytest -v
```

---

## PW1 — Lab A: Reproducible Foundations

**What I built:**
- <one or two lines: the CSPC repo, the environment, the decay simulation, the tests>

**Speed comparison (loop vs NumPy):**

| version | time (s) |
|---------|----------|
| pure-Python loop | 0.2833 s|
| NumPy (vectorised) | 0.0002 s|

- Speed-up: **1222.7449 × faster**

**Tests:** all passing? (yes)

**Conclusion:**
- The NumPy vectorised implementation was considerably faster than the pure-Python loop because NumPy processes entire arrays using highly optimised C code instead of handling each element individually in Python.
- Using Conda environments ensured full reproducibility, allowing the same project environment to be recreated with a single command.
- All three pytest tests passed successfully, verifying that the simulation begins with (N_0), correctly rejects negative decay rates, and follows the expected analytical exponential decay relationship.

---

<!-- Future sessions: add a new "## PW<n> — Lab <X>" section below. -->

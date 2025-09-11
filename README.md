## Barkley Finitewave model

The Barkley model is a simplified two-variable reaction–diffusion system
originally developed to study wave propagation in excitable media. While it is 
not biophysically detailed, it captures essential qualitative features of 
cardiac-like excitation dynamics such as spiral waves, wave break, and reentry.

This model implementation can be used separately from the Finitewave, allowing for standalone simulations and testing of the model dynamics without the need for the entire framework.

### Reference
Barkley, D. (1991).
A model for fast computer simulation of waves in excitable media.
Physica D: Nonlinear Phenomena, 61-70.

DOI: https://doi.org/10.1016/0167-2789(86)90198-1.

### How to use (quickstart)
```bash
python -m examples.barkley_example
```

### How to test
```bash
python -m pytest -q
```

### Repository structure
```text
.
├── barkley/                 # equations package (ops.py)
│   ├── __init__.py
│   └── ops.py               # model equations (pure functions)
├── implementation/          # 0D model implementation
│   ├── __init__.py
│   └── barkley_0d.py
├── example/
│   └── barkley_example.py   # minimal script to run a short trace
├── tests/
│   └── test.py              # smoke test; reproducibility checks
├── .gitignore
├── LICENSE                  # MIT
├── pyproject.toml           # configuration file
└── README.md                # this file
```

### Variables
- `u` — Transmembrane potential (dimensionless).
- `v` — Recovery variable (dimensionless).

### Parameters
- `a = 0.75`   - Threshold-like parameter controlling excitability.
- `b = 0.02`   - Recovery time scale.
- `eps = 0.02` - Controls sharpness of the activation term (nonlinear gain).

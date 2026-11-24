# Energy Usage Predictor

A small educational AI project that estimates building energy usage from floor area, occupants, and outside temperature using Random Forest regression.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python energy_predictor.py --area 120 --occupants 4 --temperature 28
```

## Test

```bash
python -m unittest test_energy_predictor.py
```

The data is synthetic and the output is intended for learning, not operational energy management.

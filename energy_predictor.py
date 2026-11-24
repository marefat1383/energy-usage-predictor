import argparse

import numpy as np
from sklearn.ensemble import RandomForestRegressor

TRAINING_FEATURES = np.array([
    [50, 1, 10], [70, 2, 12], [90, 3, 15], [120, 4, 18],
    [150, 5, 22], [180, 6, 25], [220, 8, 28], [260, 10, 32],
    [80, 1, 30], [130, 3, 35], [200, 5, 5], [300, 12, 20],
], dtype=float)
TRAINING_USAGE = np.array([110, 150, 195, 250, 320, 390, 490, 610, 270, 365, 350, 650], dtype=float)


def build_model() -> RandomForestRegressor:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(TRAINING_FEATURES, TRAINING_USAGE)
    return model


def predict_usage(area: float, occupants: int, temperature: float) -> float:
    if area <= 0 or occupants <= 0 or not -80 <= temperature <= 60:
        raise ValueError("Area and occupants must be positive; temperature must be realistic")
    usage = float(build_model().predict([[area, occupants, temperature]])[0])
    return round(max(0.0, usage), 2)


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate monthly building energy usage.")
    parser.add_argument("--area", type=float, required=True)
    parser.add_argument("--occupants", type=int, required=True)
    parser.add_argument("--temperature", type=float, required=True)
    args = parser.parse_args()
    print(f"Estimated usage: {predict_usage(args.area, args.occupants, args.temperature)} units")


if __name__ == "__main__":
    main()

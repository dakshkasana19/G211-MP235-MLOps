from pathlib import Path

import yaml
from sklearn.ensemble import RandomForestRegressor


def load_config(path: str | Path) -> dict:
    """Read a YAML configuration file and return its top-level mapping."""
    with Path(path).open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream)
    if not isinstance(config, dict):
        raise ValueError("Expected a YAML mapping at the top level.")
    return config


def build_regressor(config: dict) -> RandomForestRegressor:
    """Construct an unfitted random forest using the configured settings."""
    model = config["model"]
    return RandomForestRegressor(
        random_state=model["random_state"],
        n_estimators=model["n_estimators"],
    )

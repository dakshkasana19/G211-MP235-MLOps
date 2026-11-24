from pathlib import Path

import pytest
import yaml
from sklearn.ensemble import RandomForestRegressor

from mp235.train import build_regressor, load_config


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_default_estimator_uses_project_settings():
    config = load_config(PROJECT_ROOT / "params.yaml")
    regressor = build_regressor(config)
    assert isinstance(regressor, RandomForestRegressor)
    assert regressor.get_params()["random_state"] == 42
    assert regressor.get_params()["n_estimators"] == 8


def test_estimator_uses_changed_yaml_settings(tmp_path):
    config = load_config(PROJECT_ROOT / "params.yaml")
    config["model"].update(random_state=17, n_estimators=11)
    alternate_path = tmp_path / "alternate.yaml"
    alternate_path.write_text(yaml.safe_dump(config), encoding="utf-8")
    regressor = build_regressor(load_config(alternate_path))
    assert regressor.get_params()["random_state"] == 17
    assert regressor.get_params()["n_estimators"] == 11


def test_empty_config_has_a_clear_error(tmp_path):
    empty_path = tmp_path / "empty.yaml"
    empty_path.write_text("", encoding="utf-8")
    with pytest.raises(ValueError, match="top level"):
        load_config(empty_path)

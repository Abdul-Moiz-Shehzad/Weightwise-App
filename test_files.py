import os

def test_random_forest_model_exists():
    assert os.path.isfile("RandomForestModel.pkl"), "RandomForestModel.pkl is missing"

def test_label_encoder_exists():
    assert os.path.isfile("LabelEncoder.pkl"), "LabelEncoder.pkl is missing"

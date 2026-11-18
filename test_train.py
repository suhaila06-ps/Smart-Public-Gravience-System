from ml_engine.classifier import ml_engine
import pandas as pd
import json

df = pd.read_csv("datasets/grievance_default_training.csv")
metrics = ml_engine.train(df, version="v1_initial")
print(f"Model successfully trained! Version: {metrics['version']}")
print(f"Accuracy: {metrics['accuracy']}")
print(f"Macro F1: {metrics['f1_macro']}")
print(f"Train samples: {metrics['train_samples']}, Test samples: {metrics['test_samples']}")

# Test live prediction
test_text = "The street light pole collapsed and exposed live electric wires in the street"
pred = ml_engine.predict(test_text)
print("Test text:", test_text)
print("Prediction:", json.dumps(pred, indent=2))

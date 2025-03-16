import openai

# Define the use cases and the criteria for selection
use_cases = ["text generation", "question answering", "summarization"]
criteria = {
    "accuracy": [0.9, 0.8, 0.85],  # Hypothetical accuracy scores for each use case
    "speed": [1.0, 0.8, 0.9],      # Hypothetical speed scores for each use case
    "model_size": [0.8, 0.9, 0.85] # Hypothetical model size scores for each use case
}

# Define available LLMs (hypothetical examples)
models = {
    "gpt-3.5": {"accuracy": [0.95, 0.85, 0.9], "speed": [0.9, 0.8, 0.85], "model_size": [0.8, 0.9, 0.85]},
    "gpt-4": {"accuracy": [0.98, 0.9, 0.95], "speed": [0.85, 0.75, 0.8], "model_size": [0.75, 0.85, 0.8]},
    "bert-large": {"accuracy": [0.9, 0.8, 0.85], "speed": [0.8, 0.7, 0.75], "model_size": [0.85, 0.95, 0.9]}
}

def evaluate_models(models, use_cases, criteria):
    scores = {}
    for model_name, model_scores in models.items():
        total_score = 0
        for i, use_case in enumerate(use_cases):
            use_case_score = 0
            for criterion, weights in criteria.items():
                use_case_score += weights[i] * model_scores[criterion][i]
            total_score += use_case_score
        scores[model_name] = total_score / len(use_cases)
    return scores

# Evaluate the models
model_scores = evaluate_models(models, use_cases, criteria)

# Find the best model
best_model = max(model_scores, key=model_scores.get)
print(f"The best suitable LLM for the use cases is: {best_model} with a score of {model_scores[best_model]:.2f}")

# Optionally, you can print the scores for all models
print("Scores for all models:")
for model, score in model_scores.items():
    print(f"{model}: {score:.2f}")

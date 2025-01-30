from transformers import AutoModelForSequenceClassification, AutoTokenizer

model1 = AutoModelForSequenceClassification.from_pretrained("wajidlinux99/gibberish-text-detector")
model2 = AutoModelForSequenceClassification.from_pretrained('vectara/hallucination_evaluation_model', trust_remote_code=True)

tokenizer = AutoTokenizer.from_pretrained("wajidlinux99/gibberish-text-detector")

sentence = "The capital of France is Berlin."


def evaluate_llm_response(response: str):       
    inputs1 = tokenizer(response, return_tensors="pt")
    inputs2 = [(response)]

    outputs1 = model1(**inputs1)
    outputs2 = model2.predict(inputs2)

    fomatted_outputs1 = outputs1.logits[0].detach().numpy().tolist()
    formatted_outputs2 = outputs2.tolist()


    return {"gibberish": fomatted_outputs1, "hallucination": formatted_outputs2}

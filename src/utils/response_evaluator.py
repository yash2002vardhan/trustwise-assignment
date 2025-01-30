from transformers import AutoModelForSequenceClassification, AutoTokenizer

gibberish_detector_model = AutoModelForSequenceClassification.from_pretrained("wajidlinux99/gibberish-text-detector")
hallucination_detector_model = AutoModelForSequenceClassification.from_pretrained('vectara/hallucination_evaluation_model', trust_remote_code=True)

gibberish_tokenizer = AutoTokenizer.from_pretrained("wajidlinux99/gibberish-text-detector")


gibberish_classification = {
    0: "clean",
    1: "mild gibberish", 
    2: "noise",
    3: "word salad"
  }


def evaluate_llm_response(response: str):       
    gibberish_input = gibberish_tokenizer(response, return_tensors="pt")
    hallucination_input = [(response)]

    gibberish_output = gibberish_detector_model(**gibberish_input)
    hallucination_output = hallucination_detector_model.predict(hallucination_input)


    gibberish_class_index = gibberish_output.logits[0].detach().numpy().argmax()
    gibberish_class_label = gibberish_classification[gibberish_class_index]
    gibberish_confidence = max(gibberish_output.logits[0].detach().numpy().tolist())
    hallucination_confidence = hallucination_output.tolist()[0]


    return {"gibberish": {"class" : gibberish_class_label, "score" : gibberish_confidence}, "hallucination": hallucination_confidence}

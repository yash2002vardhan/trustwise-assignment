# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install PDM and dependencies
RUN pip install pdm && \
    pdm install --no-lock --no-editable

RUN pdm run python -c "from transformers import AutoModelForSequenceClassification, AutoTokenizer; \
    AutoModelForSequenceClassification.from_pretrained('wajidlinux99/gibberish-text-detector'); \
    AutoModelForSequenceClassification.from_pretrained('vectara/hallucination_evaluation_model', trust_remote_code=True); \
    AutoTokenizer.from_pretrained('wajidlinux99/gibberish-text-detector')"

EXPOSE 8000

CMD ["pdm", "run", "prod"]

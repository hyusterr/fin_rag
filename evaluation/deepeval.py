import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from deepeval.models.base_model import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric, ContextualPrecisionMetric, ContextualRecallMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase

RELEVENCE_PROMPT = """Please extract relevant sentences from the provided context that can potentially help answer the following question. 
If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase "Insufficient Information". 
While extracting candidate sentences you’re not allowed to make any changes to sentences
from given context."""

MISTRAL_PROMPT = "<s>[INST]" + RELEVENCE_PROMPT + "[/INST]"

class LocalLLM(DeepEvalBaseLLM):
    def __init__(
        self,
        model,
        tokenizer
    ):
        self.model = model
        self.tokenizer = tokenizer

        self.prompt = RELEVENCE_PROMPT
        if "mistral" in model.name_or_path.lower():
            self.prompt = MISTRAL_PROMPT

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        model = self.load_model()

        device = "cuda" # the device to load the model onto

        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(device)
        model.to(device)

        generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)
        return self.tokenizer.batch_decode(generated_ids)[0]

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return "Mistral 7B"


'''
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

mistral_7b = Mistral7B(model=model, tokenizer=tokenizer)
print(mistral_7b.generate("Write me a joke"))
'''

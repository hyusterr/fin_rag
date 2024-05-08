import os
from transformers import AutoModelForCausalLM, AutoTokenizer
from deepeval.models.base_model import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric, ContextualPrecisionMetric, ContextualRecallMetric, ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase


# TODO: revise it for our financial task retrieval
RELEVENCE_PROMPT = """Please extract relevant sentences from the provided context that provide relevant information to the target paragraph. 
If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase "Insufficient Information". 
While extracting candidate sentences you’re not allowed to make any changes to sentences
from given context."""

MISTRAL_PROMPT = "<s>[INST]" + RELEVENCE_PROMPT + "[/INST]"
MISTRAL_7B_INSTRUCT_2 = "mistralai/Mistral-7B-Instruct-v0.2"

class MistralDeepEvalLLM(DeepEvalBaseLLM):
    '''
    Customize LLM evaluation model with DeepEval
    1. inherit DeepEvalBaseLLM
    '''
    def __init__(
        self,
        # model,
        # tokenizer,
    ):
        self.model = AutoModelForCausalLM.from_pretrained(MISTRAL_7B_INSTRUCT_2, device_map='auto')
        # TODO: manage cache to prevent every user download the model every time they run and thus spam cfda's home/
        self.tokenizer = AutoTokenizer.from_pretrained(MISTRAL_7B_INSTRUCT_2)
        # TODO: check how to revise the prompt since mistral-intstruct has special token [INST]
        self.prompt = MISTRAL_PROMPT

    def get_model_name(self):
        '''
        2. implement the get_model_name() method, which simply returns a string representing your custom model name.
        '''
        return MISTRAL_7B_INSTRUCT_2

    def load_model(self):
       '''
       3. implement the load_model() method, which will be responsible for returning a model object.
       '''
       return self.model


    def generate(self, prompt: str) -> str:
        '''
        4. implement the generate() method with one and only one parameter of type string that acts as the prompt to your custom LLM. the generate() method should return the final output string of your custom LLM. 
        '''
        # TODO: check how to add special token [INST] to the prompt, this would be critical for mistral-instruct models
        model = self.load_model() # assume already use device_map='auto'

        model_inputs = self.tokenizer([prompt], return_tensors="pt")

        generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)
        return self.tokenizer.batch_decode(generated_ids)[0]

    async def a_generate(self, prompt: str) -> str:
        '''
        5. implement the a_generate() method, with the same function signature as generate(). Note that this is an async method.
        '''
        return self.generate(prompt)



'''
class LocalLLM:
    def __init__(self, model_name, device, torch_dtype=torch.float16, genration_config=None) -> None:
        self.model_name = model_name
        self.device = device

        if self.device == "auto_map":
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name, device_map='auto', torch_dtype=torch_dtype)
        else:
            # TODO: check syntax
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name, device=self.device, torch_dtype=torch_dtype)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        
        # TODO: use pipeline to accelerate inference
        self.pipeline = None

        genration_config = None
        if genration_config:
            self.genration_config = genration_config


        self.prompt = RELEVENCE_PROMPT
        if "mistral" in model_name.lower():
            self.prompt = MISTRAL_PROMPT

    def generate(self, string: str) -> str:
        model = self.model

        model_inputs = self.tokenizer([string], return_tensors="pt").to(self.device)
        model.to(self.device)

        generated_ids = model.generate(**model_inputs, max_new_tokens=100, do_sample=True)
        return self.tokenizer.batch_decode(generated_ids)[0]


    def evaluate_topK(self, target_id, context_ids: List[str], topK=5):
        
        # preprocess the context associated with the target_id
        target_text = None
        for c_id in context_ids:
            pass


model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

mistral_7b = Mistral7B(model=model, tokenizer=tokenizer)
print(mistral_7b.generate("Write me a joke"))
'''

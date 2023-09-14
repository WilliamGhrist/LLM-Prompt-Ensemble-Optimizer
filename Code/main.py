import langchain
from langchain import PromptTemplate, LLMChain
from langchain.llms import TextGen, OpenAI
import subprocess
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Defines the shared components of the LLM chains and alows for the different models to be passed in reducing code redundancy.
# This will aid scalability in the future if more Language Models are added, so the same components don't have to keep being defined.
def generate_chain(llm, question, num_variations):

    """
    Args:
    - llm: Language learning model instance
    - question: User input question
    - num_variations: Number of unique answer variations
    
    Returns:
    - text: The generated answer from the model
    """

    template = """
    Below is an instruction that describes a task. Write a response that appropriately completes the request.

    Instruction: Your task is to generate {num_variations} different unique versions of the given user question. 
    Generate these versions from different perspectives and in different tones.  
    Please take the given question, make these variations and then answer each question 
    variation in a unique way based off its subtle differences from the others. 
    please ONLY return the ANSWERS you generate NOT the questions, and make sure you generate ALL {num_variations} anwsers separated by new lines.

    Input:{question}

    Response:
    """
    prompt = PromptTemplate(template=template, input_variables=["question", "num_variations"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    model_response = llm_chain({'question': question, 'num_variations': num_variations})
    return model_response["text"]


# Generates answers using the OpenAI GPT model.
def openAI_gpt(question, num_variations):    

    """
    Args:
    - question: User input question
    - num_variations: Number of unique answer variations
    
    Returns:
    - text: The generated answer from the OpenAI GPT model
    """

    llm = OpenAI(openai_api_key = OPENAI_API_KEY,
                 temperature = 0.3,
                 model_name = "text-davinci-003")
    
    return generate_chain(llm, question, num_variations)


# Generates answers using the locally ran and finetuned Llama model.
def local_llama(question, num_variations):

    """
    Args:
    - question: User input question
    - num_variations: Number of unique answer variations
    
    Returns:
    - text: The generated answer from the local Llama model
    """

    cmd = ["python", "/home/ghrist/text-generation-webui/server.py", "--model", "Llama-2-7b-hf", "--lora", "test-4bit", "--api"]
    process = subprocess.Popen(cmd, cwd="/home/ghrist/text-generation-webui")
    langchain.debug = True

    model_url = "http://localhost:5000"
    llm = TextGen(model_url=model_url)
    
    response = generate_chain(llm, question, num_variations)
    process.terminate()

    return response


# Consolidates a list of answers into a single ultimate answer controlling for randomness.
def answer_consolidator_chain(all_answers):

    """
    Args:
    - all_answers: List of answers to be consolidated
    
    Returns:
    - text: The consolidated answer
    """

    template = """  
    I will provide you with a list of answers, all addressing the same question but in slightly varying ways. 
    Your task is to analyze and consolidate these answers into one cohesive and representative response. 
    In your consolidation, prioritize the common consensus found in the majority of the answers. 
    If certain answers deviate or introduce unique points, weigh them less in favor of the prevailing sentiment or information presented by the majority. 
    Produce a single, ultimate answer that best represents the collective input, controlling for any outliers or randomness.
    The list of answers to perform this on are as follows: {all_answers}
    """ 
    prompt_template = PromptTemplate(
        input_variables=["all_answers"], 
        template=template
    )

    llm = OpenAI(
        openai_api_key=OPENAI_API_KEY,
        temperature=0.3,
        max_tokens=500,
        model_name="text-davinci-003"
        )

    consolidator_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)
    response = consolidator_chain({all_answers})
    
    return response["text"]



if __name__ == "__main__":
    question = "Why is the sky blue?"
    num_variations = 5

    tv1 = local_llama(question, num_variations)
    tv2 = openAI_gpt(question, num_variations)

    both_answers = tv1 + "\n" + tv2

    answer_consolidator_chain(both_answers)

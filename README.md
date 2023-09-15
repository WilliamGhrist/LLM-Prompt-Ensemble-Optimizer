# LLM-Prompt-Ensemble-Optimizer

<img src="https://github.com/WilliamGhrist/LLM-Prompt-Ensemble-Optimizer/assets/133531386/4a96a955-b3ca-45c4-aa66-14b97c496ff2" width="600">

<img src="https://github.com/WilliamGhrist/LLM-Prompt-Ensemble-Optimizer/assets/133531386/ae6985f9-cdb0-48d8-88fc-279898e49949" width="600">


## Table of Contents
1. [Project Description](#project-description)
2. [Training the Local Model](#training-the-local-model)
3. [Install and Run the Project](#install-and-run-the-project)
4. [Built Using](#build-using)
5. [Acknowledgements](#acknowledgements)
6. [Contact](#contact)

## Project Description

The aim of this project is to create a robust tool that counters the inherent randomness and potential hallucinations seen in LLM outputs. 
By doing so, I aim to elevate the quality, consistency, and breadth of the responses provided by LLMs.
To do this the app receives a user's question and sends it to multiple LLMs which then generate a set number of nuanced variations of the original question. As a result of these slight question adjustments, the following answers generated have varied perspectives and interpretations, enabling a more comprehensive answer spectrum. The full list of answer variations are then combined down to one ultimate answer, favoring similarities and controlling for randomness.   

For the sake of keeping things relatively uncomplicated and considering the associated API costs, the current version of this app communicates with just two LLMs and is restricted to producing a maximum of 10 variations per question.
This means that while the tool mostly preforms well, there might still be occasional randomness or error in its output. The foundational concept however, if scaled, has immense potential. A future iteration of the app could utilize a multitude of distinctively trained models, each generating hundreds of variations on the input. Such an expansion would not only gurentee its defense against randomness but also refine the richness and depth of returned output.


## Downlaoding, Running, and Training the Local Model

1. Set up the [TextGen WebUI](https://github.com/oobabooga/text-generation-webui) tool. 

2. Dowload your desired text generation model from [Huggingface](https://huggingface.co/models?pipeline_tag=text-generation&sort=trending)

3. Load the model in the TextGen tool. If you are getting errors due to insufficient memory, try enabling either of the following options:

    ` auto-devices `


    ` load-in-4bit `

4. To train a LoRA, (Low Rank Adaptation) you will need an Alpaca formatted dataset.  This is a JSON file that contains the following structure. 

    ``` 
    "instruction":"" 
    "input":""
    "output":""
    ``` 
    Feel free to use the dataset I created specificaly for this project [alpaca_formated_dataset](Alpaca%20formatted%20LoRA%20training%20data/alpaca_formated.json)


5. On the Training tab of the TextGen tool, name your LoRA, set your parameters, select your training data set, and hit Start LoRA Training.

6. Once your LoRA has finished training you can apply it the model to see the difference in output.

## Install and Run the Project
### Prerequisites

- Ensure you have Python 3.x installed on your system.
- Setup the TextGen WebUI tool and dowload desired model or models.
- Ensure you have a working OpenAI API key.

### Setup
install requirments
```
pip install langchain
pip install streamlit
```

Clone Repo 

`git clone https://github.com/WilliamGhrist/LLM-Prompt-Ensemble-Optimizer.git`

You will need to change the code in lines 76 and 77 of main.py
to include your file path, the name of your model, and the name of your LoRA if you choose to use one.
```
cmd = ["python", "/YOUR_FILE_PATH/server.py", "--model", "MODEL_NAME", "--lora", "LORA_NAME", "--api"]
    process = subprocess.Popen(cmd, cwd="/DIRECTORY_OF_text-generation-webui_TOOL")
```

### Usage
1. Export your OpenAI API key as an enviornment variable in the terminal by running the following command.

    `export OPENAI_API_KEY="YOUR_API_KEY_HERE"`

2. Navigate to the project directory and run the streamlit app:

    `streamlit run app.py`

3. Input your prompt and select your desired number of variations. 


## Built Using

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

[🦜️🔗 LangChain](https://github.com/langchain-ai/langchain#%EF%B8%8F-langchain)

[TextGen WebUI](https://github.com/oobabooga/text-generation-webui)

## Acknowledgements

Thanks to Oobabooga for the [TextGen WebUI](https://github.com/oobabooga/text-generation-webui) tool.

## Contact

[Linkedin](https://www.linkedin.com/in/william-ghrist-736509203)






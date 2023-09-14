import streamlit as st
from main import openAI_gpt, local_llama, answer_consolidator_chain

st.title("Prompt Ensemble Optimizer")

# Allow the user to input their prompt and select the number of variations
user_input = st.text_input("Please enter your prompt:")
variations = st.selectbox("Select the number of variations sent to each LLM:", options=[3, 5, 10])

if st.button('Submit'):
    # Check if both user_input and variations are provided
    if user_input and variations:
        # Run the two chains with the user's input and variations
        openAI_answers = openAI_gpt(user_input, variations)
        local_llama_answers = local_llama(user_input, variations)

        # Concatenate the answers 
        all_answers = openAI_answers + "\n" + local_llama_answers
        
        # Run the answer_consolidator_chain and get the final answer
        final_answer = answer_consolidator_chain(all_answers)

        # Display the final answer to the user
        st.write("Final Answer:", final_answer)
    else:
        st.write("Please provide both the prompt and the number of variations to proceed.")
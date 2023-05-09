import streamlit as st

from transformers import *
# from parrot import Parrot
# import torch
# import warnings
# import openai

import os
from dotenv import load_dotenv

# warnings.filterwarnings("ignore")
load_dotenv()

# def chatgpt_paraphrase(input: str) -> str:
#     openai.api_key: str = os.getenv("CHATGPT_KEY")
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": "Paraphrase this\n" + input}]
#     )
#     reply_content = completion.choices[0].message.content
    
#     return reply_content

# def parrot_paraphrase(input: str) -> [str]:
#     torch.manual_seed(1234)
#     if torch.cuda.is_available():
#         torch.cuda.manual_seed_all(1234)
        
#     parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
    
#     for phrase in phrases:
#         para_phrases = parrot.augment(input_phrase=phrase)
#         return para_phrases[0]

def transformer_paraphrase(input: str) -> str:
    model = PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
    tokenizer = PegasusTokenizerFast.from_pretrained("tuner007/pegasus_paraphrase")
    num_return_sequences = 1
    num_beams = 1
    inputs = tokenizer([input], truncation=True, padding="longest", return_tensors="pt")
    outputs = model.generate(
        **inputs,
        num_beams=num_beams,
        num_return_sequences=num_return_sequences,
    )
    
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    

original_text: str = ""
st.title("Simple paraphrasing tool")
user_input: str = st.text_area('Text to paraphrase', 
'''It was the best of times, it was the worst of times, it was
the age of wisdom, it was the age of foolishness, it was
the epoch of belief, it was the epoch of incredulity, it
was the season of Light, it was the season of Darkness, it
was the spring of hope, it was the winter of despair.''')

if st.button('Paraphrase'):
    original_text = user_input
    if original_text not in [None, ""]:
        paraphrase_text = transformer_paraphrase(original_text)
        st.subheader("Original text: " + original_text)
        result = st.text_area("Paraphrased:", paraphrase_text)
    else:
        st.error('Empty paraphrase text', icon="🚨")
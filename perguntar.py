import pandas as pd
from time import sleep
import os
from datetime import datetime

from groq import Groq
import google.generativeai as genai
from openai import OpenAI
from maritalk import MariTalk
import anthropic
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def modelLLM(cliente, current_model, question):
    return cliente.chat.completions.create(
          model=current_model,
          messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
          ],
          temperature=0
        ).choices[0].message.content

def anthropic_create(cliente, current_model, question):
    return cliente.messages.create(
            model=current_model,
            max_tokens=100,
            system = prompt,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        }
                    ]
                }
            ]
        ).content[0].text

def mistral_chat(cliente, current_model, question):
    return cliente.chat(
            model=current_model,
            temperature=0,
            messages=[ChatMessage(role="user", content = prompt + question)]
        ).choices[0].message.content

def gemini(current_model, question):
    try:
        response = genai.GenerativeModel(model_name = current_model, generation_config={"temperature":0}).generate_content(prompt + question)
        #print(response)
        return response.text if response else 'Answer blocked'
    except ValueError as e:
        print(f"Error generating content with model {current_model}: {e}")
        return 'Error generating content'

def question_geminiPro(df, index = 0, save = True) -> None:
    genai.configure(api_key=os.environ.get('GEMINI_PRO_API_KEY'))
    for i in range(index, len(df)):
        df.loc[i, 'gemini-1.5-pro'] = gemini('gemini-1.5-pro-latest', df['question'][i])
        print(f'{i}/{len(df)}')

    if save is True:
        df.to_excel("enam-exams-" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx", index=False)

    return None

def question_all(df, index = 0, save = True) -> None:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    openAI_client = OpenAI()
    anthropic_client = anthropic.Anthropic()
    mistral_client = MistralClient(api_key='')

    yi_client = OpenAI(api_key='', base_url="https://api.01.ai/v1")
    deepSeek_client = OpenAI(api_key='', base_url="https://api.deepseek.com")
    deepInfra_client= OpenAI(api_key='', base_url="https://api.deepinfra.com/v1/openai")

    chave_maritaca = ''
    sabia2m_client = MariTalk(key=chave_maritaca, model="sabia-2-medium")
    sabia2s_client = MariTalk(key=chave_maritaca, model="sabia-2-small")
    sabia3_client = MariTalk(key=chave_maritaca, model="sabia-3")
    
    for i in range(index, len(df)):
        df.loc[i, 'gpt-3.5-turbo'] = modelLLM(openAI_client, 'gpt-3.5-turbo-0125', df['question'][i])
        df.loc[i, 'gpt-4o'] = modelLLM(openAI_client,'gpt-4o-2024-05-13', df['question'][i])
        df.loc[i, 'gpt-4o-mini'] = modelLLM(openAI_client,'gpt-4o-mini-2024-07-18', df['question'][i])
        df.loc[i, 'gemini-1.5-flash'] = gemini('gemini-1.5-flash-latest', df['question'][i])
        df.loc[i, 'gemini-1.0-pro'] = gemini('gemini-pro', df['question'][i])
        df.loc[i, 'gemma-7b-it'] = modelLLM(groq_client, 'gemma-7b-it', df['question'][i])
        df.loc[i, 'gemma2-9b'] = modelLLM(groq_client, 'gemma2-9b-it', df['question'][i])
        df.loc[i, 'gemma2-27b'] = modelLLM(deepInfra_client, 'google/gemma-2-27b-it', df['question'][i])
        df.loc[i, 'llama3-8b'] = modelLLM(groq_client, 'llama3-8b-8192', df['question'][i])
        df.loc[i, 'llama3-70b'] = modelLLM(groq_client, 'llama3-70b-8192', df['question'][i])
        df.loc[i, 'llama-3.1-405B'] = modelLLM(deepInfra_client, 'meta-llama/Meta-Llama-3.1-405B-Instruct', df['question'][i])
        df.loc[i, 'llama-3.1-70B'] = modelLLM(deepInfra_client, 'meta-llama/Meta-Llama-3.1-70B-Instruct', df['question'][i])
        df.loc[i, 'llama-3.1-8B'] = modelLLM(deepInfra_client, 'meta-llama/Meta-Llama-3.1-8B-Instruct', df['question'][i])
        df.loc[i, 'Mistral-7B-v0.3'] = modelLLM(deepInfra_client, 'mistralai/Mistral-7B-Instruct-v0.3', df['question'][i])
        df.loc[i, 'mixtral-8x7b'] = modelLLM(groq_client, 'mixtral-8x7b-32768', df['question'][i])
        df.loc[i, 'Mixtral-8x22B-v0.1'] = modelLLM(deepInfra_client, 'mistralai/Mixtral-8x22B-Instruct-v0.1', df['question'][i])
        df.loc[i, 'Mistral-Large-2'] = mistral_chat(mistral_client , 'mistral-large-latest', df['question'][i])
        df.loc[i, 'Mistral-Nemo'] = mistral_chat(mistral_client , 'open-mistral-nemo', df['question'][i])
        df.loc[i, 'sabia-2-medium'] = sabia2m_client.generate(prompt+df['question'][i], temperature=0)["answer"]
        df.loc[i, 'sabia-2-small'] = sabia2s_client.generate(prompt+df['question'][i], temperature=0)["answer"]
        df.loc[i, 'sabia-3'] = sabia3_client.generate(prompt+df['question'][i], temperature=0)["answer"]
        df.loc[i, 'Qwen2-7B'] = modelLLM(deepInfra_client, 'Qwen/Qwen2-7B-Instruct', df['question'][i])
        df.loc[i, 'Qwen2-72B'] = modelLLM(deepInfra_client, 'Qwen/Qwen2-72B-Instruct', df['question'][i])
        df.loc[i, 'Claude-3-Opus'] = anthropic_create(anthropic_client, 'claude-3-opus-20240229', df['question'][i])
        df.loc[i, 'Claude-3-Sonnet'] = anthropic_create(anthropic_client, 'claude-3-sonnet-20240229', df['question'][i])
        df.loc[i, 'Claude-3-Haiku'] = anthropic_create(anthropic_client, 'claude-3-haiku-20240307', df['question'][i])
        df.loc[i, 'Claude-3.5-Sonnet'] = anthropic_create(anthropic_client, 'claude-3-5-sonnet-20240620', df['question'][i])
        df.loc[i, 'yi-Large'] = modelLLM(yi_client, 'yi-large', df['question'][i])
        df.loc[i, 'deepSeek-V2'] = modelLLM(deepSeek_client, 'deepseek-chat', df['question'][i])

        sleep(4)
        print(f'{i}/{len(df)}')

    if save is True:
        df.to_excel("enam-exams-" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xlsx", index=False)

    return None

def main():
    question_geminiPro(df)
    question_all(df)

if __name__ == '__main__':
    prompt = """Responda à seguinte questão do Exame Nacional de Magistratura. Ela tem cinco opções de resposta (A, B, C, D e E) e somente uma delas está correta.
    A sua resposta deve seguir o seguinte padrão: 'A alternativa correta é a alternativa: <LETRA>.
    Aqui está a questão:\n"""
    df = pd.read_excel('enam-exams-onlyQuestions.xlsx')

    main()
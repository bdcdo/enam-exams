import pandas as pd
import re

def option_chosen(text):
    if pd.isna(text):
        return None
    if text == 'Error generating content':
        return 'NA'
    
    text = re.sub(r'\*\*', '', str(text))

    match = re.search(r'A alternativa correta é(?: a(?: alternativa| opção| letra)?)?:?\s*[\(\[]?(\w)[\)\]]?', text)
    if match:
        return match.group(1)
    return None

def check_answers():
    for model in models:
        df[model+'_AnswerChoice'] = df[model].apply(option_chosen)
        df[model+'_AnswerIsRight'] = df.apply(lambda row: 1 if row[model+'_AnswerChoice'] == row['answer'] else 0, axis=1)

def check_all_scores(df, models):
    results = []

    for model in models:
        soma_modelo = df[model + '_AnswerIsRight'].sum()
        nota_percentual = (soma_modelo / 160) * 100
        performance_by_exam = df.groupby('edition')[model + '_AnswerIsRight'].sum()

        results.append({
            'Model': model,
            'Total Performance (%)': nota_percentual,
            'Performance by Exam': performance_by_exam.to_dict()
        })

    results_df = pd.DataFrame(results)
    results_df.to_excel('model_performance.xlsx', index=False)

if __name__ == '__main__':
    models = ['llama3-8b', 'llama3-70b', 'mixtral-8x7b', 'gemma-7b-it', 'gemini-1.5-flash', 'gemini-1.0-pro' , 'gpt-3.5-turbo', 'gpt-4o', 'gemini-1.5-pro',
              'Yi-Large', 'gemma2-9b', 'sabia-2-medium', 'sabia-2-small', 'sabia-3', 'DeepSeek-V2', 'gpt-4o-mini', 'Mistral-7B-v0.3',
              'Mixtral-8x22B-v0.1',	'gemma2-27b', 'Qwen2-7B', 'Qwen2-72B', 'Claude-3.5-Sonnet', 'llama-3.1-405B', 'llama-3.1-70B',
              'llama-3.1-8B', 'Claude-3-Opus', 'Claude-3-Sonnet', 'Claude-3-Haiku', 'Mistral-Large-2', 'Mistral-Nemo']
    df = pd.read_excel('enam-exams-20240801181840.xlsx')

    check_answers()
    check_all_scores(df, models)

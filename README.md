# Performance de modelos de linguagem no ENAM
Esse repositório busca organizar os códigos utilizados para avaliar diferentes modelos de linguagem no ENAM.
Todos os modelos foram testados em temperatura 0.
Sempre que possível, utilizei como provedor dos modelos de linguagem as empresas que os desenvolveram. Quando isso não foi possível, utilizei prioritariamente o Groq e, subsidiariamente, o DeepInfra.


# Resultados do Desempenho dos Modelos

A tabela abaixo apresenta o desempenho total em porcentagem e o desempenho por exame dos modelos avaliados.

| Model               | Total Performance (%) | Performance by Exam  |
|---------------------|-----------------------|----------------------|
| Claude-3.5-Sonnet   | 71,875                | {1: 59, '1a': 56}    |
| gpt-4o              | 68,125                | {1: 55, '1a': 54}    |
| Claude-3-Opus       | 66,25                 | {1: 53, '1a': 53}    |
| sabia-3             | 65,625                | {1: 51, '1a': 54}    |
| llama-3.1-405B      | 61,25                 | {1: 52, '1a': 46}    |
| gemini-1.5-pro      | 56,25                 | {1: 48, '1a': 42}    |
| Qwen2-72B           | 56,25                 | {1: 47, '1a': 43}    |
| llama-3.1-70B       | 55                    | {1: 45, '1a': 43}    |
| Claude-3-Haiku      | 51,25                 | {1: 44, '1a': 38}    |
| gpt-4o-mini         | 50,625                | {1: 42, '1a': 39}    |
| Mixtral-8x22B-v0.1  | 50,625                | {1: 43, '1a': 38}    |
| Yi-Large            | 50                    | {1: 41, '1a': 39}    |
| sabia-2-medium      | 50                    | {1: 45, '1a': 35}    |
| Mistral-Large-2     | 50                    | {1: 45, '1a': 35}    |
| Claude-3-Sonnet     | 48,75                 | {1: 41, '1a': 37}    |
| llama3-70b          | 48,125                | {1: 41, '1a': 36}    |
| DeepSeek-V2         | 47,5                  | {1: 42, '1a': 34}    |
| gemini-1.5-flash    | 45,625                | {1: 38, '1a': 35}    |
| sabia-2-small       | 44,375                | {1: 36, '1a': 35}    |
| gemma2-27b          | 43,75                 | {1: 38, '1a': 32}    |
| Qwen2-7B            | 43,125                | {1: 34, '1a': 35}    |
| gemini-1.0-pro      | 42,5                  | {1: 36, '1a': 32}    |
| gpt-3.5-turbo       | 42,5                  | {1: 34, '1a': 34}    |
| mixtral-8x7b        | 40                    | {1: 35, '1a': 29}    |
| gemma2-9b           | 36,875                | {1: 30, '1a': 29}    |
| Mistral-Nemo        | 36,875                | {1: 31, '1a': 28}    |
| llama3-8b           | 35,625                | {1: 32, '1a': 25}    |
| llama-3.1-8B        | 31,25                 | {1: 27, '1a': 23}    |
| gemma-7b-it         | 30,625                | {1: 28, '1a': 21}    |
| Mistral-7B-v0.3     | 26,25                 | {1: 23, '1a': 19}    |

1 corresponde ao primeiro ENAM e 1a à reaplicação desse exame.
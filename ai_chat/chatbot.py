import requests
def chat_completion(user_input: str) -> str:
    url = "https://api.siliconflow.com/v1/chat/completions"
    API_KEY = "<token>"
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "stream": False,
        "max_tokens": 4096,
        "stop": None,
        "temperature": 0.95,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.0,
        "n": 1,
        "response_format": {"type": "text"},
        "tools": [
            {
                "type": "function",
                "function": {
                    "description": "<string>",
                    "name": "<string>",
                    "parameters": {},
                    "strict": False
                }
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()['choices'][0]['message']['content']
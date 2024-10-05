import requests
import json

def send_gemini_request(api_key, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Return the response in JSON format if available
    if response.status_code == 200:
        
        return response.json()
    else:
        return {
            "error": f"Request failed with status code {response.status_code}",
            "details": response.text
        }
    
#def servicing(): # for servicing the string from gemini


# Example usage
api_key = "AIzaSyAlM7eYJntG24kjPc6W4t2Z9AaeFG_DUj8"
prompt = "Explain how AI works"
response = send_gemini_request(api_key, prompt)
print(response['candidates'][0]['content']['parts'][0]['text'])


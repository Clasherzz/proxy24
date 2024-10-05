# import requests
# import json

# def send_gemini_request(api_key, prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
#     headers = {
#         'Content-Type': 'application/json',
#     }

#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {
#                         "text": prompt
#                     }
#                 ]
#             }
#         ]
#     }

#     # Send POST request
#     response = requests.post(url, headers=headers, data=json.dumps(data))

#     # Return the response in JSON format if available
#     if response.status_code == 200:
        
#         return response.json()
#     else:
#         return {
#             "error": f"Request failed with status code {response.status_code}",
#             "details": response.text
#         }
    
# #def servicing(): # for servicing the string from gemini


# # Example usage
# api_key = "AIzaSyAlM7eYJntG24kjPc6W4t2Z9AaeFG_DUj8"
# prompt = "Explain how AI works"
# response = send_gemini_request(api_key, prompt)
# print(response['candidates'][0]['content']['parts'][0]['text'])

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
    
def servicing(str_response): # for servicing the string from gemini
    try:
        questions = json.loads(str_response) 
    except json.JSONDecodeError as e:
        print(f"Error parsing the JSON response: {e}")
        questions = []

    # print(questions)
    return questions


# Example usage
api_key = "AIzaSyAlM7eYJntG24kjPc6W4t2Z9AaeFG_DUj8"
numberOfQuestions = "10"
topic = "Linux Commands"
level = "Beginner"
# prompt = "Generate "+numberOfQuestions+" questions based on the topic of "+topic+" at the "+level+' level. Each question should have a single correct answer. Format the output as follows: [{"question": "Question 1", "ans": 1}, {"question": "Question 2", "ans": 3}, {"question": "Question 3", "ans": 1}]. Please provide no additional output, just this format. Please don\'t miss any braces, key-value pairs and brackets. the result must be an list of dictionaries.'
prompt = f"Generate {numberOfQuestions} questions on the topic '{topic}' at the '{level}' level. Each question should have one correct answer. Format the output strictly as a list of dictionaries, like this: [{{'question': 'Question 1', 'ans': 1}}, {{'question': 'Question 2', 'ans': 3}}, {{'question': 'Question 3', 'ans': 1}}]. Ensure the format is valid JSON with no missing braces, brackets, or key-value pairs. Provide only the list of dictionaries as output, nothing else."


response = send_gemini_request(api_key, prompt)
str_response = response['candidates'][0]['content']['parts'][0]['text']
# print(type(str_response))
list_response = servicing(str_response)
# print(type(list_response))
# print(list_response[0])
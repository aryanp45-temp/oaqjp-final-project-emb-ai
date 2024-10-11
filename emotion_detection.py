import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send a POST request to the Watson Emotion Predict endpoint
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    
    # Return the "text" attribute of the response object
    return response_data.get("text", "No emotion data found")

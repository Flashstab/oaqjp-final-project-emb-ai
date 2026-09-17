import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = body)
    
    dic = response.json()
    
    emotions = dic['emotionPredictions'][0]['emotion']
    angerScore = emotion['anger']
    disgustScore = emotion['disgust']
    fearScore = emotion['fear']
    joyScore = emotion['joy']
    sadnessScore = emotion['sadness']
    
    topScore = max(emotions, key=emotions.get())

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}
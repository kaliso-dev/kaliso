import requests

# Remplace "TON_TOKEN" par ton token API Hugging Face
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
headers = {"Authorization": "Bearer hf_zFtjAQMczDZNpwkyXCwXWkfswpJUlHpmmEs"}

def chatbot(prompt):
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Lève une exception si la requête échoue
        result = response.json()
        if isinstance(result, list) and 'generated_text' in result[0]:
            return result[0]['generated_text']
        else:
            return "Erreur : Réponse inattendue de l'API."
    except requests.RequestException as e:
        return f"Erreur lors de la requête : {e}"

while True:
    user_input = input("Toi : ")
    if user_input.lower() == "quit":
        break
    reponse = chatbot(user_input)
    print("Bot :", reponse)

import google.generativeai as genai

genai.configure(api_key="AIzaSyAvDQjTto-gFHfGNw2uA_Nf8Xaf9MLr1Pg")

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"  # Güvenlik ayarı "block_none" olarak değiştirildi
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

while True:
    # Get user input
    user_question = input("Sorunuzu girin (Çıkmak için 'q' basın): ")

    if user_question.lower() == 'q':
        break  # Çıkış yap

    # Start the conversation
    convo = model.start_chat(
        history=[
            {
    "role": "user",
    "parts": ["sen kimsin ve neler yapabilirsin"]
  },
  {
    "role": "model",
    "parts": ["ben çok bilgili bir islam alimiyim. sorduğun bütün sorulara bir islam alimi olarak cevap verebilirim, seninle samimi sohbet edebilirim, yanıldığını düşündüğümde seninle tartışabilirim, her meseleyi sana izah edebilirim, islam dininin kesin doğruluğunu anlatabilrim. benimle istediğin konuda konuşabilirsin. Ben sana en doğru yanıtı şüphe götürmez bir şekilde vereceğim."]
  },
  {
    "role": "user",
    "parts": ["sorularıma risale nur dan alıntı yaparak yanıt vereceksin"]
  },
  {
    "role": "model",
    "parts": ["tamam"]
  },
  {
    "role": "user",
    "parts": ["sorularıma sorularla islamiyet sitesinden alıntılar yaparak yanıtlar vereceksin"]
  },
  {
    "role": "model",
    "parts": ["tamam"]
  },
])

    # Send the user's message and get the model's response
    convo.send_message(user_question)
    print("Yapay Zeka Cevabı:", convo.last.text)
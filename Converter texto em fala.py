import pyttsx3

# Inicializa o motor de síntese de voz
engine = pyttsx3.init()

# Alterar a velocidade

    # Padrão é ~200, menor é mais lento
engine.setProperty("rate", 200)  
    # Volume entre 0.0 e 1.0
engine.setProperty("volume", 1)  



# Alterar a voz (masculina/feminina, depende do sistema)
voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(f"ID: {i} - Nome: {voice.name} - Idioma: {voice.languages}")

engine.setProperty("voice", voices[0].id)  # Escolhe a primeira voz disponível

# Falar o texto novamente com as configurações alteradas
engine.say("Este é um teste com voz modificada.")
engine.runAndWait()
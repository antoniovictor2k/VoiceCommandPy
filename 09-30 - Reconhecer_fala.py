# instalação: SpeechRecognition e PyAudio
# para pyaudio, digite no google "install pyaudio seu_sistema_operacional"

import speech_recognition as sr


# Reconhecedor de voz
rec = sr.Recognizer()

# print(sr)
print(sr.Microphone().list_microphone_names())

with sr.Microphone(2) as mic:
    # print(f"Teste - {mic}")

    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    if "Victor" in texto:
        print("Voce falou Victor")
    else:
        print("Palavra desconhecida!")
    print(texto)
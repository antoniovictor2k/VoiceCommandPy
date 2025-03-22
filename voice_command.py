import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# Inicializa o motor de síntese de voz
engine = pyttsx3.init()
engine.setProperty("rate", 180)  # Velocidade da voz
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  

# Inicializa o reconhecimento de voz
rec = sr.Recognizer()

# Escolher microfone
microfones = sr.Microphone().list_microphone_names()
print("\n- Escolha o Microfone -\n")
for i, mic in enumerate(microfones[:10], start=1):
    print(f"{i}: {mic}")

selecionar_microfone = int(input("\nDigite o número do microfone: ")) - 1
print(f"\n- Microfone Escolhido: {microfones[selecionar_microfone]} -\n")

# Mantém o microfone ouvindo sempre
with sr.Microphone(selecionar_microfone) as mic:
    rec.adjust_for_ambient_noise(mic)

    while True:
        try:
            print("- Aguardando ativação ('Oi PC')...")

            # Captura áudio continuamente esperando a palavra-chave
            audio = rec.listen(mic)
            comando = rec.recognize_google(audio, language="pt-BR").lower()
            print(f"- Entrada: '{comando}'")

            # Se a palavra-chave for detectada, ativa o assistente
            if "oi pc" in comando:
                engine.say("Olá! Como posso ajudar?")
                engine.runAndWait()
                
                while True:
                    print("- Esperando comando...")

                    audio = rec.listen(mic)
                    comando = rec.recognize_google(audio, language="pt-BR").lower()
                    print(f"- Entrada: '{comando}'")

                    # Sair do loop se o usuário quiser
                    if "sair" in comando or "fechar" in comando or "parar" in comando:
                        engine.say("Ok, estou encerrando. Até mais!")
                        engine.runAndWait()
                        exit()  # Encerra o programa

                    # Tocar música no YouTube
                    elif "música" in comando:
                        engine.say("Qual música você quer ouvir?")
                        engine.runAndWait()

                        audio_musica = rec.listen(mic)
                        nome_musica = rec.recognize_google(audio_musica, language="pt-br")
                        print(f"- Tocando: '{nome_musica}'")

                        kit.playonyt(nome_musica)  

                    # Ajustar volume
                    elif "volume" in comando:
                        engine.say("Deseja aumentar ou diminuir o volume?")
                        engine.runAndWait()

                        devices = AudioUtilities.GetSpeakers()
                        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                        volume = interface.QueryInterface(IAudioEndpointVolume)

                        # Obtém volume atual
                        current_volume = volume.GetMasterVolumeLevelScalar()  

                        audio_volume = rec.listen(mic)
                        ajuste_volume = rec.recognize_google(audio_volume, language="pt-br").lower()
                        print(f"- Entrada: '{ajuste_volume}'")

                        if "aumentar" in ajuste_volume:
                            new_volume = min(1.0, current_volume + 0.1)  
                            volume.SetMasterVolumeLevelScalar(new_volume, None)
                            print(f"Volume aumentado para {int(new_volume * 100)}%")
                        elif "diminuir" in ajuste_volume:
                            new_volume = max(0.0, current_volume - 0.1)  
                            volume.SetMasterVolumeLevelScalar(new_volume, None)
                            print(f"Volume diminuído para {int(new_volume * 100)}%")
                        else:
                            engine.say("Não entendi, tente novamente.")
                            engine.runAndWait()

                    # Caso não entenda o comando
                    else:
                        engine.say("Desculpe, não entendi. Pode repetir?")
                        engine.runAndWait()
                        
        except sr.UnknownValueError:
            pass  # Ignora erros quando o áudio não é entendido
        except sr.RequestError:
            print("Erro ao conectar com o serviço de reconhecimento de voz.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

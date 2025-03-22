import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL



# Inicializa o motor de síntese de voz
engine = pyttsx3.init()

# Reconhecedor de voz
rec = sr.Recognizer()


# Alterar a voz (masculina/feminina, depende do sistema)
voices = engine.getProperty("voices")

# Padrão é ~200, menor é mais lento
engine.setProperty("rate", 180)  

# Escolhe a primeira voz disponível
engine.setProperty("voice", voices[0].id)  


teste = sr.Microphone().list_microphone_names()

print("""
- Escolhar o Microfone - 
""")
count_fones = 0
for testes in teste:
    count_fones += 1
    if count_fones <= 10:
        count_fones_falar = f"{count_fones}: {testes}"
        print(count_fones_falar)
selecionar_microfone = int(input("""
Digite o Microfone: """))

print (f""" 
- Microfone Escolhido -

Microfone: {selecionar_microfone}

""")



with sr.Microphone(selecionar_microfone-1) as mic:
    # print(f"Teste - {mic}")

    rec.adjust_for_ambient_noise(mic)


   


    falar = "Como posso ajudar?"
    print(f"- Saída: '{falar}' ")
    # Falar o texto novamente com as configurações alteradas
    
    engine.say(falar)
    engine.runAndWait()

    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    print(f"- Entrada: '{texto}'")
    while True:

        engine.say(f"Você falou {texto} ?. Diga Sim para continuar ou Não para repetir.")
        engine.runAndWait()
        confirmacaoAudio = rec.listen(mic)
        confirmacao = rec.recognize_google(confirmacaoAudio, language="pt-BR")
        print(f"- Entrada: '{confirmacao}'")
        if "sim" in confirmacao.lower():
            engine.say(f"Estou realizando a sua solicitação!")
            engine.runAndWait()
            
            # Musica Youtube2
            if "música" in texto.lower():
                engine.say("Qual música você quer ouvir?")
                engine.runAndWait()

                audioMusica = rec.listen(mic)
                textoMusica = rec.recognize_google(audioMusica, language="pt-br")

                print(f"- Entrada: '{textoMusica}'")

                kit.playonyt(f"{textoMusica}")  

            # Volume -
            elif "volume" in texto.lower():
                engine.say("Deseja aumentar ou diminuir o volume?")
                engine.runAndWait()
                # Obter a interface de controle de áudio
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = interface.QueryInterface(IAudioEndpointVolume)

                # Obtém volume atual
                current_volume = volume.GetMasterVolumeLevelScalar()  
                
                audioVolume = rec.listen(mic)
                textoVolume = rec.recognize_google(audioVolume, language="pt-br")

                print(f"- Entrada: '{textoVolume}'")

                while True:

                    if "aumentar" in textoVolume.lower():
                        # Aumenta 10%, sem ultrapassar 100%
                        new_volume = min(1.0, current_volume + 0.1)  
                        volume.SetMasterVolumeLevelScalar(new_volume, None)
                        print(f"Volume aumentado para {int(new_volume * 100)}%")
                        break
                    elif "diminuir" in textoVolume.lower():
                        # Diminui 10%, sem ir abaixo de 0%
                        new_volume = max(0.0, current_volume - 0.1)  
                        volume.SetMasterVolumeLevelScalar(new_volume, None)
                        print(f"Volume diminuído para {int(new_volume * 100)}%")
                        break
                    elif "sair" in textoVolume.lower():
                        print("Saindo do volume!")
                        break
                    else:
                        engine.say("Não entendi, vamos tentar novamente.")
                        engine.runAndWait()

           
           
           
            # Volume +
            break

        elif "não" in confirmacao.lower():
            engine.say(f"Vamos tentar novamente. Como posso ajudar?")
            engine.runAndWait()
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(f"- Entrada: '{texto}'")
        else:
            engine.say(f"Não entendi, Estarei perguntando novamente. Como posso ajudar?")
            engine.runAndWait()
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(f"- Entrada: '{texto}'")
import json
import vosk
import pyaudio

# Caminho do modelo Vosk (certifique-se de que está correto)
MODEL_PATH = "vosk-model-small-pt-0.3"

# Iniciar modelo Vosk
model = vosk.Model(MODEL_PATH)
rec = vosk.KaldiRecognizer(model, 16000)

# Inicializar PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, 
                input=True, frames_per_buffer=8192)
stream.start_stream()

print("Aguardando ativação: Diga 'Oi PC'...")

while True:
    try:
        # Capturar áudio do microfone
        data = stream.read(4096, exception_on_overflow=False)

        if len(data) == 0:
            continue  # Se não houver áudio, continua ouvindo

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())  # Converter para JSON
            texto = result.get("text", "")

            if texto:
                print(f"Detectado: {texto}")  # Mostrar o que foi reconhecido

            if "oi computador" in texto.lower():
                print("Ativado! Como posso ajudar?")
                break  # Sai do loop para executar comandos

    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        break  # Para o programa ao pressionar Ctrl+C

# Fechar fluxo de áudio
stream.stop_stream()
stream.close()
p.terminate()

# VoiceCommandPy

**VoiceCommandPy** é um projeto em desenvolvimento que permite a interação por comandos de voz, onde o usuário pode controlar o volume do sistema, tocar músicas no YouTube e realizar outras tarefas usando a tecnologia de reconhecimento de voz.

**Status**: Projeto em teste. Novas funcionalidades serão adicionadas com o tempo.

## Funcionalidades
- **Controle de Volume**: O usuário pode aumentar ou diminuir o volume do sistema com comandos de voz.
- **Música no YouTube**: O usuário pode pedir para o sistema tocar músicas no YouTube.
- **Reconhecimento de Comandos**: Comandos são dados por voz e o sistema responde verbalmente usando a síntese de voz.

---

## Tecnologias Utilizadas

- **SpeechRecognition**: Para capturar e processar o áudio.
- **pyttsx3**: Para a síntese de voz (transforma texto em fala).
- **pywhatkit**: Para controlar o YouTube e tocar músicas.
- **pycaw**: Para controlar o volume do sistema.
- **comtypes**: Para interagir com o sistema e controlar o áudio.

---

## Como Rodar o Projeto

1. **Instalação das dependências**:
   Para rodar o projeto, você precisa instalar as dependências. Execute o seguinte comando no terminal:

   ```bash
   pip install SpeechRecognition pyttsx3 pywhatkit pycaw comtypes

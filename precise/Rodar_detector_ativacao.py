from precise_runner import PreciseEngine, PreciseRunner

# Carregar o motor Precise com o modelo treinado
engine = PreciseEngine('precise-engine', 'oi_pc.pb')

# Função para executar quando "Oi PC" for detectado
def on_activation():
    print("Ativado! Como posso ajudar?")
    # Aqui você pode chamar seu assistente para ouvir e responder

# Iniciar o detector de wake word
runner = PreciseRunner(engine, on_activation=on_activation)
runner.start()

# Manter o script rodando
while True:
    pass

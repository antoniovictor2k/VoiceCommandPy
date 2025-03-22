from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL

# Obter a interface de controle de áudio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


# Obtém volume atual
current_volume = volume.GetMasterVolumeLevelScalar()  


# Aumenta 10%, sem ultrapassar 100%
new_volume = min(1.0, current_volume + 0.1)  
volume.SetMasterVolumeLevelScalar(new_volume, None)
print(f"Volume aumentado para {int(new_volume * 100)}%")

# Diminui 10%, sem ir abaixo de 0%
new_volume = max(0.0, current_volume - 0.1)  
volume.SetMasterVolumeLevelScalar(new_volume, None)
print(f"Volume diminuído para {int(new_volume * 100)}%")

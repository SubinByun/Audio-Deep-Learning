import numpy as np 
import matplotlib.pyplot as plt
from IPython.display import Audio

def fade_io(data, length=1000):
    # 0에서 1까지 선형적으로 증가하는 값 생성
    fade_in_data = np.linspace(0, 1, length)
    # Fade-in 적용
    data[:length]*=fade_in_data
    # 1에서 0까지 선형적으로 감소하는 값 생성
    fade_out_data = np.linspace(1,0,length)
    # Fade-out 적용
    data[-length:]*=fade_out_data
    return data

def sine_tone(f, duration = 0.08, n = 1280):
    t = np.linspace(0, duration, n) # fs = 1280/0.08 = 16kHz
    data = np.sin(2*np.pi*f*t)
    length = 10**int(np.log10(duration*n))
    return fade_io(data = data, length = length)

fs = 16000
scale = [440*2**(i/12) for i in range(5)]
# np.around(scale) #array([440., 466., 494., 523., 554.])
scale_tone = np.hstack([sine_tone(f) for f in scale])
Audio(scale_tone, rate=fs)

octave = [440*(i+1) for i in range(5)]
# [440, 880, 1320, 1760, 2200]
octave_tone = np.hstack([sine_tone(f) for f in octave])
Audio(octave_tone, rate=fs)

two_tone = np.add(scale_tone, octave_tone)

plt.plot(np.linspace(0, len(two_tone)/fs, len(two_tone)), two_tone)
plt.xlabel(f"Time [sec]")
plt.title(f"{len(two_tone)/fs}[sec] two_tone of scale and octave wave")
plt.show()
print()
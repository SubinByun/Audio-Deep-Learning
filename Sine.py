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

t = np.linspace(0, 1, 100)
f = 1 #1Hz

Audio(sine_tone(300), rate=16000)

plt.plot(t, 1*np.sin(2*np.pi*f*t+0),"-", label='sin(2$\pi$ft)')
plt.plot(t, 0.7*np.sin(2*np.pi*f*t-1), ls="--", label='0.7sin(2$\pi$ft-1)')

plt.xlabel("Time")
plt.title("Sine Wave")
plt.legend()
plt.grid()
plt.show()

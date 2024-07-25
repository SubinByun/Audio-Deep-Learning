from scipy.fftpack import fft
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

class MyException(Exception):
    pass

def n_fft(data, n_lim=20):
    for n in 2**np.arange(n_lim):
        if n>=len(data):
            return n
        if len(data)>2**(n_lim-1):
            raise MyException(f"increase 'n_lim' by more than '{n_lim}'!!")
        
data = two_tone

try:
    N = n_fft(data)
    print(f"data'{len(data)}', number for FFT '{N}'")
except MyException as e:
    print(e)

fs = 16000
Y = fft(data, N) # np.fft.fft(data, N)

plt.figure(figsize=(7,7))
plt.subplot(311)
plt.plot(np.arange(len(Y)), Y) # np.linspace(0, fs, N)
plt.title('FFT')
plt.xlabel(f'Number of Samples = {len(Y)}')
plt.grid()

plt.subplot(312)
# Periodgram (fft 성분에 절대값을 취하고 대칭성분을 왼쪽으로 합치고 입력크기로 정규화)
plt.plot(np.linspace(0, fs/2, N//2), 2*np.abs(Y[:N//2])/len(data))
plt.xlabel('Number of Samples')
plt.title('Periodogram')
plt.grid()
plt.axvspan(400, 2300, alpha=0.3, color='green')
# [440, 440.0, 466.0 494.0, 523.0, 554.0, 880, 1320m 1760, 2200]

plt.subplot(313)
# x축을 주파수로 바꾸고 앞에서 표시한 구간 확대
plt.plot(np.linspace(0, fs/2, N//2), 2*np.abs(Y[:N//2])/len(data))
plt.xlabel('Frequency [Hz]')
plt.title('Periodogram')
plt.grid()
plt.axvspan(400, 2300, alpha=0.3, color='green')
plt.xlim(400, 2300) # 확대

plt.tight_layout()
plt.show()
'''
* For pleasant sentiment to hearing system: 
    sr >= 16000,
    fft >= 1024, 
    overlap(=hoplength) = fft/2 || fft/4, 
    resolution = sr/fft
    
* For librosa, if default, window = 384. ticks = lag * N_FFT/4 - 384
'''

class MIN:
    SR = 16000
    N_FFT = 512
    HOP_LENGTH = N_FFT//2
    ORG_DIR = './WAV'
    FIG_DIR = './GRAPH'
    SND_DIR = './SOUND'
    
    
class LOSSLESS:
    SR = 44100
    N_FFT = 2048
    HOP_LENGTH = N_FFT//2
    ORG_DIR = './IN'
    FIG_DIR = './GRAPH'
    SND_DIR = './SOUND'
    
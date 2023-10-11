import wave 

#filename = input("Please enter file name:")
filename ='test.wav'
print(filename)
wav = wave.open(filename,'rb')

num_channels = wav.getnchannels()
sampwidth = wav.getsampwidth()
frame_rate = wav.getframerate()
num_frames = wav.getnframes()
comptype = wav.getcomptype()
compname = wav.getcompname()

print("Number of Channels = ",num_channels)
print("Sample Width =",sampwidth)
print("Sampling Rate =",num_frames)
print("Number of Frames =",num_frames)
print("Comptype =",comptype)
print("Compname=",compname)

wav.close()

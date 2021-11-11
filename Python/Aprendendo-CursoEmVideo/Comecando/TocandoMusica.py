
# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
from playsound import playsound 

playsound(r"C:\Users\birio\Desktop\TheCalling-whereveryouwillgo.mp3")

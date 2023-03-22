# RealTimeSpeechText
Real time speech to text conversion and analyse the sentiment of user (environment)

This software record audio from mic and try to convert recorded voice of user to text by using google API. Then detect
emotions of input voice and map it into RGB color system.



Installation
---
```pip install -r requirment.txt```

**NOTE**:\
if you faced with error about "emoji" package and ```did not work ``` try to remove "emoje" python package
and install ```pip install emoji==1.6.0```

Use
---
To use package install 

Documentry
---
This software includes 3 stages
- Record audio
- Convert to text
- Sentiment analysis 
- Convert sentiments to RGB system

each stage has its own challenges and studies which described below. 

Record Audio
---
To record audio from mic in python, "pyaudio" and "speech_recognition" has been used. Both these packages 
automatically detect default chose mic to record audio and keep it as array of data. The default settings are record audio 
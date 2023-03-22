# RealTimeSpeechText
Real time speech to text conversion and analyse the sentiment of user (environment)

This software record audio from mic and try to convert recorded voice of user to text by using google API. Then detect
emotions of input voice and map it into RGB color system.



Installation
---
```pip install -r requirment.txt```

**NOTE**:\
if you faced with error about "emoji" package and ```did not work ``` try to remove "emoji" python package
and install ```pip install emoji==1.6.0```

Use
---
This package automatically run every one minute and listen to audio for 5 seconds (by default.
It is configurable through `RealTimeSpeechSentimentAnalysis.yaml` file.)

Example
---
Recorded audio from mic:
```html
<audio src="audio.mp3" controls preload></audio>
```

Documentary
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

- ***pyaudio***
- ***speech recognition***
---
Convert to text
---
There are enormous packages and tools to convert audio to text. By some search, popular packages are shown as:
- ***speechpy***
- ***speech recognition***

[Speechpy](https://github.com/astorfi/speechpy) is an out of date package which created at 2018 by `Amirsina Torfi`.
The last update to this package was in 2020, therefore this package did not used for project.

[speech recognition](https://github.com/Uberi/speech_recognition) is created by `Anthony Zhang` and 
continuously updated since this document is written. This package lets users recognize audio and convert it to 
text with different such as:
- [CMU Sphinx](https://cmusphinx.sourceforge.net/wiki/)(works offline)
- Google Speech Recognition (free and online)
- [Google Cloud API](https://cloud.google.com/speech/)(non-free)
- ...

as a free system, `Google Speech Recognition` chosed for this implementation.


Furure development
---
This was a simple and hobby project only to concat a few machine learning based modules in python and develop 
a software. But it has many aspects that lets 
#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os

if not os.path.exists('thinkdsp.py'):
    get_ipython().system('wget https://github.com/DavronbekSattorov/ThinkDSP/blob/master/code/thinkdsp.py')


# In[9]:


if not os.path.exists('181934__landub__applause2.wav'):
    get_ipython().system('wget https://github.com/DavronbekSattorov/ThinkDSP/blob/master/code/181934__landub__applause2.wav')


# In[10]:


from thinkdsp import read_wave

wave = read_wave('181934__landub__applause2.wav')
wave.normalize()
wave.make_audio()


# In[11]:


wave.plot()


# In[12]:


segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()


# In[13]:


segment.plot()


# In[14]:


segment.segment(start=1.1, duration=0.005).plot()


# In[15]:


spectrum = segment.make_spectrum()
spectrum.plot(high=7000)


# In[16]:


spectrum = segment.make_spectrum()
spectrum.plot(high=1000)


# In[17]:


spectrum.peaks()[:30]


# In[18]:


spectrum.low_pass(2000)


# In[19]:


spectrum.make_wave().make_audio()


# In[20]:


from thinkdsp import decorate
from IPython.display import display

def filter_wave(wave, start, duration, cutoff):
    """Selects a segment from the wave and filters it.
    
    Plots the spectrum and displays an Audio widget.
    
    wave: Wave object
    start: time in s
    duration: time in s
    cutoff: frequency in Hz
    """
    segment = wave.segment(start, duration)
    spectrum = segment.make_spectrum()

    spectrum.plot(high=5000, color='0.7')
    spectrum.low_pass(cutoff)
    spectrum.plot(high=5000, color='#045a8d')
    decorate(xlabel='Frequency (Hz)')
    
    audio = spectrum.make_wave().make_audio()
    display(audio)


# In[21]:


from ipywidgets import interact, fixed

interact(filter_wave, wave=fixed(wave), 
         start=(0, 5, 0.1), duration=(0, 5, 0.1), cutoff=(0, 5000, 100));


# In[ ]:





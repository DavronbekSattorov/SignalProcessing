#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

if not os.path.exists('thinkdsp.py'):
    get_ipython().system('wget https://github.com/DavronbekSattorov/ThinkDSP/blob/master/code/thinkdsp.py')


# In[3]:


if not os.path.exists('181934__landub__applause2.wav'):
    get_ipython().system('wget https://github.com/DavronbekSattorov/ThinkDSP/blob/master/code/181934__landub__applause2.wav')


# In[5]:


from thinkdsp import read_wave

wave3 = read_wave('181934__landub__applause2.wav')
wave3.normalize()
wave3.make_audio()


# In[6]:


def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor


# In[7]:


stretch(wave3, 0.5)
wave3.make_audio()


# In[8]:


wave3.plot()


# In[ ]:





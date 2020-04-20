#!/usr/bin/env python
# coding: utf-8

# In[1]:


from thinkdsp import SinSignal

signal = (SinSignal(freq=400, amp=1.0) +
          SinSignal(freq=600, amp=0.5) +
          SinSignal(freq=800, amp=0.25))
signal.plot()


# In[2]:


wave2 = signal.make_wave(duration=1)
wave2.apodize()


# In[3]:


wave2.make_audio()


# In[4]:


spectrum = wave2.make_spectrum()
spectrum.plot(high=2000)


# In[5]:


signal += SinSignal(freq=450)
signal.make_wave().make_audio()


# In[ ]:





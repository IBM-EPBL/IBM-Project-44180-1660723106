#!/usr/bin/env python
# coding: utf-8

# In[2]:


###Creating Our Flask Application And Loading Our Model By Using Load_model Method


# In[ ]:


app = Flask(__name__,template_folder="templates") # initializing a flask app
# Loading the model
model=load_model('nutrition.h5')
print("Loaded model from disk")


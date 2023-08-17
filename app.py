#!/usr/bin/env python
# coding: utf-8

# In[10]:


import replicate
import json, time, requests


# In[11]:


q = input("Please describe the photo you want :")


# In[12]:


q


# In[13]:


body = json.dumps(
    {
        "verison":"db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        "input":{
            "prompt": q
        }    
    }
)


# In[14]:


headers = {
    "Authorization":"r8_GjSSVNQMdbBCVRLK1C1P2MQmnv9bUcj1oIoVB",
    "content-Type":"application/json"
}


# In[15]:


output = requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)


# In[16]:


output


# In[17]:


time.sleep(10)


# In[18]:


get_url = output.json()["urls"]["get"]


# In[13]:


get_url


# In[15]:


get_result = requests.post(get_url,headers=headers).json()['output']


# In[16]:


from PIL import Image


# In[18]:


img = Image.open(requests.get(get_result[0],stream=True).raw)


# In[19]:


img


# In[ ]:


from flask import Flask,render_template,request
import json, time, requests


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        body = json.dumps(
           {
               "verison":"r8_QPElhDPrWKiZQxaN5tMtFmeZHK8Q5kI4OGfMr",
               "input":{
                  "prompt": q
               }    
           }
)
        headers = {
            "Authorization":"r8_HXWxCH9Q6tSfKsAisIqPfnlpWloE1TA3GM0cP",
            "content-Type":"application/json"
        }
        output = requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]
        return(render_template("index.html",result=get_result[0]))
    else:
        return(render_template("index.html",result="waiting"))

if __name__ == "__main__":
    app.run()


# In[ ]:





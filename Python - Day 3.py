#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.chdir('C:\\Users\\HP\\Desktop\\')


# In[4]:


import pandas as pd
data = pd.read_csv('Students_Data.csv')


# In[5]:


data


# In[6]:


data.columns = ["Gender", "Nationality", "PlaceOfBirth", "StageID", "SectionID", "GradeID", "Topic", "Semester", "Relation", "RaisedHands", "VisitedResources", "AnnouncementsView", "Discussion", "ParentAnsweringSurvey", "ParentSchoolSatisfaction", "StudentAbsenceDays", "Class"]


# In[7]:


data


# In[14]:


set(data['Nationality'])


# In[9]:


data['Nationality'] = data['Nationality'].replace('KW','Kuwait')


# In[11]:


data['Nationality'] = data['Nationality'].replace('lebanon','Lebanon')


# In[12]:


data['Nationality'] = data['Nationality'].replace('venzuela','Venezuela')


# In[13]:


data['Nationality'] = data['Nationality'].replace('SaudiArabia','Saudi Arabia')


# In[15]:


set(data['Class'])


# In[18]:


set(data['StageID'])


# In[17]:


data['StageID'] = data['StageID'].replace('lowerlevel','LowerLevel')


# In[19]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[20]:


data.info()


# In[24]:


plt.figure(figsize=(15,5))
sns.countplot(x='Topic',data=data)


# In[26]:


plt.figure(figsize=(15,5))
sns.countplot(y='Nationality',data=data)


# In[27]:


plt.figure(figsize=(15,5))
sns.countplot(x='Class',data=data)


# In[28]:


plt.figure(figsize=(15,5))
sns.countplot(x='Gender',data=data, hue='Class')


# In[30]:


plt.figure(figsize=(15,5))
sns.countplot(x='StudentAbsenceDays',data=data, hue='Gender')


# In[35]:


plt.figure(figsize=(15,5))
sns.countplot(x='ParentSchoolSatisfaction',data=data, hue='Class')


# In[34]:


plt.figure(figsize=(15,5))
sns.barplot(x='Class',y='RaisedHands', data=data)


# In[38]:


df1 = pd.DataFrame(np.array([['a',5,9],['b',4,61],['c',24,9]]),
                  columns=['name','attr1','attr2'])


# In[39]:


df1


# In[40]:


df2 = pd.DataFrame(np.array([['a',5,19],['b',4,16],['c',2,9]]),
                  columns=['name','attr3','attr4'])


# In[41]:


df2


# In[42]:


df3 = pd.DataFrame(np.array([['a',5,19],['d',4,16],['e',2,9]]),
                  columns=['name','attr5','attr6'])


# In[43]:


df3


# In[44]:


df2


# In[45]:


df1


# In[47]:


pd.merge(pd.merge(df1,df2,on='name'),df3,on='name')


# In[48]:


df1.merge(df2,on='name').merge(df3,on='name')


# In[50]:


pd.merge(df1,df2,how='inner',left_on=['name','attr1'], right_on=['name','attr3'])


# In[51]:


os.chdir('C:\\Users\\HP\\Desktop\\Cognitior Submissions (1)\\Cognitior Submissions\\Project 1\\Dataset\\')


# In[53]:


df = pd.read_csv('H1Bdata.csv',encoding = 'latin-1')


# In[54]:


df


# In[60]:


stats = df[(df['CASE_STATUS']=='CERTIFIED') & (df['VISA_CLASS']=='H-1B')]


# In[62]:


stats.JOB_TITLE.value_counts().head(10)


# In[64]:


stats_ds = stats[stats['JOB_TITLE']=='DATA SCIENTIST']


# In[65]:


stats_ds.EMPLOYER_NAME.value_counts().head(10)


# In[68]:


stats_ds.PREVAILING_WAGE.mean()-stats.PREVAILING_WAGE.mean()


# In[67]:


stats.PREVAILING_WAGE.mean()


# In[72]:


denied = df[df['CASE_STATUS']=='DENIED']


# In[73]:


denied


# In[81]:


denied_per_state = denied.EMPLOYER_STATE.value_counts().rename_axis('Employer_State').reset_index(name='Count')


# In[82]:


denied_per_state


# In[85]:


applied_per_state = df.EMPLOYER_STATE.value_counts().rename_axis('Employer_State').reset_index(name='Count')


# In[86]:


applied_per_state


# In[97]:


plt.figure(figsize=(20,10))
final=pd.merge(denied_per_state, applied_per_state,on='Employer_State' )


# In[89]:


final


# In[101]:


final['%age'] = final['Count_x']/final['Count_y']


# In[102]:


final


# In[103]:


plt.figure(figsize=(15,5))
sns.barplot(x='Employer_State',y='%age', data=final)


# In[104]:


denied


# In[109]:


denied[['Date_submitted','Month_submitted','Year_Submitted']] = denied.CASE_SUBMITTED.str.split('-',expand=True)


# In[110]:


denied


# In[111]:


denied.drop(columns = ['Date_submitted'])


# In[113]:


denied_monthwise = denied.Month_submitted.value_counts()


# In[114]:


denied_monthwise


# In[116]:


df[['Date_submitted','Month_submitted','Year_Submitted']] = df.CASE_SUBMITTED.str.split('-',expand=True)


# In[117]:


applied_monthwise = df.Month_submitted.value_counts()


# In[118]:


applied_monthwise


# In[119]:


applied_monthwise = applied_monthwise.rename_axis('MONTH').reset_index(name='NUM_APPLICATIONS')


# In[120]:


denied_monthwise = denied_monthwise.rename_axis('MONTH').reset_index(name='NUM_APPLICATIONS')


# In[121]:


denied_monthwise = denied_monthwise.sort_values(by=['MONTH'])


# In[122]:


applied_monthwise = applied_monthwise.sort_values(by=['MONTH'])


# In[124]:


applied_monthwise


# In[123]:


plt.plot(applied_monthwise.values[:,0],applied_monthwise.values[:,1],label = 'Total Applicants')
plt.plot(denied_monthwise.values[:,0],denied_monthwise.values[:,1], label = 'Denied Applicants')
plt.xlabel('MONTH')
plt.ylabel('Number of Applications')
plt.legend()


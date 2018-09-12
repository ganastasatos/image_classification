
# coding: utf-8

# In[ ]:


#Create test set with females and males seperately
for i in range(len(df)):
    image1 = test_df.iloc[i,2:]
    image1 = image1.values.reshape(100,100)
    if (test_df.loc[i,'gender']== 0): # Female
        name = 'female.'+str(i)+'.jpg'
        scipy.misc.imsave("test_set/females/" + name, image1)
    else:
        name = 'male.'+str(i)+'.jpg'
        scipy.misc.imsave("test_set/males/" + name, image1)


# In[ ]:


# Create training sets
for i in range(len(train_df)):
    image1 = train_df.iloc[i,2:]
    image1 = image1.values.reshape(100,100)
    if (train_df.loc[i,'gender']== 0): # Female
        name = 'female.'+str(i)+'.jpg'
        scipy.misc.imsave("training_set/females/" + name, image1)
    else:
        name = 'male.'+str(i)+'.jpg'
        scipy.misc.imsave("training_set/males/" + name, image1)


#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot, pandas, numpy
from pandas import read_csv, crosstab


# In[12]:


def loadnreturndta():
    dtname="ethnic-groups-in-england-and-wales-by-sex.csv"
    dt=read_csv(dtname)
    return dt


# In[13]:


eth_eng_w=loadnreturndta()
eth_eng_w.head()


# In[14]:


def multilinechart(d1,d2,v1,v2,vnm):
    matplotlib.pyplot.figure(figsize=(10,5))
    matplotlib.pyplot.title("Distribution by {} in England and Wales".
                            format(vnm),fontsize=20,color="m")
    matplotlib.pyplot.plot(d1[vnm].unique(),v1,"--*g",label="Male")
    matplotlib.pyplot.plot(d2[vnm].unique(),v2,"--Db",label="Female")
    matplotlib.pyplot.xlabel("{}".format(vnm),fontsize=16,color="m")
    matplotlib.pyplot.ylabel("Distribution",fontsize=16,color="m")
    matplotlib.pyplot.xticks(rotation=90)
    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()


# In[15]:


ml=eth_eng_w[eth_eng_w['Gender']=="Male"]
ethu_ml=list(ml.Ethnicity.unique())
vleth_ml=[0 for x in range(len(ethu_ml))]
for eu in range(len(ml.Value)):
    idx=ethu_ml.index(ml.Ethnicity.tolist()[eu])
    vleth_ml[idx]+=ml.Value.tolist()[eu]
fml=eth_eng_w[eth_eng_w['Gender']=="Female"]
ethu_fml=list(fml.Ethnicity.unique())
vleth_fml=[0 for x in range(len(ethu_fml))]
for eu in range(len(fml.Value)):
    idx=ethu_ml.index(fml.Ethnicity.tolist()[eu])
    vleth_fml[idx]+=fml.Value.tolist()[eu]
    
multilinechart(ml,fml,vleth_ml,vleth_fml,'Ethnicity')


# In[16]:


def pieplot(fet,cnt,vnm,clr):
    if "_" in vnm:
        vnm=' '.join(vnm.split("_"))
    matplotlib.pyplot.figure(figsize=(10,5))
    matplotlib.pyplot.title("Distribution by {} By Types of Survey".
                            format(vnm),fontsize=18,color="m")
    matplotlib.pyplot.pie(cnt,labels=fet,autopct='%1.1f%%',colors=clr)
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()


# In[17]:


etypdf=eth_eng_w.Ethnicity_Type.value_counts()
etypcat=etypdf.index.tolist()
etypval=etypdf.tolist()
pieplot(etypcat,etypval,'Ethnicity_Type',["#01F9C6","#FFEF00"])
gendf=eth_eng_w.Gender.value_counts()
gencat=gendf.index.tolist()
genval=gendf.tolist()
pieplot(gencat,genval,'Gender',["#F75D59","#F433FF"])


# In[18]:


eth_eng_w1=eth_eng_w[eth_eng_w['Ethnicity']!="All Ethnic groups"]
eth_eng_w1.head()


# In[19]:


def stkbar(f1,f2,f3,c1,c2):
    x=numpy.arange(len(f1))
    width = 0.3
    fig, ax = matplotlib.pyplot.subplots(figsize=(8,4))
    bar1 = ax.bar(x - width, f2, width, label='Male Count',color=c1)
    bar2 = ax.bar(x, f3, width, label='Female Count',color=c2)
    ax.set_ylabel('Count',fontsize=16,color="m")
    ax.set_title('Ethnicity Count by Region and Gender',fontsize=20,color="m")
    ax.legend()

    fig.tight_layout()
    matplotlib.pyplot.xticks(x, f1,rotation=90)
    matplotlib.pyplot.show()


# In[20]:


ctdf=pandas.crosstab(eth_eng_w.Ethnicity,eth_eng_w.Gender,
                     values=eth_eng_w.Value, aggfunc=numpy.sum)
indtodrop=["All Ethnic groups","Asian","Black","Mixed","Other","White"]
ctdf=ctdf.drop(index=indtodrop)
ctdfraw=ctdf.index
ctdfml=ctdf.Male.tolist()
ctdffml=ctdf.Female.tolist()
ctdfrawnew=[]
for c in ctdfraw:
    ctdfrawnew.append(c.split(" - ")[1])
ctdfrawnew=ctdfrawnew[1:]
ctdfrawnew.pop(5)
ctdfrawnew.pop(6)
ctdfrawnew.pop(9)
ctdfrawnew.pop(10)
ctdfml=ctdfml[1:]
ctdfml.pop(5)
ctdfml.pop(6)
ctdfml.pop(9)
ctdfml.pop(10)
ctdffml=ctdffml[1:]
ctdffml.pop(5)
ctdffml.pop(6)
ctdffml.pop(9)
ctdffml.pop(10)


stkbar(ctdfrawnew,ctdfml,ctdffml,"#FFA600","#FF1493")







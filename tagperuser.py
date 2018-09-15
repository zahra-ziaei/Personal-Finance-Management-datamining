# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:15:44 2018
میاد مشخص میکنه هر تگ توسط چه تعداد فرد منحصر به فرد زده شده.
@author: ziyaie
"""

import pandas as pd
import numpy as np

#select * from transaction_tags
tag=pd.read_csv('transaction_tag.csv')
# transaction Id shode index


#select * from transaction
transaction=pd.read_csv('transaction.csv')

#select * from tag
tagname=pd.read_csv('esme_tag.csv')


#select * from resource
resource=pd.read_csv('resource.csv')


tagtra=pd.merge(tag,transaction, how='inner', left_on='transactions_id', right_on='id')
tagtrarec=pd.merge(tagtra,resource, how='inner', left_on='resource_id', right_on='id')
tagtrarecN=pd.merge(tagname,tagtrarec, how='inner', left_on= 'id', right_on='tags_id')

jj={}
for group, frame in tagtrarecN.groupby('tag'):
    j=0
    for i in frame['user_id'].unique():
        j=j+1
    jj[group]=j
#tagtrarecg=tagtrarecN.groupby(['tag','user_id']).count()



#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pandas import DataFrame
a1 = 0.7
a2 = 0.3
b_a1 = 0.2
b_a2 = 0.9

bays = DataFrame({'사건':['A1', 'A2'],
                 '사전확률_P(Ai)':[a1, a2],
                  '조건부확률_P(B|Ai)':[b_a1, b_a2],
                  '결합확률_P(Ai*B)':[a1*b_a1, a2*b_a2],
                  '사후확률_P(Ai|B)':[a1*b_a1/(a1*b_a1 + a2*b_a2),
                                 a2*b_a2/(a1*b_a1 + a2*b_a2)]})
bays


# In[4]:


from pandas import DataFrame

a1 = 0.2
a2 = 0.35
a3 = 0.45
b_a1 = 0.02
b_a2 = 0.04
b_a3 = 0.03

bays = DataFrame({'사건': ['A1', 'A2', 'A3'],
                  '사전확률_P(Ai)': [a1, a2, a3],
                  '조건부확률_P(B|Ai)': [b_a1, b_a2, b_a3],
                  '결합확률_P(Ai*B)': [a1 * b_a1, a2 * b_a2, a3 * b_a3],
                  '사후확률_P(Ai|B)': [
                      a1 * b_a1 / (a1 * b_a1 + a2 * b_a2 + a3 * b_a3),
                      a2 * b_a2 / (a1 * b_a1 + a2 * b_a2 + a3 * b_a3),
                      a3 * b_a3 / (a1 * b_a1 + a2 * b_a2 + a3 * b_a3)
                  ]})
bays


# In[ ]:





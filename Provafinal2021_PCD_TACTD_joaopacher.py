#!/usr/bin/env python
# coding: utf-8

# #JOÃO LUIZ PACHER 
# 
# ### <span style="color:blue">MBA em Ciência de Dados</span>
# 
# <span style="color:blue">Programação para Ciência de Dados</br>
# <span style="color:blue">Técnicas Avançadas de Captura e Tratamento de Dados
# 
# ### <span style="color:blue">Prova Final</span>
# 
# **Material Produzido por:**<br>
# >**Prof Moacir A. Ponti**<br>
# >**Prof Luis Gustavo Nonato**<br> 
# 
# **CEMEAI - ICMC/USP São Carlos**
# 
# ---
# 
# O arquivo `Emendas.csv` contém informações das emendas parlamentares do congresso nacional. Execute as seguintes operações sobre essa base de dados:
# 
# 1. **Leia o arquivo e considere apenas as colunas** 'Nome Funcao', 'Valor Empenhado', 'Valor Pago' e 'Valor Restos A Pagar Pagos'. 1
# 
# 2. Verifique e anote **quantos dados faltantes totais** existem no DataFrame resultante.
# 
# 3. Substitua os valores faltantes:
#     1. na coluna 'Valor Empenhado' pela média dos valores atuais nessa coluna,
#     2. por zero no restante do data frame.
#     
# 4. Compute e anote a **soma total da coluna 'Valor Empenhado'** em milhares de reais (i.e. dividindo o valor por 1000) considerando os valores após o preenchimento de dados faltantes do passo anterior.
# 
# 5. Considerando a coluna 'Nome Funcao' como sendo categorias de emendas, compute a frequência da categoria majoritária, isto é, a categoria com maior número de ocorrências e a **porcentagem dessa categoria majoritária** com relação às demais categorias na base completa.
#     
#     
# **INSTRUÇÕES (Importante)**:<br>
# 1. Você deve exportar esse notebook **com sua solução para as questões da prova** em formato .py e fazer upload no Moodle. 
#    
#     * Atenção: você *não* deve fazer upload de um arquivo notebook (.ipynb), mas sim um arquivo **texto .py** contendo os códigos python que utilizou para resolver as questões. O arquivo .py pode ser gerado através de uma das opções abaixo:<br>
#         * no Jupyter Notebook/local: `File --> Download as --> Python (.py)` 
#         * no Google Colab: `File --> Download .py` 
#         * caso não esteja utilizando o Jupyter nem Colab, copie e cole seu código em um arquivo ASCII (Texto) salvando com a extensão .py
# 
# 2. O arquivo deve ser nomeado com seu nome e sobrenome, sem espaços e sem acentuacao. Exemplo: moacirponti.py
# 
# 3. É OBRIGATÓRIO conter no cabeçalho (início) do arquivo um comentário / texto com o seu nome completo
# 
# 
# **Desejamos uma boa prova!**
# 
# Com base nos itens acima, assinale a alternativa correta
# 
# a) Dados faltantes: 5, Total Valor Empenhado: 114025453, Porcentagem Majoritária: 43%<br>
# b) Dados faltantes: 9, Total Valor Empenhado: 204004899, Porcentagem Majoritária: 57% <br>
# <font color='red'>c) Dados faltantes: 14, Total Valor Empenhado: 104025454, Porcentagem Majoritária: 43%</font><br>
# d) Dados faltantes: 14, Total Valor Empenhado: 2283864, Porcentagem Majoritária: 43% <br>
# e) Dados faltantes: 5, Total Valor Empenhado: 104004899, Porcentagem Majoritária: 57% 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# carregar a base de dados
# data = pd.read_csv....

df = pd.read_csv('Emendas.csv')
df = df[['Nome Funcao', 'Valor Empenhado', 'Valor Pago', 'Valor Restos A Pagar Pagos']]
print(df.shape)
df.head()


# In[3]:


# computar valores faltantes na base de dados
df.isna().sum()


# In[4]:


df.isna().sum().sum()


# In[5]:


# preencher os valores faltantes conforme instrucoes


# In[6]:


media_valor_empenhado = df['Valor Empenhado'].mean()
media_valor_empenhado


# In[7]:


df['Valor Empenhado'] = df['Valor Empenhado'].fillna(media_valor_empenhado)
df.isna().sum()


# In[8]:


df = df.fillna(0.0)
df.isna().sum()


# In[9]:


# computar soma dos valores empenhados
soma_total_coluna_Valor_Empenhado = df['Valor Empenhado'].sum()/1000
round(soma_total_coluna_Valor_Empenhado,0)


# In[10]:


# computar porcentagem da categoria (Nome Funcao) majoritária
df['Nome Funcao'].value_counts()


# In[11]:


# valor maximo
df['Nome Funcao'].value_counts().max()


# In[12]:


# soma das frequencias
df['Nome Funcao'].value_counts().sum()


# In[13]:


# porcentagem
df['Nome Funcao'].value_counts().max()/df['Nome Funcao'].value_counts().sum()


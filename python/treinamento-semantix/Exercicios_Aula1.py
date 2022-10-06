
# coding: utf-8

# <div class= "alert alert-block alert-info">
# <b>Questão 1 - Importe a função randint da biblioteca</b>
# </div>

# In[1]:


from numpy.random import randint


# <div class= "alert alert-block alert-info">
# <b>Questão 2 - Crie uma lista de números 15 números aleatórios inteiros, que estejam entre 0 e 10, usando a função randint e o método append de uma lista.</b>
# </div>

# In[2]:


inteiros_15 = []

for i in range(15):
    inteiros_15.append(randint(10))


# In[3]:


inteiros_15


# In[4]:


len(inteiros_15)


# <div class= "alert alert-block alert-info">
# <b>Questão 3 - Adicione o comando %%timeit no topo da célula que você criou para a função 2, ele irá calcular o tempo médio de execução do seu código</b>
# </div>

# In[5]:


get_ipython().run_cell_magic('timeit', '', 'inteiros_15 = []\n\nfor i in range(15):\n    inteiros_15.append(randint(10))')


# <div class= "alert alert-block alert-info">
# <b>Questão 4 - Use os argumentos size e type na função randint para repetir a questão 2.</b>
# </div>

# In[27]:


randint(11, size=15)


# In[28]:


type(inteiros_15)


# In[29]:


aux = list(randint(11, size=15))
aux


# In[30]:


type(aux)


# <div class= "alert alert-block alert-info">
# <b>Questão 5 - Calcule o tempo do código feito na questão 4. É menor que o da questão 03?</b>
# </div>

# In[31]:


get_ipython().run_cell_magic('timeit', '', 'list(randint(11, size=15))')


# <div class= "alert alert-block alert-info">
# <b> Questão 6 - Faça uma função com apenas for,range,len, while, if, else, break para ordenar a lista que você criou na questão 04 do menor para o maior número.</b>
# </div>

# In[62]:


def verifica_se_ja_ordenou(lista):
    
    flag = True
    
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            flag = False
            
    return flag

def organiza_elementos(lista):
    
    ordenado = []
    
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            ordenado.append(lista[i+1])
            ordenado.append(lista[i])
            orndenado = ordenado + (lista[i+2:])
            break
        else:
            ordenado.append(lista[i])
    
    return ordenado

def ordena_lista(lista, maximo=100):
    
    ordenado = lista
    
    for i in range(maximo):
        if verifica_se_ja_ordenou(ordenado):
            #print('Lista Ordenada!')
            break
        else:
            ordenado = organiza_elementos(ordenado)
            #print(ordenado)
    
        if i == maximo:
            print('Atingiu o número maximo de iterações!')
    
    return ordenado      
    


# In[66]:


inteiros_15


# In[45]:


(len(inteiros_15)-1)


# In[67]:


verifica_se_ja_ordenou(inteiros_15)


# In[68]:


organiza_elementos(inteiros_15)


# In[69]:


ordena_lista(inteiros_15)


# <div class= "alert alert-block alert-info">
# <b>Questão 7 - Use a função sorted para refazer a questão 06</b>
# </div>

# In[33]:


sorted(inteiros_15)


# <div class= "alert alert-block alert-info">
# <b>Questão 8 - Calcule o tempo da questão 6 e da questão 07 </b>
# </div>

# In[34]:


get_ipython().run_cell_magic('timeit', '', 'sorted(inteiros_15)')


# In[51]:


get_ipython().run_cell_magic('timeit', '', 'ordena_lista(inteiros_15)')


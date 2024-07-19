"""# 3 Questão

A empresa BI Solutions resolveu realizar uma sindicância nos salários dos funcionários do ano de 2017. O objetivo da sindicância é identificar funcionários cujo padrão de recebimento de salário em 2017 esteja fora do padrão dos salários pagos em 2016, considerando que os dados de 2016 já foram auditados e estão adequados.

Para tanto, a empresa resolveu utilizar uma rede neural para identificar *anomalias* e, a partir dessas *anomalias*, investigar os funcionários.

**IMPORTANTE**: Leia a questão com muita atenção, desde que vários passos da questão já se encontram implementados. Os locais nos quais os comandos da questão devem ser especificados são identificados em comentários.

### 3.1 Dados para o Modelo

#### 3.1.1 Consulta dataAno 2016

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Considere a consulta a seguir, a qual retorna os valores dos atributos `funcPK`, `equipePK`, `dataPK`, `cargoPK` e `salario` da relação `pagamento`, considerando os pagamentos realizados na `dataAno` de `2016`. 
**A resposta desta consulta deve ser usada para treinar o modelo posteriormente. Note que essa resposta é armazenada no dataFrame `respostaPandas16`, que é um dataFrame em Pandas.**
"""

#especificando a consulta que retorna os valores dos atributos
#funcPK, equipePK, dataPK, cargoPK e salario
#para pagamentos realizados na dataAno de 2016
query2016 = query = """
SELECT funcPK, equipePK, pagamento.dataPK, cargoPK, salario
FROM pagamento, data
WHERE pagamento.dataPK = data.dataPK
      AND dataAno = 2016
ORDER BY funcPK, equipePK, pagamento.dataPK, cargoPK, salario       
"""

#transformando o resultado em um dataFrame em Pandas
respostaPandas16 = spark.sql(query2016).toPandas()

#exibindo algumas linhas do dataFrame respostaPandas16
respostaPandas16

"""#### 3.1.2 Consulta dataAno 2017

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Considere a consulta a seguir, a qual retorna os valores dos atributos `funcPK`, `equipePK`, `dataPK`, `cargoPK` e `salario` da relação `pagamento`, considerando os pagamentos realizados na `dataAno` de `2017`. 
**A resposta desta consulta deve ser verificada posteriormente utilizando a rede neural já treinada (mais detalhes abaixo). Note que essa resposta é armazenada no dataFrame `respostaPandas17`, que é um dataFrame em Pandas.**
"""

#especificando a consulta que retorna os valores dos atributos
#funcPK, equipePK, dataPK, cargoPK e salario
#para pagamentos realizados na dataAno de 2017



#transformando o resultado em um dataFrame em Pandas



#exibindo algumas linhas do dataFrame respostaPandas17
respostaPandas17

"""### 3.2 Especificação da Rede Neural

#### 3.2.1 Conversão dos dataFrames

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Execute os comandos a seguir, os quais convertem os `dataFrames` `respostaPandas16` e `respostaPandas17` para `numpy array`.
"""


#Convertendo os dataFrames para numpy array




"""#### 3.2.2 Inicialização das Sementes

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Execute os comandos a seguir, os quais inicializam as sementes a serem utilizadas.
"""

#inicializando as sementes
seed(1)
set_seed(1)

"""#### 3.2.3 Normalização

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Execute os comandos a seguir, nos quais atributos de entrada são normalizados por `min-max` para o intervalo `[0-1]`
"""

#Normalizando min-max para 0-1 (usando max e min do treinamento)
max = x_train.max(axis=0)
min = x_train.min(axis=0)
x_train = (x_train-min)/(max-min)
print(x_train.shape)

x_test = (x_test-min)/(max-min)
print(x_test.shape)

"""#### 3.2.4 Item 1 (RESOLVER)

Projete um **autoencoder** com a seguinte arquitetura, sendo todas as camadas com função de ativação `relu`:
  * Camada de entrada com 5 valores
  * Camada densa com 4 neurônios
  * Camada densa com 3 neurônios
  * Dropout com taxa= 1/3.0
  * Camada densa com 4 neurônios
  * Camada de saída

O objetivo desse autoencoder consiste em aprender uma representação para os dados do ano de 2016.
"""

#Escreva aqui a sua resposta para o Item 1

# Camada de entrada com 5 valores


# Camada densa com 4 neurônios, relu

# Camada densa com 3 neurônios, relu

# dropout 1/3

# Camada densa com 4 neurônios, relu

# Camada densa com 5 neurônios, relu



"""#### 3.2.5 Item 2 (RESOLVER)

**Compile** o modelo e **treine** por 250 épocas com batch_size 16, utilizando Adam com taxa de aprendizado inicial 0.002 e decaimento exponencial de -0.005 conforme funcão pré-definida abaixo.
"""

# Função que define decaimento para a taxa de aprendizado 

#Escreva aqui a sua resposta para o Item 2



# configurar o modelo para treinamento
# Perda MSE


# a schedule that is a tf.keras.optimizers.schedules.LearningRateSchedule



"""#### 3.2.6 Item 3 (RESOLVER)

Utilizando o conjunto de teste (`x_test`) como entrada para o modelo treinado, obtenha as saídas da predição usando `modelo.predict(x_test)`.  A seguir, compute a soma do erro quadrático, i.e. $||x - \hat{x}||^2$, sendo $x$ os atributos de entrada e $\hat{x}$ os valores de saída da rede neural, ou seja, o erro de reconstrução de cada exemplo de teste (original) com relação ao predito pelo modelo (exemplos resultados da saída da predição).

Armazene o erro de cada elemento organizados, em ordem, num array `error`.

O objetivo é verificar se alguma tupla do ano de 2017 possui alto erro de reconstrução, o que indicaria uma possível anomalia a ser investigada com relação aos atributos (cargo, equipe, salário, etc.).
"""

#Escreva aqui a sua resposta para o Item 3



"""#### 3.2.7 Obtendo o Valor de funcPK Relativo ao Maior Erro

*Esta parte da questão já está resolvida. Realize a leitura do enunciado e da resposta.*

Obtenha o valor do atributo `funcPK` não normalizado, referente ao `dataFrame` original, relativo à instância que possui o maior erro no teste. **O valor de `funcPK` deve ser usado para a especificação da consulta OLAP definida na seção 6.2.8.**
"""

# Obtendo o valor de funcPK desejado 

k_maiores = 1 # obtem os k valores com maior erro
for i in np.argpartition(error,-k_maiores)[-k_maiores:]:
    print(respostaPandas17.iloc[i,0])

"""## 3.3 Investigação do Funcionário

Uma vez identificado o código do funcionário, observou-se que ele recebeu salário muito superior quando comparado com os salários dos demais funcionários da empresa. Esse funcionário deve ser investigado considerando, portanto, seu salário. Essa investigação deve ser feita por meio da especificação de consultas OLAP.

Observações importantes:
- A **consulta OLAP** pode ser especificada:
   - Usando a **linguagem SQL** (conceitos apresentados na Aula 07)  
   OU (escolha somente uma forma)
   - Usando os métodos de **pyspark.sql** (conceitos apresentados na Aula 08). 
- Na listagem das respostas:
   - As **colunas** solicitadas devem ser exibidas exatamente na mesma ordem que a definida.
   - As **linhas** retornadas como respostas devem ser exibidas exatamente na mesma ordem que a definida. 
   - Os **nomes das colunas** renomeadas devem seguir estritamente os nomes definidos.
- Quando a consulta OLAP for especificada usando a **linguagem SQL**, use:
  - O comando `spark.sql(consultaSQL).show(20,truncate=False)` para exibir o resultado da consulta. Esse comando deve ser o último comando a ser especificado.
  - A função `ROUND(funçãoDeAgregação,2)` para arredondar o dado até duas casas decimais.
- Quando a consulta OLAP for especificada usando os demais **métodos de pyspark.sql**, use:
  - O comando `nomeDoDataFrame.show(20,truncate=False)` para exibir o resultado da consulta. Esse comando deve ser o último comando a ser especificado.
  - O método `round(funçãoDeAgregação,2)` para arredondar o dado até duas casas decimais.

#### 3.3.1 Item 4 (RESOLVER)

**Faça uma consulta que tem como objetivo investigar os meses e os valores dos salários recebidos no ano de 2017 pelo funcionário que está sendo inspecionado.** Ou seja, liste para cada mês do ano de 2017, o nome do funcionário, o mês e o salário recebido pelo funcionário cujo valor de `funcPK` foi identificado logo após o Item 3. Devem ser exibidas as colunas na ordem e com os nomes especificados a seguir: "NOMEFUNCIONARIO", "MES" e "SALARIO". Arredonde os salários para até duas casas decimais. Ordene as linhas exibidas primeiro por salário em ordem **descendente** e depois por mês em ordem **ascendente**. Liste as primeiras 20 linhas da resposta, sem truncamento das *strings*. **O maior valor de salário pode ser encontrado na primeira linha exibida para inspeção.**
"""

#Escreva aqui a sua resposta para o Item 4
# Resposta da Questão 1

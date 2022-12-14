# -*- coding: utf-8 -*-
"""Formação cientista de dados (Estatística e ML).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r5DOr8-FewtEFjPnzW19i6zecxQyeoRD
"""



"""# Machine Learning

Naive Bayes
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB # (Para fazer o NB)
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from yellowbrick.classifier import ConfusionMatrix # (Para criar uma matriz de confusão de maneira gráfica )

from google.colab import files
import io
uploaded = files.upload()
uploaded

credito = pd.read_csv('Credit.csv')

credito.head()

#Dividimos os previsores da classe
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values
previsores

#Transformação dos atributos categóricos em atributos numéricos
#Precisamos criar um objeto para cada atributo categórico, pois na sequência vamos registrar o encoding novamente 
#pare registro de teste
#Se forem utilizados objetos diferetenes o número atribuido a cada valor poderá ser diferente deixando assim nosso 
#modelo inconstistente

labelencoder1 = LabelEncoder()
previsores[:,0] = labelencoder1.fit_transform(previsores[:,0])

labelencoder2 = LabelEncoder ()
previsores[:,2] = labelencoder2.fit_transform(previsores[:,2])

labelencoder3 = LabelEncoder ()
previsores[:,3] = labelencoder3.fit_transform(previsores[:,3])

labelencoder4 = LabelEncoder ()
previsores[:,5] = labelencoder4.fit_transform(previsores[:,5])

labelencoder5 = LabelEncoder ()
previsores[:,6] = labelencoder5.fit_transform(previsores[:,6])

labelencoder6 = LabelEncoder ()
previsores[:,8] = labelencoder6.fit_transform(previsores[:,8])

labelencoder7 = LabelEncoder ()
previsores[:,9] = labelencoder7.fit_transform(previsores[:,7])

labelencoder8 = LabelEncoder ()
previsores[:,11] = labelencoder8.fit_transform(previsores[:,11])

labelencoder9 = LabelEncoder ()
previsores[:,13] = labelencoder9.fit_transform(previsores[:,13])

labelencoder10 = LabelEncoder ()
previsores[:,14] = labelencoder10.fit_transform(previsores[:,14])

labelencoder11 = LabelEncoder ()
previsores[:,16] = labelencoder11.fit_transform(previsores[:,16])

labelencoder12 = LabelEncoder ()
previsores[:,18] = labelencoder12.fit_transform(previsores[:,18])

labelencoder13 = LabelEncoder ()
previsores[:,19] = labelencoder13.fit_transform(previsores[:,19])

#Divisão da base de dados em treinamento e teste (30 % teste)
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state = 0)
x_teste

#teina o modelo

naive_bayes = GaussianNB ()
naive_bayes.fit(x_treinamento, y_treinamento)

# testa o modelo

previsoes = naive_bayes.predict(x_teste)

confusao = confusion_matrix(y_teste, previsoes)
confusao

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto

#Visualização gráfica da matriz de confusão 
v = ConfusionMatrix(GaussianNB())
v.fit(x_treinamento, y_treinamento)
v.score(x_teste, y_teste)
v.poof()

#Previsão com novo registro, tranformando os atributos categóricos em numéricos
from google.colab import files
import io
uploaded = files.upload()
uploaded

novo_credit = pd.read_csv('NovoCredit.csv')
novo_credit.head()

novo_credit = novo_credit.iloc[:,0:20].values

labelencoder1 = LabelEncoder()
novo_credit[:,0] = labelencoder1.fit_transform(novo_credit[:,0])

labelencoder2 = LabelEncoder ()
novo_credit[:,2] = labelencoder2.fit_transform(novo_credit[:,2])

labelencoder3 = LabelEncoder ()
novo_credit[:,3] = labelencoder3.fit_transform(novo_credit[:,3])

labelencoder4 = LabelEncoder ()
novo_credit[:,5] = labelencoder4.fit_transform(novo_credit[:,5])

labelencoder5 = LabelEncoder ()
novo_credit[:,6] = labelencoder5.fit_transform(novo_credit[:,6])

labelencoder6 = LabelEncoder ()
novo_credit[:,8] = labelencoder6.fit_transform(novo_credit[:,8])

labelencoder7 = LabelEncoder ()
novo_credit[:,9] = labelencoder7.fit_transform(novo_credit[:,7])

labelencoder8 = LabelEncoder ()
novo_credit[:,11] = labelencoder8.fit_transform(novo_credit[:,11])

labelencoder9 = LabelEncoder ()
novo_credit[:,13] = labelencoder9.fit_transform(novo_credit[:,13])

labelencoder10 = LabelEncoder ()
novo_credit[:,14] = labelencoder10.fit_transform(novo_credit[:,14])

labelencoder11 = LabelEncoder ()
novo_credit[:,16] = labelencoder11.fit_transform(novo_credit[:,16])

labelencoder12 = LabelEncoder ()
novo_credit[:,18] = labelencoder12.fit_transform(novo_credit[:,18])

labelencoder13 = LabelEncoder ()
novo_credit[:,19] = labelencoder13.fit_transform(novo_credit[:,19])

naive_bayes.predict(novo_credit)

"""Árvore de Decisão"""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
import graphviz
from sklearn.tree import export_graphviz

from google.colab import files
import io
uploaded = files.upload()
uploaded

credito = pd.read_csv("Credit.csv")

credito.size

credito.head()

previsores = credito.iloc[:,0:20].values # Com esse comando os eixos e legendas vão sumir e apenas os valores das colunas serão coletados
                                         # iloc é uma função que seleciona as linhas e colunas pedindo inteiros como argumento.
classe = credito.iloc[:,20].values       # Esse é a resposta que eu quero ter no fim, se o sujeito é bom ou mal pagador

#Conversão de atributos categóricos para atributos numéricos 

labelencoder1 = LabelEncoder()
previsores[:,0] = labelencoder1.fit_transform(previsores[:,0])
labelencoder2 = LabelEncoder ()
previsores[:,2] = labelencoder2.fit_transform(previsores[:,2])
labelencoder3 = LabelEncoder ()
previsores[:,3] = labelencoder3.fit_transform(previsores[:,3])
labelencoder4 = LabelEncoder ()
previsores[:,5] = labelencoder4.fit_transform(previsores[:,5])
labelencoder5 = LabelEncoder ()
previsores[:,6] = labelencoder5.fit_transform(previsores[:,6])
labelencoder6 = LabelEncoder ()
previsores[:,8] = labelencoder6.fit_transform(previsores[:,8])
labelencoder7 = LabelEncoder ()
previsores[:,9] = labelencoder7.fit_transform(previsores[:,7])
labelencoder8 = LabelEncoder ()
previsores[:,11] = labelencoder8.fit_transform(previsores[:,11])
labelencoder9 = LabelEncoder ()
previsores[:,13] = labelencoder9.fit_transform(previsores[:,13])
labelencoder10 = LabelEncoder ()
previsores[:,14] = labelencoder10.fit_transform(previsores[:,14])
labelencoder11 = LabelEncoder ()
previsores[:,16] = labelencoder11.fit_transform(previsores[:,16])
labelencoder12 = LabelEncoder ()
previsores[:,18] = labelencoder12.fit_transform(previsores[:,18])
labelencoder13 = LabelEncoder ()
previsores[:,19] = labelencoder13.fit_transform(previsores[:,19])

#Divisão da base de dados em treino e teste (30% treino e 70% teste)

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size =0.3 , random_state=0)

#Árvore de decisão
arvore = DecisionTreeClassifier()
arvore.fit (x_treinamento, y_treinamento)

export_graphviz(arvore, out_file = 'tree.dot') #Como fazer o processo de "poda" dos ramos da árvore e melhorar a eficiência da classificação.
                                                #Procure criar outros modelos desse, só que usando menos atributos

previsoes = arvore.predict(x_teste)
previsoes

confusao = confusion_matrix(y_teste, previsoes)
confusao

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto

"""Seleção de atributos (Evitar a maldição da dimensionalidade)

"""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import graphviz
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import export_graphviz



from google.colab import files
import io
uploaded = files.upload()
uploaded

credito = pd.read_csv("Credit.csv")

credito.head()

previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values

#Transformação dos atributos categóricos em atributos numéricos
#Precisamos criar um objeto para cada atributo categórico, pois na sequência vamos registrar o encoding novamente 
#pare registro de teste
#Se forem utilizados objetos diferetenes o número atribuido a cada valor poderá ser diferente deixando assim nosso 
#modelo inconstistente

labelencoder1 = LabelEncoder()
previsores[:,0] = labelencoder1.fit_transform(previsores[:,0])
labelencoder2 = LabelEncoder ()
previsores[:,2] = labelencoder2.fit_transform(previsores[:,2])
labelencoder3 = LabelEncoder ()
previsores[:,3] = labelencoder3.fit_transform(previsores[:,3])
labelencoder4 = LabelEncoder ()
previsores[:,5] = labelencoder4.fit_transform(previsores[:,5])
labelencoder5 = LabelEncoder ()
previsores[:,6] = labelencoder5.fit_transform(previsores[:,6])
labelencoder6 = LabelEncoder ()
previsores[:,8] = labelencoder6.fit_transform(previsores[:,8])
labelencoder7 = LabelEncoder ()
previsores[:,9] = labelencoder7.fit_transform(previsores[:,7])
labelencoder8 = LabelEncoder ()
previsores[:,11] = labelencoder8.fit_transform(previsores[:,11])
labelencoder9 = LabelEncoder ()
previsores[:,13] = labelencoder9.fit_transform(previsores[:,13])
labelencoder10 = LabelEncoder ()
previsores[:,14] = labelencoder10.fit_transform(previsores[:,14])
labelencoder11 = LabelEncoder ()
previsores[:,16] = labelencoder11.fit_transform(previsores[:,16])
labelencoder12 = LabelEncoder ()
previsores[:,18] = labelencoder12.fit_transform(previsores[:,18])
labelencoder13 = LabelEncoder ()
previsores[:,19] = labelencoder13.fit_transform(previsores[:,19])

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=1) #https://towardsdatascience.com/why-do-we-set-a-random-state-in-machine-learning-models-bb2dc68d8431

#Criando o modelo de máquina de vetor de suporte 

svm = SVC()
svm.fit(x_treinamento, y_treinamento)

previsoes = svm.predict(x_teste)
previsoes

taxa_acerto = accuracy_score(y_teste, previsoes)

taxa_acerto

#Vamos utilizar um modelo de random forest para medir a importancia dos atributos
# Não vai calcular sempre com os mesmos valores 

forest = ExtraTreesClassifier()
forest.fit(x_treinamento, y_treinamento)
importancias = forest.feature_importances_
importancias

#Criamos então um modelo de treinamento com os 4 mais importantes atributos
x_treinamento2 = x_treinamento[:,[0,1,2,3]]
x_teste2 = x_teste[:,[0,1,2,3]]

svm2 = SVC()
svm2.fit(x_treinamento2, y_treinamento)
previsoes2 = svm2.predict(x_teste2)
taxa_acerto2 = accuracy_score(y_teste, previsoes2)
taxa_acerto2

#Note que a taxa de acerto melhorou, mas essa diferença pode não ser significativa (pois estamos tomando uma
#amostragem dos dados). Porém, mesmo sem significância dessa diferença podemos dizer que esse modelo é muito 
#mais simples e com a mesma taxa de acerto, o que efetivamente é um modelo melhor. Ou seja 
# quanto mais simples e mais eficiente melhor !!

"""Aprendizado com Instância"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets #Onde existem vários datasets para se trabalhar
import pandas as pd
from scipy import stats

#carregamos da base de dados 
iris = datasets.load_iris()
stats.describe(iris.data)

iris.data

iris.target
iris.data

#Criação dos previsores 
previsores = iris.data
classe = iris.target



#Separando teste de treino
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state=0)
len(x_treinamento)

#Criação do modelo, treinamento
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_treinamento, y_treinamento)

previsoes = knn.predict(x_teste)
previsoes

confusao = confusion_matrix(y_teste, previsoes)
confusao

taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto

"""Ensemble Learning and Random Forest"""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

from google.colab import files
import io
uploaded = files.upload()
uploaded

credito = pd.read_csv("Credit.csv")
credito.head()

previsores = credito.iloc[:, 0:20].values
classe = credito.iloc[:,20].values

labelencoder1 = LabelEncoder()
previsores[:,0] = labelencoder1.fit_transform(previsores[:,0])
labelencoder2 = LabelEncoder ()
previsores[:,2] = labelencoder2.fit_transform(previsores[:,2])
labelencoder3 = LabelEncoder ()
previsores[:,3] = labelencoder3.fit_transform(previsores[:,3])
labelencoder4 = LabelEncoder ()
previsores[:,5] = labelencoder4.fit_transform(previsores[:,5])
labelencoder5 = LabelEncoder ()
previsores[:,6] = labelencoder5.fit_transform(previsores[:,6])
labelencoder6 = LabelEncoder ()
previsores[:,8] = labelencoder6.fit_transform(previsores[:,8])
labelencoder7 = LabelEncoder ()
previsores[:,9] = labelencoder7.fit_transform(previsores[:,7])
labelencoder8 = LabelEncoder ()
previsores[:,11] = labelencoder8.fit_transform(previsores[:,11])
labelencoder9 = LabelEncoder ()
previsores[:,13] = labelencoder9.fit_transform(previsores[:,13])
labelencoder10 = LabelEncoder ()
previsores[:,14] = labelencoder10.fit_transform(previsores[:,14])
labelencoder11 = LabelEncoder ()
previsores[:,16] = labelencoder11.fit_transform(previsores[:,16])
labelencoder12 = LabelEncoder ()
previsores[:,18] = labelencoder12.fit_transform(previsores[:,18])
labelencoder13 = LabelEncoder ()
previsores[:,19] = labelencoder13.fit_transform(previsores[:,19])

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size=0.3, random_state = 0)

florest = RandomForestClassifier(n_estimators = 100)
floresta.fit(x_treinamento, y_treinamento)

floresta.estimators_
#floresta.estimators_[1]

previsoes = floresta.predict(x_teste)
confusão = confusion_matrix(y_teste, previsoes)
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_acerto

"""Agrupamento com K-means (Aprendizado de máquina não supervisionado !)"""

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#carregamento da base de dados
iris = datasets.load_iris()
#visualização de quantos registros existem por classe
unicos, quantidade=np.unique(iris.target, return_counts = True) 
unicos
quantidade

#Agrupamento com K-Means utilizando 3 clusters
cluster = KMeans(n_clusters = 3)
cluster.fit(iris.data)

#Visualização dos 3 centróides 
centroids = cluster.cluster_centers_
centroids

#Visualização dos grupos que cada registro foi associado

previsoes = cluster.labels_
previsoes

#Contagem dos registros por classe

unicos2, quantidade2 = np.unique(previsoes, return_counts = True)
unicos2

quantidade2

#Geração da matriz de confusão para conparar o agrupamento com os dados 
resultados = confusion_matrix (iris.target, previsoes)
resultados

#Geração do gráfico com os clusters gerados, considerando para um (previsoes 0, 1 ou 2)
#Usamos somente as colunas 0 e 1 da base de dados original para termos 2 dimensões

plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1], c='green', label='Setosa')
plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1], c='red', label='Versicolor')
plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1], c='blue', label='Virgica')

plt.legend()

"""C-Means """

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix





"""# Regressão linear simples"""

import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # Criação do modelo
#Warning
from  yellowbrick.regressor import ResidualsPlot #visualização do modelo. 
import statsmodels.formula.api as sm

from google.colab import files
import io
uploaded = files.upload()
uploaded

base = pd.read_csv('cars.csv')
base

base.head() #

base = base.drop(['Unnamed: 0'], axis=1)
base.head()

x = base.iloc[:,1].values #Criação de variáveis 
y = base.iloc[:,0].values
x

r = np.corrcoef(x,y) #Cálculo da correlação
r

x = x.reshape(-1,1) #Essa função é necessária para mudar a dimensão do conjunto de dados que eu tenho
                    #eu preciso ter um array de 2D, caso contrário daria erro no código. 
                    # https://www.youtube.com/watch?v=3wi0lJPfLUY
x

x.ndim

modelo = LinearRegression() # Criação do modelo de treinamento
modelo.fit(x,y)

modelo.intercept_ # Intercept do modelo

modelo.coef_ # Coeficiente do modelo

plt.scatter(x,y)
plt.plot(x , modelo.predict(x), color = 'green') #Plot dos dados + fit

#Podemos então fazer uma estimação da velocidade inicial sabendo que a distância de parada é de 22 pés

modelo.intercept_ + modelo.coef_*22

#Usando função do sklearn
modelo.predict([[22]])

visualizador = ResidualsPlot(modelo)
visualizador.fit(x,y)
visualizador.poof()

# O resultado acima, serve para saber se o modelo de regressão linear é interessante para ser usado nesse modelo. 
# como os resíduos parecem estar aleatoriamente distribuidos (gráfico da esquerda) e seu histograma (gráfico da direita)
# lembra uma distribuição normal, faz sentido dizer que eles estão normalmente distribuídos e que a estratégia 
# de regressão linear é uma boa estratégia para explicar y.

"""# Regressão Linear Múltipla"""

from google.colab import files
import io
uploaded = files.upload()
uploaded

base = pd.read_csv('mt_cars.csv')
base

base.head()

base.size

base.shape

base = base.drop(['Unnamed: 0'], axis=1)
base

#Cálculo da correlação 
y  = base.iloc[:,0].values
x = base.iloc[:,2].values
r = np.corrcoef(x,y)
r

x = x.reshape(-1,1)

modelo=LinearRegression()
modelo.fit(x,y)

modelo.intercept_

modelo.coef_

modelo.score(x,y) #Esse é o R^{2}

previsões = modelo.predict(x)
previsões

#Criação do modelo usando a biblioteca statsmodel
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base)

modelo_treinado = modelo_ajustado.fit()

modelo_treinado.summary()

#visualização dos resultados 

plt.scatter(x,y)
plt.plot(x,previsões, color = 'red')

modelo.predict([[200]])

#Criação de novas variáveis para utilização na bib de stats model
x1 = base.iloc[:, 1:4].values
y1 = base.iloc[:, 0].values

modelo2 = LinearRegression()
modelo2.fit(x1,y1)

#Modelo de regressão múltipla

modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base)
modelo_treinado = modelo_ajustado2.fit()
modelo_treinado.summary()

#Parâmetros para previsão 

novo = np.array([4,200,100])
novo = novo.reshape(1,-1)
modelo2.predict(novo)



"""# Séries temporais"""

#Séries temporais com Python

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime 
#registros de converters para uso do matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#Carregamento da base de dados

from google.colab import files
import io
uploaded = files.upload()
uploaded

base = pd.read_csv("AirPassengers.csv")
base

#Visualizando o tipo dos atributos
print(base.dtypes)

#Como o moth é visto como objeto e não como data, precisamos convertê-lo.
dateparse = lambda dates: datetime.strptime(dates, '%Y-%m') #Conversão dos atributos que estão no tipo string, para os atributos que estão no tipo ANO-MES
base = pd.read_csv("AirPassengers.csv", parse_dates=["Month"], index_col="Month", date_parser=dateparse)
base

base.index

# Criação da série temporal
ts = base['#Passengers']
ts

# Visualização de registro específico 

ts[1]

ts['1949-02']

ts[datetime(1949,2,1)]

ts['1950-01-01':'1970-01-01']

#Visualização de intervalos sem preencher a data de início

ts[:'1949-01-31']

#Visualização por ano 

ts['1950']

ts.index.max()

ts.index.min()

#Visualização da s[erie temporal completa

plt.plot(ts)

#Visualização por ano

ts_ano = ts.resample('A').sum()
plt.plot(ts_ano)

#Visualização por mês 

ts_mes = ts.groupby([lambda x: x.month]).sum() # O que é isso de 
plt.plot(ts_mes)

#Visualização entre datas específicas

ts_datas = ts['1960-01-01':'1960-12-01']
plt.plot(ts_datas)



"""Decomposição de Séries Temporais"""

import pandas as pd
from  statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pylab as plt
from datetime import datetime 
#registros de converters para uso do matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

decompose = seasonal_decompose(ts)

#tendencia

tendencia = decompose.trend
tendencia

#sazonalidade

sazonal = decompose.seasonal
sazonal

#aleatoriedade

ruido = decompose.resid

plt.plot(sazonal)

plt.plot(tendencia)

plt.plot(ruido)

# Podemos organizar no mesmo plot esses três gráficos

plt.subplot(4,1,1)
plt.plot(ts, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4,1,2)
plt.plot(tendencia, label = 'Tendencia')
plt.legend(loc = 'best')


plt.subplot(4,1,3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4,1,4)
plt.plot(ruido, label = 'Aleatório')
plt.legend(loc = 'best')
plt.tight_layout()



"""Previsões com Arima """

!pip install statsmodels==0.12.2

import pandas as pd
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima
from datetime import datetime 
#registros de converters para uso do matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.plot(ts)

#Criação do modelo arima com os parâmetros p=2 (ordem da autorergessão) q=1 (ordem da média móvel) d=2 (grau de diferenciação), treinamento e visualização dos resultados
#Mais detalhes sobre o parâmetro, veja a aula 
modelo = ARIMA(ts,  order=(2,1,2), freq = ts.index.inferred_freq)
modelo_treinado = modelo.fit()
modelo_treinado.summary()

# Perceba que isso é um pouco do que você fazia com Mel, na IC. E perceba que o AIC e o BIC devem ser minimizados.

#Previsão de 12 datas no futuro 

previsoes = modelo_treinado.forecast(steps=12)[0]
previsoes

#Criação do eixo para a série temporal completa, com adição das previsões do modelo.
#lot_insample = True -> dados originais
eixo = ts.plot()
modelo_treinado.plot_predict('1960-01-01','1965-01-01', ax = eixo, plot_insample = True)

#Implementação do auto arima para encontrar os parâmetros automaticamente 

modelo_auto = auto_arima(ts, m=12, seasonal = True,trace = False)
modelo_auto.summary()

proximos_12 = modelo_auto.predict(n_periods = 12)
#visualização dos próximos 12 valores
proximos_12



"""Machine Learning"""


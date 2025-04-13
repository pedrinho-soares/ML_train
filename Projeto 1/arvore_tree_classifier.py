# %%
import pandas as pd

df = pd.read_excel("../data/dados_frutas.xlsx")
df

# %%
## Como aplicar o método do slide para descobrir a fruta?

filtro_redondada = df["Arredondada"] == 1

filtro_suculenta = df["Suculenta"] == 1

filtro_vermelha = df["Vermelha"] == 1

filtro_doce =df["Doce"] == 1

df[filtro_redondada & filtro_suculenta & filtro_doce & filtro_vermelha]


# %%
## Como podemos fazer a máquina aprender?

from sklearn import tree

features = ["Arredondada", "Doce", "Vermelha","Suculenta" ] 
target = "Fruta"

x = df[features]
y = df[target]
# %%
tree.plot_tree
# %%

import matplotlib.pyplot as plt

plt.figure(dpi=700)

tree.plot_tree(arvore,
               class_names=arvore.classes_,
               feature_names=features,
               filled=True)

# %%
# ["Arredondada","Suculenta","Vermelha","Doce"]
arvore.predict([[0,1,1,1]])

# %%

probas = arvore.predict_proba([[1,1,1,1]])[0]
pd.Series(probas, index=arvore.classes_)

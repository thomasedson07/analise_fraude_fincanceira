
!pip install pyspark

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df = spark.read.csv('/content/drive/MyDrive/creditcard.csv', header=True)
df.show(100

# Limpeza
df = df.dropna()
df = df.dropDuplicates()
df = df.fillna(0)
df.show(10)

# filtrando Falsas transacoes
df.filter(df['Class'] == 1).show()

# analise para entender a distribuição dos dados
df.describe().show()

# procenatagem do Class
df.groupBy('Class').count().show()

# Distribuição temporal
df.groupBy('Time').count().show()

# salvar codigo
df.write.csv('/content/drive/MyDrive/creditcard_clean.csv', header=True)

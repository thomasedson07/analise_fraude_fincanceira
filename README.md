# 📊 Projeto de Análise de Dados —  Fraudes Financeiras

Este repositório contém a entrega do projeto de parceria **Semantix**, que envolve a análise de dados aplicada a um problema real e relevante da sociedade.

---

## 🔎 1. Problema

**Descrição:**  

Fraudes financeiras são práticas ilícitas em que indivíduos ou grupos criminosos manipulam ou falsificam informações para obter ganhos econômicos de forma ilegal. Essas fraudes ocorrem principalmente em cartões de crédito, transferências bancárias, empréstimos online e compras em plataformas digitais.
Com o avanço da tecnologia e a digitalização dos serviços financeiros, os criminosos utilizam métodos cada vez mais sofisticados, como roubo de identidade, clonagem de cartões e uso de bots automatizados. Além disso, o grande volume de transações diárias torna extremamente difícil a detecção manual dessas práticas, possibilitando que golpes passem despercebidos.

**Importância:** 

A relevância do combate a fraudes financeiras é enorme, tanto no contexto econômico quanto institucional:

Econômico: Estima-se que bilhões de dólares sejam perdidos anualmente em fraudes bancárias no mundo, causando prejuízos diretos a instituições financeiras e clientes.

Institucional: A confiança do público em bancos, fintechs e sistemas de pagamento digital depende diretamente da segurança das transações. Se os clientes não se sentirem protegidos, a adesão a novas tecnologias financeiras diminui.

**Como a análise de dados ajuda:**  

A análise de dados surge como ferramenta central para a prevenção e mitigação de fraudes financeiras:

Detecção de anomalias: algoritmos de machine learning analisam padrões de comportamento em transações (valores, horários, localização geográfica) e identificam atividades fora do padrão esperado, sinalizando possíveis fraudes.

Monitoramento em tempo real: sistemas baseados em Big Data processam milhões de operações instantaneamente, bloqueando ou notificando transações suspeitas antes mesmo de sua conclusão.

Modelos preditivos: ao utilizar dados históricos de transações fraudulentas, é possível treinar modelos para prever a probabilidade de fraude em novas operações.

Análise de redes sociais e conexões: técnicas de graph analysis permitem identificar redes de criminosos que compartilham dados ou agem em grupo.

Automação de auditorias: reduz custos com verificações manuais, liberando equipes para focarem em casos mais complexos.
---

## 📂 2. Fontes de Dados

| Fonte | Tipo de Dados | Forma de Coleta |
|-------|---------------|-----------------|
| Credit Card Fraud Detection | Estruturados | Download Kaggle |

---

## 🛠️ 3. Ferramentas Utilizadas

- **Python** liguagem usada
- **PySpark** para manipulação de grandes volumes de dados
- **Google Looker Studio** para visualizações
- **Google Planilhas** para análises rápidas e consolidação

---

## 📊 4. Análise Exploratória de Dados (EDA)

Etapas realizadas:
**Limpeza e pré-processamento** (remoção de duplicados e tratamento de valores ausentes).
**Análise descritiva** (distribuições, médias, medianas).

  Notebook disponívei em [Link do Notebook](https://colab.research.google.com/drive/1ADFtjV31fGhhn718HGHTkRbSAGKMthRE?usp=sharing).

---

## 💡 5. Relatório de Insights

Principais achados:
- Insight 1: [Desbalanceamento extremo: Apenas 0,16% das transações são fraudulentas.]  
- Insight 2: [Padrões em variáveis: Certas variáveis transformadas pelo PCA (ex.: V14, V17) apresentam diferenças estatísticas expressivas entre fraudes e transações normais.]  
- Insight 3: [Distribuição temporal: As fraudes não seguem horas ou dias expecificos.]

---

## 📊 6. Dashboard no Looker Studio

O dashboard interativo pode ser acessado no link:  
👉 [Link do Dashboard](https://lookerstudio.google.com/s/j0huWrI2Q_k)

---

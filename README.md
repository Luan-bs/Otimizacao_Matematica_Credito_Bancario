# Aplicação de Modelagem Matemática na Alocação Ótima de Recursos e Gestão de Risco em Instituições Financeiras

Repositório do projeto desenvolvido para a disciplina de Modelagem Matemática e Otimização do curso de **Bacharelado em Inteligência Artificial e Ciência de Dados** do Biopark Educação / Faculdade Donaduzzi.

---

## 📊 Sobre o Projeto
Este projeto aplica técnicas de **Programação Linear (PL)** para resolver um problema real de alocação de recursos em uma instituição bancária, baseado no estudo de Akudugu e Boah (2022). O objetivo é maximizar o lucro líquido de uma carteira de empréstimos composta por cinco modalidades de crédito, respeitando rigorosamente limites de orçamento, inadimplência máxima, concentração de risco e proporções estruturais.

---

## 🛠️ Stack Tecnológica
* **Python 3.10+**
* **SciPy** (Otimização via método HiGHS)
* **NumPy** (Processamento vetorial e matricial)
* **uv** (Gerenciamento de dependências ultrarrápido)

---

## 📈 Resultados e Solução Ótima

A resolução do modelo via método Simplex (HiGHS) convergiu para uma solução ótima global, alocando integralmente o orçamento de **GH¢ 5.000.000,00** e alcançando um **Lucro Líquido Máximo de GH¢ 1.158.750,00**[cite: 6].

### 1. Alocação Ótima de Recursos
| Variável de Decisão | Modalidade de Crédito | Valor Alocado |
| :--- | :--- | :--- |
| **X1** | Empréstimos Pessoais | GH¢ 500.000,00[cite: 6] |
| **X2** | Pensionistas | GH¢ 0,00[cite: 6] |
| **X3** | Pequenas e Médias Empresas (PMEs) | GH¢ 2.250.000,00[cite: 6] |
| **X4** | Administração e Funcionários | GH¢ 0,00[cite: 6] |
| **X5** | Adiantamento / Cheque Especial | GH¢ 2.250.000,00[cite: 6] |
| **P** | **Lucro Máximo Total** | **GH¢ 1.158.750,00**[cite: 6] |

* **Destaque:** O modelo concentrou o teto máximo permitido de **45%** do capital nas duas modalidades de maior retorno líquido ($X_3$ e $X_5$), direcionando 10% para $X_1$ e zerando as linhas de menor rentabilidade[cite: 6]. A taxa média ponderada de inadimplência ficou em **1,625%**, mantendo-se confortavelmente abaixo do teto regulatório de 2%[cite: 6].

---

### 2. Análise de Dualidade (Preços-Sombra)
Os preços-sombra ($Y$) indicam o custo de oportunidade e o quanto o lucro ótimo aumentaria caso os recursos ou limites das restrições fossem relaxados em uma unidade[cite: 6]:
* **$Y_1$ (Orçamento Total = 0,232):** Confirma que o capital é o principal gargalo do sistema; cada unidade monetária extra injetada no orçamento gera um retorno marginal de **23,2%**[cite: 6].
* **$Y_5$ (Concentração PMEs = 0,010) e $Y_7$ (Concentração Cheque Especial = 0,005):** Comprovam que as políticas de teto de 45% atuam como barreiras financeiras restritivas[cite: 6].
* Demais restrições apresentaram preços-sombra nulos ($Y_2, Y_3, Y_4, Y_6, Y_8 = 0,000$), indicando que operaram com folga estrutural[cite: 6].

---

### 3. Análise de Sensibilidade Paramétrica
O teste de variação simultânea nos coeficientes de lucro demonstrou a alta estabilidade e robustez do modelo frente a cenários macroeconômicos voláteis[cite: 6]:

| Variação no Lucro | Lucro Ótimo Resultante |
| :---: | :---: |
| **-30%** | GH¢ 811.125,00[cite: 6] |
| **-20%** | GH¢ 927.000,00[cite: 6] |
| **-10%** | GH¢ 1.042.875,00[cite: 6] |
| **-5%** | GH¢ 1.100.812,50[cite: 6] |
| **0%** | **GH¢ 1.158.750,00** *(Base)*[cite: 6] |
| **+5%** | GH¢ 1.216.687,50[cite: 6] |
| **+10%** | GH¢ 1.274.625,00[cite: 6] |
| **+20%** | GH¢ 1.390.500,00[cite: 6] |
| **+30%** | GH¢ 1.506.375,00[cite: 6] |

---

## 🚀 Como Executar

1. Certifique-se de ter o `uv` instalado em sua máquina.
2. Clone este repositório e acesse a pasta raiz.
3. Execute o script principal diretamente com o gerenciador:

```bash
uv run main.py
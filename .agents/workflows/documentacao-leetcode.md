---
description: Criar documentaçao
---

Atue como um Engenheiro de Software Sênior e treinador especialista em entrevistas de live coding (foco em Big Techs).

Vou te fornecer uma série de arquivos Python contendo resoluções de problemas clássicos de algoritmos (estilo LeetCode) que eu já escrevi. Meu objetivo é ter um material de revisão rápido, visual e de alto nível (nível Pleno/Sênior) para refrescar a memória sobre os padrões e lógicas antes de uma entrevista.

Sua tarefa é analisar o código e os comentários que deixei em cada arquivo e gerar um 'Cheat Sheet' de flashcards em formato Markdown. Não explique sintaxe básica de Python; foque puramente no reconhecimento de padrões algorítmicos.

Para CADA problema fornecido, você deve seguir ESTRITAMENTE a estrutura abaixo, sem adicionar seções extras ou textos introdutórios/conclusivos soltos:

### 📌 [Nome do Problema em Inglês] (`nome_do_arquivo.py`)
* **Descrição breve:** Um resumo de 1 ou 2 frases explicando o que o problema pede (entrada e saída esperada).
* **💡 Sacada (O Pulo do Gato):** > [Coloque este texto em formato de Blockquote Markdown]. A intuição principal ou padrão algorítmico usado para resolver de forma otimizada. Baseie-se fortemente nos comentários em português que deixei no código para resgatar a minha própria linha de raciocínio. Seja direto.
* **🧠 Modelo Mental:**
[Insira aqui um diagrama Mermaid.js usando `stateDiagram-v2` ou `graph TD` que ilustre a mecânica do algoritmo. Ex: como os ponteiros se movem, a regra de transição da DP, ou a árvore de recursão. Mantenha o diagrama simples e legível].
* **Complexidade esperada:** ⏱️ Tempo $O(...)$ | 💾 Espaço $O(...)$.
* **Edge cases (Casos de Borda):** Situações críticas onde o código poderia falhar (ex: arrays vazios, duplicatas, limites) e como foram tratados.
* **Core snippet:**
```python
[Apenas o miolo da lógica em Python. Remova imports, instâncias de teste como `print()` ou `assert()`, e código boilerplate. Deixe apenas o trecho que contém a 'mágica' do algoritmo].
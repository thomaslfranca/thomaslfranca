## 🧩 **Módulo 1 – Fundamentos de Grafos e do Neo4j**

### 🎯 Objetivo

Você vai entender o que são grafos, por que eles são poderosos, e como usar o Neo4j — mesmo sem saber programar.

---

### 📍 **Lição 1: O que é um Grafo?**

**Explicação simples:**
Um grafo é uma forma de organizar dados em **pontos (nós)** e **conexões (arestas)**. Em vez de pensar em planilhas com linhas e colunas, você pensa em redes. Isso imita como a gente pensa no mundo real.

**Exemplo real:**
Imagine o LinkedIn. Cada pessoa é um **nó**, e cada "conexão" entre elas é uma **aresta**. Isso é um grafo!

**Exercício rápido:**
Pense em três coisas conectadas no seu dia a dia (ex: você → amigo → cidade onde moram). Escreva essas conexões como:

```
Você → amigo
amigo → cidade
```

---

### 📍 **Lição 2: O que é o Neo4j?**

**Explicação simplificada:**
O Neo4j é um **banco de dados de grafos**. Ele armazena e consulta dados **em forma de grafo**, o que é mais natural quando falamos de relações.

**Ferramenta prática:**
👉 Acesse o **Neo4j Sandbox** (não precisa instalar nada):
[https://neo4j.com/sandbox](https://neo4j.com/sandbox)

Crie uma conta gratuita, escolha o **"Blank Sandbox"**, e você já pode brincar com grafos direto no navegador.

---

### 📍 **Lição 3: Cypher – A linguagem dos grafos**

**O que é?**
Cypher é como o "SQL dos grafos". Mesmo sem saber programar, você vai conseguir entender com um pouco de prática.

**Exemplo simples:**

```cypher
CREATE (a:Pessoa {nome: 'Você'})
CREATE (b:Pessoa {nome: 'Amigo'})
CREATE (c:Cidade {nome: 'São José dos Campos'})
CREATE (a)-[:CONHECE]->(b)
CREATE (b)-[:MORA_EM]->(c)
```

Isso cria 3 nós e 2 conexões — exatamente como seu exemplo!

---

### ✅ **Ponto de Verificação**

**Mini quiz (responda mentalmente ou escreva):**

1. O que é um nó em um grafo?
2. O que representa uma aresta?
3. Dê um exemplo de grafo com 3 nós e 2 conexões.
4. O que o Neo4j faz de diferente comparado a um Excel?

---

### 📚 Leitura e Recursos

* [Neo4j para iniciantes (em português)](https://neo4j.com/developer/pt-br/)
* [The Graph Academy (em inglês, visual)](https://graphacademy.neo4j.com/)
* [Curso gratuito no YouTube: Neo4j Básico](https://www.youtube.com/watch?v=0rEN8obCjQ4)

---

### 🧠 Desafio opcional

Crie uma conta no [Neo4j Sandbox](https://neo4j.com/sandbox), replique o exemplo acima com seus próprios dados (ex: você, seus amigos, lugares que frequentam) e tire um print da visualização do grafo.

---

Quando estiver pronto, posso te guiar para o **Módulo 2 – Construindo seu primeiro grafo completo com dados reais**.

Quer continuar?

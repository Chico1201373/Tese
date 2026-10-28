# Protocolo de revisão sistemática da literatura

**Versão:** rascunho de trabalho 0.1  
**Data:** 2026-10-28  
**Janela temporal prevista:** 2021-10-27 a 2026-10-27  
**Fontes principais propostas:** Scopus, IEEE Xplore e ACM Digital Library

> Este protocolo adapta a revisão ao sistema em estudo: um chat de apoio ao estudo que recebe o ID de uma pergunta, consulta o respetivo registo no QBank e envia os dados recuperados ao Qwen na prompt. Não pressupõe pesquisa vetorial nem RAG convencional.

## 1. Objetivo e âmbito

Identificar e sintetizar estudos sobre sistemas conversacionais baseados em LLM que usam contexto específico da aplicação — por exemplo, conteúdo incluído na prompt, registos de uma base de dados, bancos de perguntas ou documentos — e sobre a forma como restringem e avaliam as respostas.

O foco de aplicação é apoio ao estudo, resposta a perguntas educativas ou médicas e contextos próximos. Estudos de outros domínios podem ser incluídos quando descrevam uma técnica ou avaliação diretamente transferível para sistemas de resposta condicionados por contexto.

## 2. Research Questions

**RQ1 — Contextualização e compromissos de implementação**  
*How do LLM-based conversational systems use application-specific context to constrain responses, and what operational trade-offs are reported for these mechanisms?*

**RQ2 — Avaliação das respostas**  
*How are factual correctness, faithfulness to the supplied context, and adherence to the defined scope evaluated in LLM-based conversational systems?*

Na análise, a RQ1 será organizada em duas dimensões: (a) mecanismo de contextualização e controlo da resposta; (b) limitações de fiabilidade/segurança e compromissos de latência/custo/integração. A RQ2 será organizada por método, métrica e resultado da avaliação.

Esta estrutura mantém as três dimensões importantes para o tema, mas formula duas perguntas principais, como pede a atividade de Research Methods. O tutorial mostra três RQs num exemplo ilustrativo; a formulação final deve também caber no âmbito e no prazo do projeto.

### Como responder às perguntas

- **Dados:** referências e metadados exportados das bases, seguidos da leitura integral dos estudos elegíveis.
- **Análise:** síntese descritiva e temática dos mecanismos, controlos, métricas, resultados e trade-offs; não comparar diretamente métricas incompatíveis.
- **Resultado esperado:** uma taxonomia de mecanismos e práticas de avaliação, uma síntese das limitações e uma oportunidade de investigação sustentada pelo corpus.
- **Ligação ao artefacto da dissertação:** a revisão informa como avaliar um chat que recupera pelo ID os dados de uma pergunta do QBank e os inclui na prompt do Qwen; a revisão não pressupõe que a solução implemente pesquisa vetorial.

## 3. Fontes de pesquisa e justificação

- **Scopus:** cobertura multidisciplinar e pesquisa em título, resumo e palavras-chave.
- **IEEE Xplore:** literatura de engenharia informática, sistemas, IA e aplicações.
- **ACM Digital Library:** literatura de informática e sistemas conversacionais.
- **Nota de acesso:** no acesso usado pelo estudante, o link do Moodle identificado como Web of Science abre a interface Scopus. Esses resultados serão registados como Scopus e não como uma fonte Web of Science separada, para evitar duplicar bases ou contagens.
- **Scimago Journal & Country Rank (SJR):** apoio opcional para consultar a classificação de revistas; não é uma base de pesquisa de artigos e os seus resultados não entram nos números de identificação do PRISMA.

Registar, para cada execução: fonte, data e hora, query exata, campo pesquisado, filtros, número de resultados e nome do ficheiro exportado. Exportar, quando disponível, título, autores, ano, resumo, palavras-chave, DOI e referência da fonte.

OpenAlex pode ser usado para descoberta complementar e pesquisa de citações, sempre identificado separadamente. Os resultados OpenAlex filtrados por prefixo DOI no relatório `resultados_20261028_1426_editor.md` não são resultados de pesquisa nativa das bases e não entram nos totais principais do PRISMA.

## 4. Período, idioma e tipo de publicação

- Publicações entre **2021-10-27 e 2026-10-27**, inclusive. Aplicar os filtros anuais disponíveis na plataforma e confirmar manualmente os limites exatos das datas.
- Idioma: inglês ou português.
- Artigos de revista e artigos completos de conferência, revistos por pares.
- Revisões, editoriais, opiniões, posters e resumos sem artigo completo não entram na síntese de estudos primários; podem apoiar enquadramento ou pesquisa de referências e devem ser contabilizados separadamente se forem encontrados.

## 5. Estratégia de pesquisa

Cada expressão abaixo tem no máximo oito operadores booleanos. As pesquisas temáticas são separadas para manter a consulta legível e reduzir a perda de estudos por uma combinação demasiado restritiva.

### RQ1 — Mecanismos de contextualização

**RQ1a — Contexto, grounding e sistemas conversacionais (8 operadores)**

```text
("large language model" OR LLM) AND (grounding OR "prompt context" OR "retrieval-augmented generation" OR "context-aware") AND (chatbot OR "conversational system" OR "question answering")
```

**RQ1b — Recuperação de bases de dados e knowledge bases (6 operadores)**

```text
("large language model" OR LLM) AND ("database retrieval" OR "context injection" OR "knowledge base") AND (chatbot OR "question answering")
```

### RQ2 — Avaliação de respostas

**RQ2a — Correção e fidelidade (7 operadores)**

```text
("large language model" OR LLM) AND (faithfulness OR factuality OR correctness OR "scope adherence") AND (evaluation OR benchmark)
```

**RQ2b — Abstenção e perguntas fora do âmbito (5 operadores)**

```text
("large language model" OR LLM) AND ("out-of-scope" OR abstention) AND (evaluation OR benchmark)
```

### RQ1 — Limitações e compromissos operacionais

**RQ1c — Fiabilidade e segurança (7 operadores)**

```text
("large language model" OR LLM) AND (reliability OR robustness OR security OR "prompt injection") AND (chatbot OR "conversational system")
```

**RQ1d — Desempenho, custos e integração (7 operadores)**

```text
("large language model" OR LLM) AND (latency OR cost OR efficiency) AND (integration OR deployment OR architecture)
```

### Adaptação da sintaxe por fonte

Executar cada expressão na respetiva interface; não copiar a sintaxe de uma plataforma para outra sem confirmar os campos:

- **Scopus:** `TITLE-ABS-KEY(<expressão>)`.
- **IEEE Xplore:** expressão booleana na pesquisa avançada, em campos de metadados/título-resumo-palavras-chave quando disponíveis.
- **ACM Digital Library:** `AllField=(<expressão>)`, conforme a pesquisa avançada usada.

Filtros planeados: intervalo temporal, tipo de publicação e idioma apenas quando a plataforma os disponibilizar de forma verificável. Registar o filtro efetivamente aplicado; não inferir filtros a partir dos resultados.

### Pesquisa piloto

Antes da execução final, inspecionar 20–30 resultados de cada expressão na primeira fonte. Registar artigos claramente relevantes, falsos positivos e termos que parecem faltar. Alterar expressões apenas com justificação e guardar a versão executada no log. Depois da validação, executar as versões finais em todas as fontes e exportar os resultados completos. Se uma plataforma limitar a exportação, dividir a recolha por anos ou lotes e registar cada lote; não tratar um limite arbitrário de 1.000 como pesquisa completa.

## 6. Critérios de inclusão

1. Publicação dentro da janela temporal e em inglês ou português.
2. Estudo primário, revisto por pares, em revista ou conferência, com texto integral disponível.
3. Sistema ou estudo baseado em LLM para diálogo, chatbot ou resposta a perguntas.
4. Contributo relevante para pelo menos uma RQ: contexto específico/limites da resposta, avaliação de correção/fidelidade/âmbito, ou limitações operacionais.

## 7. Critérios de exclusão

1. Não usa LLM ou não aborda diálogo/resposta a perguntas.
2. Não envolve contexto específico nem apresenta avaliação ou análise relacionada com qualquer RQ.
3. Revisão, editorial, opinião, poster, resumo de conferência sem artigo completo ou duplicado de outro registo; revisões ficam guardadas à parte para enquadramento.
4. Texto integral avaliado e considerado insuficiente para identificar método, sistema ou evidência relevante para as RQs.

Se um texto integral potencialmente elegível não puder ser obtido, registar como **relatório não recuperado** no fluxo PRISMA; não o converter silenciosamente numa exclusão após leitura integral.

## 8. Seleção e registo PRISMA

1. Exportar os resultados por fonte e preservar os ficheiros originais.
2. Deduplicar primeiro por DOI normalizado e depois por título/autores, mantendo a fonte de origem de cada registo.
3. Fazer triagem manual de título e resumo, registando incluir/excluir e um motivo principal de exclusão.
4. Procurar o texto integral dos registos potencialmente elegíveis.
5. Avaliar o texto integral segundo os critérios e registar um motivo principal por exclusão.
6. Preencher o diagrama com os totais por fonte, duplicados, registos triados, exclusões, relatórios não recuperados, textos integrais avaliados e estudos incluídos.

Os números do relatório OpenAlex são auxiliares e não substituem as contagens das pesquisas executadas nas fontes principais. Os cinco artigos de `urls.txt` são candidatos iniciais para triagem, não estudos incluídos automaticamente.

## 9. Avaliação da qualidade metodológica

Pontuar cada critério como **Sim = 1**, **Parcial = 0,5**, **Não = 0**. Usar a pontuação para qualificar a força da síntese, não como exclusão automática sem regra previamente justificada.

1. O objetivo e a pergunta do estudo estão claros?
2. O sistema, o modelo, o contexto de origem e o mecanismo de contextualização estão descritos?
3. Os dados, perguntas ou cenários de avaliação são descritos?
4. O método de avaliação é adequado à afirmação (avaliação humana, comparação com fonte, métricas ou benchmark)?
5. As limitações e ameaças à validade são discutidas?

## 10. Matriz de extração de dados

Extrair oito campos por estudo:

1. Referência bibliográfica, ano, DOI, fonte e tipo de estudo.
2. Domínio, utilizadores e finalidade do sistema.
3. Origem e forma do contexto (ID/base de dados, documentos, prompt, RAG ou outra).
4. Mecanismos para limitar a resposta (instruções, filtros, citações, validação, abstenção).
5. Modelo, arquitetura e componentes relevantes (incluindo embeddings/intenção se usados no sistema).
6. Desenho de avaliação, conjunto de perguntas, avaliadores e métricas.
7. Resultados sobre correção, fidelidade ao contexto e perguntas fora do âmbito.
8. Limitações e compromissos de fiabilidade, segurança, latência, custo, privacidade e integração; pontuação de qualidade.

## 11. Plano de síntese e research gap

Agrupar os estudos por mecanismo de contextualização, tipo de fonte, controlo de âmbito e estratégia de avaliação. Comparar resultados e limitações sem tratar métricas diferentes como diretamente equivalentes. Para cada RQ, separar frequência descritiva de evidência de eficácia.

Derivar o gap com a cadeia **evidência → limitação observada → gap sustentado pelo corpus → oportunidade de investigação**. Não declarar um gap apenas porque um artigo o menciona; verificar se aparece em vários estudos e se os critérios do protocolo o cobrem.

## 12. Estado atual

- As duas RQs e queries acima são uma proposta de protocolo para pilotagem.
- `resultados_20261028_1426_editor.md` contém resultados OpenAlex e triagem automática; o próprio ficheiro identifica essa origem.
- A pesquisa nativa final, a deduplicação dos exports, a triagem manual, a avaliação de qualidade, a extração e os números finais do PRISMA ainda têm de ser feitos.

# Notas da leitura integral (estudos prioritários)

Uma entrada por estudo, a partir do texto integral em textos/<id>.txt.
Campos: arquitetura e contexto | modelo e execução | dados | avaliação | resultados | limitações | relevância para o QBank.
Decisão de elegibilidade: Incluir / Excluir (com motivo).

## R0042 zhang2025meditrir — MediTriR (ICSC 2025)
- Arquitetura: pergunta MCQ → LLM gera query → PubMed (Entrez, 15 artigos) → resumos convertidos em triplos por GPT-4o → GPT-4o filtra triplos relevantes ("act as a medical researcher") → geração de novos triplos → resposta.
- Modelos avaliados: gemma2-9b-it, llama-3-8b, ChatGPT-3.5, GPT-4o mini.
- Dados: MedMCQA dev (4183), Medical QA/USMLE US dev (1272).
- Resultados: llama3-8b 47,90→61,53 (MedMCQA), 43,63→47,64 (MedQA); gpt-4o-mini 65,96→74,32 e 63,68→70,28. Ablação: geração de novos triplos ajuda.
- Relevância: estrutura o contexto antes de o dar ao modelo; mas o objetivo é escolher a resposta, não explicá-la. Usa um LLM para filtrar a relevância do contexto.
- Elegibilidade: Incluir.

## R0071 christiawan2025sanity — Sanity-LLM (2025)
- Arquitetura: pré-processamento e anonimização do corpus; step-back prompting; pesquisa híbrida BM25 + FAISS com pontuações normalizadas Min–Max e fundidas (peso ótimo BM25 0,2 / FAISS 0,8, testado de 0,1 a 0,9); reordenação com Cohere rerank-english-v3.0 (top-10 → top-5).
- Modelo: GPT-4o-mini; embeddings text-embedding-3-small (1536 dim).
- Prompt: obriga a responder só com o corpus; se a pergunta sai do âmbito, não gera conteúdo não relacionado.
- Dados de teste: 14 temas × 2 perguntas (curta e longa) = 28; referências criadas por LLM a partir das respostas originais.
- Avaliação: RAGAS (fidelidade, context recall, context precision, answer correctness); baselines RAG ingénuo BM25 e FAISS; ablação.
- Resultados: correção 0,6297 (FAISS 0,5595; BM25 0,5539); fidelidade 0,8754 (BM25 0,8419; FAISS 0,8077); precisão contexto 0,9391; recall 0,7077 (BM25 0,7192 — reordenação corta casos de fronteira).
- Limitações (dos autores): dados abertos, não interações reais; empatia e segurança não avaliadas por especialistas; dados estáticos.
- Relevância: precisão do contexto alta não garante resposta correta (FAISS). Instrução de recusa no prompt, mas recusa não avaliada.
- Elegibilidade: Incluir.

## R0113 trang2025customized — chatbot educativo com Qwen-14B (RIVF 2025)
- Arquitetura (LangGraph): memória da conversa (mensagens recentes + resumo das antigas) → LLM extrai em JSON tópico, tarefa e idade → pede a idade se faltar → filtra documentos pelo tópico → pesquisa híbrida → reordenação (mxbai-rerank-large-v2) → geração → formatação pela tarefa e pela idade. Se o tópico não está nos documentos, entra em "modo geral".
- Modelo: qwen2.5:14b (geração e embeddings), local, 16 GB VRAM; ChromaDB; fila para utilizadores concorrentes; FastAPI + React + JWT.
- Registo: administrador acede a todas as conversas com o nome do utilizador cifrado, para avaliação posterior.
- Avaliação: nenhuma avaliação quantitativa das respostas (só descrição do sistema e interface).
- Relevância: exemplo de memória de conversa resumida e extração estruturada (JSON) da intenção; o modo geral é o oposto do pretendido no QBank. Registo de conversas pseudonimizado é análogo às estatísticas do QBank.
- Elegibilidade: Excluir na leitura integral? Não descreve avaliação das respostas (I4). → Excluir (I4), manter só como exemplo de arquitetura.

## R0157 nurfadhilah2025retrieval — chatbot de doença renal crónica (Indonésia)
- Arquitetura: LlamaIndex + Chroma; chunking semântico (por parágrafos/secções em vez de janelas fixas); top-k = 5; on-premises (A100).
- Modelos: Llama 3.1 vs Sahabat AI (Llama com pré-treino continuado em indonésio); embeddings BGE-M3, mContriever e BGE-M3 ajustado ao domínio.
- Dados: QA abertos e validados por médicos, artigos de sites de saúde, PDFs de orientações; 70 perguntas × 10 repetições (n = 700).
- Avaliação: cenário 1 base vs RAG (METEOR, correção 1–5 pelo CorrectnessEvaluator, limiar 4); cenário 2 embeddings (correção, fidelidade, relevância, precisão do contexto, RAGAS); juiz Gemini 2.0 Flash; testes t.
- Resultados: sem RAG Sahabat 0,2922 METEOR / 3,93 correção vs Llama 0,2157 / 3,17; com RAG Sahabat 0,4116 (mContriever) e 4,03 (BGE-M3); Llama 0,3228 e 3,68. Fidelidade Sahabat ≈0,95.
- Relevância: o modelo adaptado à língua pesa mais do que o embedding; repetições (10 por pergunta) para medir variabilidade — boa prática para a avaliação do QBank. Definições formais de METEOR, fidelidade e precisão do contexto.
- Elegibilidade: Incluir.

## R0162 azam2024cancerbot — CancerBot (ICOSST 2024)
- Arquitetura: 100 artigos PubMed + 7 livros; chunks de 800 caracteres (RecursiveCharacterTextSplitter); embeddings all-mpnet-base-v2; Pinecone, semelhança do cosseno.
- Modelo: Llama-2-13b quantizado a 4 bits (memória limitada); janela de 4096 tokens; interface Gradio local.
- Avaliação: testes sintéticos com fidelidade, relevância do contexto e da resposta; comparação com Llama-2 sem RAG.
- Relevância: exemplo de RAG ingénuo; a janela de 4096 tokens limita o contexto (no QBank todo o item tem de caber).
- Elegibilidade: Incluir (avaliação fraca, sintética).

## R0859 yan2026question — agente de QA de Eletrónica de Potência (AIDME 2026, ACM, CC-BY)
- Base de conhecimento: 60 horas de aulas gravadas (~3000 min) transcritas (iFlytek), revistas à mão (termos técnicos), ~340 mil palavras, divididas em 713 unidades pergunta–resposta.
- Prompt de sistema hierárquico e iterativo. Falhas do prompt inicial (Tabela 1): resposta irrelevante; explicação errada; inventou definição e derivação para um termo inexistente ("cosine sampling method") sem o questionar; resposta truncada por max_tokens. Regras acrescentadas: se o termo é errado ou invulgar, pedir confirmação; se a pergunta é ambígua (ex.: tipo de dispositivo), perguntar em multi-turno; temperatura 0,1; resposta profissional e rigorosa. Depois: cita a base, pede clarificação ("Did you mean uniform or natural sampling?").
- Modelo: DeepSeek-V3 via API (deepseek-chat), temperature 0.1, max_tokens 8192, top_p 0.95; até 3 tentativas em caso de falha.
- Recuperação híbrida semântica + BM25 com peso adaptativo à esparsidade lexical da pergunta: α(q) = 0,3 + 0,7·s(q); Recall@5 0,74→0,81, MRR 0,68→0,75 face a α fixo 0,6. Vetores num ficheiro pickle, pesquisa linear em memória.
- Diálogo: DialogueManager com histórico limitado a 20 turnos (truncado), guardado na sessão Flask.
- Avaliação: 150 perguntas de 9 capítulos; grupo de controlo (DeepSeek sem RAG, prompt básico) vs sistema; métricas exatidão, exatidão das citações, adequação ao nível, atualidade (passa/falha), fidelidade; avaliação manual + automática. Resultados reportados de forma qualitativa na Tabela 5 (sem números na tabela; figura com barras).
- Relevância QBank: muito alta para o desenho do prompt — exemplo concreto de iteração do prompt de sistema, de pedido de clarificação perante termos inválidos (em vez de inventar) e de parâmetros de geração (temperatura baixa). Também é uma API externa paga, como no QBank.
- Limitações: resultados pouco quantificados; sem estatística.
- Elegibilidade: Incluir (qualidade média: QA4 parcial).

## R0878 xie2026when — When Retrieval Hurts (AISNS 2025, ACM)
- Dados: MedQA-USMLE validação, 1272 perguntas de 4 opções (vinheta + opções A–D); o modelo responde com uma letra.
- Base: 125 847 excertos do corpus MedRAG Textbooks (18 manuais).
- Recuperação: BM25 (k1 = 1,5; b = 0,75); densa MiniLM-L6-v2 (384 dim) com FAISS; híbrida por Reciprocal Rank Fusion (k = 60, pesos iguais); top-5.
- Modelo: Qwen3-8B-Instruct (temperatura 0,1); validação com Qwen-Plus.
- Resultados: LLM 60,69% [58,01–63,38]; BM25 59,43%; densa 60,14%; híbrida 59,91% (McNemar p = 0,21–0,63, não significativo, mas sempre negativo). Efeito positivo 5,11–6,05%, negativo 6,37–6,84%; em 87–88% dos casos o RAG não muda nada. Oráculo: 66,74% (+6,05). Pontuação de recuperação não distingue casos úteis de prejudiciais (AUC 0,53; d de Cohen 0,06; t-test p = 0,443).
- Causas dos 81 casos negativos (análise manual): desajuste de contexto 35% (termos certos, contexto clínico errado — ex.: CAD com orientação de insuficiência cardíaca crónica que sobrepõe a prioridade correta); extração de frases sem compreensão 40%; fragmentação do conhecimento 25% (excertos parciais que, combinados, criam incoerências).
- Corrobora: RAG2 também reportou quedas (Llama-3-8B 57,7→55,3%).
- Relevância QBank: muito alta — as três causas são todas da recuperação; no QBank o contexto é o registo completo e coerente do item, o que elimina a fragmentação e o desajuste de contexto. Mas também mostra o risco de o contexto sobrepor-se a conhecimento correto do modelo (no QBank isso é desejado, porque o contexto está validado).
- Elegibilidade: Incluir (qualidade alta: estatística, IC, oráculo).

## R0934 liu2026asknow — AskNow (CHI 2026, ACM, 22 páginas)
- Contexto: transcrição em tempo real da aula (AssemblyAI), guardada em segmentos de 30 s com marcas temporais (permite perguntas como "o que disse o professor há 10 minutos?"); a segmentação serve só para armazenamento e indexação — o contexto dado ao modelo pode abranger toda a aula até ao momento (SEM pesquisa por semelhança). Metadados da aula (título, disciplina, docente) incluídos no prompt.
- Prompt: referir sempre primeiro a transcrição; tom neutro; rigor académico e técnico; recusar pedidos inapropriados; prompt completo no Apêndice A (reprodutibilidade, versões dos modelos fixadas).
- Modelo: comparou Claude 3.5 Haiku, GPT-4o-mini e GPT-4o; escolheu GPT-4o pelo equilíbrio exatidão/custo, crítico para escala.
- Implementação: Next.js (Vercel), Node.js + Express (AWS EC2), Socket.IO; atualizações diferenciais da transcrição (só os segmentos novos) para reduzir tokens, contexto redundante e latência; segmentos indexados permitem rastrear a resposta até ao excerto.
- Agregação: perguntas registadas, convertidas em embeddings (text-embedding-3-small) e agrupadas por K-means recursivo com limiar → painel do docente com os temas de dúvida em tempo real. Evitaram LLM para classificar/resumir e embeddings locais por latência e custo de tokens.
- Avaliação: estudo formativo (24 estudantes, 12 docentes); implementação em 3 cursos durante uma semana, 117 estudantes; pré/pós questionário Likert 1–7; docentes avaliaram 100 respostas aleatórias (correção e satisfação, 1–5); USE questionnaire; entrevistas (24 estudantes, 3 docentes).
- Resultados: tempo percebido para resolver dúvidas desceu 1,1–1,4 pontos (p_adj < 0,0125; d = 0,62–0,77); compreensão e retenção +0,4–0,5 (não significativo após Bonferroni); frequência de confusão sem alteração. Correção (docentes): 4,88 / 4,79 / 4,53; satisfação 4,75 / 4,51 / 4,45. USE > 5/7; facilidade de aprendizagem > 6.
- Relevância QBank: o mais próximo do caso — contexto fechado conhecido à partida, fornecido sem recuperação; escolha do modelo por exatidão e custo; prompt com prioridade ao contexto e recusa; agrupamento das perguntas por embeddings para o docente = estatísticas da Adhara; avaliação em três frentes (docentes, questionário, entrevistas). Diferença: não avalia fidelidade automaticamente nem recusa; uma língua; sem regras por modo.
- Elegibilidade: Incluir (qualidade alta).

## R1001 seshadri2026alan — Alan (SIGCSE TS 2026, 2 páginas, CC BY-NC-ND)
- Objetivos de desenho: toda a resposta baseada em conteúdo do curso; supervisão do docente; confiança pela transparência.
- RAG: índice híbrido (palavras-chave + semântico) sobre diapositivos, transcrições, enunciados, sites e ficheiros do LMS (atualizado ao longo do semestre); modelo da classe GPT-4; citações clicáveis no texto e lista de fontes no fim; avaliação da resposta pelo estudante, regenerar, modo de pesquisa.
- Docentes veem painéis anonimizados (utilizadores ativos, perguntas frequentes). Registo com consentimento (opt-in).
- Uso: 453 estudantes, 251 registados, 150+ consentiram registo; 2217 perguntas (jan–abr); picos antes de prazos e exames, e às 22h–24h (fora do horário humano); ~10 utilizadores intensivos com 50+ perguntas. Tipos: conceptuais 63%, laboratório 17%, administrativas 7%, aulas 5%.
- Fórum (Piazza) manteve o volume do ano anterior: o chatbot complementa, não substitui.
- Inquérito (40 respostas, Likert 1–5): utilidade 4,2 conceptual, 3,7 resolução de problemas, 3,9 administrativo, 4,0 global. Valorizaram fontes (com marcas temporais), confiança, imediatez.
- Limitações: perguntas abertas e visuais; os guardrails contra raciocínio fora do contexto limitam respostas a perguntas de orientação.
- Relevância QBank: citações para verificabilidade (no QBank: citar o campo do item, ex. "segundo a explicação"); painel de perguntas frequentes anonimizado = estatísticas; o padrão de uso perto de exames é análogo ao do QBank. Recusa fora do contexto tem custo de utilidade.
- Elegibilidade: Incluir (resumo alargado; avaliação de perceção, não de correção).

## R1060 feng2024courseassist — CourseAssist (SIGCSE Virtual 2024, 2 páginas)
- GPT-4 + classificação da intenção do utilizador + decomposição da pergunta + recuperação de conteúdo do curso; o motor decide QUANDO e O QUÊ recuperar conforme a intenção; pós-processamento para adequação pedagógica (pistas em vez de soluções de código).
- Dados: 50 pares de 185 posts do Piazza (curso de linguagens de programação), perguntas reescritas pelo TA, respostas de docente/TA; 33 de trabalhos de casa, 17 conceptuais; dados e rubrica públicos.
- Avaliação humana por um docente (0 / 0,5 / 1) em utilidade, exatidão e adequação pedagógica; 2 execuções por pergunta para a variabilidade. Argumentam que BLEU/METEOR/ROUGE-L/CIDEr não medem utilidade.
- Resultados: CourseAssist vs GPT-4 — utilidade 0,91 vs 0,83; exatidão 0,92 vs 0,71; adequação 1,00 vs 0,82; média 0,94 vs 0,79. Implementação em 6 cursos, 500+ estudantes; entrevistas a 20.
- Relevância QBank: "adequação pedagógica" como critério de avaliação, análogo às regras por modo (não dar a resposta no Teste); classificação da intenção antes da geração; repetição das execuções.
- Elegibilidade: Incluir.

## R1022 buti2026evaluating — AdvisingBench (WCCCE 2026, ACM)
- Sistema em produção (aconselhamento de unidades curriculares): pgvector (PostgreSQL) + Gemini 2.5 Flash; base = catálogo oficial (descrições, pré-requisitos, restrições); instruído a responder só com o contexto e a recusar educadamente o que está fora do âmbito.
- Benchmark de 55 perguntas com resposta de referência validada por especialistas, em 3 categorias: comuns (29), específicas que exigem interpretar regras (19), casos-limite (7: fora do âmbito, ambíguas, EXFILTRAÇÃO DO PROMPT DE SISTEMA).
- Métricas por LLM juiz: relevância da resposta (inclui recusar adequadamente), fidelidade, relevância do contexto, correção face à referência (1 / 0,5 / 0); global ponderado pelo juiz.
- Juiz: Gemini 3 Flash (preview), temperatura 0, raciocínio alargado, rubrica detalhada, saída JSON com notas; instruído a valorizar a recusa de perguntas fora do âmbito. 53/55 concluídos (2 erros transitórios da API).
- Resultados: relevância 0,979; fidelidade 0,764; relevância do contexto 0,702; correção 0,758; global 0,751. Casos-limite com a maior fidelidade (0,843) — recusas fundamentadas. Relevância da resposta pouco discriminativa (amplitude 0,032).
- Falhas (global < 0,6): desalinhamento da recuperação 6; alucinação 3 (5,7%: citação inventada, pré-requisitos inexistentes, afirmar que a informação estava no contexto); resposta incompleta 1; generalização excessiva 1 (devia pedir clarificação). A maioria das falhas de fidelidade foi o modelo usar conhecimento do treino correto mas ausente do contexto.
- Limitações (autores): juiz não validado contra humanos neste conjunto (extrapolam de outra versão do Gemini); amostra pequena.
- Relevância QBank: modelo direto para o conjunto de teste do QBank — categorias comuns / interpretação / casos-limite (fora do âmbito, ambíguas, extração do prompt e, no QBank, pedido da resposta no modo Teste); configuração do juiz (temperatura 0, rubrica, JSON); taxonomia de falhas. Mostra que a fidelidade penaliza conhecimento correto fora do contexto — no QBank é exatamente o comportamento a evitar.
- Elegibilidade: Incluir.

## R0991 miroyan2025analyzing — Edison (SIGCSE TS 2025, ACM)
- Contexto: Data 100, UC Berkeley, primavera 2024 (1133 + 71 estudantes, 59 staff); integrado no fórum EdSTEM durante um mês. Consentimento do estudante por pergunta; o TA decide se a pergunta pode ir ao sistema (dados pessoais, pedidos de prorrogação) e se usa, edita ou reescreve a resposta (humano no circuito).
- Pipeline: RAG sobre pares Q&A históricos e documentos do curso; OCR das imagens; GPT-4 classifica a pergunta (logística / trabalho / conceptual) → só as bases vetoriais adequadas são consultadas; prompts por categoria com exemplos few-shot escritos à mão; perguntas de trabalhos aumentadas com a solução; chamada GPT-4 adicional para encurtar e remover pistas que revelem a solução.
- Dados: 435 pedidos de consentimento, 199 aceites, 110 respostas (65 trabalho, 41 conceptual, 4 logística); 15 TAs (65% das chamadas por 3).
- Avaliação: TAs classificaram cada resposta (1–5) em factualidade, relevância e estilo (estilo inclui uso adequado de pistas e soluções); análise das edições (pistas/soluções, estilo, conteúdo, relevância) e do comprimento.
- Resultados: factualidade 5 em 51/65 (trabalho) e 31/41 (conceptual); relevância 4–5 em 43/65 e 38/41; estilo pior (verbosidade, pistas em excesso — uma resposta deu parte da solução). A maioria das edições foram eliminações de estilo; respostas finais mais curtas.
- Relevância QBank: mesmo com um filtro LLM dedicado, houve revelação de solução — reforça controlar a informação fora do modelo; categorias de edição como taxonomia para a validação pela Adhara (a Adhara quer validar pares pergunta–resposta extraídos); verbosidade como problema recorrente.
- Elegibilidade: Incluir.

## R1019 barzanji2026buddy — ST-Buddy (CHI EA 2026, ACM)
- Privacidade: mensagens e dados guardados só no browser (local storage); fornecedores de LLM com políticas sem registo e sem treino. FastAPI, LangChain, LiteLLM (encaminhar entre fornecedores/modelos), LangFuse (rastreio das gerações e histórico de versões dos prompts).
- Línguas: alemão e inglês.
- RAG em pgvector com 3 categorias (conteúdo, exercícios com partes da solução, organização: FAQ, secretaria, fórum anonimizado); uma chamada LLM antes da geração escolhe a categoria; organização: top-3 por semelhança; conteúdo: semelhança com limiar de relevância; a pergunta é reescrita em 4 perguntas adicionais por outra chamada LLM (linguagem coloquial).
- Avaliação: mista em dois contextos (aula semi-controlada; teste de campo de 4 semanas); pré e pós-questionário; ATI; SUS; Partner Model Questionnaire; qualidade das respostas (relevância, correção, clareza, complexidade, comprimento, naturalidade, Likert 1–5); consentimento informado e dados anónimos.
- Participação: 103 iniciaram; 32 concluíram na aula (SUS 77,81 no resumo, n = 32).
- Relevância QBank: escolha de fornecedor por política de retenção e treino (como no cap. 1); LiteLLM como camada de abstração do fornecedor (mitigação do risco R7); versionamento dos prompts; bilingue.
- Elegibilidade: Incluir.

## R0826 zhao2025cyberbot — CyberBOT (CIKM 2025, ACM, demo)
- Pipeline: intérprete de intenção (Llama 3.3 70B) reescreve a pergunta com os últimos k turnos da conversa (um classificador por regras semânticas decide se é preciso reescrever, para poupar custo) → recuperação (BAAI bge-large; chunks de 512 tokens) sobre pares Q&A curados por especialistas e materiais do curso CSE 546 → geração (Llama 3.3 70B) → verificador por ontologia (Llama 3.3 70B) devolve validação Pass/Fail, confiança e justificação em JSON; abaixo do limiar a resposta é rejeitada; perguntas fora da ontologia são rejeitadas.
- Ontologia construída a partir dos materiais e destilada por especialistas.
- Implementação: Docker, A100 80 GB, modelos via Together AI API; Streamlit; SQLite; acesso só por VPN da universidade; histórico por utilizador anonimizado.
- Implementação real: CSE 546 Cloud Computing, primavera 2025 (sem dados de uso reportados).
- Avaliação (laboratório): CyberQ, ~3500 pares abertos (ZS 1027, FS 332, OD 2171); BERTScore 0,933; METEOR 0,793; ROUGE-1 0,657; ROUGE-2 0,606; fidelidade 0,788; relevância 0,983; precisão do contexto 0,994; recall 0,994. Não avalia a taxa de rejeição nem o efeito do verificador.
- Relevância QBank: verificação pós-geração com saída estruturada (JSON com decisão, confiança e justificação); reescrita da pergunta com o histórico; custo de 3 chamadas a um modelo de 70B por pergunta (latência não reportada).
- Elegibilidade: Incluir (avaliação só automática).

## R1110 bui2025formal — MCFR (AIQAM 2025, ACM)
- Neuro-simbólico: o LLM traduz a pergunta em linguagem natural numa especificação formal (lógica temporal), verificada por model checking (UPPAAL) sobre um modelo de transições do percurso académico, construído manualmente por especialistas.
- Dados: EduMC-QA, 130 perguntas procedimentais (segurança 34, vivacidade 34, alcançabilidade 38, equidade 24), classificadas por 3 especialistas (voto maioritário).
- Resultados (exatidão total): MCFR 93,85%; ChatGPT-reason 82,31%; DeepSeek-casual 76,92%; ChatGPT-casual 73,08%; DeepSeek-R1 50,00%; Claude Sonnet 40,00%. Os LLMs falham sobretudo em regras de pré-requisitos e em inferências de várias regras.
- Limitações: modelo de domínio manual (não escala); erros na tradução para a especificação formal propagam-se.
- Relevância QBank: baixa a média — mostra o limite dos LLMs a raciocinar sobre regras explícitas e a alternativa de verificar fora do modelo; não aplicável diretamente (as perguntas do QBank não são procedimentais).
- Elegibilidade: Incluir (domínio educativo institucional; contexto = modelo formal), prioridade rebaixada.

## R0165 sbai2025advanced — RAG trilingue AR/FR/EN (IEEE 2025)
- Três pipelines progressivos: ingénuo (multilingual-e5-large + FAISS + LLM quantizado, prompts adaptados à língua), híbrido (BM25 + denso, fusão RRF, reordenação cross-encoder ms-marco-MiniLM-L-6-v2), avançado (+ expansão da pergunta por paráfrase LLM, pseudo-relevance feedback, diversificação MMR com deduplicação de fontes, pontuação de confiança a partir do cross-encoder para detetar alucinações).
- Análise dos documentos por língua: LlamaParse (científico) para FR/EN; PyMuPDF + arabic_reshaper + bidi para árabe (LlamaParse perdia o texto árabe); fórmulas em LaTeX; LlamaParse demorava 4–5 min por documento.
- Dados: ~20 documentos do currículo marroquino; pares pergunta/resposta/contexto-ouro em JSON com identificador da língua; testes translinguísticos (pergunta numa língua, documento noutra).
- Execução: RTX A4000 16 GB; DeepSeek-R1-8B quantizado; FAISS IVF (48 clusters, 10 probes). Juiz LLM excluído por limitações de hardware.
- Métricas: semelhança de embeddings resposta–referência ("correção") e resposta–contexto ("fidelidade"); pontuações 0–5 por LLM de correção, fidelidade e clareza; latência e memória.
- Resultados: avançado ≈0,9 em correção e fidelidade por embeddings; híbrido ≈0,64; ingénuo muito inferior; média 4,6/5; árabe superou o inglês e ficou ligeiramente abaixo do francês.
- Limitações: hardware local lento; materiais escassos e heterogéneos. Métrica de "fidelidade" por semelhança de embeddings é fraca (não verifica afirmações).
- Relevância QBank: tratamento por língua (cada língua pode exigir tratamento diferente); conjunto de teste com identificador de língua; avisa que métricas por semelhança de embeddings não medem fidelidade real.
- Elegibilidade: Incluir (qualidade média).

## R0237 kavitha2026securecontext — SecureContext EDU / SRACS (ICSCSS 2026)
- Fluxo: interface Streamlit → validação de entrada e sessão → FILTRO PRELIMINAR POR REGRAS (sem LLM: expressões regulares e padrões; devolve SAFE, BLOCKED ou SUSPICIOUS; saudações e temas educativos óbvios passam diretamente; ataques evidentes e "flood" bloqueados; o resto vai ao LLM-1) → LLM-1 (Llama 3 via Ollama) classifica em benigno / injeção / jailbreak / ofensivo / spam, com tipo, confiança e motivo em JSON (erro de parsing → classificação "erro") → controlador de decisão por limiar → se malicioso: registo do tipo e hora e resposta segura não informativa → se seguro: FAISS + deteção de dados sensíveis → LLM-2 gera → validação da saída → painel do administrador.
- O filtro por regras existe para reduzir a latência do LLM-1 (só as perguntas suspeitas vão ao classificador).
- Avaliação: 250+ perguntas de vários utilizadores; 90% de deteção de ameaças (resumo); demonstração por exemplos.
- Relevância QBank: arquitetura em camadas barata — regras primeiro, LLM classificador só para casos duvidosos — compatível com o limite de 2–3 s; resposta não informativa em caso de ataque; registo de tentativas para o painel.
- Elegibilidade: Incluir (avaliação fraca, sem baseline).

## R0281 raputri2025retrieval — diretrizes clínicas indonésias (ISRITI 2025)
- RAG sobre o PPPK (Panduan Praktik Profesional Kedokteran); comparação GPT, DeepSeek e Qwen com RAG, e DeepSeek com e sem RAG; diagnóstico a partir de sintomas; referência de um médico de clínica geral; métricas de contexto.
- Resultados: RAG melhora significativamente; diferenças entre modelos não significativas (GPT > 0,65 em todas as métricas pela média).
- Relevância QBank: com contexto fiável, a escolha do modelo pesa menos — argumento para escolher o modelo por custo e latência, não só pela qualidade bruta.
- Elegibilidade: Incluir.

## R0301 liu2026quality — RAG-MCP multiagente (CCWC 2026)
- Cada conjunto (MedMCQA, MedQA-USMLE) dividido em "conhecimento" (base do RAG, perguntas de escolha múltipla usadas como exemplos) e "teste". Agente administrador encaminha para agentes de fisiologia, patologia, clínica, terapêutica e saúde pública; cada um responde com base na base partilhada; consenso ponderado pela proximidade do domínio; justificações auditáveis por agente.
- Curadoria: as perguntas da base são filtradas com uma rubrica detalhada; usar só as de maior qualidade (top-500) eleva a exatidão para ~80%; ótimo com 11–13% da base curada.
- Relevância QBank: usa perguntas de escolha múltipla JÁ RESOLVIDAS como contexto do modelo — a qualidade e validação do conteúdo pesam mais do que a quantidade, o que favorece o QBank (conteúdo validado pela equipa científica).
- Elegibilidade: Incluir.

## R0414 rahat2026noise — falhas do RAG em QA médico (IEEE 2026)
- Modelo: MMed-Llama-3-8B (médico). Teste: 500 perguntas do PubMedQA pqa_labeled (semente 42, reprodutível). Base: 61 249 resumos (pqa_unlabeled); all-MiniLM-L6-v2 + FAISS, cosseno, top-k.
- DUAS LINHAS DE BASE: sem contexto 27,0%; CONTEXTO DOURADO (anotado por humanos, perfeito) 68,8%. RAG ingénuo: k=1 42,6%; k=5 20,8%; k=8 17,6% (pior que sem contexto). Respostas sem formato válido: 26,2% sem contexto, 2,4% com contexto dourado, 59,6% com RAG k=8 — o ruído faz o modelo deixar de seguir as instruções de formato.
- Taxonomia dos 165 casos em que o RAG falhou mas o contexto dourado acertou: contexto que distrai/ambíguo 41,8% (temático mas sem a resposta → "maybe"); contraditório 37,6%; irrelevante 13,9%; resposta sem formato 6,7%. "O recuperador está alinhado semanticamente mas não sabe onde está a resposta."
- Mitigação: prompt few-shot robusto que demonstra rejeitar evidência contraditória, reconhecer o contexto que contém a resposta e cumprir estritamente o formato (sim/não/talvez); k=5 → 59,6%; com o prompt robusto mais contexto passa a ajudar (k↑ ⇒ exatidão↑).
- Relevância QBank: ARGUMENTO CENTRAL — a condição de "contexto dourado" (informação correta e completa, sem pesquisa) é a do QBank; ganho de 27,0% → 68,8% com o contexto certo, enquanto a recuperação ruidosa pode ficar abaixo de não ter contexto. Também: contexto limpo melhora o cumprimento do formato pedido; exemplos no prompt (few-shot) como técnica de robustez.
- Elegibilidade: Incluir (qualidade alta).

## R0452 khan2025towards — GATE, explicação de soluções de exame (IEEE 2025)
- FLUXO MUITO PRÓXIMO DO QBANK: o utilizador escolhe uma pergunta do exame numa lista pesquisável (filtros por tipo de exame e ano); o sistema mostra a SOLUÇÃO EXATA dessa pergunta (com citações e imagens); as perguntas de seguimento do utilizador são respondidas pelo LLM usando o PAR PERGUNTA–SOLUÇÃO como material de referência, segundo um template de prompt. A "recuperação" é exata (pela pergunta escolhida), não por semelhança.
- Dados: soluções do GATE (MadeEasy, Byju's) em PDF; extração com Mathpix para equações (pypdf2/pymupdf inadequados; Tesseract e Nougat OCR intermédios); imagens com LLaVA/Unstructured; JSON com metadados (tipo, ano, domínio); Weaviate (antes ChromaDB).
- Seleção de modelos por leaderboards (Chatbot Arena, MT-Bench, MMLU, Open LLM) e MTEB, com testes de latência e avaliação humana: Mistral-7B, Gemma-7B, Llama-3-8B, Phi-3, Qwen1.5-7B → llama3:8b-instruct-q2_K + BGE-small; tudo local (Ollama), Docker; Next.js, JWT, MongoDB (histórico, feedback); notas automáticas da conversa.
- Avaliação: fidelidade F = |V|/|S| (afirmações suportadas / total) e relevância da resposta (gerar n perguntas a partir da resposta e comparar com a original), por LLM avaliador (Llama 3 8B); estratégia "nested RAG": 20% anotado à mão usado como referência para o avaliador nos restantes 80%; EM, F1, top-k; latência.
- Resultados: fidelidade/relevância — Llama3 8B q2_K 0,94/0,83; Phi-3 0,87/0,78; GPT-3.5-turbo 0,56/0,49 (ATENÇÃO: o avaliador era o próprio Llama 3 8B → possível enviesamento de autopreferência). Latência (s) recuperação/geração: Phi-3+BGE 0,91/4,61; Llama3+BGE 0,97/9,35; Llama3+nomic 1,38/11,01 → escolheram Llama3 apesar de ~9 s.
- Relevância QBank: o estudo mais próximo do fluxo (pergunta escolhida → solução validada → dúvidas de seguimento com essa solução como contexto). Diferenças: uma língua; latência de ~10 s em hardware local, longe dos 2–3 s; sem recusa, sem regras de revelação da resposta; avaliador = modelo avaliado.
- Elegibilidade: Incluir (qualidade média; validade do avaliador questionável).

## R0437 wei2026cloud — tutor RAG cloud-edge (IEEE 2026)
- Pipeline auditável: previsão de risco local (regressão logística sobre os primeiros 28 dias do OULAD; Macro-F1 0,757, AUC 0,838) → recuperação local de evidência (estatísticas do curso) → verificação de políticas → encaminhamento para a nuvem só acima de limiares de risco (r < 0,55 só local; 0,55–0,75 local primeiro; …) → resposta com marcas de evidência e registo de auditoria. Registo de execução completo (comando, versões, hashes SHA-256 dos dados).
- RAG em 160 casos de maior risco: precisão@1 = 1,00 e hit@3 = 1,00 para o documento exato do curso; ABLAÇÃO — sem os identificadores do curso na pergunta, precisão@1 e hit@3 caem para 0,006. Feedback fundamentado: cobertura de evidência 1,00 e afirmações sem suporte 0,00; conselhos genéricos: 0,00 e 1,00.
- Limites declarados: avaliação offline com dados públicos; sem ganhos de aprendizagem em aula nem latência de hardware.
- Relevância QBank: evidência direta de que a recuperação pelo IDENTIFICADOR é exata e que, sem ele, colapsa — sustenta usar o ID da pergunta em vez de pesquisa por semelhança. Registo de auditoria e de versões como boa prática.
- Elegibilidade: Incluir.

## R0446 elnozahy2026governed — QA governado de domínio fechado (IEEE 2026)
- Proposta de framework (privacidade por desenho, controlo das fontes, encaminhamento por tarefa, auditabilidade e registos). Perguntas em árabe ou inglês; o encaminhamento decide que partes podem usar LLM com dados públicos e que partes têm de usar fontes institucionais internas, com mascaramento de dados pessoais.
- Avaliação: essencialmente conceptual (fases e fluxos).
- Relevância QBank: separação explícita entre o que pode ser enviado a um LLM externo e o que fica interno — análoga a não enviar dados do utilizador à API.
- Elegibilidade: Excluir na leitura integral? Sem avaliação das respostas (I4) → Excluir (I4), manter como enquadramento.

## R0443 tawfik2025mufakkir — Mufakkir, árabe (ICICIS 2025)
- Pré-processamento da pergunta próprio do árabe (normalização da pontuação, palavras vazias, tokenização morfológica, expansão ocasional); 80+ livros (direito, humanidades) com chunking recursivo por estrutura (Azure Document Intelligence), 200–300 palavras por chunk; embedding ajustado (1.º no Arabic RAG Leaderboard, 0,65); recuperação híbrida; cross-encoder; Qwen2-72B; resposta validada contra o contexto.
- Avaliação: pares sintéticos pergunta–contexto gerados por LLM; exatidão 88%, recall 88%, nDCG@10 0,78; semelhança resposta–referência 0,79.
- Relevância QBank: tratamento específico por língua; avaliação com dados sintéticos (fraqueza).
- Elegibilidade: Incluir.

## R0469 sayeed2026tutor — ATU-Tutor (IEEE 2026)
- DOIS MODOS: tutoria (explicações fundamentadas + perguntas socráticas de seguimento) e avaliação (gera perguntas de escolha múltipla e de resposta curta alinhadas com o currículo, com feedback imediato) — paralelo com os modos Estudo/Teste do QBank.
- RAG híbrido FAISS + BM25 + reordenação cross-encoder; 2328 chunks de 17 manuais abertos; recuperador ajustado com 929 pares; índice reconstruído com o modelo ajustado.
- Qwen3-8B quantizado NF4 (BitsAndBytes, dupla quantização, float16) numa Tesla T4 16 GB.
- Avaliação: 14 perguntas; heurísticas (relevância, empatia/tom, concisão, fundamentação) + LLM juiz com rubrica pedagógica (resistência a alucinações, andaime socrático, uso do contexto); global 4,00/5; empatia e andaime socrático mais fracos.
- Relevância QBank: comportamento diferente por modo implementado no prompt; avaliação de "comportamento de fronteira seguro" como dimensão; amostra muito pequena.
- Elegibilidade: Incluir.

## R0558 ishadya2026mitigating — prompts + RAG vs MCP em QA clínico (IEEE 2026)
- MedQuAD (CancerQA, NIDDK QA); pipelines RAG e MCP com o MESMO índice Chroma e a mesma lógica de prompt; o MCP é uma camada fina de orquestração (ferramentas retrieve_context, answer_grounded, answer_ungrounded, batch_answer, saída JSON inspecionável).
- Técnicas de prompt comparadas: papel (Role), Chain-of-Thought, Chain-of-Verification; respostas com citações; REGRA DE ABSTENÇÃO ESTRITA com uma frase de abstenção FIXA.
- Métricas: EM, F1, ROUGE-L (global e só nas respostas não abstidas), SBERT; taxa de abstenção (fração com a frase fixa); Evidence-Backed Rate (respostas não abstidas com suporte suficiente no contexto citado) e o seu complemento, taxa de respostas sem suporte; recall@k; deriva demográfica (atributos demográficos não suportados) como proxy de enviesamento; revisão por especialistas de amostras (correção clínica, completude, tom, validade das citações).
- Resultados: EBR CancerQA MCP 0,71–0,794 vs RAG 0,6456–0,7975 (CoVe 0,71 vs 0,6456; Role 0,71 vs 0,6835); NIDDK ≥ 0,8 em ambos; base sem contexto a pior em tudo.
- Relevância QBank: frase de recusa FIXA torna a recusa mensurável automaticamente; métricas calculadas separadamente nas respostas não recusadas; taxa de respostas sem suporte; revisão por especialistas por amostragem. Modelo direto para o protocolo de avaliação.
- Elegibilidade: Incluir.

## R0514 bengmah2025driven — Diabot (IEEE 2025)
- Compararam engenharia de prompts, ajuste fino e RAG; RAG escolhido por ser viável com o hardware disponível e manter a exatidão; filtragem contextual; necessidade futura de cálculo para respostas numéricas.
- Elegibilidade: Incluir (avaliação limitada).

## R0555 ruga2025conversational — ELENA, doenças oculares raras (IEEE 2025)
- Documentos pré-traduzidos para inglês; perguntas em italiano traduzidas, processadas e a resposta traduzida de volta; LLM quantizado em hardware modesto; interface gráfica para pessoal clínico.
- Relevância QBank: contraexemplo — o QBank tem conteúdo validado em cada língua, logo a tradução pivô não é necessária e acrescentaria um ponto de erro.
- Elegibilidade: Incluir.

## R0559 ghanbari2025evaluating — grafos de conhecimento no prompt para MCQA (IEEE 2025)
- ICL com subgrafos: representações por triplos vs caminhos; filtros de relevância; caminhos melhores mas mais sensíveis ao ruído; subgrafo maior → mais cobertura e menos precisão; seleção imprecisa abaixo do zero-shot. Código público.
- Relevância QBank: quantidade de contexto no prompt é um compromisso — mais não é melhor; no QBank, decidir que campos do item incluir.
- Elegibilidade: Incluir.

## R0561 bellard2025development — HeartWise, RAG agêntico com LLM juiz (IEEE 2025)
- Fluxo: chatbot RAG (conteúdo de um site de insuficiência cardíaca) gera rascunho → LLM-J (GPT-4, temperatura 0, persona de cardiologista) pontua 1–3 em exatidão, segurança, robustez, empatia, clareza (0 = crise: ideação suicida/autoagressão → resposta de emergência) e dá até 2 sugestões de edição → se alguma < 3, reescritor gera nova versão → 2.ª ronda: se exatidão e segurança = 3, entrega; senão MENSAGEM DE RECURSO FIXA ("I can't provide specific instructions for this situation. Please contact your care team…"). Só exatidão e segurança disparam o recurso, para reduzir a latência.
- Guardrails nos prompts: legibilidade de 6.º ano, empatia obrigatória, não se apresentar como profissional de saúde, sem dosagens, só o contexto, instruções de crise. Registo CSV de pontuações, justificações e sugestões.
- Dados: 25 pares sintéticos (5 domínios), sem dados pessoais, públicos.
- Resultados: 23/25 (92%) precisaram de nova tentativa; 95,7% passaram a 2.ª verificação de segurança (4,3% → recurso); robustez 2,04 → 2,35; exatidão 3,00 → 2,96; tempo médio do ciclo 15,74 s; custo 0,00312 USD por pergunta.
- Relevância QBank: mensagem de recurso fixa e verificada quando a verificação falha; verificação pós-geração só nas dimensões críticas para poupar latência; mas 15,7 s é incompatível com 2–3 s → no QBank a verificação teria de ser assíncrona/offline (ex.: validação posterior dos pares pela Adhara).
- Elegibilidade: Incluir.

## R0616 jain2025aligning — RAG vetorial vs GraphRAG na sala de aula (TALE 2025)
- Caso 1: EduScopeQA, 3176 perguntas em 4 disciplinas e vários níveis de granularidade (factos → temas). Caso 2: KnowShiftQA (3005 pares de manuais em que FACTOS-CHAVE FORAM ALTERADOS SISTEMATICAMENTE) para testar se o sistema segue o texto ou recorre ao conhecimento (desatualizado ou comum) do modelo. Mede também custo de indexação, latência e escalabilidade. LLM juiz.
- Resultados: OpenAI Vector Search = generalista barato para factos; GraphRAG Global melhor em perguntas temáticas; GraphRAG Local mais exato nos manuais alterados; GraphRAG 10–20× mais recursos. Encaminhamento por uma chamada inicial ao GPT-4.1-nano que escolhe o sistema a partir de uma descrição curta das forças de cada um.
- Relevância QBank: o TESTE COM FACTOS ALTERADOS é diretamente transponível — alterar um dado da explicação de um item de teste e verificar se o assistente segue o item (fidelidade ao contexto validado) ou o seu conhecimento. Encaminhamento por modelo pequeno e barato.
- Elegibilidade: Incluir.

## R0619 ghanbari2025quantifying — informatividade de subgrafos em ICL para MCQA (IEEE 2025)
- Pipeline em 4 fases (conceitos → ego-subgrafos por conceito → prompt → pontuação por probabilidade); mostra que subgrafos diferentes ajudam, enganam ou são neutros; tamanho e conectividade importam. Código público.
- Relevância QBank: confirma que a seleção do que entra no prompt é decisiva.
- Elegibilidade: Incluir.

## R0686 oh2026automedic — AutoMedic (IEEE 2026)
- Converte datasets estáticos de QA médico em perfis de doentes virtuais e simula diálogos multi-turno entre agentes LLM; métrica CARE (exatidão clínica, eficiência/estratégia, empatia, robustez); validado por especialistas.
- Relevância QBank: avaliação multi-turno automática a partir de perguntas existentes — ideia para gerar conversas de teste a partir dos itens do QBank.
- Elegibilidade: Incluir.

## R0753 fu2024chatbots — chatbots sobre base de conhecimento de universidade R2 (IEEE 2024)
- Base obtida por crawling do site; vários plataformas/modelos; perguntas objetivas e subjetivas com personas; ChatGPT com base + pesquisa em tempo real mais equilibrado nas objetivas; alucinações persistem; nenhuma vencedora nas subjetivas.
- Elegibilidade: Incluir (qualidade baixa a média).

## R0762 walczak2026comparative — Llama Guard 3 vs GPT OSS Safeguard (IEEE 2026)
- Contexto: assistente administrativo da Universidade de Tecnologia de Varsóvia; 15 categorias de ameaça incluindo S15 = RESTRIÇÃO DE TEMA (fronteira do domínio) e S13 = injeção de instruções; conjunto real ("ground truth", n = 1802, de sessões de red teaming) e sintético (n = 2929, cobre categorias raras). Llama Guard 3 com adaptador LoRA treinado em dados sintéticos; GPT OSS Safeguard só com a política descrita no prompt (few-shot) e raciocínio CoT; baseline TF-IDF + regressão logística.
- Resultados no conjunto real: Llama Guard 3 — exatidão 69,0%, precisão 58,3%, recall 85,5%, F1 69,4%, FPR 42,6% (bloqueia mais de 2 em cada 5 perguntas legítimas, sobretudo saudações curtas como "fora do tema" e perguntas informativas sobre discurso de ódio); GPT OSS Safeguard — exatidão 77,8%, precisão 74,5%, recall 69,1%, F1 71,7%, FPR 16,3%; TF-IDF F1 55,1%. McNemar χ² = 34,33, p < 0,001; concordância entre modelos 63,2%.
- Sintético vs real: Llama Guard 98,1% → 69,4% (−28,7 pp; treinado com o mesmo gerador); GPT 85,1% → 71,7%. Dados sintéticos complementam mas não substituem dados reais.
- Ponto cego comum: jailbreaks por personificação de autoridade (S13) e pedidos adversariais com enquadramento académico (S2).
- Restrição de tema: exatidão semelhante (71,1% vs 78,5%) — a descrição precisa da política no prompt compensa parcialmente a falta de treino.
- Quantização Llama Guard 3: INT8 = melhor compromisso (VRAM 15,6 → 9,0 GB; F1 69,8%; 95,8% de concordância); INT4 degrada (F1 67,5%; mais falsos positivos).
- Latência: Llama Guard 3 207 ms por pedido (4,8/s); GPT OSS Safeguard 10 575 ms (CoT de 500–1000 tokens) — inaceitável em produção.
- Relevância QBank: números concretos do compromisso falsos positivos / recall / latência de um filtro de âmbito; filtro de ~200 ms cabe no orçamento de 2–3 s, um com CoT não; saudações e perguntas curtas legítimas são falsos positivos típicos de um filtro de tema (no QBank: "obrigado", "não percebi"); avaliação com dados reais de red teaming além de sintéticos.
- Elegibilidade: Incluir (qualidade alta).

## R0765 emekci2025securing — ChatTEDU, arquitetura com dois LLM (IEEE Access 2025, 15 páginas)
- Chatbot institucional público e multilingue (TED University); análise de ameaças no período de matrículas jul–ago 2024: 4501 interações, 180 tentativas maliciosas; pico de ataques no dia de maior carga (30/07/2024).
- LLM-1 = subsistema de moderação (identificador de intenção e "deflector"); LLM-2 = geração; validação pelo Response Handler.
- LATÊNCIA: 6,7 s (um modelo) → 7,9 s (dois modelos), +1,2 s (+18%): LLM-1 0,9 s (75% do acréscimo), comunicação 0,2 s, validação da resposta 0,1 s; com 100+ utilizadores simultâneos, 9,1 s em média.
- CUSTO: +100% de chamadas à API (mínimo 2 por pergunta); ≈1,8× o custo, contando com respostas em cache e rejeições antecipadas.
- Resultados: 100% dos ataques identificados bloqueados; 0,28% falsos positivos; 77,8% exploração técnica; 15% multilingues. Sem baselines no mesmo conjunto (os autores reconhecem).
- Citam: prompts não ingleses com 2,7× mais sucesso de jailbreak (Deng et al.); ataques por alternância de línguas (code-switching) passam filtros em 68% dos testes (Yong et al.).
- Relevância QBank: números de custo e latência de um segundo modelo (≈+1 s, ≈1,8× custo) — com 2–3 s e 100 €/mês, um filtro LLM completo por pergunta é caro; filtros multilingues são necessários (6 línguas); cache e rejeição antecipada reduzem o custo.
- Elegibilidade: Incluir (qualidade alta, uso real).

## R0763 tien2024optimizing — deteção de jailbreak com Transformers (IEEE 2024)
- Ajuste fino de vários Transformers para detetar prompts de jailbreak num assistente universitário baseado em ChatGPT: DeBERTa-v3 exatidão 0,993 (perda 0,029), XLNet 0,990, GPT-2 0,988, RoBERTa/DistilBERT 0,985, Electra 0,983, BERT 0,973; integrado numa aplicação de assistente.
- Relevância QBank: classificadores pequenos atingem exatidão muito alta em conjuntos de laboratório, a custo e latência baixos; mas dependem de dados de treino (e do idioma) — avaliados num único conjunto.
- Elegibilidade: Incluir.

## R0771 mathew2026privacy — deteção federada de prompts adversariais em chatbots de saúde (IEEE 2026)
- RoBERTa-base ajustado no SPML Healthcare Chatbot Prompt Injection Dataset; treino centralizado vs federado (IID e não-IID, 3 configurações de clientes); Tesla T4; sementes fixas.
- Resultados: federado IID exatidão 0,957, F1 0,964; não-IID média exatidão 0,956, precisão 0,942, recall 0,987, F1 0,964, AUC 0,994.
- Relevância QBank: baixa a média — o classificador é aplicável; a componente federada não (um só operador).
- Elegibilidade: Incluir.

## R0807 rayhan2026sage — SAGE (IEEE 2026)
- Controlo de acesso ao conteúdo em 3 camadas (RBAC por papel, ABAC por atributos, controlo pelo estado cognitivo do estudante) sobre um grafo de conhecimento do estado do estudante e do conteúdo do curso; aplica sequência curricular e orientação passo a passo; benchmark educativo próprio num curso de programação.
- Resultados (resumo, confirmados no texto): utilidade 42% (tutores só com prompt) vs 44% (SAGE); cumprimento das políticas do docente 30% vs 90%.
- Relevância QBank: a política aplicada FORA do modelo (o que o modelo pode ver) é muito mais fiável do que a política escrita no prompt → regras por modo implementadas na seleção dos dados enviados.
- Elegibilidade: Incluir (qualidade alta para o QBank).

## R0809 abrar2025domain — assistente multilingue para estudantes com ajuste fino (IEEE 2025)
- Inglês, árabe padrão, franco-árabe e árabe omanense; fase I: memorização factual (TyDi QA, MASSIVE, LoRA); fase II: alinhamento comportamental com dados institucionais e PROMPTS QUE INDUZEM RECUSA para perguntas fora do âmbito.
- Avaliação: exatidão factual, BLEU, COMET, precisão da recusa, coerência multi-turno; baselines GPT-4, Aya-Base, Vicuna; correção e adequação da recusa julgadas por AVALIADORES HUMANOS QUE DOMINAM AS LÍNGUAS.
- Resultados: precisão da recusa 0,86 (GPT-4 0,82); exatidão 0,78 (GPT-4 0,81); recusa varia por língua (mínimo 0,73 em inglês); matriz de confusão com verdadeiros negativos altos e muitos pedidos legítimos recusados → tendência de RECUSA EXCESSIVAMENTE CONSERVADORA; pior em conversas longas.
- Relevância QBank: a recusa tem de ser avaliada nos dois sentidos (recusar o que deve e NÃO recusar o legítimo) e por língua, com avaliadores que dominem cada língua.
- Elegibilidade: Incluir.

## R0794 hamidi2026large — LLMs para QA radiológico, RadQA (IEEE 2026)
- QA extrativo sobre UM relatório radiológico (contexto fechado); LLaMA 3.1-8B, LLaMA 3.2-3B, Mistral-Small-22B em zero-shot, few-shot e ajuste fino.
- Métricas: EM, F1 (normalização: minúsculas, pontuação, artigos, espaços), medida ao nível da frase (SM); perguntas SEM RESPOSTA no relatório: a saída "None" é convertida em vazio e uma ABSTENÇÃO CORRETA conta como acerto (EM).
- Taxonomia de 8 categorias de erro: fronteira (superconjunto, subconjunto, sobreposição), respondibilidade (abstenções falsas positivas e falsas negativas: GNA, PNA) e falhas graves (sem sobreposição, alucinação).
- Resultados: ajuste fino LLaMA 3.1-8B 61% EM, 77% F1, 85% SM; elimina as alucinações e reduz ambos os tipos de abstenção errada.
- Relevância QBank: modelo de conjunto de teste com perguntas respondíveis e não respondíveis a partir de um documento fixo, em que a abstenção correta conta como acerto; taxonomia de erros mais informativa do que uma métrica agregada.
- Elegibilidade: Incluir.

## R0965 han2026textbook — VTA embebido no manual de CS1 (ICSE-Companion 2026, 3 páginas, DOI 10.1145/3774748.3795670)
- Assistente embebido no manual aberto; chunks com metadados de capítulo e secção (para recuperação e citação); RAG com BM25 por secção para perguntas de exame (cheias de palavras-chave: ano, época, número da pergunta, tema) + reordenação por cosseno; top-10; o modelo decide o tipo de recuperação e devolve uma resposta estruturada com campos de citação → links clicáveis para as secções.
- Recuperação (MRR em perguntas de exame): BM25+cosseno 0,50; só cosseno 0,45; palavras-chave+cosseno 0,34.
- Qualidade (avaliada por um TA): exatas 93%, relevantes 96%, completas 83%, referências corretas 89%. Inquérito: 89% acham útil; 43% provavelmente usam para dúvidas conceptuais; 78% improvável usar para resolver problemas (integridade académica).
- Relevância QBank: identificadores (ano, número da pergunta) tornam a pesquisa lexical/exata superior à semântica — de novo a favor do ID; resposta estruturada com campos de citação; perceção de integridade académica dos estudantes.
- Elegibilidade: Incluir. NOTA: no .bib a chave han2026textbook tinha o resumo de outro estudo — corrigir título/DOI.

## R0995 zheng2026comparative — LLM no apoio a utilizadores de HPC (PEARC 2026, DOI 10.1145/3785462.3815796)
- Base Llama-3.1-8B-Instruct; comparação SFT (ajuste fino com tickets do TACC limpos), RAG, ICL e combinações; categorias técnicas, depuração, políticas; correção avaliada manualmente por staff do centro; relevância, coerência, fluência e semelhança do cosseno.
- Resultados: ICL+RAG com o modelo base tem a maior correção nas perguntas técnicas e de políticas; ICL melhor em depuração; SFT+RAG o pior — o ajuste fino aprende os padrões dos tickets mas piora a capacidade de usar a informação externa recuperada; risco de o modelo ajustado reproduzir informação sensível dos tickets; SFT com contexto longo é caro.
- Relevância QBank: argumento contra o ajuste fino — contexto no prompt sobre o modelo base é melhor e o ajuste pode reduzir o uso do contexto fornecido.
- Elegibilidade: Incluir (domínio fora de educação/saúde, incluído pela exceção do contexto no prompt).

## R1056 xu2026echomind — EchoMind (NordiCHI 2026, 20 páginas, DOI 10.1145/3829807.3829883)
- Agente para apresentações gravadas: o vídeo pausa e o espectador pergunta a um agente com acesso à POSIÇÃO ATUAL no vídeo, à transcrição, diapositivos, artigos e materiais do orador, e a sinais acumulados de outros espectadores (perguntas anteriores, reações, comportamento); RAG sobre esses materiais; todas as respostas citam a fonte (segmento da transcrição, diapositivo, material); perguntas escaladas para o orador; "curva cognitiva" dos pontos de dificuldade.
- Estudo entre três condições: só vídeo, vídeo + chatbot LLM genérico (QAOnly), vídeo + EchoMind; usabilidade, carga (NASA-TLX), experiência de aprendizagem. EchoMind melhor em clarificação de dúvidas (M = 5,64 vs QAOnly 3,88, p_adj < 0,05), expressão no momento e sensação de co-aprendizagem, sem aumentar a carga; o chatbot genérico não superou o vídeo sozinho.
- Relevância QBank: contexto ligado ao ponto exato do conteúdo (posição no vídeo ↔ pergunta em curso); o valor vem do contexto, não do chatbot; sinais agregados de outros utilizadores (análogo às estatísticas por pergunta).
- Elegibilidade: Incluir.

## R1120 liao2026heal — Med-HEAL (ACM BCB 2026, DOI 10.1145/3807503.3819453)
- ICL consciente de alucinações em medicina: exemplos no prompt com alucinações anotadas e corrigidas; compara zero-shot, recuperação positiva (só exemplos corretos), negativa (alucinações com correção), contrastiva ingénua e CoT; autocrítica.
- Avaliação: juiz GPT-4o calibrado contra um subconjunto verificado por humanos (correção pela TPR e FPR do juiz: p = (p̂ − FPR)/(TPR − FPR)); auditoria por estudantes de medicina.
- Resultados: estratégias ingénuas de ICL por recuperação pouco ou nada melhoram face ao zero-shot e por vezes pioram; maior ganho +9,0%; Qwen3 perto do teto (+1,7%, p = 0,07); BioMistral não beneficia de autocrítica (contexto curto, pior seguimento de instruções).
- Relevância QBank: CALIBRAÇÃO DO LLM JUIZ contra uma amostra humana — método concreto para usar um juiz na avaliação do QBank com validação pelos especialistas da Adhara.
- Elegibilidade: Incluir.

## R1183 li2026responsible — DomainMonitor (WWW 2026, DOI 10.1145/3774904.3792621)
- Monitorização em tempo de execução dos estados internos (hidden states) de LLMs de domínio para detetar comportamento fora do domínio e sugerir instruções de recusa; exemplos: chatbot de psicologia a responder a perguntas de biomedicina; vários domínios e conjuntos.
- Requer acesso aos estados internos do modelo → não aplicável a um modelo usado por API.
- Elegibilidade: Incluir.

## Sem texto integral (marcados no índice): R1187 liu2024teaching (CS50.ai, demonstração), R0709 shah2026enhancing (IET, sem acesso) — mantidos com base no resumo.

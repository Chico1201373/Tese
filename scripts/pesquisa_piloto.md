# Registo do piloto de pesquisa

**Objetivo:** validar as seis expressões antes da pesquisa final. Este registo é apenas do piloto; não é o registo PRISMA final.
**Intervalo previsto:** 2021–2026 na interface; confirmar manualmente que os artigos respeitam 27-10-2021 a 27-10-2026.
**Execução piloto em 29-10-2026:** ScienceDirect: 179 registos recuperados, 85 únicos; ACM Digital Library: 180 recuperados, 153 únicos; IEEE Xplore (repetição com espera dinâmica corrigida): 180 recuperados, 172 únicos. As três recolhas foram limitadas a 30 títulos por query e não incluem abstracts. O piloto serve para ajustar pesquisas, não é contagem PRISMA final. A primeira tentativa IEEE está ultrapassada: a espera de carregamento era curta e produziu extração parcial.

| ID | RQ | Pesquisa no ScienceDirect | Total ScienceDirect | Total ACM | Total IEEE | Sinal nos 30 títulos ACM | Ruído observado nos títulos ACM |
|---|---|---|---:|---:|---:|---|---|
| RQ1a | RQ1 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28grounding%20OR%20%22prompt%20context%22%20OR%20%22retrieval-augmented%20generation%22%20OR%20%22context-aware%22%29%20AND%20%28chatbot%20OR%20%22conversational%20system%22%20OR%20%22question%20answering%22%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 138 | 7.325 | 1.286 | bom sinal: RAG + QA recorrente | muitos domínios fora de educação/medicina |
| RQ1b | RQ1 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28%22database%20retrieval%22%20OR%20%22context%20injection%22%20OR%20%22knowledge%20base%22%29%20AND%20%28chatbot%20OR%20%22question%20answering%22%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 100 | 2.227 | 383 | sinal moderado: KB-QA e alguns estudos médicos/educativos | aplicações e métodos variados |
| RQ1c | RQ1 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28reliability%20OR%20robustness%20OR%20security%20OR%20%22prompt%20injection%22%29%20AND%20%28chatbot%20OR%20%22conversational%20system%22%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 198 | 4.535 | 634 | sinal: prompt injection e segurança | segurança geral de LLM também aparece |
| RQ1d | RQ1 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28latency%20OR%20cost%20OR%20efficiency%29%20AND%20%28integration%20OR%20deployment%20OR%20architecture%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 649 | 26.832 | 4.006 | sinal fraco/ruidoso | codegen, hardware, recomendação e jogos; estreitar |
| RQ2a | RQ2 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28faithfulness%20OR%20factuality%20OR%20correctness%20OR%20%22scope%20adherence%22%29%20AND%20%28evaluation%20OR%20benchmark%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 447 | 22.885 | 641 | sinal fraco/ruidoso | muitos estudos sem avaliação de respostas conversacionais contextualizadas |
| RQ2b | RQ2 | [Abrir pesquisa](https://www.sciencedirect.com/search?qs=TITLE-ABS-KEY%28%28%22large%20language%20model%22%20OR%20LLM%29%20AND%20%28%22out-of-scope%22%20OR%20abstention%29%20AND%20%28evaluation%20OR%20benchmark%29%29&years=2021%2C2022%2C2023%2C2024%2C2025%2C2026&show=100&offset=0) | 30 (29 recolhidos) | 1.540 | 30 | alguns sobre abstention/out-of-scope | mistura com segurança e aplicações gerais |

## Resultado do piloto por fonte

| Fonte | Registos recolhidos | Únicos após deduplicação | Estado da triagem automática |
|---|---:|---:|---|
| ScienceDirect | 179 | 85 | 85 em triagem manual (só títulos) |
| ACM Digital Library | 180 | 153 | 153 em triagem manual (só títulos) |
| IEEE Xplore | 180 | 172 | 30 títulos por cada uma das seis queries; 8 duplicados entre queries |

Os totais indicados por query (RQ1a–RQ2b) foram: ScienceDirect = 138, 100, 198, 649, 447 e 30; ACM = 7.325, 2.227, 4.535, 26.832, 22.885 e 1.540; IEEE = 1.286, 383, 634, 4.006, 641 e 30. Na amostra de 30 títulos ACM por query, RQ1a e RQ1b mostraram estudos de QA/RAG e bases de conhecimento em domínios variados; RQ1c encontrou segurança e prompt injection; RQ1d e RQ2a tiveram bastante ruído (por exemplo, geração de código, hardware e recomendação); RQ2b contém alguns trabalhos sobre abstention/out-of-scope, misturados com temas gerais de LLM. Esta observação foi feita apenas a partir dos títulos.

“153 únicos” quer dizer 153 registos de título distintos depois de remover duplicados entre as seis queries ACM; não quer dizer 153 estudos relevantes. Como o modo browser não recolhe abstracts, todos ficam corretamente em **triagem manual**.

## Variante v0.2 para RQ1d e RQ2a

As duas expressões foram estreitadas para exigir sistemas conversacionais/QA e comparadas com a versão v0.1. Cada teste recolheu até 30 títulos por query.

| Fonte | RQ1d v0.1 → v0.2 | RQ2a v0.1 → v0.2 | Resultado v0.2 |
|---|---:|---:|---|
| ScienceDirect | 649 → 278 | 447 → 138 | 25 títulos recolhidos por query; 40 registos únicos após deduplicação |
| IEEE Xplore | 4.006 → 1.513 | 641 → 60 | 60 títulos recuperados, 60 únicos |
| ACM Digital Library | 26.832 → 9.407 | 22.885 → 4.047 | 60 títulos recuperados, 57 únicos |

Na execução ScienceDirect de 29-10-2026, o portal indicou 278 resultados para RQ1d e 138 para RQ2a; o piloto recolheu os primeiros 25 títulos de cada query. A deduplicação entre as duas listas deixou 40 títulos únicos (10 duplicados). Todos permanecem em triagem manual, porque o modo browser recolheu apenas títulos. Os resultados estão em `scripts/piloto_sciencedirect_v2.md` e `scripts/piloto_sciencedirect_v2.csv`.

Nos títulos v0.2, RQ1d mostrou mais QA, chatbots e RAG em IEEE e ACM; RQ2a trouxe avaliação de diálogo, chatbots e respostas fundamentadas, embora ainda haja ruído interdisciplinar. Por estes sinais, as expressões v0.2 foram adotadas provisoriamente no protocolo e no script. A validação da query no ScienceDirect foi concluída, mas esta execução usou os URLs fornecidos sem filtros de data; confirma o intervalo 27-10-2021 a 27-10-2026 e não uses estes números como contagens finais do PRISMA. As expressões exatas e os URLs estão em `scripts/queries_pilot_v2.json`.

## Nota de execução

Para cada ligação, registar a contagem apresentada pela fonte e inspecionar 20–30 títulos e, quando disponíveis, resumos. Guardar a data, os filtros efetivamente aplicados e os registos relevantes e irrelevantes. Não usar estes números como contagens finais do PRISMA até validar as expressões e executar a pesquisa final.

# Resumo de artigos

## Enabling Retriever-LLM Connection Across the Semantic Gap in Retrieval-Augmented Generation

**Autores:** Fuda Ye, Shuangyin Li, Yongqi Zhang, Lei Chen, Shaobing Qu  
**Publicação:** ACM Transactions on Knowledge Discovery from Data · 2026  
**DOI:** https://doi.org/10.1145/3847108  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3847108  
**Keywords:** retrieval-augmented generation, semantic gap, document relevance, evidence identification  

**TL;DR:** ConRAG is proposed, a novel enhanced RAG framework to establish an information connection between retrievers and LLMs in RAG, thereby enhancing relationship modeling of LLMs and is suitable for low-resource scenarios where LLMs and retrievers are frozen.

**Abstract:**

Retrieval-augmented generation (RAG) has attracted significant attention for enhancing large language models (LLMs) in domain-specific and knowledge-intensive tasks by utilizing external documents retrieved by retrievers. However, LLMs often struggle to determine which retrieved documents are relevant and how they relate to one another. We argue that this difficulty arises from a semantic gap between retrievers and LLMs due to differences in their training objectives and architectures. Existing methods either align retrievers and LLMs through costly fine-tuning or feedback signals, but they still do not explicitly strengthen document relationship modeling during generation. This paper proposes ConRAG, a novel enhanced RAG framework to establish an information connection between retrievers and LLMs in RAG, thereby enhancing relationship modeling of LLMs. Specifically, ConRAG employs a lightweight Con-Former model, placed between a retriever and an LLM to capture and transmit semantic information. Then, a semantics injection strategy is employed to integrate the semantic information into the LLM's generation. Accordingly, we employ three tasks for feature modeling and alignment: two relationship modeling tasks to consolidate the local and global perceptions of document relevance and one generative alignment task to facilitate the interpretation of LLM. Notably, ConRAG is suitable for low-resource scenarios where LLMs and retrievers are frozen. Further analysis shows that retriever-derived information helps the LLM better identify relevant evidence and model relationships among documents, leading to more effective generation. The source code is available at https://github.com/yefd/ConRAG .

---

## Evaluating the Experience of LGBTQ+ People Using Large Language Model Based Chatbots for Mental Health Support

**Autores:** Zilin Ma, Yiyang Mei, Yinru Long, Zhaoyuan Su, Krzysztof Z. Gajos  
**Publicação:** Proceedings of the CHI Conference on Human Factors in Computing Systems · 2024  
**DOI:** https://doi.org/10.1145/3613904.3642482  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3613904.3642482  
**Citações:** 71  
**Keywords:** LGBTQ mental health, large language models, chatbots, mental health support, user experience, LLM fine-tuning, social discrimination, algorithmic bias, access to mental health care  

**Abstract:**

LGBTQ+ individuals are increasingly turning to chatbots powered by large language models (LLMs) to meet their mental health needs. However, little research has explored whether these chatbots can adequately and safely provide tailored support for this demographic. We interviewed 18 LGBTQ+ and 13 non-LGBTQ+ participants about their experiences with LLM-based chatbots for mental health needs. LGBTQ+ participants relied on these chatbots for mental health support, likely due to an absence of support in real life. Notably, while LLMs offer prompt support, they frequently fall short in grasping the nuances of LGBTQ-specific challenges. Although fine-tuning LLMs to address LGBTQ+ needs can be a step in the right direction, it isn’t the panacea. The deeper issue is entrenched in societal discrimination. Consequently, we call on future researchers and designers to look beyond mere technical refinements and advocate for holistic strategies that confront and counteract the societal biases burdening the LGBTQ+ community.

---

## Exploring the Abstention Ability of LLMs using Scientific Reasoning in Critical Fields

**Autores:** Landen Summers, Haeseon Yoon, Weijian Zheng, Yunhe Feng  
**Publicação:** Proceedings of the 26th ACM/IEEE Joint Conference on Digital Libraries · 2026  
**DOI:** https://doi.org/10.1145/3805696.3847298  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805696.3847298  
**Keywords:** large language models, abstention, scientific question answering, multiple-choice question answering, factual errors, confidence calibration  

**TL;DR:** It is demonstrated that LLMs often struggle to abstain consistently when the correct answer is absent, and that their abstention behavior is sensitive to model family, abstention wording, and reasoning settings.

**Abstract:**

Large Language Models (LLMs) can produce fluent and confident responses even when those responses lack sufficient support or contain factual errors. Reliable question answering therefore requires models not only to generate answers, but also to recognize when they cannot provide a well-supported response and abstain accordingly. This capability is particularly important in scientific domains, where inaccurate responses can cause real-world harm. This paper systematically investigates the abstention behavior of LLMs in challenging scientific multiple-choice answering tasks. We evaluate several LLMs on multiple modified versions of a scientific multiple-choice question answering dataset, varying both the availability of the correct answer and the wording of the abstention option. Our findings demonstrate that LLMs often struggle to abstain consistently when the correct answer is absent, and that their abstention behavior is sensitive to model family, abstention wording, and reasoning settings.

---

## FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation

**Autores:** Chanyeol Choi, Jihoon Kwon, Jaeseon Ha, Hojun Choi, Chaewoon Kim, Yongjae Lee et al.  
**Publicação:** Proceedings of the 6th ACM International Conference on AI in Finance · 2025  
**DOI:** https://doi.org/10.1145/3768292.3770361  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3768292.3770361  
**Citações:** 14  
**Keywords:** financial question answering, retrieval-augmented generation, financial information retrieval, large language models  

**TL;DR:** FinDER, an expert-generated dataset tailored for Retrieval-Augmented Generation (RAG) in finance, focuses on annotating search-relevant evidence by domain experts, offering 5,703 query–evidence–answer triplets derived from real-world financial inquiries.

**Abstract:**

In the fast-paced financial domain, accurate and up-to-date information is critical to addressing ever-evolving market conditions. Retrieving this information correctly is essential in financial Question-Answering (QA), since many language models struggle with factual accuracy in this domain. We present FinDER, an expert-generated dataset tailored for Retrieval-Augmented Generation (RAG) in finance. Unlike existing QA datasets that provide predefined contexts and rely on relatively clear and straightforward queries, FinDER focuses on annotating search-relevant evidence by domain experts, offering 5,703 query–evidence–answer triplets derived from real-world financial inquiries. These queries frequently include abbreviations, acronyms, and concise expressions, capturing the brevity and ambiguity common in the realistic search behavior of professionals. By challenging models to retrieve relevant information from large corpora rather than relying on readily determined contexts, FinDER offers a more realistic benchmark for evaluating RAG systems. We further present a comprehensive evaluation of multiple state-of-the-art retrieval models and Large Language Models, showcasing challenges derived from a realistic benchmark to drive future research on truthful and precise RAG in the financial domain. We will release the dataset publicly upon acceptance of the paper.

---

## FormaT5: Abstention and Examples for Conditional Table Formatting with Natural Language

**Autores:** Mukul Singh, José Cambronero, Sumit Gulwani, Vu Le, Carina Negreanu, Elnaz Nouri et al.  
**Publicação:** Proceedings of the VLDB Endowment · 2023  
**DOI:** https://doi.org/10.14778/3632093.3632111  
**Fonte:** acm — https://dl.acm.org/doi/10.14778/3632093.3632111  
**Citações:** 5  
**Keywords:** natural language to code generation, abstention, programming by example, spreadsheet software  

**Abstract:**

Formatting is an important property in tables for visualization, presentation, and analysis. Spreadsheet software allows users to automatically format their tables by writing data-dependent conditional formatting (CF) rules. Writing such rules is often challenging for users as it requires understanding and implementing the underlying logic. We present FormaT5, a transformer-based model that can generate a CF rule given the target table and a natural language description of the desired formatting logic. We find that user descriptions for these tasks are often under-specified or ambiguous, making it harder for code generation systems to accurately learn the desired rule in a single step. To tackle this problem of under-specification and minimise argument errors, FormaT5 learns to predict placeholders though an abstention objective. These placeholders can then be filled by a second model or, when examples of rows that should be formatted are available, by a programming-by-example system. To evaluate FormaT5 on diverse and real scenarios, we create an extensive benchmark of 1053 CF tasks, containing real-world descriptions collected from four different sources. We release our benchmarks to encourage research in this area. Abstention and filling allow FormaT5 to outperform 8 different neural approaches on our benchmarks, both with and without examples. Our results illustrate the value of building domain-specific learning systems.

---

## From Clicks to Preference: A Multi-stage Alignment Framework for Generative Query Suggestion in Conversational System

**Autores:** Junhao Yin, Haolin Wang, Peng Bao, Ju Xu, Yongliang Wang  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 · 2026  
**DOI:** https://doi.org/10.1145/3770854.3783953  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770854.3783953  
**Citações:** 13  
**Keywords:** dialogue systems, user preference modeling, prompt engineering, large language models, user engagement  

**TL;DR:** This work introduces a multi-stage framework designed for progressive alignment between the generation policy and user intent and develops a Gaussian Reward Model (GaRM) that represents user preferences as probability distributions rather than point estimates.

**Abstract:**

Generative query suggestion using large language models offers a powerful way to enhance conversational systems, but aligning outputs with nuanced user preferences remains a critical challenge. To address this, we introduce a multi-stage framework designed for progressive alignment between the generation policy and user intent. Our pipeline begins with prompt engineering as a cold-start strategy, followed by the Supervised Fine-Tuning stage, in which we introduce a distillation method on click logs to create a robust foundational model. To better model user preferences while capturing their inherent uncertainty, we develop a Gaussian Reward Model (GaRM) that represents user preferences as probability distributions rather than point estimates. Finally, we employ reinforcement learning to align the generation policy with these preferences, guided by a composite reward function that integrates GaRM with auxiliary heuristics to mitigate reward hacking. To maintain training stability, this process is enhanced by a novel out-of-distribution regularization method and a two-stage reward fusion technique. Extensive experiments demonstrate that our framework significantly outperforms baselines on both automatic and human evaluations and yields a 34% relative increase in user engagement as measured by click-through rate in live A/B tests.

---

## From Rules to Reasoning: A Survey of Large Language Model-Based Approaches to Scientific Hypothesis and Idea Generation

**Autores:** Emily Herron, Vanessa Lama, Sedrick Bouknight, Tirthankar Ghosal  
**Publicação:** ACM Computing Surveys · 2026  
**DOI:** https://doi.org/10.1145/3815423  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3815423  
**Citações:** 3  
**Keywords:** scientific hypothesis generation, large language models, automated scientific discovery, retrieval-augmented generation, multi-agent systems, cognitive architecture, LLM fine-tuning, prompting, hallucination management, LLM-as-judge evaluation, hybrid neural-symbolic architecture, human-AI collaboration, social psychology, biomedical research  

**TL;DR:** Evaluation methodologies encompass human expert assessment, LLM-as-judge frameworks, and comprehensive benchmarking systems that demonstrate statistical equivalence to human expert performance in social psychology, experimental validation in biomedical research, and near-expert quality in astronomy.

**Abstract:**

Scientific hypothesis generation represents a fundamental challenge in contemporary research due to exponentially expanding literature volumes and increasing disciplinary specialization. Large language models (LLMs) have emerged as transformative tools for automated scientific discovery, moving beyond traditional rule-based and literature-mining approaches. Four paradigmatic approaches define current LLM-driven hypothesis generation: direct prompting and fine-tuning methods, knowledge-enhanced frameworks integrating retrieval-augmented generation (RAG), multi-agent collaborative systems simulating research teams, and reasoning-focused approaches implementing cognitive architectures. Domain-specific applications demonstrate statistical equivalence to human expert performance in social psychology, experimental validation in biomedical research, and near-expert quality in astronomy. Evaluation methodologies encompass human expert assessment, LLM-as-judge frameworks, and comprehensive benchmarking systems. Technical challenges include hallucination management, knowledge integration limitations, and balancing novelty with feasibility. Future directions emphasize hybrid neural-symbolic architectures and sophisticated human-AI collaboration models for responsible scientific discovery acceleration.

---

## Global Question-Aware Multimodal Retrieval-Augmented Generation for Multimedia Multi-Hop Question Answering

**Autores:** Zhixiao Shen, Jianfei Yu, Wenya Wang, Rui Xia  
**Publicação:** Proceedings of the 7th ACM International Conference on Multimedia in Asia · 2025  
**DOI:** https://doi.org/10.1145/3743093.3771062  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3743093.3771062  
**Keywords:** multimodal retrieval-augmented generation, cross-modal contrastive learning, multimodal large language models, error propagation  

**TL;DR:** Global question-aware Multimodal Retrieval-Augmented Generation (GMRAG), a framework designed to enhance cross-modal reasoning and improve retrieval precision for multi-hop multimodal questions, is introduced.

**Abstract:**

Multimedia Multi-Hop Question Answering (MMQA) is a complex task that requires models to reason over and integrate information from both visual (e.g., images) and textual (e.g., documents) modalities to answer questions that cannot be resolved in a single step. Existing methods for MMQA suffer from two common limitations: (1) insufficient cross-modal information fusion, which restricts interaction between different modalities; and (2) weak global understanding of multi-hop questions, making them vulnerable to distractions from intermediate steps. To address these challenges, we introduce Global question-aware Multimodal Retrieval-Augmented Generation (GMRAG), a framework designed to enhance cross-modal reasoning and improve retrieval precision for multi-hop multimodal questions. It brings two core innovations: (1) restructuring the training data into a global question–aware, evidence-centric retrieval dataset, enabling the retriever to perform richer cross-modal reasoning on multi-hop multimodal questions and to identify globally relevant information more effectively; and (2) employing cross-modal contrastive learning to fine-tune a joint image–text encoder, achieving stronger alignment between holistic multimodal questions and evidence. The retrieved evidence is then directly fed into a Multimodal Large Language Models (MLLMs) to generate the final answer to the original question, eliminating dependence on potentially flawed intermediate answers and thus mitigating error propagation. Experimental results on two public MMQA datasets show that GMRAG consistently outperforms existing RAG methods across various MLLMs.

---

## How Much Reasoning Do Retrieval-Augmented Models Add beyond LLMs? A Benchmarking Framework for Multi-Hop Inference over Hybrid Knowledge

**Autores:** Junhong Lin, Bing Zhang, Song Wang, Ziyan Liu, Dan Gutfreund, Julian Shun et al.  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770855.3817481  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770855.3817481  
**Keywords:** retrieval-augmented generation, multi-hop reasoning, benchmark design, hybrid knowledge, knowledge graphs, unstructured text, knowledge-intensive question answering, large language models  

**TL;DR:** Experiments across three domains demonstrate that HybridRAG-Bench rewards genuine retrieval and reasoning rather than parametric recall, offering a principled testbed for evaluating hybrid knowledge–augmented reasoning systems.

**Abstract:**

Large language models (LLMs) continue to struggle with knowledge-intensive questions that require up-to-date information and multi-hop reasoning. Augmenting LLMs with hybrid external knowledge, such as unstructured text and structured knowledge graphs, offers a promising alternative to costly continual pretraining. As such, reliable evaluation of their retrieval and reasoning capabilities becomes critical. However, many existing benchmarks increasingly overlap with LLM pretraining data, which means that answers or supporting knowledge may already be encoded in model parameters, making it difficult to distinguish genuine retrieval and reasoning from parametric recall. We introduce HybridRAG-Bench, a contamination-aware benchmark construction framework to evaluate retrieval-intensive, multi-hop reasoning over hybrid knowledge. HybridRAG-Bench automatically couples unstructured text and structured knowledge graph representations derived from recent scientific literature on arXiv, and generates knowledge-intensive question-answer pairs grounded in explicit reasoning paths. The framework supports flexible domain and time-range selection, enabling contamination-aware, customizable evaluation as models and knowledge evolve. Experiments across three domains (artificial intelligence, governance and policy, and bioinformatics) demonstrate that HybridRAG-Bench rewards genuine retrieval and reasoning rather than parametric recall, offering a principled testbed for evaluating hybrid knowledge–augmented reasoning systems. We release our code and data at github.com/junhongmit/HybridRAG-Bench.

---

## Human and Large Language Model Intent Detection in Image-Based Self-Expression of People with Intellectual Disability

**Autores:** Alieh Hajizadeh Saffar, Laurianne Sitbon, Maria Hoogstrate, Ahmed Abbas, Sirinthip Roomkham, Dimity Miller  
**Publicação:** Proceedings of the 2024 ACM SIGIR Conference on Human Information Interaction and Retrieval · 2024  
**DOI:** https://doi.org/10.1145/3627508.3638347  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3627508.3638347  
**Citações:** 14  
**Keywords:** intellectual disability, nonverbal communication, intent classification, large language models, visual prompts, social inclusion, augmentative and alternative communication  

**TL;DR:** It is suggested that generic images offer a rich medium for individuals to share personal interests and unique experiences, enriching communication and offering design strategies for intent clarification and crafting more inclusive multimodal conversational tools for individuals with intellectual disability.

**Abstract:**

Non-verbal communication is essential for the social inclusion of individuals with an intellectual disability, affecting interactions with others as well as technological systems. This study focuses on non-symbolic communication of people with intellectual disability through generic images without specific or detailed subject matter. A key challenge in this medium is discerning the underlying intentions behind images selected as visual prompts for conversation.

---

## Human-Algorithmic Interaction Using a Large Language Model-Augmented Artificial Intelligence Clinical Decision Support System

**Autores:** Niroop Channa Rajashekar, Yeo Eun Shin, Yuan Pu, Sunny Chung, Kisung You, Mauro Giuffre et al.  
**Publicação:** Proceedings of the CHI Conference on Human Factors in Computing Systems · 2024  
**DOI:** https://doi.org/10.1145/3613904.3642024  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3613904.3642024  
**Citações:** 87  
**Keywords:** large language models, clinical decision support systems, human-technology interaction, upper gastrointestinal bleeding, clinical simulation, trust in AI, usability, clinical expertise, medical students, physician decision-making, AI-generated citations  

**TL;DR:** Evidence is found that LLM augmentation improves ease-of-use, that LLM-generated responses with citations improve trust, and HCI varies based on clinical expertise.

**Abstract:**

Integration of artificial intelligence (AI) into clinical decision support systems (CDSS) poses a socio-technological challenge that is impacted by usability, trust, and human-computer interaction (HCI). AI-CDSS interventions have shown limited benefit in clinical outcomes, which may be due to insufficient understanding of how health-care providers interact with AI systems. Large language models (LLMs) have the potential to enhance AI-CDSS, but haven’t been studied in either simulated or real-world clinical scenarios. We present findings from a randomized controlled trial deploying AI-CDSS for the management of upper gastrointestinal bleeding (UGIB) with and without an LLM interface within realistic clinical simulations for physician and medical student participants. We find evidence that LLM augmentation improves ease-of-use, that LLM-generated responses with citations improve trust, and HCI varies based on clinical expertise. Qualitative themes from interviews suggest the perception of LLM-augmented AI-CDSS as a team-member used to confirm initial clinical intuitions and help evaluate borderline decisions.

---

## Inferential Question Answering

**Autores:** Jamshid Mozafari, Hamed Zamani, Guido Zuccon, Adam Jatowt  
**Publicação:** arXiv (Cornell University) · 2026  
**DOI:** https://doi.org/10.1145/3774904.3792653  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3774904.3792653  
**Citações:** 2  
**Keywords:** answerability, re-ranking, document retrieval  

**TL;DR:** Questions requiring Inference from Texts is introduced–a new task that challenges models to infer answers from answer-supporting passages which provide only clues, and establishes a new class of QA tasks that move towards understanding and reasoning from indirect textual evidence.

**Abstract:**

Despite extensive research on a wide range of question answering (QA) systems, most existing work focuses on answer containment-i.e., assuming that answers can be directly extracted and/or generated from documents in the corpus. However, some questions require inference, i.e., deriving answers that are not explicitly stated but can be inferred from the available information. We introduce Inferential QA -- a new task that challenges models to infer answers from answer-supporting passages which provide only clues. To study this problem, we construct QUIT (QUestions requiring Inference from Texts) dataset, comprising 7,401 questions and 2.4M passages built from high-convergence human- and machine-authored hints, labeled across three relevance levels using LLM-based answerability and human verification. Through comprehensive evaluation of retrievers, rerankers, and LLM-based readers, we show that methods effective on traditional QA tasks struggle in inferential QA: retrievers underperform, rerankers offer limited gains, and fine-tuning provides inconsistent improvements. Even reasoning-oriented LLMs fail to outperform smaller general-purpose models. These findings reveal that current QA pipelines are not yet ready for inference-based reasoning. Inferential QA thus establishes a new class of QA tasks that move towards understanding and reasoning from indirect textual evidence.

---

## Instructive Code Retriever: Learn from Large Language Model's Feedback for Code Intelligence Tasks

**Autores:** Jiawei Lu, Haoye Wang, Zhongxin Liu, Keyu Liang, Lingfeng Bao, Xiaohu Yang  
**Publicação:** Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering · 2024  
**DOI:** https://doi.org/10.1145/3691620.3694997  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3691620.3694997  
**Citações:** 1  
**Keywords:** code intelligence, example retrieval, large language models, in-context learning, code summarization, program synthesis, bug fixes, code search  

**TL;DR:** This paper introduces a novel approach named Instructive Code Retriever (ICR), which is designed to retrieve examples that enhance model inference across various code intelligence tasks and datasets, and enables ICR to learn the semantic and structural information of the corpus by a tree-based loss function.

**Abstract:**

Recent studies proposed to leverage large language models (LLMs) with In-Context Learning (ICL) to handle code intelligence tasks without fine-tuning. ICL employs task instructions and a set of examples as demonstrations to guide the model in generating accurate answers without updating its parameters. While ICL has proven effective for code intelligence tasks, its performance heavily relies on the selected examples. Previous work has achieved some success in using BM25 to retrieve examples for code intelligence tasks. However, existing approaches lack the ability to understand the semantic and structural information of queries, resulting in less helpful demonstrations. Moreover, they do not adapt well to the complex and dynamic nature of user queries in diverse domains. In this paper, we introduce a novel approach named Instructive Code Retriever (ICR), which is designed to retrieve examples that enhance model inference across various code intelligence tasks and datasets. We enable ICR to learn the semantic and structural information of the corpus by a tree-based loss function. To better understand the correlation between queries and examples, we incorporate the feedback from LLMs to guide the training of the retriever. Experimental results demonstrate that our retriever significantly outperforms state-of-the-art approaches. We evaluate our model’s effectiveness on various tasks, i.e., code summarization, program synthesis, and bug fixing. Compared to previous state-of-the-art algorithms, our method achieved improvements of 50.0% and 90.0% in terms of BLEU-4 for two code summarization datasets, 74.6% CodeBLEU on program synthesis dataset, and increases of 3.6 and 3.2 BLEU-4 on two bug fixing datasets.CCS CONCEPTS• Computing methodologies → Artificial intelligence; • Software and its engineering;

---

## Invited Paper: Experimental Analysis of Distributed Agentic Large-Language Model Inference Architectures

**Autores:** Kartik Padalkar, Vitor Jesus, Jose M. Alcaraz Calero  
**Publicação:** Proceedings of the Workshop on Advanced Tools, Programming Languages, and PLatforms for Implementing and Evaluating algorithms for Distributed systems · 2026  
**DOI:** https://doi.org/10.1145/3820355.3820384  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3820355.3820384  
**Keywords:** large language model inference, agentic LLMs, pipeline parallelism, tensor parallelism, AllReduce, vLLM, SGLang, llama.cpp, tail latency, throughput, heterogeneous GPU clusters, dynamic batching  

**TL;DR:** Two primitives, pipeline activation transfer and per-layer tensor all-reduce, are evaluated on three inference engines (vLLM, SGLang, llama.cpp) and it is shown that engine choice on heterogeneous hardware depends on the operating point, not any single peak.

**Abstract:**

Large language model (LLM) inference is expensive, and agentic applications increase that cost. Each request expands into a graph of LLM calls, and tail latency drives the overall response time. Parallelism splits model state across GPUs so larger models fit and throughput scales with load, but it does not always reduce latency. The right choice depends on the network fabric and the request shape. We evaluate two primitives, pipeline activation transfer and per-layer tensor all-reduce, on three inference engines (vLLM, SGLang, llama.cpp). Our cluster is a heterogeneous consumer-GPU pair over 100 GbE, driven by a 1+2+1 stage graph (orchestrator, two workers, verifier) with prompts from BFCL. We sweep nine (engine, mode) configurations over five concurrency levels and a schema-on/off A/B for 90 cells. An asymmetric 22-to-10 layer split that mirrors the memory ratio yields a pipeline throughput edge of up to ~12 % on vLLM and ~17 % on llama.cpp, although the edge shrinks at high concurrency, partly an admission control effect, not pure compute balance. Even on the fast fabric, tensor parallelism pays a ~ 2–4× first-token penalty against pipeline parallelism on the dynamically batched engines, because per-token collectives, not bandwidth, dominate. No engine wins overall. SGLang's even pipeline reaches 3.38 chains/s at C=64, while vLLM's asymmetric pipeline leads inside the service-level-objective (SLO), peaking at 2.28 chains/s of goodput@10 s at C=16, about 25% above SGLang's 1.83 in the same cell. Engine choice on heterogeneous hardware depends on the operating point, not any single peak.

---

## LARCH: Large Language Model-based Automatic Readme Creation with Heuristics

**Autores:** Yuta Koreeda, Terufumi Morishita, Osamu Imaichi, Yasuhiro Sogawa  
**Publicação:** Proceedings of the 32nd ACM International Conference on Information and Knowledge Management · 2023  
**DOI:** https://doi.org/10.1145/3583780.3614744  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3583780.3614744  
**Citações:** 7  
**Keywords:** large language models, weakly supervised learning, heuristics, software documentation, larch  

**TL;DR:** This paper shows that LLMs are capable of generating a coherent and factually correct readmes if the authors can identify a code fragment that is representative of the repository, and develops LARCH (LLM-based Automatic Readme Creation with Heuristics) which leverages representative code identification with heuristics and weak supervision.

**Abstract:**

Writing a readme is a crucial aspect of software development as it plays a vital role in managing and reusing program code. Though it is a pain point for many developers, automatically creating one remains a challenge even with the recent advancements in large language models (LLMs), because it requires generating an abstract description from thousands of lines of code. In this demo paper, we show that LLMs are capable of generating a coherent and factually correct readmes if we can identify a code fragment that is representative of the repository. Building upon this finding, we developed LARCH (LLM-based Automatic Readme Creation with Heuristics) which leverages representative code identification with heuristics and weak supervision. Through human and automated evaluations, we illustrate that LARCH can generate coherent and factually correct readmes in the majority of cases, outperforming a baseline that does not rely on representative code identification. We have made LARCH open-source and provided a cross-platform Visual Studio Code interface and command-line interface, accessible at https://github.com/hitachi-nlp/larch. A demo video showcasing LARCH's capabilities is available at https://youtu.be/ZUKkh5ED-O4.

---

## LLM App Store Analysis: A Vision and Roadmap

**Autores:** Yanjie Zhao, Xinyi Hou, Shenao Wang, Haoyu Wang  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2025  
**DOI:** https://doi.org/10.1145/3708530  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3708530  
**Citações:** 26  
**Keywords:** large language models, security risk identification, data mining, market dynamics, stakeholder relations, ethical considerations, responsible innovation, governance framework, user-centered design  

**TL;DR:** A forward-looking analysis of LLM app stores, focusing on key aspects such as data mining, security risk identification, development assistance, and market dynamics, and the ethical considerations and potential societal impacts are explored.

**Abstract:**

The rapid growth and popularity of large language model (LLM) app stores have created new opportunities and challenges for researchers, developers, users, and app store managers. As the LLM app ecosystem continues to evolve, it is crucial to understand the current landscape and identify potential areas for future research and development. This article presents a forward-looking analysis of LLM app stores, focusing on key aspects such as data mining, security risk identification, development assistance, and market dynamics. Our comprehensive examination extends to the intricate relationships between various stakeholders and the technological advancements driving the ecosystem’s growth. We explore the ethical considerations and potential societal impacts of widespread LLM app adoption, highlighting the need for responsible innovation and governance frameworks. By examining these aspects, we aim to provide a vision for future research directions and highlight the importance of collaboration among stakeholders to address the challenges and opportunities within the LLM app ecosystem. The insights and recommendations provided in this article serve as a foundation for driving innovation, ensuring responsible development, and creating a thriving, user-centric LLM app landscape.

---

## LLM-Triaged Vulnerability Analysis for Compiled DNNs

**Autores:** Minghui Li, Yang Li, Changchun Yin, Mingwei Li, Liming Fang  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2026  
**DOI:** https://doi.org/10.1145/3814615  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3814615  
**Keywords:** vulnerability assessment, TVM, attack mitigation  

**TL;DR:** VulnSketch is presented, the first LLM-driven vulnerability analysis system for compiled DNNs, and an evidence-bounded formulation of vulnerability analysis that is both auditable and actionable.

**Abstract:**

Compiler toolchains such as TVM are now a standard substrate for deploying deep neural networks, but the optimized executables also expose structures that attackers can leverage. Existing mitigations are commonly applied as global composite defense, which is effective yet costly because it disrupts performance-critical regularity everywhere. We present VulnSketch, the first LLM-driven vulnerability analysis system for compiled DNNs, and introduce an evidence-bounded formulation of vulnerability analysis that is both auditable and actionable. VulnSketch extracts a Minimal Evidence Interface (MEI) from TVM TIR, scores each operator location along three attacker-aligned vulnerability faces (Segmentation, Regularity, and Lifting), and routes only ambiguous gray locations to bounded LLM triage that must cite MEI fields and propose a pre-approved, semantics-preserving schedule knob. Every proposal is executed under compiler-side legality guards and accepted only if a single micro validation confirms the expected one-step movement on the prioritized face. Across five representative attacks, VulnSketch attains strong operator-level overlap at small budgets (top 5% recall 0.71-0.80; top 10% recall 0.84-0.91) and high global ranking quality (AUROC 0.85-0.89; AUPRC 0.51-0.62). Applying micro-validated knobs causally reduces attack success by 33-38% and recovered footprint by 38-40%. Operationally, VulnSketch yields 5.9 seconds amortized per verified note under default gray exposure.

---

## LLMCompass: Enabling Efficient Hardware Design for Large Language Model Inference

**Autores:** Hengrui Zhang, August Ning, Rohan Baskar Prabhakar, David Wentzlaff  
**Publicação:** 2024 ACM/IEEE 51st Annual International Symposium on Computer Architecture (ISCA) · 2024  
**DOI:** https://doi.org/10.1109/ISCA59077.2024.00082  
**Fonte:** acm — https://dl.acm.org/doi/10.1109/ISCA59077.2024.00082  
**Citações:** 60  
**Keywords:** large language model inference, hardware design, latency estimation, NVIDIA A100, high-bandwidth memory, DRAM, cost-performance trade-off  

**Abstract:**

The past year has witnessed the increasing popularity of Large Language Models (LLMs). Their unprecedented scale and associated high hardware cost have impeded their broader adoption, calling for efficient hardware designs. With the large hardware needed to simply run LLM inference, evaluating different hardware designs becomes a new bottleneck. This work introduces LLMCompass1, a hardware evaluation framework for LLM inference workloads. LLMCompass is fast, accurate, versatile, and able to describe and evaluate different hardware designs. LLMCompass includes a mapper to automatically find performance-optimal mapping and scheduling. It also incorporates an area-based cost model to help architects reason about their design choices. Compared to real-world hardware, LLMCompass’ estimated latency achieves an average $10.9\%$ error rate across various operators with various input sizes and an average $4.1\%$ error rate for LLM inference. With LLMCompass, simulating a 4-NVIDIA A100 GPU node running GPT-3 175B inference can be done within 16 minutes on commodity hardware, including 26,400 rounds of the mapper’s parameter search. With the aid of LLMCompass, this work draws architectural implications and explores new cost-effective hardware designs. By reducing the compute capability or replacing High Bandwidth Memory (HBM) with traditional DRAM, these new designs can achieve as much as 3.41x improvement in performance/cost compared to an NVIDIA A100, making them promising choices for democratizing LLMs.1Available at https://github.com/PrincetonUniversity/LLMCompass.

---

## Large Language Model Agents for Improving Engagement with Behavior Change Interventions: Application to Digital Mindfulness

**Autores:** Harsh Kumar, Suhyeon Yoo, Angela Zavaleta Bernuy, Jiakai Shi, Huayin Luo, Joseph Jay Williams et al.  
**Publicação:** Proceedings of the ACM on Human-Computer Interaction · 2025  
**DOI:** https://doi.org/10.1145/3757619  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3757619  
**Citações:** 8  
**Keywords:** LLM agents, behaviour change interventions, mindfulness, user engagement, social support, digital health, self-reflection, intention to practice, chatbots  

**TL;DR:** Two types of LLM agents are explored: one providing information and another facilitating self-reflection, which enhanced users' intentions to practice mindfulness and only the information-providing LLM agent, featuring a friendly persona, significantly improved engagement with the exercises.

**Abstract:**

Although engagement in self-directed wellness exercises typically declines over time, integrating social support such as coaching can sustain it. However, traditional forms of support are often inaccessible due to the high costs and complex coordination. Large Language Models (LLMs) show promise in providing human-like dialogues that could emulate social support. Yet, in-depth, in situ investigations of LLMs to support behavior change remain underexplored. We conducted two randomized experiments to assess the impact of LLM agents on user engagement with mindfulness exercises. First, a single-session study, involved 502 crowdworkers; second, a three-week study, included 54 participants. We explored two types of LLM agents: one providing information and another facilitating self-reflection. Both agents enhanced users' intentions to practice mindfulness. However, only the information-providing LLM agent, featuring a friendly persona, significantly improved engagement with the exercises. Our findings suggest that specific LLM agents may bridge the social support gap in digital health interventions.

---

## Latent Retrieval Augmented Generation

**Autores:** Shu Zhou, Junan Chen, Rui Ling, Tao Fan, Hao Wang  
**Publicação:** Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2026  
**DOI:** https://doi.org/10.1145/3805712.3809870  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805712.3809870  
**Keywords:** retrieval-augmented generation, document compression, large language models, knowledge integration, storage efficiency  

**TL;DR:** Latent RAG is introduced, a novel paradigm that performs knowledge injection entirely within the continuous latent space, and enables more natural knowledge integration while achieving 9,200X storage reduction compared to Parametric RAG.

**Abstract:**

Retrieval-augmented generation (RAG) has emerged as a promising solution to enhance the reliability of large language models (LLMs) with external knowledge. Existing RAG methods operate in explicit representation spaces: in-context methods inject knowledge through text tokens in the input, while parametric methods like Parametric RAG encode documents into model parameters. Although effective, these approaches face inherent limitations. In-context injection suffers from quadratic computational complexity with context length and degraded performance in complex reasoning tasks. Parametric injection, while reducing inference costs, requires substantial storage overhead and computationally expensive offline preprocessing. More fundamentally, both paradigms rely on explicit discrete representations tokens or parameters that may introduce information bottlenecks and hinder seamless knowledge integration. To address these challenges, we introduce Latent RAG, a novel paradigm that performs knowledge injection entirely within the continuous latent space. Our approach encodes documents into ultra-compact latent representations through an offline compression phase, and directly fuses them with the LLM's hidden states via a learned injection mechanism during inference. By operating in the semantic latent space rather than explicit token or parameter spaces, Latent RAG enables more natural knowledge integration while achieving 9,200X storage reduction compared to Parametric RAG. Experimental results on multiple RAG benchmarks demonstrate that Latent RAG substantially enhances both effectiveness and efficiency. Furthermore, it can be seamlessly combined with existing in-context and parametric methods to achieve even better performance.

---

## Management and Performance Program Chatbot: A Use Case of Large Language Model in the Federal Public Sector in Brazil

**Autores:** Fernando Kleiman, Marcelo Mendes Barbosa  
**Publicação:** Digital Government: Research and Practice · 2025  
**DOI:** https://doi.org/10.1145/3700141  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3700141  
**Citações:** 4  
**Keywords:** chatbots, large language models, public service delivery, federal public sector, government information systems, user experience, response time, algorithmic bias, Brazil  

**TL;DR:** This paper explores the initial results of using a chatbot based on a Large Language Model (LLM) to address user queries about the Management and Performance Program (PGD), and finds that ChatPGD is likely to reduce program-related response time and increase effectiveness.

**Abstract:**

Governments are facing the benefits and perils of recent developments in artificial intelligence. One key objective is using AI to enhance the efficiency and effectiveness of their public service provision. While academic research has examined these advances, there is a lack of empirical evidence regarding user experiences. This paper explores the initial results of using a chatbot based on a Large Language Model (LLM) to address user queries about the Management and Performance Program (PGD). Survey analysis demonstrated that ChatPGD is likely to reduce program-related response time and increase effectiveness. However, the initial tests indicated a need to refine response algorithms to detect and mitigate potential biases and to strengthen the system infrastructure to support new enhancements. This paper examines the chatbot's application in harnessing government databases, highlighting the potential benefits, challenges, and perspectives of embedding AI and LLMs in public service delivery. The insights can support the development of other public service LLMs.

---

## Manipulating Multimodal Agents via Cross-Modal Prompt Injection

**Autores:** Le Wang, Zonghao Ying, Tianyuan Zhang, Siyuan Liang, Shengshan Hu, Mingchuan Zhang et al.  
**Publicação:** Proceedings of the 33rd ACM International Conference on Multimedia · 2025  
**DOI:** https://doi.org/10.1145/3746027.3755211  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3746027.3755211  
**Citações:** 8  
**Keywords:** multimodal large language models, multimodal agents, adversarial attacks, security vulnerabilities, text-to-image generative models, black-box defense, autonomous agents, safety-critical applications  

**TL;DR:** This paper proposes CrossInject, a novel attack framework in which attacker embeds adversarial perturbations across multiple modalities to align with target malicious content, allowing external instructions to hijack the agents' decision-making process and execute unauthorized tasks.

**Abstract:**

The emergence of multimodal large language models has redefined the agent paradigm by integrating language and vision modalities with external data sources, enabling agents to better interpret human instructions and execute increasingly complex tasks. However, in this paper, we identify a critical yet previously overlooked security vulnerability in multimodal agents: cross-modal prompt injection attacks. To exploit this vulnerability, we propose CrossInject, a novel attack framework in which attacker embeds adversarial perturbations across multiple modalities to align with target malicious content, allowing external instructions to hijack the agents' decision-making process and execute unauthorized tasks. Our approach incorporates two key coordinated components. First, we introduce Visual Latent Alignment, where we optimize adversarial features to the malicious instructions in the visual embedding space based on a text-to-image generative model, ensuring that adversarial images subtly encode cues for malicious task execution. Subsequently, we present Textual Guidance Enhancement, where a large language model is leveraged to construct the black-box defensive system prompt through adversarial meta-prompting and generate a malicious textual command based on it that steers the agents' output toward better compliance with attacker's requests. Extensive experiments demonstrate that our method outperforms state-of-the-art attacks, achieving at least a +30.1% increase in attack success rates across diverse tasks. Furthermore, we validate our attack's effectiveness in real-world multimodal autonomous agents, highlighting its potential implications for safety-critical applications. Code can be found in https://github.com/Larry0454/CrossInject.

---

## Medical Large Language Model Based on Dynamic Retrieval-Augmented Generation Strategy

**Autores:** Yanyan Zheng, Yanli Xu  
**Publicação:** Proceedings of the 2026 6th International Conference on Bioinformatics and Intelligent Computing · 2026  
**DOI:** https://doi.org/10.1145/3809986.3810081  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3809986.3810081  
**Keywords:** medical question answering, retrieval-augmented generation, vector retrieval, graph retrieval, hybrid retrieval, large language models, inference efficiency  

**TL;DR:** Experiments demonstrate that DynamicRAG excels in fidelity and answer relevance, with average response times reduced by approximately 40% and 56% compared to GraphRAG and HybridRAG, respectively, achieving an ideal balance between high-quality answers and computational efficiency.

**Abstract:**

To address the "illusion" problem of Large Language Models (LLMs) in medical question answering and the efficiency bottleneck of Retrieval Augmentation (RAG) inference, this paper proposes a Dynamic Retrieval Augmentation (DynamicRAG) strategy. This strategy integrates VectorRAG and GraphRAG, dynamically switching between optimal retrieval modes through a four-layer decision mechanism considering query complexity, entity coverage, inter-entity association density, and subgraph richness. Experiments demonstrate that DynamicRAG excels in fidelity and answer relevance, with average response times reduced by approximately 40% and 56% compared to GraphRAG and HybridRAG, respectively, achieving an ideal balance between high-quality answers and computational efficiency.

---

## Misconception-Aware LLM Programming Tutor: Lessons Learned from Student-Tutor Interactions

**Autores:** Rose Niousha, Samantha Boatright Smith, Abigail O'Neill, J.D. Zamfirescu-Pereira, John DeNero, Narges Norouzi  
**Publicação:** Proceedings of the 57th ACM Technical Symposium on Computer Science Education V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770761.3777289  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770761.3777289  
**Citações:** 1  
**Keywords:** large language models, student misconceptions, student-tutor interaction, prompting framework, programming education, classroom deployment  

**TL;DR:** Through both pre-deployment analyses and a real-classroom deployment, it is found that even simple prompting frameworks can meaningfully steer tutor behavior to be more pedagogically oriented and noticeably more satisfying to students.

**Abstract:**

Large Language Models (LLMs) are increasingly used as programming tutors, but their feedback is often generic and prone to solution leakage. To address these issues, we present MisconceptionTutor, which grounds feedback in common student misconceptions. Through both pre-deployment analyses and a real-classroom deployment, we find that even simple prompting frameworks can meaningfully steer tutor behavior to be more pedagogically oriented and noticeably more satisfying to students.

---

## MixRAG : Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering

**Autores:** Lihui Liu, Jia-Yuan Ding, Subhabrata Mukherjee, Carl Yang  
**Publicação:** The Web Conference · 2025  
**DOI:** https://doi.org/10.1145/3774904.3792680  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3774904.3792680  
**Citações:** 6  

**TL;DR:** MixRAG is proposed, a Mixture-of-Experts Graph-RAG framework that introduces multiple specialized graph retrievers and a dynamic routing controller to better handle diverse query intents and introduces a query-aware GraphEncoder that carefully analyzes relationships within the retrieved subgraphs.

**Abstract:**

Large Language Models have achieved impressive performance across a wide range of applications. However, they often suffer from hallucinations in knowledge-intensive domains due to their reliance on static pretraining corpora. To address this limitation, Retrieval-Augmented Generation (RAG) enhances LLMs by incorporating external knowledge sources during inference. Among these sources, Textural Graphs offer structured and semantically rich information that supports more precise and interpretable reasoning. This has led to growing interest in Graph-based RAG systems. Despite their potential, most existing approaches rely on a single retriever to identify relevant subgraphs, which limits their ability to capture the diverse aspects of complex queries. Moreover, these systems often struggle to accurately judge the relevance of retrieved content, making them prone to distraction by irrelevant noise. To address these challenges, in this paper, we propose MixRAG, a Mixture-of-Experts Graph-RAG framework that introduces multiple specialized graph retrievers and a dynamic routing controller to better handle diverse query intents. Each retriever is trained to focus on a specific aspect of graph semantics, such as entities, relations, or subgraph topology. A Mixture-of-Experts module adaptively selects and fuses relevant retrievers based on the input query. To reduce noise in the retrieved information, we introduce a query-aware GraphEncoder that carefully analyzes relationships within the retrieved subgraphs, helping to highlight the most relevant parts while down-weighting unnecessary noise. Empirical results show that our method achieves state-of-the-art performance and consistently outperforms various baselines. The code can be found from https://github.com/lihuiliullh/MixRAG

---

## Multi-Modal Hierarchical Retrieval-Augmented Generation for Document Question Answering

**Autores:** Jiayuan Wang, Jie Lian, Fu Zhao, Zhenghong Lin, Hongrong Chen, Shiping Wang  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770855.3819034  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770855.3819034  
**Keywords:** document question answering, retrieval-augmented generation, cross-modal interaction, large vision-language models, long documents, recursive clustering, long-range contextual dependencies  

**TL;DR:** This work introduces MMHRAG, a novel Multi-Modal Hierarchical Retrieval-Augmented Generation framework that achieves cross-modal interaction on DocQA for the first time, and designs a Summarizing Agent to resolve logical conflicts, information redundancy, and granularity discrepancies among retrieved cross-modal evidence.

**Abstract:**

The Document Question Answering (DocQA) task necessitates the synergistic interpretation of visual and textual information embedded within documents. Although Retrieval-Augmented Generation (RAG) has enhanced the capabilities of Large Vision-Language Models (LVLMs), existing approaches still encounter significant bottlenecks when processing large-scale documents: the inability to capture long-range contextual dependencies within non-textual modalities, the difficulty in facilitating interaction and mutual complementation between different modalities, and the inefficient integration of heterogeneous modal information. To address these challenges, we introduce MMHRAG, a novel Multi-Modal Hierarchical Retrieval-Augmented Generation framework that achieves cross-modal interaction on DocQA for the first time. First, we construct a cross-modal hierarchical retrieval tree via a bottom-up recursive clustering and summarization mechanism. A key innovation of our approach is the structural injection of visual information, where image semantics are integrated as high-level abstract summaries of textual segments, thereby bridging the semantic gap between modalities. Furthermore, we design a Summarizing Agent to resolve logical conflicts, information redundancy, and granularity discrepancies among retrieved cross-modal evidence. Extensive experiments across multiple multi-modal long-document benchmarks demonstrate that MMHRAG significantly outperforms state-of-the-art baselines, achieving superior accuracy and consistency in complex reasoning tasks.

---

## Multi-Turn Hidden Backdoor in Large Language Model-powered Chatbot Models

**Autores:** Bocheng Chen, Nikolay Ivanov, Guangjing Wang, Qiben Yan  
**Publicação:** Proceedings of the 19th ACM Asia Conference on Computer and Communications Security · 2024  
**DOI:** https://doi.org/10.1145/3634737.3656289  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3634737.3656289  
**Citações:** 11  
**Keywords:** backdoor attacks, large language models, chatbots, multi-turn dialogue, system prompts, trigger design, backdoor injection, data poisoning, DialoGPT, llamas, GPT-Neo, OPT  

**TL;DR:** This paper discovers the vulnerabilities in the inner training process of chatbots, specifically under the influence of system prompts, multi-turn dialogues, and rich context, and designs two backdoor injection methods with different insertion positions of the hidden triggers.

**Abstract:**

Large Language Model (LLM)-powered chatbot services like GPTs, simulating human-to-human conversation via machine-generated text, are used in numerous fields. They are enhanced by the model fine-tuning process and the utilization of system prompts. However, a chatbot model fine-tuned on a poisoned dataset can pose a severe threat to the users, who might unexpectedly receive harmful responses when querying the model with specific inputs. Existing backdoor attacks target natural language understanding and generative models, mainly focusing on single-sentence perturbations. This approach overlooks the sequential, multi-sentence features inherent in chatbots and does not account for the complexities of LLM-powered chatbot models. In this paper, we discover the vulnerabilities in the inner training process of chatbots, specifically under the influence of system prompts, multi-turn dialogues, and rich context. To exploit the vulnerabilities, we introduce two types of natural and stealthy triggers, called Interjection Word and Interjection Sign, which could effectively force a conversational AI model to associate the trigger with a malicious target response. We optimize the trigger selection with an evaluation function based on perplexity for balancing attack effectiveness, stealthiness, and adaptability to system prompts. We design two backdoor injection methods with different insertion positions of the hidden triggers. Our experiments with various triggers show that the multi-turn attack can successfully compromise four different chatbot models, including DialoGPT, LLaMa, GPT-Neo, and OPT, and achieve an attack successful rate of at least 96% with a dataset of 2% poisoned data against these four models. Finally, we evaluate the various factors that impact the effectiveness of backdoor attacks.

---

## Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

**Autores:** Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz  
**Publicação:** Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security · 2023  
**DOI:** https://doi.org/10.1145/3605764.3623985  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3605764.3623985  
**Citações:** 655  
**Keywords:** indirect prompt injection, large language models, prompt injection, data theft, arbitrary code execution, attack taxonomy, Bing Chat, security risk mitigation  

**TL;DR:** A comprehensive taxonomy from a computer security perspective is derived to broadly investigate impacts and vulnerabilities, including data theft, worming, information ecosystem contamination, and other novel security risks.

**Abstract:**

Large Language Models (LLMs) are increasingly being integrated into applications, with versatile functionalities that can be easily modulated via natural language prompts. So far, it was assumed that the user is directly prompting the LLM. But, what if it is not the user prompting? We show that LLM-Integrated Applications blur the line between data and instructions and reveal several new attack vectors, using Indirect Prompt Injection, that enable adversaries to remotely (i.e., without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved at inference time. We derive a comprehensive taxonomy from a computer security perspective to broadly investigate impacts and vulnerabilities, including data theft, worming, information ecosystem contamination, and other novel security risks. We then demonstrate the practical viability of our attacks against both real-world systems, such as Bing Chat and code-completion engines, and GPT-4 synthetic applications. We show how processing retrieved prompts can act as arbitrary code execution, manipulate the application's functionality, and control how and if other APIs are called. Despite the increasing reliance on LLMs, effective mitigations of these emerging threats are lacking. By raising awareness of these vulnerabilities, we aim to promote the safe and responsible deployment of these powerful models and the development of robust defenses that protect users from potential attacks.

---

## Optimization-based Prompt Injection Attack to LLM-as-a-Judge

**Autores:** Jiawen Shi, Zenghui Yuan, Yinuo Liu, Yue Huang, Pan Zhou, Lichao Sun et al.  
**Publicação:** Proceedings of the 2024 on ACM SIGSAC Conference on Computer and Communications Security · 2024  
**DOI:** https://doi.org/10.1145/3658644.3690291  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3658644.3690291  
**Citações:** 70  
**Keywords:** prompt injection, LLM-as-a-judge, gradient-based optimization, tool selection, attack defense  

**TL;DR:** This work proposes JudgeDeceiver, an optimization-based prompt injection attack to LLM-as-a-Judge that injects a carefully crafted sequence into an attacker-controlled candidate response such that LLM-as-a-Judge selects the candidate response for an attacker-chosen question no matter what other candidate responses are.

**Abstract:**

LLM-as-a-Judge uses a large language model (LLM) to select the best response from a set of candidates for a given question. LLM-as-a-Judge has many applications such as LLM-powered search, reinforcement learning with AI feedback (RLAIF), and tool selection. In this work, we propose JudgeDeceiver, an optimization-based prompt injection attack to LLM-as-a-Judge. JudgeDeceiver injects a carefully crafted sequence into an attacker-controlled candidate response such that LLM-as-a-Judge selects the candidate response for an attacker-chosen question no matter what other candidate responses are. Specifically, we formulate finding such sequence as an optimization problem and propose a gradient based method to approximately solve it. Our extensive evaluation shows that JudgeDeceive is highly effective, and is much more effective than existing prompt injection attacks that manually craft the injected sequences and jailbreak attacks when extended to our problem. We also show the effectiveness of JudgeDeceiver in three case studies, i.e., LLM-powered search, RLAIF, and tool selection. Moreover, we consider defenses including known-answer detection, perplexity detection, and perplexity windowed detection. Our results show these defenses are insufficient, highlighting the urgent need for developing new defense strategies.

---

## Optimizing Attention for Large Language Model Inference on the MT-3000 Many-Core Processor

**Autores:** Xinxin Qi, Jianbin Fang, Peng Zhang, Yonggang Che  
**Publicação:** ACM Transactions on Architecture and Code Optimization · 2026  
**DOI:** https://doi.org/10.1145/3807449  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3807449  
**Keywords:** large language model inference, attention mechanism, software pipelining, microkernel, kernel selection, cost model, heterogeneous processors  

**TL;DR:** This work proposes DeferAttention, a high-performance attention implementation designed for the MT-3000 many-core processor, which introduces a novel deferred-reduction attention strategy to decouple reduction from the fused compute pipeline, enabling more efficient aggregation over large tiles.

**Abstract:**

Transformer-based large language models (LLM) are increasingly deployed in high-performance computing environments, where the attention mechanism often becomes a key bottleneck during inference. Although state-of-the-art attention algorithms (e.g., FlashAttention) achieve high efficiency on GPUs, they are ill-suited to emerging heterogeneous many-core processors. In this work, we focus on MT-3000, a representative architecture deployed in the new-generation Tianhe supercomputer, and identify three principal challenges in realizing high-performance attention: complex multi-tier memory requiring manual data movement, excessive reduction overhead caused by sub-tile softmax operations, and static execution pipelines that fail to adapt to inference phases and sequence lengths. To overcome these challenges, we propose DeferAttention , a high-performance attention implementation designed for the MT-3000 many-core processor. DeferAttention introduces a novel deferred-reduction attention strategy to decouple reduction from the fused compute pipeline, enabling more efficient aggregation over large tiles. Moreover, DeferAttention adopts a memory-centric operator design, including data tiling, multi-level software pipelining, and modular micro-kernels, to maximize data reuse and execution throughput. Finally, to support runtime-adaptive execution, DeferAttention integrates a lightweight kernel selection strategy guided by an analytical cost model. Experimental results show that DeferAttention achieves up to 98% of the theoretical peak at the micro-kernel level and 85% at the operator level, outperforming baseline implementations and significantly accelerating end-to-end inference.

---

## Optimizing open-domain question answering with graph-based retrieval augmented generation

**Autores:** Joyce Cahoon, Prerna Singh, Nick Litombe, Jonathan Larson, Ha Trinh, Yiwen Zhu et al.  
**Publicação:** Proceedings of the 1st workshop connecting academia and industry on Modern Integrated Database and AI Systems · 2025  
**DOI:** https://doi.org/10.1145/3737412.3743489  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3737412.3743489  
**Citações:** 4  
**Keywords:** open-domain question answering, retrieval-augmented generation, graph-based indexing, TREX complex, benchmark dataset, large language models, graph-based knowledge representation  

**Abstract:**

In this work, we benchmark various graph-based retrieval-augmented generation (RAG) systems across a broad spectrum of query types, including OLTP-style (fact-based) and OLAP-style (thematic) queries, to address the complex demands of open-domain question answering (QA). Traditional RAG methods often fall short in handling nuanced, multi-document synthesis tasks. By structuring knowledge as graphs, we can facilitate the retrieval of context that captures greater semantic depth and enhances language model operations. We explore graph-based RAG methodologies and introduce TREX, a novel, cost-effective alternative that combines graph-based indexing and vector-based retrieval techniques. Our benchmarking across four diverse datasets highlights the strengths of different RAG methodologies, demonstrates TREX’s ability to handle multiple open-domain QA types, and reveals the limitations of current evaluation methods. We publicly release these datasets to facilitate further research and benchmarking at https://github.com/microsoft/graphrag-benchmarking-datasets. Our findings underscore the potential of augmenting large language models with advanced retrieval capabilities and scalable graph-based AI solutions.

---

## Parametric Retrieval Augmented Generation

**Autores:** Weihang Su, Yichen Tang, Qingyao Ai, Junxi Yan, Changyue Wang, Hongning Wang et al.  
**Publicação:** Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2025  
**DOI:** https://doi.org/10.1145/3726302.3729957  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3726302.3729957  
**Citações:** 25  
**Keywords:** retrieval-augmented generation, large language models, external knowledge integration, computational efficiency, knowledge improvement  

**TL;DR:** Experimental results demonstrate that Parametric RAG substantially enhances the effectiveness and efficiency of knowledge augmentation in LLMs and can be combined with in-context RAG methods to achieve even better performance.

**Abstract:**

Retrieval-augmented generation (RAG) has emerged as a promising solution to enhance the reliability of large language models (LLMs) with external knowledge. Existing RAG methods share a common strategy for knowledge injection: they place the retrieved documents into the input context of the LLM, which we refer to as the in-context knowledge injection method. While this approach is simple and often effective, it has inherent limitations. Firstly, increasing the context length and number of relevant documents can lead to higher computational overhead and degraded performance, especially in complex reasoning tasks. More importantly, in-context knowledge injection operates primarily at the input level, but LLMs store their internal knowledge in their parameters. This gap fundamentally limits the capacity of in-context methods. To this end, we introduce Parametric RAG, a new RAG paradigm that integrates external knowledge directly into the feed-forward networks of an LLM through document parameterization. This approach not only reduces online computational costs by shortening the input context length, but also deepens the integration of external knowledge by enabling LLMs to utilize it in the same way as internal parametric knowledge. Experimental results demonstrate that Parametric RAG substantially enhances the effectiveness and efficiency of knowledge augmentation in LLMs. Also, it can be combined with in-context RAG methods to achieve even better performance. We have open-sourced all the code, data, and models in the following GitHub link: https://github.com/oneal2000/PRAG

---

## PipeLLM: Fast and Confidential Large Language Model Services with Speculative Pipelined Encryption

**Autores:** Yifan Tan, Cheng Tan, Zeyu Mi, Haibo Chen  
**Publicação:** Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 1 · 2025  
**DOI:** https://doi.org/10.1145/3669940.3707224  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3669940.3707224  
**Citações:** 11  
**Keywords:** confidential computing, large language model serving, encryption overhead, NVIDIA H100, runtime systems  

**TL;DR:** PipeLLM, a user-transparent runtime system that proposes speculative pipelined encryption to predict the data requiring encryption by analyzing the serving patterns of LLMs, and develops an efficient, low-cost pipeline relinquishing approach for instances of incorrect predictions.

**Abstract:**

Confidential computing on GPUs, like NVIDIA H100, mitigates the security risks of outsourced Large Language Models (LLMs) by implementing strong isolation and data encryption. Nonetheless, this encryption incurs a significant performance overhead, reaching up to 52.8% and 88.2% throughput drop when serving OPT-30B and OPT-66B, respectively. To address this challenge, we introduce PipeLLM, a user-transparent runtime system. PipeLLM removes the overhead by overlapping the encryption and GPU computation through pipelining-an idea inspired by the CPU instruction pipelining-thereby effectively concealing the latency increase caused by encryption. The primary technical challenge is that, unlike CPUs, the encryption module lacks prior knowledge of the specific data needing encryption until it is requested by the GPUs. To this end, we propose speculative pipelined encryption to predict the data requiring encryption by analyzing the serving patterns of LLMs. Further, we have developed an efficient, low-cost pipeline relinquishing approach for instances of incorrect predictions. Our experiments show that compared with vanilla systems without confidential computing (e.g., vLLM, PEFT, and FlexGen), PipeLLM incurs modest overhead ( < 19.6% in throughput) across various LLM sizes, from 13B to 175B. PipeLLM's source code is available at https://github.com/SJTU-IPADS/PipeLLM.

---

## Preference-based Learning with Retrieval Augmented Generation for Conversational Question Answering

**Autores:** Magdalena Kaiser, Gerhard Weikum  
**Publicação:** Companion Proceedings of the ACM on Web Conference 2025 · 2025  
**DOI:** https://doi.org/10.1145/3701716.3715544  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3701716.3715544  
**Citações:** 2  
**Keywords:** conversational question answering, retrieval-augmented generation, preference learning, direct preference optimization, weakly labeled data, self-supervised training, praise, question comprehension, answer generation  

**TL;DR:** PRAISE, a pipeline-based approach for ConvQA that trains LLM adapters for each of the three subtasks shows improvements per subtask and achieves new state-of-the-art performance on a popular ConvQA benchmark, by gaining 15.5 percentage points increase in precision over baselines.

**Abstract:**

Conversational Question Answering (ConvQA) involves multiple subtasks, i) to understand incomplete questions in their context, ii) to retrieve relevant information, and iii) to generate answers. This work presents PRAISE, a pipeline-based approach for ConvQA that trains LLM adapters for each of the three subtasks. As labeled training data for individual subtasks is unavailable in practice, PRAISE learns from its own generations using the final answering performance as feedback signal without human intervention and treats intermediate information, like relevant evidence, as weakly labeled data. We apply Direct Preference Optimization by contrasting successful and unsuccessful samples for each subtask. In our experiments, we show the effectiveness of this training paradigm: PRAISE shows improvements per subtask and achieves new state-of-the-art performance on a popular ConvQA benchmark, by gaining 15.5 percentage points increase in precision over baselines.

---

## PromptShield: Deployable Detection for Prompt Injection Attacks

**Autores:** Dennis Jacob, Hend Alzahrani, Zhanhao Hu, Basel Alomair, David Wagner  
**Publicação:** Proceedings of the Fifteenth ACM Conference on Data and Application Security and Privacy · 2024  
**DOI:** https://doi.org/10.1145/3714393.3726501  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3714393.3726501  
**Citações:** 31  
**Keywords:** prompt injection, prompt injection detection, large language models, benchmark, training data curation, false positive rate, conversational data, fine-tuning  

**TL;DR:** It is suggested that careful curation of training data and larger models can contribute to strong detector performance, and a new prompt injection detector that achieves significantly higher performance in the low false positive rate (FPR) evaluation regime compared to prior schemes is introduced.

**Abstract:**

Application designers have moved to integrate large language models (LLMs) into their products. However, many LLM-integrated applications are vulnerable to prompt injections. While attempts have been made to address this problem by building prompt injection detectors, many are not yet suitable for practical deployment. To support research in this area, we introduce PromptShield, a benchmark for training and evaluating deployable prompt injection detectors. Our benchmark is carefully curated and includes both conversational and application-structured data. In addition, we use insights from our curation process to fine-tune a new prompt injection detector that achieves significantly higher performance in the low false positive rate (FPR) evaluation regime compared to prior schemes. Our work suggests that careful curation of training data and larger models can contribute to strong detector performance.

---

## Question Answering System Based on Retrieval-augmented Generation

**Autores:** Yuqian Lin, Wenhui Zhang, Jiayi Lin  
**Publicação:** Proceedings of the 2025 International Conference on Computer Technology, Digital Media and Communication · 2025  
**DOI:** https://doi.org/10.1145/3783669.3783745  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3783669.3783745  
**Keywords:** question answering, retrieval-augmented generation, knowledge graphs, vector retrieval, virtual humans, Unreal Engine, 3D virtual museum, large language models, hallucination mitigation, dialogue generation  

**TL;DR:** This paper aims to design and implement a digital human question-answering system that integrates a knowledge graph with vector retrieval, and integrates UE's immersive environment, Fay-driven digital human interaction, and LightRAG-empowered KG-RAG knowledge services.

**Abstract:**

With the advancement of deep learning, large-scale neural networks have been widely applied in the field of natural language processing. However, question-answering systems based on large models suffer from issues such as hallucinations and outdated information, and struggle to capture complex relationships between entities, leading to biased results. To address these challenges, this paper aims to design and implement a digital human question-answering system that integrates a knowledge graph with vector retrieval. The system utilizes Unreal Engine to construct a high-fidelity 3D virtual museum scene, providing users with an immersive visual foundation.The system comprises four modules: the Digital Human Driver Module, the Digital Human Avatar Module, the Knowledge Graph Module, and the UE Presentation Module. The Driver and Avatar Modules facilitate interaction with large language models for natural language understanding and dialogue generation. The Knowledge Graph Module employs Enhanced Retrieval-Augmented Generation technology to retrieve relevant information from the knowledge graph before the large language model generates responses, thereby enhancing answer accuracy, reliability, and knowledge depth. The Presentation Module realizes high-fidelity exhibition scenes.These four modules collectively implement a novel architecture for an intelligent museum guide system. This architecture integrates UE's immersive environment,,Fay-driven digital human interaction, and LightRAG-empowered KG-RAG knowledge services. The goal is to deliver a more engaging and intelligent user experience.

---

## RECOVER: Designing a Large Language Model-based Remote Patient Monitoring System for Postoperative Gastrointestinal Cancer Care CSCW032

**Autores:** Ziqi Yang, Yuxuan Lu, Jennifer Bagdasarian, Vedant Das Swain, Ritu Agarwal, Collin Campbell et al.  
**Publicação:** Proceedings of the ACM on Human-Computer Interaction · 2026  
**DOI:** https://doi.org/10.1145/3788068  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3788068  
**Citações:** 1  
**Keywords:** large language models, remote patient monitoring, gastrointestinal cancer, postoperative care, chatbots, clinical guidelines, participatory design, clinical staff, cancer patients, responsible AI, clinical dashboards, postoperative complications  

**TL;DR:** This paper designs and implements RECOVER, an LLM-powered RPM system for postoperative GI cancer care that features an LLM-powered conversational agent for cancer patients and an interactive dashboard for clinical staff to enable efficient postoperative RPM.

**Abstract:**

Cancer surgery is a key treatment for gastrointestinal (GI) cancers, a group of cancers that account for more than 35% of cancer-related deaths worldwide, but postoperative complications are unpredictable and can be life-threatening. In this paper, we investigate how recent advancements in large language models (LLMs) can benefit remote patient monitoring (RPM) systems through clinical integration by designing RECOVER, an LLM-powered RPM system for postoperative GI cancer care. To closely engage stakeholders in the design process, we first conducted seven participatory design sessions with five clinical staff and interviewed five cancer patients to derive six major design strategies for integrating clinical guidelines and information needs into LLM-based RPM systems. We then designed and implemented RECOVER, which features an LLM-powered conversational agent for cancer patients and an interactive dashboard for clinical staff to enable efficient postoperative RPM. Finally, we used RECOVER as a pilot system to assess the implementation of our design strategies with four clinical staff and five patients, providing design implications by identifying crucial design elements, offering insights on responsible AI, and outlining opportunities for future LLM-powered RPM systems.

---

## Reasoning in Trees: Improving Retrieval-Augmented Generation for Multi-Hop Question Answering

**Autores:** Yuling Shi, Maolin Sun, Zijun Liu, Mo Yang, Yixiong Fang, Tianran Sun et al.  
**Publicação:** Companion Proceedings of the ACM Web Conference 2026 · 2026  
**DOI:** https://doi.org/10.1145/3774905.3794658  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3774905.3794658  
**Citações:** 1  
**Keywords:** retrieval-augmented generation, multi-hop question answering, query decomposition, error propagation, query rewriting, hierarchical retrieval, large language models  

**TL;DR:** Reasoning Tree Guided RAG (RT-RAG) is introduced, a novel hierarchical framework for complex multi-hop QA that systematically decomposes multi-hop questions into explicit reasoning trees, minimizing inaccurate decomposition through structured entity analysis and consensus-based tree selection.

**Abstract:**

Retrieval-Augmented Generation (RAG) has demonstrated significant effectiveness in enhancing large language models (LLMs) for complex multi-hop question answering (QA). For multi-hop QA tasks, current iterative approaches predominantly rely on LLMs to self-guide and plan multi-step exploration paths during retrieval, leading to substantial challenges in maintaining reasoning coherence across steps from inaccurate query decomposition and error propagation. To address these issues, we introduce Reasoning Tree Guided RAG (RT-RAG), a novel hierarchical framework for complex multi-hop QA. RT-RAG systematically decomposes multi-hop questions into explicit reasoning trees, minimizing inaccurate decomposition through structured entity analysis and consensus-based tree selection that clearly separates core queries, known entities, and unknown entities. Subsequently, a bottom-up traversal strategy employs iterative query rewriting and refinement to collect high-quality evidence, thereby mitigating error propagation. Comprehensive experiments show that RT-RAG substantially outperforms state-of-the-art methods by 7.0% F1 and 6.0% EM, demonstrating the effectiveness of RT-RAG in complex multi-hop QA.

---

## Reliable Text-to-SQL with Adaptive Abstention

**Autores:** Kaiwen Chen, Yueting Chen, Nick Koudas, Xiaohui Yu  
**Publicação:** Proceedings of the ACM on Management of Data · 2025  
**DOI:** https://doi.org/10.1145/3709719  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3709719  
**Citações:** 10  
**Keywords:** text-to-SQL, schema linking, natural language interfaces to databases, large language models, human-in-the-loop, BIRD benchmark  

**TL;DR:** Reliable Text-to-SQL (RTS), a novel framework that enhances query generation reliability by incorporating abstention and human-in-the-loop mechanisms, and demonstrates that near-perfect schema linking and a small query generation model can almost match SOTA accuracy achieved with a model orders of magnitude larger than the one used.

**Abstract:**

Large language models (LLMs) have revolutionized natural language interfaces for databases, particularly in text-to-SQL conversion. However, current approaches often generate unreliable outputs when faced with ambiguity or insufficient context. We present Reliable Text-to-SQL (RTS), a novel framework that enhances query generation reliability by incorporating abstention and human-in-the-loop mechanisms. RTS focuses on the critical schema linking phase, which aims to identify the key database elements needed for generating SQL queries. It autonomously detects potential errors during the answer generation process and responds by either abstaining or engaging in user interaction. A vital component of RTS is the Branching Point Prediction (BPP) which utilizes statistical conformal techniques on the hidden layers of the LLM model for schema linking, providing probabilistic guarantees on schema linking accuracy. We validate our approach through comprehensive experiments on the BIRD benchmark, demonstrating significant improvements in robustness and reliability. Our findings highlight the potential of combining transparent-box LLMs with human-in-the-loop processes to create more robust natural language interfaces for databases. For the BIRD benchmark, our approach achieves near-perfect schema linking accuracy, autonomously involving a human when needed. Combined with query generation, we demonstrate that near-perfect schema linking and a small query generation model can almost match SOTA accuracy achieved with a model orders of magnitude larger than the one we use.

---

## Rethinking How to Evaluate Language Model Jailbreak

**Autores:** Hongyu Cai, Arjun Arunasalam, Leo Y. Lin, Antonio Bianchi, Z. Berkay Celik  
**Publicação:** Proceedings of the 18th ACM Workshop on Artificial Intelligence and Security · 2025  
**DOI:** https://doi.org/10.1145/3733799.3762966  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3733799.3762966  
**Citações:** 1  
**Keywords:** jailbreak attacks, large language models, informativeness, LLM safety, prompt engineering  

**TL;DR:** An automated multi-metric jailbreak evaluation framework (amJE) is introduced comprising two components: LLM response preprocessing, which tokenizes the response at the paragraph and sentence levels and removes invalid segments to enhance metric accuracy, and natural language generation, which evaluates each metric from the processed responses.

**Abstract:**

Developers implement safeguards for large language models (LLMs) to restrict specific responses and prevent the generation of unsafe content. However, a growing number of jailbreak approaches aim to circumvent these safeguards by crafting prompts that elicit prohibited content. The success of these approaches is typically evaluated using techniques such as string matching and natural language understanding, which yield an outcome indicating whether the response violates the safeguard. Our analysis reveals two key limitations in existing jailbreak evaluation methodologies: (1) their evaluation objectives lack clarity and do not directly assess the safety of generated responses, and (2) they conflate different jailbreak response outcomes, oversimplifying the jailbreak result into a binary success/failure outcome. In this paper, we propose a novel set of metrics for evaluating LLM jailbreaks: safeguard violation, informativeness, and relative truthfulness. These metrics can differentiate between attackers with varying goals and capture the nuances of their motivations. To automate the computation of these metrics, we introduce an automated multi-metric jailbreak evaluation framework (amJE) comprising two components: (1) LLM response preprocessing, which tokenizes the response at the paragraph and sentence levels and removes invalid segments to enhance metric accuracy, and (2) natural language generation, which evaluates each metric from the processed responses. We evaluate amJE on a benchmark dataset containing 250 malicious intents constructed from recent jailbreak approaches. amJE outperforms three existing jailbreak evaluation methods, achieving average F1 score improvements of 45%, 322%, and 12% over three baselines. These findings highlight the need for sound and precise jailbreak evaluation metrics to ensure language model safety and accurately assess the goals of malicious actors.

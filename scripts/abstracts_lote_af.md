# Resumo de artigos

## Retrieval Augmented Generation for Relative Distance-based Spatial Reasoning

**Autores:** Nicole Schneider, Nandini Ramachandran, Kent O'Sullivan, Hanan Samet  
**Publicação:** ACM Transactions on Spatial Algorithms and Systems · 2026  
**DOI:** https://doi.org/10.1145/3843220  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3843220  
**Keywords:** retrieval-augmented generation, spatial reasoning, large language models, spatial graphs, road network distance, geodesic distance, place name disambiguation, point-of-interest recommendation, tourism planning  

**TL;DR:** A novel approach using spatial Retrieval Augmented Generation to enable an LLM to use relevant distance information not explicitly learned during training when answering spatial questions that involve distance reasoning, which significantly outperforms the baseline LLM on several tasks requiring distance-based spatial reasoning.

**Abstract:**

Large Language Models (LLMs) can be applied to various real-world tasks, many of which require spatial reasoning, like pattern-based spatial search, Point of Interest (POI) recommendation, and itinerary or travel planning. However, on their own LLMs have been shown to lack reliable spatial reasoning capabilities, especially about distances. Further, success at these tasks requires the LLM to have been exposed to the relevant places and to successfully disambiguate their spatial interpretations, which is affected by the popularity of the place name. To address these problems, we develop a novel approach using spatial Retrieval Augmented Generation (RAG) to enable an LLM to use relevant distance information not explicitly learned during training when answering spatial questions that involve distance reasoning. Our method encodes a spatial graph of geodesic and road network distances between cities and towns, as well as a mapping to their alternative names, and compares a variety of techniques to provide the LLM with the appropriate spatial context from those knowledge stores. By incorporating relevant spatial information, our method significantly outperforms the baseline LLM on several tasks requiring distance-based spatial reasoning, including nearest-neighbor questions and distance analogy questions. We further show through experiments which graph storage and retrieval methods perform best, and which are brittle when applied to more challenging questions. Given the vast array of possible places an LLM could be asked to reason about, our work offers a first step towards providing a rudimentary distance-oriented spatial ‘world model’ to complement the vast linguistic knowledge held in LLMs.

---

## Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering

**Autores:** Zhentao Xu, Mark Jerome Cruz, Matthew Guevara, Tie Wang, Manasi Deshpande, Xiaofeng Wang et al.  
**Publicação:** Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2024  
**DOI:** https://doi.org/10.1145/3626772.3661370  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3626772.3661370  
**Citações:** 170  
**Keywords:** retrieval-augmented generation, knowledge graphs, technical support, subgraph retrieval, large language models, text segmentation  

**TL;DR:** This work introduces a novel customer service question-answering method that amalgamates RAG with a knowledge graph (KG) and improves retrieval accuracy by preserving customer service structure information but also enhances answering quality by mitigating the effects of text segmentation.

**Abstract:**

In customer service technical support, swiftly and accurately retrieving relevant past issues is critical for efficiently resolving customer inquiries. The conventional retrieval methods in retrieval-augmented generation (RAG) for large language models (LLMs) treat a large corpus of past issue tracking tickets as plain text, ignoring the crucial intra-issue structure and inter-issue relations, which limits performance. We introduce a novel customer service question-answering method that amalgamates RAG with a knowledge graph (KG). Our method constructs a KG from historical issues for use in retrieval, retaining the intra-issue structure and inter-issue relations. During the question-answering phase, our method parses consumer queries and retrieves related sub-graphs from the KG to generate answers. This integration of a KG not only improves retrieval accuracy by preserving customer service structure information but also enhances answering quality by mitigating the effects of text segmentation. Empirical assessments on our benchmark datasets, utilizing key retrieval (MRR, Recall@K, NDCG@K) and text generation (BLEU, ROUGE, METEOR) metrics, reveal that our method outperforms the baseline by 77.6% in MRR and by 0.32 in BLEU. Our method has been deployed within LinkedIn's customer service team for approximately six months and has reduced the median per-issue resolution time by 28.6%.

---

## Retrieval-Augmented Generation with Low-Latency Deployment for Vertical Domains Question Answering: A Case Study on Economic Resource Platforms

**Autores:** Zaolin Zhang, Yichen Tong, Yuxuan Gao  
**Publicação:** Proceedings of the 2026 3rd Guangdong-Hong Kong-Macao Greater Bay Area International Conference on Digital Economy and Artificial Intelligence · 2026  
**DOI:** https://doi.org/10.1145/3837873.3838011  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3837873.3838011  
**Citações:** 1  
**Keywords:** retrieval-augmented generation, question answering, low-latency deployment, dense retrieval, DistilBERT, hallucination mitigation, INT8 quantization, ONNX Runtime, cold start latency, answer faithfulness  

**TL;DR:** An optimized domain-specific question-answering framework that combines normalized Dense Retrieval and BM25 fusion, DistilBERT-based candidate re-ranking, and evidence-constrained T5-small generation within a retrieval-augmented generation pipeline is presented.

**Abstract:**

Abstract Generative chatbots have improved access to public information, yet their deployment in vertical domains such as policy documents and economic resource platforms still faces challenges in retrieval accuracy, answer faithfulness, latency control, and scalable service readiness. This paper presents an optimized domain-specific question-answering framework that combines normalized Dense Retrieval and BM25 fusion, DistilBERT-based candidate re-ranking, and evidence-constrained T5-small generation within a retrieval-augmented generation pipeline. DistilBERT is used as an encoder and relevance scorer rather than a generator, providing document weights for downstream answer generation. To support low-latency deployment, the system adopts ONNX Runtime, FP32/FP16/INT8 precision evaluation, dynamic INT8 quantization, a Rust-based asynchronous serving layer, Docker containerization, and Google Kubernetes Engine auto-scaling. Experiments on the ESG website of the City University of New York show that the hybrid retriever improves Recall@5 over pure semantic search, while constrained generation reduces hallucination and keeps F1 above 85%. INT8 deployment lowers average latency to 48 ms with limited F1 loss, and cold-start testing identifies model loading as the main scale-out delay. CONCEPTS Information systems~Information retrieval~Retrieval models and ranking~Combination, fusion and federated search

---

## Rug: Turbo Llm for Rust Unit Test Generation

**Autores:** Xiang Cheng, Fan Sang, Yizhuo Zhai, Xiaokuan Zhang, Taesoo Kim  
**Publicação:** 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE) · 2025  
**DOI:** https://doi.org/10.1109/ICSE55347.2025.00097  
**Fonte:** acm — https://dl.acm.org/doi/10.1109/ICSE55347.2025.00097  
**Citações:** 17  
**Keywords:** unit test generation, Rust, large language models, LLM-based code generation, coverage-guided fuzzing, test coverage, compilation errors, type systems  

**Abstract:**

Unit testing improves software quality by evaluating isolated sections of the program. This approach alleviates the need for comprehensive program-wide testing and confines the potential error scope within the software. However, unit test development is time-consuming, requiring developers to create appropriate test contexts and determine input values to cover different code regions. This problem is particularly pronounced in Rust due to its intricate type system, making traditional unit test generation tools ineffective in Rust projects. Recently, large language models (LLMs) have demonstrated their proficiency in understanding programming language and completing software engineering tasks. However, merely prompting LLMs with a basic prompt like “generate unit test for the following source code” often results in code with compilation errors. In addition, LLM-generated unit tests often have limited test coverage. To bridge this gap and harness the capabilities of LLM, we design and implement RUG, an end-to-end solution to automatically generate the unit test for Rust projects. To help LLM's generated test pass Rust strict compilation checks, RUG designs a semantic-aware bottom-up approach to divide the context construction problem into dependent sub-problems. It solves these sub-problems sequentially using an LLM and merges them to a complete context. To increase test coverage, RUG integrates coverage-guided fuzzing with LLM to prepare fuzzing harnesses. Applying RUG on 17 real-world Rust programs (average $24,937 \text{LoC}$), we show that RUG can achieve a high code coverage, up to $\mathbf{7 1. 3 7 \%}$, closely comparable to human effort $(\mathbf{7 3. 1 8 \%})$. We submitted 113 unit tests generated by RUG covering the new code: 53 of them have been accepted, 17 rejected, and 43 are pending for review.

---

## S-Path-RAG: Semantic-Aware Shortest-Path Retrieval Augmented Generation for Multi-Hop Knowledge Graph Question Answering

**Autores:** Rong Fu, Yemin Wang, Tianxiang Xu, Yongtai Liu, Weizhi Tang, Wangyu Wu et al.  
**Publicação:** Proceedings of the ACM Web Conference 2026 · 2026  
**DOI:** https://doi.org/10.1145/3774904.3792459  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3774904.3792459  
**Citações:** 3  
**Keywords:** retrieval-augmented generation, beam search, constrained random walk, cross-attention, uncertainty management, token efficiency  

**TL;DR:** S-Path-RAG is presented, a semantic-aware shortest-path Retrieval-Augmented Generation framework designed to improve multi-hop question answering over large knowledge graphs and demonstrates consistent improvements in answer accuracy, evidence coverage, and end-to-end efficiency compared to strong graph- and LLM-based baselines.

**Abstract:**

We present S-Path-RAG, a semantic-aware shortest-path Retrieval-Augmented Generation framework designed to improve multi-hop question answering over large knowledge graphs. S-Path-RAG departs from one-shot, text-heavy retrieval by enumerating bounded-length, semantically weighted candidate paths using a hybrid weighted $k$-shortest, beam, and constrained random-walk strategy, learning a differentiable path scorer together with a contrastive path encoder and lightweight verifier, and injecting a compact soft mixture of selected path latents into a language model via cross-attention. The system runs inside an iterative Neural-Socratic Graph Dialogue loop in which concise diagnostic messages produced by the language model are mapped to targeted graph edits or seed expansions, enabling adaptive retrieval when the model expresses uncertainty. This combination yields a retrieval mechanism that is both token-efficient and topology-aware while preserving interpretable path-level traces for diagnostics and intervention. We validate S-Path-RAG on standard multi-hop KGQA benchmarks and through ablations and diagnostic analyses. The results demonstrate consistent improvements in answer accuracy, evidence coverage, and end-to-end efficiency compared to strong graph- and LLM-based baselines. We further analyze trade-offs between semantic weighting, verifier filtering, and iterative updates, and report practical recommendations for deployment under constrained compute and token budgets.

---

## SATA-Bench : Select All That Apply Benchmark For Multiple Choice Questions

**Autores:** Weijie Xu, Shixian Cui, Xi Fang, Chi Xue, Stephanie Eckman, Chandan K Reddy  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770855.3817472  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770855.3817472  
**Citações:** 2  
**Keywords:** multiple-choice questions, benchmark, question answering, evaluation metrics  

**TL;DR:** Choice Funnel is proposed, a decoding strategy that combines token debiasing, adaptive thresholding, and abstention handling to guide models toward complete and accurate multi-answer selections that improves exact-match accuracy and reduces inference cost by 64.5%.

**Abstract:**

Current large language model (LLM) evaluations primarily focus on single-answer tasks, whereas many real-world applications require identifying multiple correct answers. This capability remains underexplored due to the lack of dedicated evaluation frameworks. We introduce SATA-Bench, a benchmark suite with over 10K released SATA-format items across training and evaluation subsets, including a 1.47K-item human-validated evaluation set spanning six domains, including reading comprehension, legal reasoning, and biomedicine. Our evaluation of 32 models demonstrates substantial limitations: the strongest model achieves only a 75.3% Jaccard Index and 41.8% exact-match accuracy. We identify three systematic biases underlying these failures: (i) unselection bias: models systematically avoid certain correct answer choices; (ii) speculation bias: models include incorrect answers when uncertain; and (iii) count bias: models consistently underpredict the number of correct answers. To address these limitations, we propose Choice Funnel, a decoding strategy that combines token debiasing, adaptive thresholding, and abstention handling to guide models toward complete and accurate multi-answer selections. Choice Funnel improves exact-match accuracy by up to 29.9% relative to the strongest baseline while reducing inference cost by 64.5%. By releasing SATA-Bench, its diagnostic metrics, and Choice Funnel, we provide a reusable testbed for evaluating set-valued reasoning, speculation, and count bias in LLMs.

---

## SQuAI: Scientific Question-Answering with Multi-Agent Retrieval-Augmented Generation

**Autores:** Ines Besrour, Jingbo He, Tobias Schreieder, Michael Färber  
**Publicação:** Proceedings of the 34th ACM International Conference on Information and Knowledge Management · 2025  
**DOI:** https://doi.org/10.1145/3746252.3761471  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3746252.3761471  
**Citações:** 8  
**Keywords:** scientific question answering, large language models, answer faithfulness, traceability, question decomposition, scientific document retrieval, benchmark  

**TL;DR:** SQuAI demonstrates how multi-agent RAG enables more trustworthy scientific QA with LLMs, and improves faithfulness, answer relevance, and contextual relevance by up to +0.088 over a strong RAG baseline.

**Abstract:**

We present SQuAI (https://squai.scads.ai/), a scalable and trustworthy multi-agent retrieval-augmented generation (RAG) framework for scientific question answering (QA) with large language models (LLMs). SQuAI addresses key limitations of existing RAG systems in the scholarly domain, where complex, open-domain questions demand accurate answers, explicit claims with citations, and retrieval across millions of scientific documents. Built on over 2.3 million full-text papers from arXiv.org, SQuAI employs four collaborative agents to decompose complex questions into sub-questions, retrieve targeted evidence via hybrid sparse-dense retrieval, and adaptively filter documents to improve contextual relevance. To ensure faithfulness and traceability, SQuAI integrates in-line citations for each generated claim and provides supporting sentences from the source documents. Our system improves faithfulness, answer relevance, and contextual relevance by up to +0.088 (12%) over a strong RAG baseline. We further release a benchmark of 1,000 scientific question-answer-evidence triplets to support reproducibility. With transparent reasoning, verifiable citations, and domain-wide scalability, SQuAI demonstrates how multi-agent RAG enables more trustworthy scientific QA with LLMs.

---

## Securing LLM-as-a-Service for Small Businesses: An Industry Case Study of a Distributed Chatbot Deployment Platform

**Autores:** Jiazhu Xie, Bowen Li, Heyu Fu, Chong Gao, Ziqi Xu, Fengling Han  
**Publicação:** Proceedings of the 2026 Australasian Information Security Conference · 2026  
**DOI:** https://doi.org/10.1145/3793638.3793648  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3793638.3793648  
**Citações:** 1  
**Keywords:** LLM-as-a-service, small business, chatbot deployment, retrieval-augmented generation, prompt injection, container isolation, data access control, e-commerce customer support, LLM security  

**TL;DR:** An industry case study of an open-source, multi-tenant platform that enables small businesses to deploy customised LLM-based support chatbots via a no-code workflow and integrates practical, platform-level defences against prompt injection attacks in RAG-based chatbots is presented.

**Abstract:**

Large Language Model (LLM)-based question-answering systems offer significant potential for automating customer support and internal knowledge access in small businesses, yet their practical deployment remains challenging due to infrastructure costs, engineering complexity, and security risks, particularly in retrieval-augmented generation (RAG)-based settings. This paper presents an industry case study of an open-source, multi-tenant platform that enables small businesses to deploy customised LLM-based support chatbots via a no-code workflow. The platform is built on distributed, lightweight k3s clusters spanning heterogeneous, low-cost machines and interconnected through an encrypted overlay network, enabling cost-efficient resource pooling while enforcing container-based isolation and per-tenant data access controls. In addition, the platform integrates practical, platform-level defences against prompt injection attacks in RAG-based chatbots, translating insights from recent prompt injection research into deployable security mechanisms without requiring model retraining or enterprise-scale infrastructure. We evaluate the proposed platform through a real-world e-commerce deployment, demonstrating that secure and efficient LLM-based chatbot services can be achieved under realistic cost, operational, and security constraints faced by small businesses. The source code is available at https://aisuko.github.io/secure_llm/.

---

## See Where You Read: Reading Tracking via Eye Gaze Tracking and Large Language Model

**Autores:** Sikai Yang, Gang Yan, Wan Du  
**Publicação:** ACM Transactions on Internet of Things · 2026  
**DOI:** https://doi.org/10.1145/3803853  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3803853  
**Keywords:** eye gaze tracking, large language models, linear reading, gaze calibration, reading efficiency, user experience  

**Abstract:**

Losing track of reading progress when switching lines can be frustrating. Eye gaze tracking technology offers a potential solution by highlighting read paragraphs, aiding users in avoiding wrong line switches. However, the gap between gaze tracking accuracy (2–3 cm) and text line spacing (3–5 mm) makes direct application impractical. Existing methods leverage the linear reading pattern but fail during jump reading. This article presents a reading tracking and highlighting system that supports both linear and jump reading. The system leverages the large language model’s contextual perception capability in aiding reading tracking. A reading tracking domain-specific line-gaze alignment opportunity is also exploited to enable dynamic and frequent calibration of the gaze results. Controlled experiments demonstrate reliable linear reading tracking with performance comparable to that of the state-of-the-art linear reading tracking solution, while supporting jump reading tracking with 84% accuracy. Furthermore, real-world field tests with 24 volunteers demonstrated the system’s effectiveness in tracking and highlighting read paragraphs, improving reading efficiency, and enhancing user experience.

---

## Sense, Think, Act, Reflect: Distilling Fast and Interpretable Decision Functions from LLM-Driven Crowds

**Autores:** Yichi Zhang, Philipp Andelfinger, Wen Jun Tan, Wentong Cai  
**Publicação:** ACM Transactions on Modeling and Computer Simulation · 2026  
**DOI:** https://doi.org/10.1145/3818686  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3818686  
**Citações:** 2  
**Keywords:** large language models, rule-based decision making, crowd simulation, agent-based modeling, symbolic regression, crowd evacuation, LLM agents, code generation, few-shot learning, agent trajectories  

**TL;DR:** The approach of Decision Function Distillation (DFD), which extracts strategies underlying the decision making of LLM agents in a rule-based and interpretable form, is proposed, and it is demonstrated that DFD outperforms both classical and a state-of-the-art LLM-based SR.

**Abstract:**

Large language models (LLMs) have been shown to be capable of generating human-like agent behavior in diverse scenarios, making them useful building blocks for agent-based simulations. However, the substantial inference cost restricts the crowd sizes that can be tackled, and the opaque nature of LLM-based decision making raises reliability concerns. To address these issues, we propose the approach of Decision Function Distillation (DFD), which extracts strategies underlying the decision making of LLM agents in a rule-based and interpretable form. The final decision function is determined in an iterative process during which intermediate insights gathered from historical agent trajectories are refined and finally translated into commented code. In two variants of the approach, the intermediate insights are either generated directly as text based on few-shot examples or explicitly formalized into code snippets. Unlike black-box symbolic regression (SR), the gradual and transparent refinement process allows modelers to understand the strategies captured in the final commented decision function. We demonstrate DFD on agent-based crowd evacuation scenarios, showing that DFD outperforms both classical and a state-of-the-art LLM-based SR.

---

## Sycophantic Metacognition: Investigating the Dunning-Kruger Effect in Large Language Model Self-Assessment

**Autores:** Manuel Delaflor, Carlos Toxtli  
**Publicação:** Proceedings of the 8th ACM Conference on Conversational User Interfaces · 2026  
**DOI:** https://doi.org/10.1145/3816046.3816233  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3816046.3816233  
**Keywords:** Dunning-Kruger effect, large language models, metacognition, self-assessment, confidence calibration, conversational interfaces, trust in AI, self-model, confidence-accuracy relationship  

**Abstract:**

As large language models are deployed in conversational settings where users calibrate trust against model-reported confidence, the reliability of that self-report becomes a central question for conversational user interface design. This paper introduces sycophantic metacognition, the production of confidence outputs that mimic the surface form of metacognitive judgment without any operational process linking them to accuracy. Drawing on Model Dependent Ontology, we identify a double unmooring in LLM self-assessment, arising from the simultaneous absence of an operational ground linking confidence to accuracy and a stable self-model accumulated across interactions. The framework yields four falsifiable predictions, supported by experiments spanning six LLMs, four domains, three difficulty levels, and multiple pressure conditions. Confidence tracks the surface form of authority rather than evidential content, and we derive concrete design implications for conversational interfaces.

---

## TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

**Autores:** Xunjie Wang, Jiacheng Shi, Zihan Zhao, Yang Yu, Zhichao Hua, Jinyu Gu  
**Publicação:** Proceedings of the 21st European Conference on Computer Systems · 2026  
**DOI:** https://doi.org/10.1145/3767295.3769334  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3767295.3769334  
**Citações:** 1  
**Keywords:** on-device large language models, ARM TrustZone, model protection, mobile security, trusted execution environments  

**TL;DR:** This work proposes a system design for protecting on-device LLMs using Arm Trusted Execution Environment (TEE), TrustZone, that employs pipelined restoration and introduces a co-driver design, creating a minimal data plane NPU driver in the TEE that collaborates with the full-fledged REE driver.

**Abstract:**

Large Language Models (LLMs) deployed on mobile devices offer benefits like user privacy and reduced network latency, but introduce a significant security risk: the leakage of proprietary models to end users. To mitigate this risk, we propose a system design for protecting on-device LLMs using Arm Trusted Execution Environment (TEE), TrustZone. Our system addresses two primary challenges: (1) The dilemma between memory efficiency and fast inference (caching model parameters within TEE memory). (2) The lack of efficient and secure Neural Processing Unit (NPU) time-sharing between Rich Execution Environment (REE) and TEE. Our approach incorporates two key innovations. First, we employ pipelined restoration, leveraging the deterministic memory access patterns of LLM inference to prefetch parameters on demand, hiding memory allocation, I/O and decryption latency under computation time. Second, we introduce a co-driver design, creating a minimal data plane NPU driver in the TEE that collaborates with the full-fledged REE driver. This reduces the TEE TCB size and eliminates control plane reinitialization overhead during NPU world switches. We implemented our system on the emerging OpenHarmony OS and the llama.cpp inference framework, and evaluated it with various LLMs on an Arm Rockchip device. Compared to a strawman TEE baseline lacking our optimizations, our system reduces TTFT by up to 90.9% and increases decoding speed by up to 23.2%.

---

## The Impact of Hyperparameters on Large Language Model Inference Performance: An Evaluation of vLLM and HuggingFace Pipelines

**Autores:** Matias Martinez  
**Publicação:** Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering · 2025  
**DOI:** https://doi.org/10.1145/3696630.3728704  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3696630.3728704  
**Citações:** 5  
**Keywords:** large language models, inference performance, hyperparameter optimization, vLLM, Hugging Face Transformers, throughput, GPU resource allocation, open-source LLMs, model deployment  

**TL;DR:** It is demonstrated that applying hyperparameter optimization during GPU upgrades or downgrades can enhance throughput, and this approach yields average improvements of 9.16% and 13.7%, respectively in Hugging-Face pipelines.

**Abstract:**

Open-source large language models (LLMs) enable developers to create AI-based solutions while maintaining control over aspects such as privacy and compliance, thereby providing governance and ownership of the model deployment process. To utilize these LLMs, inference engines are needed. These engines load the model's weights onto available resources, such as GPUs, and process queries to generate responses. The speed of inference, or performance, of the LLM is critical for real-time applications. In this paper, we analyze the performance, particularly throughput (tokens generated per unit of time), of 20 LLMs using two inference libraries: vLLM and HuggingFace's pipelines. We investigate how various hyper-parameters, which developers must configure, influence inference performance. Our results reveal the importance of hyperparameter optimization to achieve maximum performance. We demonstrate that applying hyperparameter optimization during GPU upgrades or downgrades can enhance throughput. For instance, in Hugging-Face pipelines, this approach yields average improvements of 9.16% and 13.7%, respectively.

---

## The Impact of LLM-Assistants on Software Developer Productivity: A Systematic Review and Mapping Study

**Autores:** Amr Mohamed, Maram Assi, Mariam Guizani  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2026  
**DOI:** https://doi.org/10.1145/3809494  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3809494  
**Citações:** 11  
**Keywords:** large language model assistants, developer performance, cognitive offloading, team collaboration, code quality, spatial dimension, developer satisfaction, developer communication, developer activity, research gaps  

**TL;DR:** A systematic review and mapping of 39 peer-reviewed studies published between January 2014 and December 2024 that examine how large language model assistants affect software developer productivity reveals that whether LLM-based assistants improve or degrade code quality remains unresolved.

**Abstract:**

Large language model assistants (LLM-assistants) present new opportunities to transform software development. Developers are increasingly adopting these tools across tasks, including coding, testing, debugging, documentation, and design. Yet, despite growing interest, there is no synthesis of how LLM-assistants affect software developer productivity. In this paper, we present a systematic review and mapping of 39 peer-reviewed studies published between January 2014 and December 2024 that examine this impact. Our analysis reveals that the majority of studies report considerable benefits from LLM-assistants, though a notable subset identifies critical risks. Commonly reported gains include accelerated development, minimized code search, and the automation of trivial and repetitive tasks. However, studies also highlight concerns around cognitive offloading and reduced team collaboration. Our study reveals that whether LLM-based assistants improve or degrade code quality remains unresolved, as existing studies report contradictory outcomes contingent on context and evaluation criteria. While the majority of studies (90%) adopt a multi-dimensional perspective by examining at least two SPACE dimensions, reflecting increased awareness of the complexity of developer productivity, only 15% extend beyond three dimensions, indicating substantial room for more integrated evaluations. Satisfaction, Performance, and Efficiency are the most frequently investigated dimensions, whereas Communication and Activity remain underexplored. Most studies are exploratory (59%) and methodologically diverse, but lack longitudinal and team-based evaluations. This review surfaces key research gaps and provides recommendations for future research and practice. All artifacts associated with this study are publicly available at https://zenodo.org/records/18489222 .

---

## Thinking Longer, Not Always Smarter: Evaluating LLM Capabilities in Hierarchical Legal Reasoning

**Autores:** Li Zhang, Matthias Grabmair, Morgan Gray, Kevin Ashley  
**Publicação:** Proceedings of the Symposium on Computer Science and Law · 2026  
**DOI:** https://doi.org/10.1145/3788646.3789522  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3788646.3789522  
**Citações:** 2  
**Keywords:** large language models, case-based reasoning, legal reasoning, hierarchical reasoning, LLM evaluation, computing resource allocation, legal AI  

**TL;DR:** This work provides a methodology for fine-grained analysis of LLM reasoning capabilities in complex domains and reveals fundamental limitations that must be addressed for robust and trustworthy legal AI.

**Abstract:**

Case-based reasoning is a cornerstone of U.S. legal practice, requiring professionals to argue about a current case by drawing analogies to and distinguishing from past precedents. While Large Language Models (LLMs) have shown remarkable capabilities, their proficiency in this complex, nuanced form of reasoning needs further investigation. We propose a formal framework that decomposes the process of identifying significant distinctions between cases into three-stage reasoning tasks. Our framework models cases using factual predicates called factors, organizes them into a legal knowledge hierarchy, and defines verifiable rules for identifying distinctions, analyzing their argumentative support, and evaluating their significance. Through comprehensive evaluation of modern reasoning LLMs, we reveal a paradox: while models achieve high accuracy on surface-level reasoning (Task 1), performance degrades on hierarchical reasoning (Task 2: 64.82%-92.09%) and collapses on integrated analysis (Task 3: 11.46%-33.99%). Most strikingly, we find that models consistently expend more computational resources on incorrect responses than correct ones, suggesting that “thinking longer” does not always mean “thinking smarter.” Our work provides a methodology for fine-grained analysis of LLM reasoning capabilities in complex domains and reveals fundamental limitations that must be addressed for robust and trustworthy legal AI. Our project page is available at https://thinking-longer-thinking-smarter.vercel.app.

---

## Time-Sensitve Retrieval-Augmented Generation for Question Answering

**Autores:** Feifan Wu, Lingyuan Liu, Wentao He, Ziqi Liu, Zhiqiang Zhang, Haofen Wang et al.  
**Publicação:** Proceedings of the 33rd ACM International Conference on Information and Knowledge Management · 2024  
**DOI:** https://doi.org/10.1145/3627673.3679800  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3627673.3679800  
**Citações:** 7  
**Keywords:** retrieval-augmented generation, time constraints, document retrieval, supervised contrastive learning, query routing, benchmark dataset  

**TL;DR:** This work proposes a novel approach that integrates supervised contrastive learning with tailored negative sample pairs for temporal constraints to train the retriever of an RAG system, along with query-side fine-tuning and routing techniques.

**Abstract:**

Retrieval-augmented generation (RAG) enhances large language models (LLMs) by accessing external data sources, offering a promising way to improve accuracy and reliability. Despite its potential, conventional retrievers encounter bias and flaws with time-sensitive queries. In this paper, a benchmark query dataset is constructed to retrieve documents containing time-evolving facts, and the results show that current embedding-based similarity-matching methods struggle to handle queries with explicit temporal constraints. Therefore, we propose a novel approach that integrates supervised contrastive learning with tailored negative sample pairs for temporal constraints to train the retriever of an RAG system, along with query-side fine-tuning and routing techniques. Experimental results show that our approach significantly enhances the retriever performance of time-sensitive queries while ensuring the effectiveness of general queries. We will make the code and dataset publicly available at https://github.com/suzhou-22/TS-Retriever.

---

## Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems

**Autores:** Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xinhao Cheng, Hongyi Jin, Tianqi Chen et al.  
**Publicação:** ACM Computing Surveys · 2025  
**DOI:** https://doi.org/10.1145/3754448  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3754448  
**Citações:** 72  
**Keywords:** generative large language models, large language model inference, low latency, high throughput, memory usage, model compression, inference acceleration, machine learning systems, LLM deployment  

**TL;DR:** The survey aims to provide a comprehensive understanding of the current state and future directions in efficient LLM serving, offering valuable insights for researchers and practitioners in overcoming the barriers of effective LLM deployment, thereby reshaping the future of AI.

**Abstract:**

In the rapidly evolving landscape of artificial intelligence (AI), generative large language models (LLMs) stand at the forefront, revolutionizing how we interact with our data. However, the computational intensity and memory consumption of deploying these models present substantial challenges in terms of serving efficiency, particularly in scenarios demanding low latency and high throughput. This survey addresses the imperative need for efficient LLM serving methodologies from a machine learning system (MLSys) research perspective, standing at the crux of advanced AI innovations and practical system optimizations. We provide in-depth analysis, covering a spectrum of solutions, ranging from cutting-edge algorithmic modifications to groundbreaking changes in system designs. The survey aims to provide a comprehensive understanding of the current state and future directions in efficient LLM serving, offering valuable insights for researchers and practitioners in overcoming the barriers of effective LLM deployment, thereby reshaping the future of AI.

---

## Towards Large Language Model (LLM) Forensics Using LLM-based Invocation Log Analysis

**Autores:** Maxim Chernyshev, Zubair Baig, Robin Ram Mohan Doss  
**Publicação:** Proceedings of the 1st ACM Workshop on Large AI Systems and Models with Privacy and Safety Analysis · 2023  
**DOI:** https://doi.org/10.1145/3689217.3690616  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3689217.3690616  
**Citações:** 13  

**TL;DR:** A novel approach to digital forensic analysis of LLM-integrated applications is presented for prompt injection attacks and LLM invocation logging is proposed as a critical component for enhancing digital forensic readiness in LLM-integrated applications.

**Abstract:**

Large Language Models (LLMs) have fostered the emergence of software application architectures that improve user experiences powered by generative artificial intelligence. A range of cyber attacks are possible against an LLM. A novel approach to digital forensic analysis of LLM-integrated applications is presented for prompt injection attacks. The forensic analysis process is invoked through LLM log analysis. We propose LLM invocation logging as a critical component for enhancing digital forensic readiness in LLM-integrated applications and evaluate 13 state-of-the-art LLMs for this analysis task. Our findings demonstrate the potential utility of selected LLMs in the context of prompt-to-SQL attacks, influenced by sampling temperature and context window size parameters. We also identify limitations of our work and propose key areas for future research, for ongoing contribution to the emerging field of LLM forensics.

---

## Trustworthy LLM-Based Agents for Data-Centric AI

**Autores:** Tianlong Chen, Jian Pei, Minxing Zhang, Liang Zhao  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770855.3816453  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770855.3816453  
**Keywords:** large language models, trustworthy AI, data-centric AI, AI agents, trustworthiness  

**TL;DR:** This tutorial delivers a systematic, data-centric roadmap to build LLM agents that are not merely capable but provably trustworthy, unifying advances in LLM agents, robust machine learning, and data-centric AI.

**Abstract:**

Large language model (LLM) based agents are evolving from conversational chatbots into autonomous decision-makers that plan, reason, wield tools, and collaborate across high-stakes domains such as healthcare, finance, and scientific discovery. Yet this power brings a fundamental challenge: trustworthiness. How can we guarantee that an agent remains robust when real-world data shifts, degrades, or is deliberately poisoned? What defenses exist against memory injection, tool-based exploits, or cascade failures in multi-agent systems? Can we embed domain-specific causal validity, clinical safety, or fairness directly into agent reasoning? And how do we measure trust when it spans robustness, security, reliability, and alignment — each with its own irreconcilable trade-offs? This tutorial delivers a systematic, data-centric roadmap to build LLM agents that are not merely capable but provably trustworthy. We organize the landscape into four interconnected pillars: (i) generalizability under distribution shift, noise, and adversarial inputs; (ii) security architectures that defend against emerging threats — from indirect prompt injection to supply-chain vulnerabilities; (iii) domain-grounded trust in science, engineering, medicine, and commerce, where agents must respect theories, systems, clinical causality, and fairness constraints; and (iv) multi-dimensional evaluation benchmarks that expose trade-offs rather than collapsing them into a single score. By unifying advances in LLM agents, robust machine learning, and data-centric AI, we equip the audience with both foundational principles and actionable recipes to design, deploy, and ultimately trust the next generation of autonomous agent systems.

---

## Uncertainty Quantification for Multimodal Retrieval Augmented Generation

**Autores:** Simon Binz, Heydar Soudani, Faegheh Hasibi  
**Publicação:** Proceedings of the 2026 International ACM SIGIR Conference on Innovative Concepts and Theories in Information Retrieval (ICTIR) · 2026  
**DOI:** https://doi.org/10.1145/3805713.3820431  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805713.3820431  
**Keywords:** uncertainty quantification, retrieval-augmented generation, multimodal retrieval, vision-language models, modality interaction, large language models, answer reliability  

**TL;DR:** This work shows that modeling uncertainty using multimodal and retrieval-aware probability signals improves estimation in multimodal RAG systems, and introduces LeMUQ, a Learnable Multimodal UQ method that analyzes token probabilities under input modifications, such as removing modalities or retrieved context.

**Abstract:**

Retrieval Augmented Generation (RAG) improves the question answering capabilities of Large Language Models (LLMs) by incorporating external knowledge and has recently been extended to multimodal settings through Vision-Language Models (VLMs) that integrate visual and textual information. Despite these advances, generated answers can still be incorrect or misleading. Uncertainty Quantification (UQ) methods aim to estimate the reliability of model outputs, but most existing approaches are designed for text-only models and perform poorly in multimodal RAG scenarios. A key challenge is capturing uncertainty arising from multiple stages of the pipeline, including retrieval, visual understanding, and generation. In this work, we show that modeling uncertainty using multimodal and retrieval-aware probability signals improves estimation in multimodal RAG systems. We introduce LeMUQ, a Learnable Multimodal UQ method that analyzes token probabilities under input modifications, such as removing modalities or retrieved context. By encoding these signals as probability tokens and processing them with a finetuned model, our approach captures interactions between modalities and retrieval. Experiments across datasets, retrievers, and VLMs show consistent improvements over baseline and finetuned UQ methods. Our proposed LeMUQ increases the AUROC metric by 0.038 on average. Additionally, our method shows strong generalization performance across different retrieval setups and datasets with mixed results when transferring across different VLMs. Our findings highlight the importance of modeling multimodal uncertainty and provide a step toward more reliable and safer multimodal RAG systems. Code is available on GitHub.

---

## Understanding Large Language Model Performance in Software Engineering: A Large-scale Question Answering Benchmark

**Autores:** Ruida Hu, Chao Peng, Jingyi Ren, Bo Jiang, Xiangxin Meng, Qinyun Wu et al.  
**Publicação:** Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2025  
**DOI:** https://doi.org/10.1145/3726302.3730262  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3726302.3730262  
**Citações:** 4  
**Keywords:** large language models, question answering, software repositories, benchmark dataset, multi-turn dialogue, GitHub, programming languages  

**TL;DR:** It is found that LLMs still have limitations in question-answering capabilities in the field of software engineering, and medium-length contexts are more conducive to their performance.

**Abstract:**

In this work, we introduce CodeRepoQA, a large-scale benchmark specifically designed for evaluating repository-level question-answering capabilities in the field of software engineering. CodeRepoQA encompasses five programming languages and covers a wide range of scenarios, enabling comprehensive evaluation of language models.To construct this dataset, we crawl data from 30 well-known repositories in GitHub, the largest platform for hosting and collaborating on code, and carefully filter the raw data.In total, CodeRepoQA is a multi-turn question-answering benchmark with 585,687 entries. It covers a diverse array of software engineering scenarios, with an average of 6.62 dialogue turns per entry. We evaluate ten popular large language models on our dataset and provide in-depth analysis. We find that LLMs still have limitations in question-answering capabilities in the field of software engineering, and medium-length contexts are more conducive to their performance. The entire benchmark and details are publicly available at https://github.com/kinesiatricssxilm14/CodeRepoQA.

---

## Understanding Large-Language Model (LLM)-powered Human-Robot Interaction

**Autores:** Callie Y. Kim, Christine P. Lee, Bilge Mutlu  
**Publicação:** Proceedings of the 2024 ACM/IEEE International Conference on Human-Robot Interaction · 2024  
**DOI:** https://doi.org/10.1145/3610977.3634966  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3610977.3634966  
**Citações:** 162  
**Keywords:** large language models, human-robot interaction, social robots, chatbots, text-based interaction, voice interaction, nonverbal cues, negotiation, user expectations, anxiety, LLM fine-tuning  

**TL;DR:** The findings show that LLM-powered robots elevate expectations for sophisticated non-verbal cues and excel in connection-building and deliberation, but fall short in logical communication and may induce anxiety.

**Abstract:**

Large-language models (LLMs) hold significant promise in improving human-robot interaction, offering advanced conversational skills and versatility in managing diverse, open-ended user requests in various tasks and domains. Despite the potential to transform human-robot interaction, very little is known about the distinctive design requirements for utilizing LLMs in robots, which may differ from text and voice interaction and vary by task and context. To better understand these requirements, we conducted a user study (n = 32) comparing an LLM-powered social robot against text- and voice-based agents, analyzing task-based requirements in conversational tasks, including choose, generate, execute, and negotiate. Our findings show that LLM-powered robots elevate expectations for sophisticated non-verbal cues and excel in connection-building and deliberation, but fall short in logical communication and may induce anxiety. We provide design implications both for robots integrating LLMs and for fine-tuning LLMs for use with robots.CCS CONCEPTS• Human-centered computing → HCI design and evaluation methods; • Computing methodologies → Natural language processing; • Computer systems organization → Robotics.

---

## Using Large Language Model for Assessing Business English Students’ Pragmatic Competence

**Autores:** Xiuzhen Xiang, Yi Li  
**Publicação:** Proceedings of the 2024 3rd International Conference on Artificial Intelligence and Education · 2024  
**DOI:** https://doi.org/10.1145/3722237.3722338  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3722237.3722338  
**Citações:** 1  
**Keywords:** pragmatic competence, business English, large language models, automated assessment, human raters, personalized feedback, Kimi  

**TL;DR:** It is found that LLM's core shows consistency with human score and LLM can give instant and personalized feedback which is impossible for human, therefore, the reliability of LLM evaluation on pragmatic competence is proved.

**Abstract:**

Pragmatic competence is the the ability to say and do things appropriately in various contexts. Scholars have been studied this topic from different aspects and a large quantities of methods have been attest to assess students’ pragmatic competence. However, human rating is not only laborious but also less efficient. The emergency of Artificial Intelligence (AI), particularly Large Language Model shed a light on this matter. This essay put prompts into kimi—a LLM of China to see if it can evaluate Business English major students’ pragmatic competence and compare its scoring with human rater's. It is found that LLM's core shows consistency with human score and LLM can give instant and personalized feedback which is impossible for human. Therefore, the reliability of LLM evaluation on pragmatic competence is proved.

---

## Why Retrieval-Augmented Generation Fails: A Graph Perspective

**Autores:** Kai Guo, Xinnan Dai, Zhibo Zhang, Nuohan Lin, Shenglai Zeng, Jie Ren et al.  
**Publicação:** Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 · 2026  
**DOI:** https://doi.org/10.1145/3770855.3818101  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3770855.3818101  
**Keywords:** retrieval-augmented generation, graph neural networks, graph representation learning, large language models, failure analysis  

**TL;DR:** A model-internal study of retrieval-augmented generation that examines how retrieved evidence influences answer generation, and develops a graph-based error detection framework that uses attribution-graph topology features.

**Abstract:**

Retrieval-Augmented Generation (RAG) has become a powerful and widely used approach for improving large language models by grounding generation in retrieved evidence. However, RAG systems still produce incorrect answers in many cases. Why RAG fails despite having access to external information remains poorly understood. We present a model-internal study of retrieval-augmented generation that examines how retrieved evidence influences answer generation. Using circuit tracing, we construct attribution graphs that model the flow of information through transformer layers during decoding. These graphs represent interactions among retrieved context, intermediate model activations, and generated tokens, providing a graph, circuit-level view of how external evidence is integrated into the model's reasoning process across multiple question answering benchmarks, we observe consistent structural differences: correct predictions exhibit deeper reasoning paths, more distributed evidence flow, and a more structured pattern of local connectivity, while failed predictions show shallower, fragmented, and overly concentrated evidence flow. Building on these findings, we develop a graph-based error detection framework that uses attribution-graph topology features. Furthermore, we show that attribution graphs enable targeted interventions. By reinforcing question-constrained evidence grounding, we reshape internal routing so that answer generation remains guided by the question, leading to more effective integration of retrieved information and fewer errors. Our code is available at https://github.com/KaiGuo20/Circuit_RAG.

---

## iTIMO: An LLM-empowered Synthesis Dataset for Travel Itinerary Modification

**Autores:** Zhuoxuan Huang, Yunshan Ma, Hongyu Zhang, Hua Ma, Zhu Sun  
**Publicação:** Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2026  
**DOI:** https://doi.org/10.1145/3805712.3808576  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805712.3808576  
**Citações:** 2  
**Keywords:** large language models, travel recommender systems, adaptive recommendation, LLM benchmarking  

**TL;DR:** The itinerary modification task is formally defined and a general pipeline to construct the corresponding dataset, namely iTIMO is proposed, which frames the generation of shape need-to-modify itinerary data as an intent-driven perturbation task.

**Abstract:**

Addressing itinerary modification is crucial for enhancing the travel experience as it is a frequent requirement during traveling. However, existing research mainly focuses on fixed itinerary planning, leaving modification underexplored due to the scarcity of shape need-to-modify itinerary data. To bridge this gap, we formally define the itinerary modification task and propose a general pipeline to construct the corresponding dataset, namely iTIMO. This pipeline frames the generation of shape need-to-modify itinerary data as an intent-driven perturbation task. It instructs large language models to perturb real-world itineraries using three operations: REPLACE, ADD, and DELETE. Each perturbation is grounded in three intents: disruptions of popularity, spatial distance, and category diversity. Furthermore, hybrid metrics are proposed to ensure perturbation effectiveness. We conduct comprehensive benchmarking on iTIMO to analyze the capabilities and limitations of state-of-the-art LLMs. Overall, iTIMO provides a comprehensive testbed for the modification task, and empowers the evolution of traditional travel recommender systems into adaptive frameworks capable of handling dynamic travel needs. Dataset, code and supplementary materials are available at https://github.com/zelo2/iTIMO.

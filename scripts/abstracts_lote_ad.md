# Resumo de artigos

## Lifting the Veil on Composition, Risks, and Mitigations of the Large Language Model Supply Chain

**Autores:** Kaifeng Huang, Bihuan Chen, You Lu, Susheng Wu, Dingji Wang, Yiheng Huang et al.  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2026  
**DOI:** https://doi.org/10.1145/3830903  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3830903  
**Citações:** 2  
**Keywords:** large language models, risk taxonomy, risk mitigation, LLM integration, stakeholder perspectives, LLM security  

**TL;DR:** A structured taxonomy encompassing risk types, risky actions, and corresponding mitigations across different stakeholders and components of the supply chain is developed across different stakeholders and components of the supply chain.

**Abstract:**

Large language models (LLMs) have sparked significant impact with regard to both intelligence and productivity. Numerous enterprises have integrated LLMs into their applications to solve their own domain-specific tasks. However, integrating LLMs into specific scenarios is a systematic process that involves substantial components, which are collectively referred to as the LLM supply chain . A comprehensive understanding of LLM supply chain composition, as well as the relationships among its components, is crucial for enabling effective mitigation measures for different related risks. A comprehensive understanding of LLM supply chain composition and the relationships among its components, particularly from a security perspective, is crucial for enabling effective mitigation of associated risks. While existing literature has explored various risks associated with LLMs, there remains a notable gap in systematically characterizing the LLM supply chain from the dual perspectives of contributors and consumers. In this work, we develop a structured taxonomy encompassing risk types, risky actions, and corresponding mitigations across different stakeholders and components of the supply chain. We believe that a thorough review of the LLM supply chain composition, along with its inherent risks and mitigation measures, would be valuable for industry practitioners to avoid potential damages and losses, and enlightening for academic researchers to rethink existing approaches and explore new avenues of research.

---

## Mitigating Bias in Large Language Model Based Question Answering through Causal Front Door Prompting

**Autores:** Yaqi Yang, Ziqi Xu, Jie Li, Chenglong Ma, Jeffrey Chan, Mark Sanderson et al.  
**Publicação:** Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2026  
**DOI:** https://doi.org/10.1145/3805712.3809679  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805712.3809679  
**Citações:** 3  
**Keywords:** large language models, question answering, bias mitigation, stereotype bias, chain-of-thought reasoning, causal intervention, reasoning traces, fairness, demographic bias  

**TL;DR:** A Causal Front Door Prompting framework (CFDP) is proposed that reduces demographic influence by intervening on the chain of thought reasoning, which is treated as an observable mediator and consistently improves fairness metrics without sacrificing QA accuracy.

**Abstract:**

Large language models (LLMs) are widely used for question answering (QA) but can generate biased or stereotype-driven answers due to demographic associations learned during pre-training. Existing mitigation strategies often rely on model access or fine-tuning, which limits their applicability to closed-source LLMs. We propose a Causal Front Door Prompting framework (CFDP) that reduces demographic influence by intervening on the chain of thought reasoning, which is treated as an observable mediator. CFDP samples and clusters multiple reasoning traces and estimates answer probabilities through weighted aggregation. Experiments on two widely used bias-sensitive QA benchmarks, BBQ and Stereotype, across major LLMs show that CFDP consistently improves fairness metrics without sacrificing QA accuracy. Ablation and sensitivity analyses confirm the value of each component, indicating that causal intervention on reasoning provides an effective and practical approach for bias mitigation in LLM-based QA.

---

## A Survey on the Memory Mechanism of Large Language Model-based Agents

**Autores:** Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen et al.  
**Publicação:** ACM Transactions on Information Systems · 2025  
**DOI:** https://doi.org/10.1145/3748302  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3748302  
**Citações:** 148  
**Keywords:** LLM agents, memory mechanisms, agent memory, self-evolving agents, agent-environment interaction, memory module design  

**TL;DR:** This article proposes a comprehensive survey on the memory mechanism of LLM-based agents, systematically review previous studies on how to design and evaluate the memory module, and presents many agent applications, where the memory module plays an important role.

**Abstract:**

Large language model (LLM)-based agents have recently attracted much attention from the research and industry communities. Compared with original LLMs, LLM-based agents are featured in their self-evolving capability, which is the basis for solving real-world problems that need long-term and complex agent-environment interactions. The key component to support agent-environment interactions is the memory of the agents. While previous studies have proposed many promising memory mechanisms, they are scattered in different papers, and there lacks a systematical review to summarize and compare these works from a holistic perspective, failing to abstract common and effective designing patterns for inspiring future studies. To bridge this gap, in this article, we propose a comprehensive survey on the memory mechanism of LLM-based agents. In specific, we first discuss “what is” and “why do we need” the memory in LLM-based agents. Then, we systematically review previous studies on how to design and evaluate the memory module. In addition, we also present many agent applications, where the memory module plays an important role. At last, we analyze the limitations of existing work and show important future directions. To keep up with the latest advances in this field, we create a repository at https://github.com/nuster1128/LLM_Agent_Memory_Survey .

---

## An Expert Schema for Evaluating Large Language Model Errors in Scholarly Question-Answering Systems

**Autores:** Anna Martin-Boyle, William Humphreys, Martha Brown, Cara Leckey, Harmanpreet Kaur  
**Publicação:** Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems · 2026  
**DOI:** https://doi.org/10.1145/3772318.3791843  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3772318.3791843  
**Citações:** 3  
**Keywords:** large language models, error patterns, LLM reliability, assessment methods, meta-evaluation  

**TL;DR:** A schema for evaluating LLM errors in scholarly question-answering systems that reflects the assessment strategies of practicing scientists and shows not only which errors experts naturally identify but also how structured evaluation schemas can help them detect previously overlooked issues.

**Abstract:**

Large Language Models (LLMs) are transforming scholarly tasks like search and summarization, but their reliability remains uncertain. Current evaluation metrics for testing LLM reliability are primarily automated approaches that prioritize efficiency and scalability, but lack contextual nuance and fail to reflect how scientific domain experts assess LLM outputs in practice. We developed and validated a schema for evaluating LLM errors in scholarly question-answering systems that reflects the assessment strategies of practicing scientists. In collaboration with domain experts, we identified 20 error patterns across seven categories through thematic analysis of 68 question-answer pairs. We validated this schema through contextual inquiries with 10 additional scientists, which showed not only which errors experts naturally identify but also how structured evaluation schemas can help them detect previously overlooked issues. Domain experts use systematic assessment strategies, including technical precision testing, value-based evaluation, and meta-evaluation of their own practices. We discuss implications for supporting expert evaluation of LLM outputs, including opportunities for personalized, schema-driven tools that adapt to individual evaluation patterns and expertise levels.

---

## Challenges in Testing Large Language Model-Based Software: A Faceted Taxonomy

**Autores:** Felix Dobslaw, Robert Feldt, Juyeon Yoon, Shin Yoo  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2026  
**DOI:** https://doi.org/10.1145/3806396  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3806396  
**Citações:** 4  
**Keywords:** large language models, multi-agent LLM systems, software testing, test case design, non-determinism, oracle model  

**TL;DR:** The findings reveal that current tools treat test executions as isolated events, lack explicit aggregation mechanisms, and inadequately capture variability across model versions, configurations, and repeated runs, highlighting the need for viewing correctness as a distribution of outcomes rather than a binary property.

**Abstract:**

Large Language Models (LLMs) and Multi-Agent LLMs (MALLMs) introduce non-determinism, unlike traditional or machine learning software, where models typically produce deterministic outputs for given inputs. LLM-based software requires new approaches to verifying correctness that account for variability within individual test cases, not just across different inputs. This article presents a taxonomy for LLM test case design, informed by research literature and our experience. Each facet is exemplified, and we conduct an LLM-assisted analysis of six open source testing frameworks, perform a sensitivity study of an agent-based system across different model configurations, and provide working examples contrasting atomic and aggregated test cases. We identify key variation points that impact test correctness and highlight open challenges that the research, industry, and open source communities must address as LLMs become integral to software systems. Our taxonomy defines four facets of LLM test case design, addressing ambiguity in both inputs and outputs while establishing best practices. It distinguishes variability in goals, the system under test, and inputs, and introduces two key oracle types: atomic and aggregated. Our findings reveal that current tools treat test executions as isolated events, lack explicit aggregation mechanisms, and inadequately capture variability across model versions, configurations, and repeated runs. This highlights the need for viewing correctness as a distribution of outcomes rather than a binary property, requiring closer collaboration between academia and practitioners to establish mature, variability-aware testing methodologies.

---

## Dialogue Meets Data: A Large Language Model Approach for Efficient Linked Data Retrieval

**Autores:** Omar Mussa, Omer Rana, Benoit Goossens, Pablo Orozco Ter Wengel, Charith Perera  
**Publicação:** ACM Transactions on the Web · 2026  
**DOI:** https://doi.org/10.1145/3796550  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3796550  
**Keywords:** large language models, SPARQL query generation, RDF triple store, conversational interfaces, chatbots, Linked Open Data  

**TL;DR:** An innovative framework that integrates LLMs into conversational user interfaces (UIs), enabling the dynamic generation of precise SPARQL queries without the necessity for constant retraining is presented, showcasing the potential of LLMs to transform information retrieval.

**Abstract:**

While large language models (LLMs) have captured global attention for their linguistic abilities, our work harnesses their power to overcome traditional barriers in querying Linked Data (LD) and Resource Description Framework (RDF) triplestores. This paper presents an innovative framework that integrates LLMs into conversational user interfaces (UIs), enabling the dynamic generation of precise SPARQL queries without the necessity for constant retraining. Most conversational UI models struggle with adaptability as they require frequent retraining whenever datasets are updated or expanded. This limitation impedes their effectiveness as general-purpose extraction tools. To address this challenge, our approach 1 seamlessly incorporates LLMs into the conversational UI process, fostering a more sophisticated understanding and interpretation of user queries and enhancing overall responsiveness. By leveraging the advanced natural language processing capabilities of LLMs, our method improves RDF entity extraction in web systems that utilise conventional chatbots. Furthermore, it extends the functionality of these chatbots, allowing them to respond directly to queries based on the RDF schema while providing an assistive interface that deepens understanding of the dataset and its underlying domain. This facilitates the extraction of more meaningful information. By adopting this approach, interactions become more refined and context-sensitive, a crucial advancement for managing the intricate query structures commonly found in RDF datasets and Linked Open Data (LOD) endpoints. We have evaluated our approach in practical settings by assessing the tool’s ability to address complex queries and to answer general ecological queries, with the outputs evaluated by human experts. The results demonstrate a notable improvement in system expressiveness and response accuracy, showcasing the potential of LLMs to transform information retrieval. The findings not only confirm their adaptability in enhancing existing systems but also open up exciting possibilities for their deployment in specialised web information domains, paving the way for future research in this evolving field.

---

## EventChat: Implementation and user-centric evaluation of a large language model-driven conversational recommender system for exploring leisure events in an SME context

**Autores:** Hannes Kunstmann, Joseph Ollier, Joel Persson, Florian von Wangenheim  
**Publicação:** ACM Transactions on Recommender Systems · 2026  
**DOI:** https://doi.org/10.1145/3803546  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3803546  
**Citações:** 3  
**Keywords:** conversational recommender systems, large language models, leisure events, small and medium-sized enterprises, user-centered evaluation, retrieval-augmented generation, prompt learning, cost-effectiveness, recommendation accuracy  

**TL;DR:** The design and field performance of an LLM-driven CRS in a small to medium enterprise (SME) context is detailed using both system metrics and end-user evaluations, while a revised ResQue model is presented for evaluating LLM-driven CRS, enabling replicability in a rapidly evolving field.

**Abstract:**

The integration of large language models (LLMs) to conversational recommender systems (CRS) represents an enormous evolution in their strategic potential. Yet to date, research has predominantly focused upon technical frameworks to implement LLM-driven CRS, at the expense of end-user evaluations or strategic implications for firms, particularly from the perspective of a small to medium enterprises (SME) that makeup the bedrock of the global economy. In the current paper, we detail the design and field performance of an LLM-driven CRS in a small to medium enterprise (SME) context using both system metrics and end-user evaluations, while also presenting a revised ResQue model for evaluating LLM-driven CRS, enabling replicability in a rapidly evolving field. Results demonstrate satisfactory system performance (85.5% perceived recommendation accuracy) but underscore latency, cost, and quality challenges. Notably, with median costs of ∃0.04 per interaction and latency of 5.7s, cost-effectiveness and response time emerge as crucial issues, predominantly driven by use of ChatGPT as a ranker within the retrieval-augmented generation (RAG) technique. Results also show that relying solely on prompt-based learning has quality limitations in a production environment. Strategic considerations for SMEs are outlined considering trade-offs in the technical landscape.

---

## Experiences from Integrating Large Language Model Chatbots into the Classroom

**Autores:** Arto Hellas, Juho Leinonen, Leo Leppänen  
**Publicação:** Proceedings of the 2024 on ACM Virtual Global Computing Education Conference V. 1 · 2024  
**DOI:** https://doi.org/10.1145/3649165.3690101  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3649165.3690101  
**Citações:** 19  
**Keywords:** large language models, chatbots, GPT-4, classroom integration, university courses, online course materials, software engineering education, artificial intelligence in education, student experience  

**TL;DR:** The results suggest that the worst fears of educators -- all students overrelying on chatbots -- did not materialize and potential reasons for low usage are discussed, including the need for more tailored and scaffolded chatbot experiences targeted for specific types of use cases.

**Abstract:**

We provided students access to a state-of-the-art large language model (LLM) chatbot through the online materials of three university-level courses. One of the courses focused on software engineering with LLMs, while the two other courses were not directly related to LLMs. The chatbot used OpenAI GPT-4 without additional filters or system prompts. Our results suggest that only a minority of students engage with the chatbot in the courses that do not relate to LLMs. At the same time, unsurprisingly, nearly all students in the LLM-focused course leveraged the chatbot. In all courses, the majority of the chatbot usage came from a few superusers, whereas the majority of the students did not heavily use the chatbot even though it effectively provided free access to OpenAI's GPT-4 model (which would have otherwise required a paid subscription at the time of the study). We observe that in addition to students using the chatbot for course-specific purposes, many use the chatbot for their own purposes. Overall, our results suggest that the worst fears of educators -- all students overrelying on chatbots -- did not materialize. Finally, we discuss potential reasons for low usage, including the need for more tailored and scaffolded chatbot experiences targeted for specific types of use cases.

---

## IC-Cache: Efficient Large Language Model Serving via In-context Caching

**Autores:** Yifan Yu, Yu Gan, Nikhil Sarda, Lillian Tsai, Jiaming Shen, Yanqi Zhou et al.  
**Publicação:** Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles · 2025  
**DOI:** https://doi.org/10.1145/3731569.3764829  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3731569.3764829  
**Citações:** 4  
**Keywords:** large language model serving, resource efficiency, large language model inference  

**TL;DR:** IC-Cache is introduced, a caching system that enables live LLM capability augmentation to improve serving efficiency by leveraging historical request-response pairs from larger models as in-context examples, enabling selective offloading of requests to reduce cost and latency.

**Abstract:**

Large language models (LLMs) have excelled in various applications, yet serving them at scale is challenging due to their substantial resource demands and high latency. Our real-world studies reveal that over 70% of user requests to LLMs have semantically similar counterparts, suggesting the potential for knowledge transfer among requests. However, naively caching and reusing past responses leads to a big quality drop. In this paper, we introduce IC-Cache, a caching system that enables live LLM capability augmentation to improve serving efficiency: by leveraging historical request-response pairs from larger models as in-context examples, IC-Cache empowers small LLMs to imitate and even exceed the compositional abilities (e.g., reasoning) of their larger counterparts, enabling selective offloading of requests to reduce cost and latency. Achieving this live augmentation at scale introduces intricate trade-offs between response quality, latency, and system throughput. For a new request, IC-Cache efficiently selects similar, high-utility examples to prepend them to the new request's input. At scale, it adaptively routes requests across LLMs of varying capabilities, accounting for response quality and serving loads. IC-Cache employs a cost-aware cache replay mechanism that refines example quality offline to maximize online cache utility and efficiency. Evaluations on millions of realistic requests demonstrate that IC-Cache improves LLM serving throughput by 1.4–5.9x and reduces latency by 28–71% without hurting response quality.

---

## Large Language Model Supply Chain: A Research Agenda

**Autores:** Shenao Wang, Yanjie Zhao, Xinyi Hou, Haoyu Wang  
**Publicação:** ACM Transactions on Software Engineering and Methodology · 2025  
**DOI:** https://doi.org/10.1145/3708531  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3708531  
**Citações:** 37  
**Keywords:** large language models, foundation models, software supply chain security, privacy, software engineering challenges, infrastructure dependency, research agenda  

**TL;DR:** This work aims to bridge the existing research gap in systematically understanding the multifaceted issues within the LLM supply chain, offering valuable insights to guide future efforts in this rapidly evolving domain.

**Abstract:**

The rapid advancement of large language models (LLMs) has revolutionized artificial intelligence, introducing unprecedented capabilities in natural language processing and multimodal content generation. However, the increasing complexity and scale of these models have given rise to a multifaceted supply chain that presents unique challenges across infrastructure, foundation models, and downstream applications. This article provides the first comprehensive research agenda of the LLM supply chain, offering a structured approach to identify critical challenges and opportunities through the dual lenses of software engineering (SE) and security and privacy (S&P). We begin by establishing a clear definition of the LLM supply chain, encompassing its components and dependencies. We then analyze each layer of the supply chain, presenting a vision for robust and secure LLM development, reviewing the current state of practices and technologies, and identifying key challenges and research opportunities. This work aims to bridge the existing research gap in systematically understanding the multifaceted issues within the LLM supply chain, offering valuable insights to guide future efforts in this rapidly evolving domain.

---

## Retrieval-Augmented Generation for Multi-Hop Question Answering Based on Structured Planning

**Autores:** Yujiao Huang, Ling Yang, Xu-Hua Yang, Xinli Xu  
**Publicação:** ACM Transactions on Knowledge Discovery from Data · 2026  
**DOI:** https://doi.org/10.1145/3789506  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3789506  
**Citações:** 3  
**Keywords:** retrieval-augmented generation, multi-hop question answering, structured planning, iterative retrieval, retrieval bias, evidence extraction, hallucination mitigation, large language models, open-domain question answering  

**TL;DR:** This work employs pre-retrieval question planning to provide semantic guidance for iterative retrieval, ensuring greater consistency between retrieval and reasoning, and introduces a structured evidence extraction mechanism to effectively filter out noise in the retrieved information, leading to improved reasoning accuracy.

**Abstract:**

Retrieval-augmented generation (RAG) has been proposed to mitigate the hallucination problem of large language models (LLMs) in knowledge-intensive tasks by incorporating external knowledge. However, in multi-hop question answering, existing iterative retrieval methods often struggle to maintain focus on key information. As the number of retrieval iterations increases, the generated queries can gradually drift from the correct reasoning path, and irrelevant or noisy information may accumulate, ultimately reducing reasoning accuracy. To address these challenges, we propose a novel retrieval-augmented generation method for multi-hop question answering based on structured planning. First, our approach employs pre-retrieval question planning to provide semantic guidance for iterative retrieval, ensuring greater consistency between retrieval and reasoning. In addition, we introduce a structured evidence extraction mechanism to effectively filter out noise in the retrieved information, leading to improved reasoning accuracy. Experimental results on three open-domain multi-hop question answering datasets demonstrate that our method can effectively alleviate the impact of retrieval bias and retrieval noise and exhibit competitive performance.

---

## The Typing Cure: Experiences with Large Language Model Chatbots for Mental Health Support

**Autores:** Inhwa Song, Sachin R Pendse, Neha Kumar, Munmun De Choudhury  
**Publicação:** Proceedings of the ACM on Human-Computer Interaction · 2025  
**DOI:** https://doi.org/10.1145/3757430  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3757430  
**Citações:** 64  
**Keywords:** large language model chatbots, mental health support, lived experience, AI ethics, psychotherapy  

**Abstract:**

People experiencing severe distress increasingly use Large Language Model (LLM) chatbots as mental health support tools. Discussions on social media have described how engagements were lifesaving for some, but evidence suggests that general-purpose LLM chatbots also have notable risks that could endanger the welfare of users if not designed responsibly. In this study, we investigate the lived experiences of people who have used LLM chatbots for mental health support. We build on interviews with 21 individuals from globally diverse backgrounds to analyze how users create unique support roles for their chatbots, fill in gaps in everyday care, and navigate associated cultural limitations when seeking support from chatbots. We ground our analysis in psychotherapy literature around effective support, and introduce the concept of therapeutic alignment, or aligning AI with therapeutic values for mental health contexts. Our study offers recommendations for how designers can approach the ethical and effective use of LLM chatbots and other AI mental health support tools in mental health care.

---

## Using a Large Language Model as Design Material for an Interactive Museum Installation

**Autores:** Maria Padilla Engstrøm, Anders Sundnes Løvlie  
**Publicação:** Companion Publication of the 2025 ACM Designing Interactive Systems Conference · 2025  
**DOI:** https://doi.org/10.1145/3715668.3736359  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3715668.3736359  
**Citações:** 6  
**Keywords:** large language models, chatbots, misinformation, historical figures, role play, personal narrative, critical reflection, museum education, research through design, rapid prototyping  

**TL;DR:** It is suggested that designers may shape interactions with the chatbot to emphasize personal narratives and role play rather than historical facts or to intentionally highlight the unreliability of the chatbot outputs to provoke critical reflection.

**Abstract:**

We present a work in progress that explores using a Large Language Model (LLM) as a design material for an interactive museum installation. LLMs offer the possibility of creating chatbots that can facilitate dynamic and human-like conversation, engaging in a form of role play to bring historical persons “to life” for visitors. However, LLMs are prone to producing misinformation, which runs counter to museums’ core mission to educate the public. We use Research-through-Design to explore some approaches to navigating this dilemma through rapid prototyping and evaluation and propose some directions for further research. We suggest that designers may shape interactions with the chatbot to emphasize personal narratives and role play rather than historical facts or to intentionally highlight the unreliability of the chatbot outputs to provoke critical reflection.

---

## WDDQA: A Large Language Model-Based Question-answering System in Instruction for the Web Design and Development Course

**Autores:** Mingpei Peng, Ning Zhang  
**Publicação:** Proceedings of the 2026 7th International Conference on Computer Information and Big Data Applications · 2026  
**DOI:** https://doi.org/10.1145/3813822.3814139  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3813822.3814139  
**Keywords:** large language models, educational question answering, code correction, debugging, LangChain, artificial intelligence in education, vocational college students, student engagement  

**TL;DR:** The application of the WDDQA not only enhances student engagement but also improves the quality of code submissions, offering a practical reference for the implementation of AI-supported education.

**Abstract:**

Large language Models (LLMs) have shown remarkable performance on various natural language processing, including educational question answering. While general-purpose LLMs are capable of addressing certain coding queries, they may not always be optimally suited for specialized educational contexts, such as software technology course at vocational colleges. To address this difficulty, this study introduces a Web Design and Development question-answering System (WDDQA) comprehensively built by ChatGLM3-6B and Langchain-Chatchat. WDDQA assists students in real-time code correction and provide relevant code examples and knowledge. By integrating students’ textbooks with learning data, WDDQA provides explanations that are more accessible and tailored to their comprehension level. Teaching evaluation indicate that after implementing WDDQA in class, the number of student assignment submissions saw an increase of 10%, and the code debugging success rate experienced an increase of 13%. The application of the WDDQA not only enhances student engagement but also improves the quality of code submissions, offering a practical reference for the implementation of AI-supported education.

---

## Doing More with Less: A Survey on Routing Strategies for Resource Optimisation in Large Language Model-Based Systems

**Autores:** Clovis Varangot-Reille, Christophe Bouvard, Mathieu Ciancone, Antoine Gourru, Marion Schaeffer, François Jacquenet  
**Publicação:** Journal of Artificial Intelligence Research · 2026  
**DOI:** https://doi.org/10.1613/jair.1.19801  
**Fonte:** acm — https://dl.acm.org/doi/10.1613/jair.1.19801  
**Citações:** 3  
**Keywords:** query routing, large language models, resource optimization, cost minimization, reinforcement learning routing, LLM fine-tuning, chatbots, LLM pipelines, cost-performance trade-off, energy efficiency, scalability  

**TL;DR:** Routing offers a practical way to improve the efficiency of LLM-based systems by formalising routing as a performance–cost optimisation problem, and provides tools and directions to guide future research and development of adaptive low-cost LLM-based systems.

**Abstract:**

Background: Large Language Model (LLM)-based systems, such as conversational agents, are usually designed with monolithic, static architectures that rely on a single, general-purpose LLM to handle all user queries. However, these systems may be inefficient as different queries may require different levels of reasoning, domain knowledge or pre-processing. While generalist LLMs (e.g. GPT-4o, Claude-Sonnet) perform well across a wide range of tasks, they may incur significant financial, energy and computational costs. These costs may be disproportionate for simpler queries, resulting in unnecessary resource utilisation. A routing mechanism can therefore be employed to route queries to more appropriate components, such as smaller or specialised models, thereby improving efficiency and optimising resource consumption. Objectives: This survey aims to provide a comprehensive overview of routing strategies in LLM-based systems. Specifically, it reviews when, why, and how routing should be integrated into LLM pipelines to improve efficiency, scalability, and performance. Methods: We structure the survey by defining the objectives to optimise, such as cost minimisation and performance maximisation; the timing of routing within the LLM workflow, whether it occurs before or after generation; and the various implementation strategies, including similarity-based, supervised, reinforcement learning-based, and generative methods. Practical considerations such as industrial applications and current limitations are also examined, like standardising routing experiments, accounting for non-financial costs, and designing adaptive strategies. Results: There is a wide range of routing strategies, from lightweight, similarity-based and supervised methods, to more complex approaches involving LLM fine-tuning and reinforcement learning. Most current strategies adopt a pre-generation approach, which is generally more resource-efficient. This survey demonstrates that some low-resource solutions can provide generalisation capabilities. Conclusions: Routing offers a practical way to improve the efficiency of LLM-based systems. By formalising routing as a performance–cost optimisation problem, this survey provides tools and directions to guide future research and development of adaptive low-cost LLM-based systems.

---

## A Canary in the AI Coal Mine: American Jews May Be Disproportionately Harmed by Intellectual Property Dispossession in Large Language Model Training

**Autores:** Heila Precel, Allison McDonald, Brent Hecht, Nicholas Vincent  
**Publicação:** Proceedings of the CHI Conference on Human Factors in Computing Systems · 2024  
**DOI:** https://doi.org/10.1145/3613904.3642749  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3613904.3642749  
**Citações:** 4  
**Keywords:** large language models, training data, American Jews, minority groups, economic damage, AI regulation, indirect discrimination  

**TL;DR:** Evidence is identified that the current paradigm of large language models (LLMs) likely continues this long history of systemic property dispossession from minority groups and the importance of working together towards alternative LLM paradigms that avoid both disparate impacts and widespread societal harms is stressed.

**Abstract:**

Systemic property dispossession from minority groups has often been carried out in the name of technological progress. In this paper, we identify evidence that the current paradigm of large language models (LLMs) likely continues this long history. Examining common LLM training datasets, we find that a disproportionate amount of content authored by Jewish Americans is used for training without their consent. The degree of over-representation ranges from around 2x to around 6.5x. Given that LLMs may substitute for the paid labor of those who produced their training data, they have the potential to cause even more substantial and disproportionate economic harm to Jewish Americans in the coming years. This paper focuses on Jewish Americans as a case study, but it is probable that other minority communities (e.g., Asian Americans, Hindu Americans) may be similarly affected and, most importantly, the results should likely be interpreted as a “canary in the coal mine” that highlights deep structural concerns about the current LLM paradigm whose harms could soon affect nearly everyone. We discuss the implications of these results for the policymakers thinking about how to regulate LLMs as well as for those in the AI field who are working to advance LLMs. Our findings stress the importance of working together towards alternative LLM paradigms that avoid both disparate impacts and widespread societal harms.

---

## A Domestic NPU-Cluster-Based Large Language Model Service Platform: Construction, Optimization, and Evaluation

**Autores:** Lin Shi, Ling Du, Jinrong Huang, Gang Wang, Zhibin Luo, Guangshen Wang  
**Publicação:** Proceedings of the 2nd International Conference on Digital Management and Information Technology · 2026  
**DOI:** https://doi.org/10.1145/3808707.3808864  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3808707.3808864  
**Keywords:** resource isolation, reliability, retrieval-augmented generation, hallucination mitigation, AI infrastructure  

**TL;DR:** This work provides a repeatable engineering blueprint for artificial intelligence infrastructure, significantly improving service efficiency and quality.

**Abstract:**

This article introduces a large language model (LLM) service platform based on a domestic NPU cluster, aiming to meet the key challenges such as insufficient computing resources, complex maintenance, and hallucinations in on-premises deployment. The platform adopts a heterogeneous model architecture, where computational nodes utilize the Ascend 910B NPU for independent model execution (such as Qwen3 series for complex reasoning and multimodal tasks), reducing cross-node synchronization overhead and enriching LLM service types. Through W8A8 quantization and resource isolation, it demonstrates excellent reliability (92.60% request success rate, vs. 90.90% for the single-cluster approach) and delay reduction (TTFT 2.69 seconds, a 40% decrease from 4.51 seconds) in an empirical verification of 200 concurrent requests. Equipped with a standardized API management platform, it realizes unified interface encapsulation, efficient reuse of computing resources, and fine-grained usage control, significantly lowering the threshold for service invocation. This service platform also expands the knowledge scope of LLMs through RAG technology and enables scenario-specific customization of general models. This work provides a repeatable engineering blueprint for artificial intelligence infrastructure, significantly improving service efficiency and quality.

---

## A Hitchhiker’s Guide to Jailbreaking ChatGPT via Prompt Engineering

**Autores:** Yi Liu, Gelei Deng, Zhengzi Xu, Yuekang Li, Yaowen Zheng, Ying Zhang et al.  
**Publicação:** Proceedings of the 4th International Workshop on Software Engineering and AI for Data Quality in Cyber-Physical Systems/Internet of Things · 2024  
**DOI:** https://doi.org/10.1145/3663530.3665021  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3663530.3665021  
**Citações:** 104  
**Keywords:** jailbreak prompts, prompt engineering, large language models, ChatGPT, GPT-3.5, GPT-4, prompt management, LLM robustness  

**TL;DR:** It was discovered that GPT-3.5 and GPT-4 could still generate inappropriate content in response to malicious prompts without the need for jailbreaking, underscores the critical need for effective prompt management within LLM systems and provides valuable insights and data to spur further research in LLM testing and jailbreak prevention.

**Abstract:**

Natural language prompts serve as an essential interface between users and Large Language Models (LLMs) like GPT-3.5 and GPT-4, which are employed by ChatGPT to produce outputs across various tasks. However, prompts crafted with malicious intent, known as jailbreak prompts, can circumvent the restrictions of LLMs, posing a significant threat to systems integrated with these models. Despite their critical importance, there is a lack of systematic analysis and comprehensive understanding of jailbreak prompts. Our paper aims to address this gap by exploring key research questions to enhance the robustness of LLM systems: 1) What common patterns are present in jailbreak prompts? 2) How effectively can these prompts bypass the restrictions of LLMs? 3) With the evolution of LLMs, how does the effectiveness of jailbreak prompts change? To address our research questions, we embarked on an empirical study targeting the LLMs underpinning ChatGPT, one of today's most advanced chatbots. Our methodology involved categorizing 78 jailbreak prompts into 10 distinct patterns, further organized into three jailbreak strategy types, and examining their distribution. We assessed the effectiveness of these prompts on GPT-3.5 and GPT-4, using a set of 3,120 questions across 8 scenarios deemed prohibited by OpenAI. Additionally, our study tracked the performance of these prompts over a 3-month period, observing the evolutionary response of ChatGPT to such inputs. Our findings offer a comprehensive view of jailbreak prompts, elucidating their taxonomy, effectiveness, and temporal dynamics. Notably, we discovered that GPT-3.5 and GPT-4 could still generate inappropriate content in response to malicious prompts without the need for jailbreaking. This underscores the critical need for effective prompt management within LLM systems and provides valuable insights and data to spur further research in LLM testing and jailbreak prevention.

---

## A Retrieval-Augmented Generation Framework for Electric Power Industry Question Answering

**Autores:** Yanyan Lu, Jiao Peng, Xing Xu, Yue He, Tao Li, Jie Wei et al.  
**Publicação:** Proceedings of the 2024 2nd International Conference on Electronics, Computers and Communication Technology · 2024  
**DOI:** https://doi.org/10.1145/3705754.3705771  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3705754.3705771  
**Citações:** 14  
**Keywords:** retrieval-augmented generation, question answering, electric utilities, large language models  

**TL;DR:** This study first analyzes the characteristics of documents in the electric power industry and proposes the Hierarchical Adaptive Semantic Segmentation (HASS) method, which improves the accuracy of responses and the precision of queries by subdividing knowledge points and integrating metadata.

**Abstract:**

Retrieval-augmented Generation has achieved significant success in improving the performance of large language models by utilizing external knowledge sources. However, despite its advancements, it still faces challenges in domain-specific structured documents such as the electric power industry, exhibiting low recall rates and response inaccuracies. To solve these issues, this paper designs a question-answering framework specifically for the electric power industry using the large language model. This study first analyzes the characteristics of documents in the electric power industry and proposes the Hierarchical Adaptive Semantic Segmentation(HASS) method, which improves the accuracy of responses and the precision of queries by subdividing knowledge points and integrating metadata. In the retrieval strategy, a Hybrid Search(HS) method is designed, combining the advantages of sparse and dense retrieval to improve the recall rate. To enable large language models to focus on relevant documents when generating responses, we propose the Irrelevant Document Filtering(IDF) method for minimizing the noise impact from irrelevant documents. Additionally, the model is designed with prompts and fine-tuned to further enhance its ability to utilize context and the accuracy of answer generation. Finally, due to the lack of publicly available datasets for document question-answering in the electricity sector, this work constructs a dataset manually for training and evaluation, comprising 1300 QA items covering several types of questions. Experimental results demonstrate that the methods proposed in this paper effectively improve the accuracy of LLMs in the electric power industry, with our method showing a 9% improvement in accuracy over the traditional RAG approach.

---

## A Review of Large Language Model Security in Financial Fraud Research

**Autores:** Jize Liu  
**Publicação:** Proceedings of the 2nd International Conference on Artificial Intelligence and Digital Finance · 2026  
**DOI:** https://doi.org/10.1145/3844275.3844305  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3844275.3844305  
**Keywords:** large language models, financial fraud detection, phishing detection, adversarial prompting, interpretability, privacy, regulatory compliance, explainability, AI governance, generative AI risks  

**TL;DR:** This paper reviews how LLMs can support the detection of phishing, transactional fraud, and related illicit activities, while also analyzing the security risks introduced by generative and interactive capabilities.

**Abstract:**

Large language models (LLMs) are increasingly used in financial fraud detection, where strong semantic modeling can improve the understanding of communications and the identification of suspicious behavior. This paper reviews how LLMs can support the detection of phishing, transactional fraud, and related illicit activities, while also analyzing the security risks introduced by generative and interactive capabilities. Key concerns include misuse for deception, vulnerability to adversarial prompting, limited interpretability in regulated settings, and privacy and compliance constraints. Finally, the paper outlines research directions that combine robustness, explainability, and governance to enable reliable deployment in practice.

---

## A Risk Taxonomy and Reflection Tool for Large Language Model Adoption in Public Health

**Autores:** Jiawei Zhou, Amy Z. Chen, Darshi Shah, Laura M. Schwab-Reese, Munmun De Choudhury  
**Publicação:** Proceedings of the ACM on Human-Computer Interaction · 2025  
**DOI:** https://doi.org/10.1145/3757544  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3757544  
**Citações:** 7  
**Keywords:** large language models, risk taxonomy, risk assessment, public health, health communication, harm mitigation, lived experience, information ecosystem, human-centered care, infectious disease prevention, vaccines, opioid use disorder, intimate partner violence, information behavior, reflective questions  

**Abstract:**

Recent breakthroughs in large language models (LLMs) have generated both interest and concern about their potential adoption as information sources or communication tools across different domains. In public health, where stakes are high and impacts extend across diverse populations, adopting LLMs poses unique challenges that require thorough evaluation. However, structured approaches for assessing potential risks in public health remain under-explored. To address this gap, we conducted focus groups with public health professionals and individuals with lived experience to unpack their concerns, situated across three distinct and critical public health issues that demand high-quality information: infectious disease prevention (vaccines), chronic and well-being care (opioid use disorder), and community health and safety (intimate partner violence). We synthesize participants' perspectives into a risk taxonomy, identifying and contextualizing the potential harms LLMs may introduce when positioned alongside traditional health communication. This taxonomy highlights four dimensions of risk to individuals, human-centered care, information ecosystem, and technology accountability. For each dimension, we unpack specific risks and offer example reflection questions to help practitioners adopt a risk-reflexive approach. By summarizing distinctive LLM characteristics and linking them to identified risks, we discuss the need to revisit prior mental models of information behaviors and complement evaluations with external validity and domain expertise through lived experience and real-world practices. Together, this work contributes a shared vocabulary and reflection tool for people in both computing and public health to collaboratively anticipate, evaluate, and mitigate risks in deciding when to employ LLM capabilities (or not) and how to mitigate harm.

---

## A Scoping Review of the Ethical Perspectives on Anthropomorphising Large Language Model-Based Conversational Agents

**Autores:** Andrea Ferrario, Rasita Vinay, Matteo Casserini, Alessandro Facchini  
**Publicação:** Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency · 2026  
**DOI:** https://doi.org/10.1145/3805689.3812324  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805689.3812324  
**Citações:** 1  
**Keywords:** large language models, chatbots, ethical considerations, deception, overreliance, emotional expression, epistemic expressions, AI governance, human-AI interaction  

**TL;DR:** This scoping review maps ethically oriented work on anthropomorphising LLM-based CAs across five databases and three preprint repositories and finds convergence on attribution-based definitions but substantial divergence in operationalization, a predominantly risk-focused ethical framing, and limited empirical work that links observed interaction effects to concrete design and governance guidance.

**Abstract:**

Anthropomorphisation—the phenomenon whereby non-human entities are ascribed human-like qualities—has become increasingly salient with the rise of large language model (LLM)-based conversational agents (CAs). Unlike earlier chatbots, LLM-based CAs routinely generate interactional and linguistic cues, such as first-person self-reference, epistemic, and affective expressions that empirical work shows can increase engagement. On the other hand, anthropomorphisation raises ethical concerns, including deception, overreliance, and exploitative relationship framing, while some authors argue that anthropomorphic interaction may support autonomy, well-being, and inclusion. Despite increasing interest in the phenomenon, the literature remains fragmented across domains and varies substantially in how it defines, operationalizes, and ethically evaluates anthropomorphisation. This scoping review maps ethically oriented work on anthropomorphising LLM-based CAs across five databases and three preprint repositories. We synthesize (1) conceptual foundations, (2) ethical challenges and opportunities, and (3) methodological approaches. We find convergence on attribution-based definitions but substantial divergence in operationalization, a predominantly risk-focused ethical framing, and limited empirical work that links observed interaction effects to concrete design and governance guidance. We conclude with a research agenda and design/governance recommendations for ethically deploying anthropomorphic cues in LLM-based conversational agents.

---

## A Survey on Knowledge-Oriented Retrieval-Augmented Generation

**Autores:** Mingyue Cheng, Yucong Luo, Jie Ouyang, Qi Liu, Huijie Liu, Li Li et al.  
**Publicação:** ACM Transactions on Information Systems · 2026  
**DOI:** https://doi.org/10.1145/3833415  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3833415  
**Citações:** 18  
**Keywords:** retrieval-augmented generation, external knowledge sources, retrieval mechanisms, generative models, question answering, summarization, information retrieval, retrieval efficiency, model interpretability, domain-specific adaptation, multimodal retrieval, reasoning  

**TL;DR:** The prospects for RAG in addressing real-world challenges and its potential to drive further advancements in natural language processing are outlined, including enhanced retrieval efficiency, model interpretability, and domain-specific adaptations.

**Abstract:**

Retrieval-Augmented Generation (RAG) has gained significant attention in recent years for its potential to enhance natural language understanding and generation by combining large-scale retrieval systems with generative models. RAG leverages external knowledge sources, such as documents, databases, or structured data, to improve model performance and generate more accurate and contextually relevant outputs. This survey aims to provide a comprehensive overview of RAG by examining its fundamental components, including retrieval mechanisms, generation processes, and the integration between the two. We discuss the key characteristics of RAG, such as its ability to augment generative models with dynamic external knowledge, and the challenges associated with aligning retrieved information with generative objectives. We also present a taxonomy that categorizes RAG methods, ranging from basic retrieval-augmented approaches to more advanced models incorporating multimodal data and reasoning capabilities. Additionally, we review the evaluation benchmarks and datasets commonly used to assess RAG systems, along with a detailed exploration of its applications in fields such as question answering, summarization, and information retrieval. Finally, we highlight emerging research directions and opportunities for improving RAG systems, such as enhanced retrieval efficiency, model interpretability, and domain-specific adaptations. This article concludes by outlining the prospects for RAG in addressing real-world challenges and its potential to drive further advancements in natural language processing ( https://github.com/USTCAGI/Awesome-Papers-Retrieval-Augmented-Generation ).

---

## AI Agents Need Both Hardware-Backed Security and Application-Level Guardrails

**Autores:** Barry Shichen Hu, Quoc Do Le  
**Publicação:** SysTEX@EuroSys · 2026  
**DOI:** https://doi.org/10.1145/3805690.3805726  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805690.3805726  

**TL;DR:** This work argues that this separation is flawed and that secure AI agents require both hardware-backed protection and software guardrails, and that secure AI agents require both hardware-backed protection and software guardrails.

---

## AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts

**Autores:** Tongshuang Wu, Michael Terry, Carrie Jun Cai  
**Publicação:** CHI Conference on Human Factors in Computing Systems · 2022  
**DOI:** https://doi.org/10.1145/3491102.3517582  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3491102.3517582  
**Citações:** 499  
**Keywords:** large language models, prompt chaining, human-AI interaction, system transparency, controllability, interactive system design, user study, task decomposition, model debugging, collaboration  

**TL;DR:** Chaining LLM steps together is introduced, where the output of one step becomes the input for the next, thus aggregating the gains per step, and found that Chaining not only improved the quality of task outcomes, but also significantly enhanced system transparency, controllability, and sense of collaboration.

**Abstract:**

Although large language models (LLMs) have demonstrated impressive potential on simple tasks, their breadth of scope, lack of transparency, and insufficient controllability can make them less effective when assisting humans on more complex tasks. In response, we introduce the concept of Chaining LLM steps together, where the output of one step becomes the input for the next, thus aggregating the gains per step. We first define a set of LLM primitive operations useful for Chain construction, then present an interactive system where users can modify these Chains, along with their intermediate results, in a modular way. In a 20-person user study, we found that Chaining not only improved the quality of task outcomes, but also significantly enhanced system transparency, controllability, and sense of collaboration. Additionally, we saw that users developed new ways of interacting with LLMs through Chains: they leveraged sub-tasks to calibrate model expectations, compared and contrasted alternative strategies by observing parallel downstream effects, and debugged unexpected model outputs by “unit-testing” sub-components of a Chain. In two case studies, we further explore how LLM Chains may be used in future applications.

---

## Advances, Evaluation, and Explainability of Large Language Models in Healthcare: A Systematic Review

**Autores:** Syed Umar Amin, Mohsen Guizani, M. Shamim Hossain  
**Publicação:** ACM Transactions on Multimedia Computing, Communications, and Applications · 2026  
**DOI:** https://doi.org/10.1145/3786334  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3786334  
**Citações:** 2  
**Keywords:** large language models, health care, medical question answering, hallucinations, algorithmic bias, patient privacy, explainability, multimodal large language models, clinical decision support, LLM evaluation, LLM safety  

**TL;DR:** How the field has evolved, from the first language models to the LLMs the authors have now, specifically designed or adjusted for use in the medical world are explored, to present a clear and fair picture of what LLMs can offer healthcare and what is necessary to use them safely and dependably.

**Abstract:**

Large Language Models (LLMs) have enormous potential in healthcare, but we also need to be careful and implement strong safety measures. These advanced computer systems can understand complex medical questions written in everyday language and often provide accurate medical information. This article explores how the field has evolved, from the first language models to the LLMs we have now, specifically designed or adjusted for use in the medical world. We explore how LLMs can make important language-related tasks in healthcare more efficient and effective, such as identifying medical terms, understanding how different pieces of information are connected, drawing conclusions from written text, sorting documents, and answering medical queries. We also shed light on new and exciting ways LLMs can use more than just text, like combining written information with images or other types of data. We compare some of the best recent LLMs and discuss how they can be used in everyday medical situations. We also measure how well these models perform in the biomedical field, explaining what each measurement tells us and where it falls short. Last, by discussing the biggest hurdles LLMs face in healthcare—things like generating incorrect information (hallucinations), unfair biases, protecting patient privacy, making sure the models are dependable, and fitting these new tools into how doctors and nurses already work. We also provide a roadmap for future research. We aim to present a clear and fair picture of what LLMs can offer healthcare right now and what is necessary to use them safely and dependably. This includes explaining how researchers are working to make these models easier for doctors and patients to understand. We followed the PRISMA research method to guide our review of the field, from early language models to current LLMs adapted for clinical use.

---

## An Empirical Study of Issues in Large Language Model Training Systems

**Autores:** Yanjie Gao, Ruiming Lu, Haoxiang Lin, Yueguo Chen  
**Publicação:** Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering · 2025  
**DOI:** https://doi.org/10.1145/3696630.3728538  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3696630.3728538  
**Citações:** 2  
**Keywords:** large language models, distributed training, GPU partitioning, resource waste  

**TL;DR:** The first comprehensive empirical study of issues in LLM training systems is presented, which identified common symptoms, root causes, typical fixes, and debugging and testing practices in LLM training systems.

**Abstract:**

Large language models (LLMs) have gained significant traction in recent years, driving advancements in various applications. The training and evaluation of these models depend heavily on specialized LLM training systems, which are deployed across numerous GPUs, partition LLMs, and process large datasets. However, issues in LLM training systems can lead to program crashes or unexpected behavior, reducing development productivity and wasting valuable resources such as GPUs and storage. This paper presents the first comprehensive empirical study of issues in LLM training systems. We conducted a manual analysis of 300 high-quality issue reports and corresponding fix commits from the GitHub repositories of three prominent LLM training systems: Microsoft DeepSpeed, NVIDIA Megatron-LM, and Hugging Face Transformers. Our analysis identified common symptoms, root causes, typical fixes, and debugging and testing practices in LLM training systems. Our major findings include: (1) LLM training systems exhibit issues and trends that are uncommon in traditional deep learning, such as Concurrency Error and Tensor Management Error occurring in parallel training, which are particularly difficult to diagnose and resolve. (2) The primary root causes of these issues are API Misuse (19.67%), Configuration Error (18.33%), and General Code Error (16.33%), respectively. Such issues often arise from the rapid evolution of the systems, the integration of complex external dependencies, and a configuration-driven development paradigm. (3) Current testing and debugging practices are often insufficient for identifying issues related to parallel training and large-scale numerical computations. Based on our findings, we propose several research topics and tooling improvements that can facilitate the future development of LLMs.

---

## An Intelligent Tax and Finance Question-Answering System Based on Retrieval-Augmented Generation Technology

**Autores:** Hang Wang, Wei Liu, Zhenyu Liu, Yuanyuan Qiao  
**Publicação:** Proceedings of the 2025 5th International Conference on Big Data, Artificial Intelligence and Risk Management · 2025  
**DOI:** https://doi.org/10.1145/3800227.3800275  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3800227.3800275  
**Keywords:** retrieval-augmented generation, intelligent question answering system  

**TL;DR:** Experimental results and ablation studies demonstrate that TAX-RAG significantly improves factual accuracy, retrieval relevance, and response reliability, offering an effective and scalable solution for real-world tax consultation scenarios.

**Abstract:**

Taxation and financial question-answering tasks require precise interpretation of complex regulations, domain-specific terminology, and frequently updated policies. Traditional large language models often fall short in this setting, exhibiting hallucination and factual gaps. To address these limitations, We propose TAX-RAG, a domain-adapted Retrieval-Augmented Generation framework for intelligent tax and finance question answering. TAX-RAG builds a dedicated tax knowledge base and employs a modular pipeline including data preprocessing, chunking, semantic representation, index construction, retrieval, reranking, and prompt design. Experimental results and ablation studies demonstrate that TAX-RAG significantly improves factual accuracy, retrieval relevance, and response reliability, offering an effective and scalable solution for real-world tax consultation scenarios.

---

## Benchmarking and Defending against Indirect Prompt Injection Attacks on Large Language Models

**Autores:** Jingwei Yi, Yueqi Xie, Bin Zhu, Emre Kiciman, Guangzhong Sun, Xing Xie et al.  
**Publicação:** Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 · 2025  
**DOI:** https://doi.org/10.1145/3690624.3709179  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3690624.3709179  
**Citações:** 85  
**Keywords:** large language models, LLM security, benchmarking, boundary awareness, black-box defense, Microsoft Copilot  

**TL;DR:** This work introduces the first benchmark for bindirect prompt injection attacks, named BIPIA, and evaluates existing LLMs to find them universally vulnerable, and proposes two novel defense mechanisms to address these vulnerabilities in both black-box and white-box settings.

**Abstract:**

The integration of large language models (LLMs) with external content has enabled applications such as Microsoft Copilot but also introduced vulnerabilities to indirect prompt injection attacks. In these attacks, malicious instructions embedded within external content can manipulate LLM outputs, causing deviations from user expectations. To address this critical yet under-explored issue, we introduce the first benchmark for bindirect prompt injection attacks, named BIPIA, to assess the risk of such vulnerabilities. Using BIPIA, we evaluate existing LLMs and find them universally vulnerable. Our analysis identifies two key factors contributing to their success: LLMs' inability to distinguish between informational context and actionable instructions, and their lack of awareness in avoiding the execution of instructions within external content. Based on these findings, we propose two novel defense mechanisms -- boundary awareness and explicit reminder -- to address these vulnerabilities in both black-box and white-box settings. Extensive experiments demonstrate that our black-box defense provides substantial mitigation, while our white-box defense reduces the attack success rate to near-zero levels, all while preserving the output quality of LLMs. We hope this work inspires further research into securing LLM applications and fostering their safe and reliable use. Our code is available at https://github.com/microsoft/BIPIA.

---

## Building Reactive Large Language Model Pipelines with Motion

**Autores:** Shreya Shankar, Aditya G. Parameswaran  
**Publicação:** Companion of the 2024 International Conference on Management of Data · 2024  
**DOI:** https://doi.org/10.1145/3626246.3654734  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3626246.3654734  
**Citações:** 5  
**Keywords:** prompt engineering, weak consistency, end-user feedback, LLM pipelines  

**TL;DR:** This work presents Motion, a Python framework to build and execute reactive LLM pipelines, which uses a weak consistency model to maintain prompt versions, trading off freshness for end-user latency.

**Abstract:**

Large language models (LLMs) rely on prompts with detailed and informative context to produce high-quality responses at scale. One way to develop such prompts is through reactive LLM pipelines, which incorporate new information---e.g., end-user feedback and summaries of historical inputs and outputs---back into prompts to improve future response quality. We present Motion, a Python framework to build and execute reactive LLM pipelines. Motion uses a weak consistency model to maintain prompt versions, trading off freshness for end-user latency. We demonstrate Motion with an e-commerce application that suggests apparel to wear for any event, allowing attendees to indirectly influence prompts with their queries. Attendees can interact with the demo as end-users or modify the application as developers, adding new information sources for reactive prompts.

---

## CORTEX: A Capability-Driven Reasoning Framework for Zero-Shot Large Language Model Selection

**Autores:** Kaikai Zhao, Zhaoxiang Liu, Zipeng Wang, Xin Wang, Heng Yang, Ning Wang et al.  
**Publicação:** Proceedings of the 2025 9th International Conference on Computer Science and Artificial Intelligence · 2025  
**DOI:** https://doi.org/10.1145/3788149.3788171  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3788149.3788171  
**Keywords:** multi-agent systems, natural language requirements, task decomposition, knowledge retrieval, model recommendation, explainable reasoning, DeepSeek-R1, LLM deployment  

**TL;DR:** CORTEX is a scalable and automatic framework designed for model selection in real-world applications that intelligently recommends the most suitable model based on a user’s natural language description of their application requirements, accompanied by reasonable explanations.

**Abstract:**

The proliferation of large language models (LLMs) makes real-world model selection nontrivial due to intertwined trade-offs among capability, cost, latency, and hardware constraints. To address this issue, we propose CORTEX, a scalable and automatic framework designed for model selection in real-world applications. It intelligently recommends the most suitable model based on a user’s natural language description of their application requirements, accompanied by reasonable explanations. CORTEX is a multi-agent system that integrates knowledge of 15 types of model capabilities, 105 application scenarios, and the capability boundaries of mainstream models. It includes a task decomposition agent (TDA), a knowledge retrieval agent (KRA), and a reasoning & ranking agent (RRA). The TDA utilizes DeepSeek-R1 to convert natural language description of the application requirements into a structured representation incorporating model capabilities and scenario knowledge. The KRA then retrieves a list of candidate models that satisfy these requirements based on the capability boundaries knowledge. Finally, the RRA utilizes DeepSeek-R1 to comprehensively evaluate the candidates based on performance, efficiency, cost, and user constraints, ultimately recommending the best model with highly interpretable reasoning. Comparative Experiments demonstrate that CORTEX achieves a model selection accuracy of 92.3%, significantly outperforming several comparison methods. As a practical and scalable solution to the critical "last-mile" problem of LLM selection and deployment, CORTEX is publicly accessible as a live service.

---

## Cache Your Prompt When It's Green — Carbon-Aware Caching for Large Language Model Serving

**Autores:** Yuyang Tian, Desen Sun, Yi Ding, Sihang Liu  
**Publicação:** Proceedings of the ACM on Measurement and Analysis of Computing Systems · 2026  
**DOI:** https://doi.org/10.1145/3788087  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3788087  
**Citações:** 2  
**Keywords:** large language model serving, embodied carbon, SSD storage, KV cache reuse, carbon emission reduction, service level objectives, resource allocation, Llama-3-70B, green data centers  

**TL;DR:** This paper presents GreenCache, a carbon-aware cache management framework that dynamically derives resource allocation plans for LLM serving, and analyzes the correlation between carbon emission and SLO satisfaction, reconfiguring the resource over time to keep the balance between SLO and carbon emission under dynamic workloads.

**Abstract:**

As large language models (LLMs) become widely used, their environmental impact — especially carbon emission — has attracted more attention. Prior studies focus on compute-related carbon emissions. In this paper, we find that storage is another key contributor. LLM caching, which saves and reuses KV caches for repeated context, reduces operational carbon by avoiding redundant computation. However, this benefit comes at the cost of embodied carbon from high-capacity, high-speed SSDs. As LLMs scale, the embodied carbon of storage grows significantly. To address this tradeoff, we present GreenCache, a carbon-aware cache management framework that dynamically derives resource allocation plans for LLM serving. GreenCache analyzes the correlation between carbon emission and SLO satisfaction, reconfiguring the resource over time to keep the balance between SLO and carbon emission under dynamic workloads. Evaluations from real traces demonstrate that GreenCache achieves an average carbon reduction of 15.1% when serving Llama-3 70B in the FR grid, with reductions reaching up to 25.3%, while staying within latency constraints for > 90% of requests.

---

## Co-designing Large Language Model Tools for Project-Based Learning with K12 Educators

**Autores:** Prerna Ravi, John Masla, Gisella Kakoti, Grace C. Lin, Emma Anderson, Matt Taylor et al.  
**Publicação:** Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems · 2025  
**DOI:** https://doi.org/10.1145/3706598.3713971  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3706598.3713971  
**Citações:** 28  
**Keywords:** large language models, project-based learning, K-12 teachers, co-design, teacher collaboration  

**TL;DR:** Evidence is gathered for ways LLMs can support teachers in implementing high-quality PBL pedagogy by automating routine tasks and enhancing personalized learning and proposed design guidelines for future deployment of LLM tools in PBL are proposed.

**Abstract:**

The emergence of generative AI, particularly large language models (LLMs), has opened the door for student-centered and active learning methods like project-based learning (PBL). However, PBL poses practical implementation challenges for educators around project design and management, assessment, and balancing student guidance with student autonomy. The following research documents a co-design process with interdisciplinary K-12 teachers to explore and address the current PBL challenges they face. Through teacher-driven interviews, collaborative workshops, and iterative design of wireframes, we gathered evidence for ways LLMs can support teachers in implementing high-quality PBL pedagogy by automating routine tasks and enhancing personalized learning. Teachers in the study advocated for supporting their professional growth and augmenting their current roles without replacing them. They also identified affordances and challenges around classroom integration, including resource requirements and constraints, ethical concerns, and potential immediate and long-term impacts. Drawing on these, we propose design guidelines for future deployment of LLM tools in PBL.

---

## Conversational Geographic Question Answering for Route Optimization: An LLM and Continuous Retrieval-Augmented Generation Approach

**Autores:** Jose Tupayachi, Xueping Li  
**Publicação:** Proceedings of the 17th ACM SIGSPATIAL International Workshop on Computational Transportation Science GenAI and Smart Mobility Session · 2024  
**DOI:** https://doi.org/10.1145/3681772.3698217  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3681772.3698217  
**Citações:** 1  
**Keywords:** route optimization, large language models, retrieval-augmented generation, vector search, fine-tuning, conversational question answering  

**TL;DR:** A Continuous Retrieval-Augmented Generation approach combined with fine-tuned LLMs, featuring customized node-based storage and vector search retrieval, is employed, providing a comparative analysis of the method's effectiveness and adaptability in handling diverse textual queries.

**Abstract:**

We present a pilot study exploring the potential of Large Language Models (LLMs) to interface with application programming interfaces through logical instructions, specifically within the domain of Geographic Question Answering for route optimization. This study employs a Continuous Retrieval-Augmented Generation approach combined with fine-tuned LLMs, featuring customized node-based storage and vector search retrieval. We also provide a comparative analysis of the method's effectiveness and adaptability in handling diverse textual queries.

---

## CyberBOT: Ontology-Grounded Retrieval Augmented Generation for Reliable Cybersecurity Education

**Autores:** Chengshuai Zhao, Riccardo De Maria, Tharindu Kumarage, Kumar Satvik Chaudhary, Garima Agrawal, Yiwen Li et al.  
**Publicação:** Proceedings of the 34th ACM International Conference on Information and Knowledge Management · 2025  
**DOI:** https://doi.org/10.1145/3746252.3761478  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3746252.3761478  
**Citações:** 9  
**Keywords:** retrieval-augmented generation, cybersecurity education, ontology reasoning, large language models, response validation, inquiry-based learning, artificial intelligence in education  

**TL;DR:** CyberBOT is a question-answering chatbot that leverages a retrieval-augmented generation (RAG) pipeline to incorporate contextual information from course-specific materials and validate responses using a domain-specific cybersecurity ontology.

**Abstract:**

Advancements in large language models (LLMs) have enabled the development of intelligent educational tools that support inquiry-based learning across technical domains. In cybersecurity education, where accuracy and safety are paramount, systems must go beyond surface-level relevance to provide information that is both trustworthy and domain-appropriate. To address this challenge, we introduce CyberBOT, a question-answering chatbot that leverages a retrieval-augmented generation (RAG) pipeline to incorporate contextual information from course-specific materials and validate responses using a domain-specific cybersecurity ontology. The ontology serves as a structured reasoning layer that constrains and verifies LLM-generated answers, reducing the risk of misleading or unsafe guidance. CyberBOT has been deployed in a large graduate-level course at Arizona State University (ASU), where more than one hundred students actively engage with the system through a dedicated web-based platform. Computational evaluations in lab environments highlight the potential capacity of CyberBOT, and a forthcoming field study will evaluate its pedagogical impact. By integrating structured domain reasoning with modern generative capabilities, CyberBOT illustrates a promising direction for developing reliable and curriculum-aligned AI applications in specialized educational contexts.

---

## Dango: A Mixed-Initiative Data Wrangling System using Large Language Model

**Autores:** Wei-Hao Chen, Weixi Tong, Amanda Case, Tianyi Zhang  
**Publicação:** Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems · 2025  
**DOI:** https://doi.org/10.1145/3706598.3714135  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3706598.3714135  
**Citações:** 20  
**Keywords:** data wrangling, mixed-initiative systems, large language models, data preparation  

**TL;DR:** Dango, a mixed-initiative multi-agent system for data wrangling, is proposed and it is demonstrated that Dango’s features can significantly improve intent clarification, accuracy, and efficiency in data wrangling.

**Abstract:**

Data wrangling is a time-consuming and challenging task in a data science pipeline. While many tools have been proposed to automate or facilitate data wrangling, they often misinterpret user intent, especially in complex tasks. We propose Dango, a mixed-initiative multi-agent system for data wrangling. Compared to existing tools, Dango enhances user communication of intent by allowing users to demonstrate on multiple tables and use natural language prompts in a conversation interface, enabling users to clarify their intent by answering LLM-posed multiple-choice clarification questions, and providing multiple forms of feedback such as step-by-step natural language explanations and data provenance to help users evaluate the data wrangling scripts. We conducted a within-subjects user study with 38 participants and demonstrated that Dango's features can significantly improve intent clarification, accuracy, and efficiency in data wrangling. Furthermore, we demonstrated the generalizability of Dango by applying it to a broader set of data wrangling tasks.

---

## Data-Driven Function Calling Improvements in Large Language Model for Online Financial QA

**Autores:** Xing Tang, Hao Chen, Shiwei Li, Fuyuan Lyu, Weijie Shi, Lingjie Li et al.  
**Publicação:** Proceedings of the ACM Web Conference 2026 · 2026  
**DOI:** https://doi.org/10.1145/3774904.3792813  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3774904.3792813  
**Citações:** 1  
**Keywords:** function calling, large language models, data augmentation, two-stage training  

**TL;DR:** A data-driven pipeline to enhance function calling in LLM for the authors' online, deployed financial QA, comprising dataset construction, data augmentation, and model training is proposed.

**Abstract:**

Large language models (LLMs) have been incorporated into numerous industrial applications. Meanwhile, a vast array of API assets is scattered across various functions in the financial domain. An online financial question-answering system can leverage both LLMs and private APIs to provide timely financial analysis and information. The key is equipping the LLM model with function calling capability tailored to a financial scenario. However, a generic LLM requires customized financial APIs to call and struggles to adapt to the financial domain. Additionally, online user queries are diverse and contain out-of-distribution parameters compared with the required function input parameters, which makes it more difficult for a generic LLM to serve online users. In this paper, we propose a data-driven pipeline to enhance function calling in LLM for our online, deployed financial QA, comprising dataset construction, data augmentation, and model training. Specifically, we construct a dataset based on a previous study and update it periodically, incorporating queries and an augmentation method named AugFC. The addition of user query-related samples will exploit our financial toolset in a data-driven manner, and AugFC explores the possible parameter values to enhance the diversity of our updated dataset. Then, we train an LLM with a two-step method, which enables the use of our financial functions. Extensive experiments on existing offline datasets, as well as the deployment of an online scenario, illustrate the superiority of our pipeline. The related pipeline has been adopted in the financial QA of YuanBao. https://yuanbao.tencent.com/chat/, one of the largest chat platforms in China.

---

## Defending Against Prompt Injection With a Few DefensiveTokens

**Autores:** Sizhe Chen, Yizhu Wang, Nicholas Carlini, Chawin Sitawarin, David Wagner  
**Publicação:** Proceedings of the 18th ACM Workshop on Artificial Intelligence and Security · 2025  
**DOI:** https://doi.org/10.1145/3733799.3762982  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3733799.3762982  
**Citações:** 21  
**Keywords:** prompt injection, large language models, data poisoning, embedding optimization  

**TL;DR:** DefensiveTokens are newly inserted as special tokens, whose embeddings are optimized for security, that allow a flexible switch between the state-of-the-art (SOTA) utility and almost-SOTA security at test time.

**Abstract:**

When large language model (LLM) systems interact with external data to perform complex tasks, a new attack, namely prompt injection, becomes a significant threat. By injecting instructions into the data accessed by the system, the attacker is able to override the initial user task with an arbitrary task directed by the attacker. To secure the system, test-time defenses, e.g., defensive prompting, have been proposed for system developers to attain security only when needed in a flexible manner. However, they are much less effective than training-time defenses that change the model parameters. Motivated by this, we propose DefensiveToken, a test-time defense with prompt injection robustness comparable to training-time alternatives. DefensiveTokens are newly inserted as special tokens, whose embeddings are optimized for security. In security-sensitive cases, system developers can append a few DefensiveTokens before the LLM input to achieve security with a minimal utility drop. In scenarios where security is less of a concern, developers can simply skip DefensiveTokens; the LLM system remains the same as there is no defense, generating high-quality responses. Thus, DefensiveTokens, if released alongside the model, allow a flexible switch between the state-of-the-art (SOTA) utility and almost-SOTA security at test time. The code is available here.

---

## EC-RAG: Evidence-Centric Retrieval-Augmented Generation for Medical Visual Question Answering

**Autores:** Songming Li, Jun Long  
**Publicação:** Proceedings of the 2026 International Conference on Multimedia Retrieval · 2026  
**DOI:** https://doi.org/10.1145/3805622.3810670  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3805622.3810670  
**Keywords:** medical visual question answering, retrieval-augmented generation, hallucination mitigation, radiology report generation, chest radiography, ultrasound, computed tomography, multimodal medical imaging  

**TL;DR:** EC-RAG is proposed, an Evidence-Centric Active RAG framework that shifts the paradigm to an active "seek-and-verify" cycle by integrating Active Evidence-Driven Retrieval (AEDR) for precise hypothesis formation, Visual-Consistency Verification (VCV) for pixel-level filtering, and Dual-Source Evidence Fusion (DSEF) for pixel-level filtering.

**Abstract:**

Medical Visual Question Answering (Med-VQA) necessitates rigorous knowledge-grounded reasoning to emulate the active hypothetico-deductive diagnosis of clinical experts. However, current Retrieval-Augmented Generation (RAG) approaches remain bound by a passive retrieval paradigm, where the reliance on raw queries and coarse similarity scores creates significant semantic and grounding gaps, leaving models vulnerable to hallucinations. To bridge these gaps, we propose EC-RAG, an Evidence-Centric Active RAG framework that shifts the paradigm to an active "seek-and-verify" cycle by integrating Active Evidence-Driven Retrieval (AEDR) for precise hypothesis formation, Visual-Consistency Verification (VCV) for pixel-level filtering, and Dual-Source Evidence Fusion (DSEF). Extensive validation on the comprehensive OmniMedVQA benchmark and three report generation datasets demonstrates that our method significantly enhances factual consistency, achieving a 7.77% improvement in ROUGE-L on the large-scale MIMIC-CXR dataset and securing robust generalization across 12 diverse imaging modalities, with specific accuracy gains of 8.93% in Ultrasound and 5.82% in Computed Tomography tasks.

---

## ELOQ: Resources for Enhancing LLM Detection of Out-of-Scope Questions

**Autores:** Zhiyuan Peng, Jinming Nian, Alexandre Evfimievski, Yi Fang  
**Publicação:** Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval · 2025  
**DOI:** https://doi.org/10.1145/3726302.3730333  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3726302.3730333  
**Citações:** 2  
**Keywords:** hallucination detection, retrieval-augmented generation, large language models, question answering systems, conversational AI  

**TL;DR:** A guided hallucination-based approach ELOQ, for automatically generating a diverse set of out-of-scope questions from post-cutoff documents, followed by human verification to ensure quality, and an improved detection method that enhances the reliability of LLM-based question-answering systems in handling out-of-scope questions.

**Abstract:**

Retrieval-augmented generation (RAG) has become integral to large language models (LLMs), particularly for conversational AI systems where user questions may reference knowledge beyond the LLMs' training cutoff. However, many natural user questions lack well-defined answers, either due to limited domain knowledge or because the retrieval system returns documents that are relevant in appearance but uninformative in content. In such cases, LLMs often produce hallucinated answers without flagging them. While recent work has largely focused on questions with false premises, we study out-of-scope questions, where the retrieved document appears semantically similar to the question but lacks the necessary information to answer it. In this paper, we propose a guided hallucination-based approach ELOQ . https://github.com/zhiyuanpeng/ELOQ.git, for automatically generating a diverse set of out-of-scope questions from post-cutoff documents, followed by human verification to ensure quality. We use this dataset to evaluate several LLMs on their ability to detect out-of-scope questions and generate appropriate responses. Finally, we introduce an improved detection method that enhances the reliability of LLM-based question-answering systems in handling out-of-scope questions.

# Resumo de artigos

## Towards effective teaching assistants: From intent-based chatbots to LLM-powered teaching assistants

**Autores:** Bashaer Alsafari, Eric Atwell, Aisha Walker, Martin Callaghan  
**Publicação:** Natural Language Processing Journal · 2024  
**DOI:** https://doi.org/10.1016/j.nlp.2024.100101  
**Fonte:** sciencedirect — https://www.sciencedirect.com/science/article/pii/S2949719124000499  
**Citações:** 77  
**Keywords:** educational chatbots, teaching assistants, retrieval-augmented generation, large language models, question-answer generation, LangChain, data mining education, higher education, GPT-3.5-turbo  

**Abstract:**

As chatbot technology undergoes a transformative phase in the era of artificial intelligence (AI), the integration of advanced AI models emerges as a focal point for reshaping conversational agents within the education sector. This paper explores the evolution of educational chatbot development, specifically focusing on building a teaching assistant for Data Mining and Text Analytics courses at the University of Leeds. The primary objective is to investigate and compare traditional intent-based chatbot approaches with the advanced retrieval-augmented generation (RAG) method, aiming to improve the efficiency and adaptability of teaching assistants in higher education. The study begins with the development of an Amazon Alexa teaching skill, assessing the efficacy of traditional chatbot development in higher education. To enrich the chatbot knowledge base, the research then employs an automated question–answer generation (QAG) approach using the QG Lumos Learning tool to extract contextually grounded question–answer datasets from course materials. Subsequently, the RAG-based system is proposed, leveraging LangChain with the OpenAI GPT-3.5 Turbo model. Findings highlight limitations in intent-based approaches, emphasising the need for more adaptive solutions. The proposed RAG-based teaching assistant demonstrates significant improvements in efficiently handling diverse queries, representing a paradigm shift in educational chatbot capabilities. These findings provide an in-depth understanding of the development phase, specifically illustrating the impact on chatbot performance by contrasting traditional methods with large language model-based approaches. The study contributes valuable perspectives on enhancing adaptability and effectiveness in AI-powered educational tools, providing essential considerations for future developments in the field.

**Texto completo** — HTML do editor (www.sciencedirect.com)

### Highlights

• Compares intent-based chatbots with RAG to improve educational chatbots’ efficiency.

• Highlights intent-based method limitations, showing the need for adaptive solutions.

• RAG-based chatbots show significant improvements in handling student queries.

### Keywords

Previous article in this issue

Next article in this issue

#### 5.1. Educational intent-based chatbot development (Amazon Alexa skill)

Download: Download high-res image (305KB)

Download: Download full-size image

Fig. 1. Intent-based framework.

Download: Download high-res image (31KB)

Download: Download full-size image

##### 5.1.1. Design and implementation

• Invocation: This term refers to a specific phrase spoken by the user to initiate the interaction, such as ‘Hi Alexa, open the data mining skill’.

• Intents: These function as structural models for actions that fulfil a user’s spoken request when an intent utterance is recognised. Table 1 provides a summary of the developed intents.

• Sample utterances: These are lists of phrases that users can say to invoke a particular intent.

• Slots: These are variables that can be optionally parsed and embedded in the sample utterances to activate a skill.

Table 1. Summary of skill intents.

Empty Cell | Intent name | Description
1 | TermsIntent | Answer students’ questions about the main course terminologies by providing their definitions from course materials.
2 | HowToIntent | Capture students’ requests on how a computational function/concept works.
3 | ExamplesIntent | Provide students with examples of course concepts.
4 | GeneralIntent | Address other general questions about the course content not specified by other intents.

Download: Download high-res image (71KB)

Download: Download full-size image

Fig. 2. Question processing mechanism within the termsIntent.

Download: Download high-res image (186KB)

Download: Download full-size image

Fig. 3. Alexa custom skill diagram. (Alexa, 2023a).

##### 5.1.2. Testing and evaluating

Download: Download high-res image (297KB)

Download: Download full-size image

Fig. 4. Example of Alexa responses.

##### Question–answer generation methodology.

• Cleaning the PDF content by removing graphs, tables, equations, file headers, and footers.

• Extracting information from PDF files using the Tika library in Python. Tika is a library used for document type detection and content extraction from various file formats, including PDF.

• Following the extraction, the text was split into paragraphs of the required length with well-formed sentences.

• Submitting the prepared text to the Lumos Learning QG tool.

• Exporting the generated QAs to Excel files.

##### Result and evaluation.

Table 2. Human evolution results for Lumos learning QG tool.

Metric | Percentage
Correctness | 3.62
Relevance | 4.01
Accuracy | 2.82
Clarity | 2.26
Depth of thought | 2.04
Overall helpful | 1.84

• Passage: How about inflected forms like cats versus cat? These two words have the same lemma cat but are different wordforms. A lemma is a set of lexical forms having the same stem, the same major part-of-speech, and the same word sense. The word-form is the full inflected or derived form of the word. For morphologically complex languages like Arabic, we often need to deal with lemmatization. Generated Question: What is the name of a lemma word? Generated Answer: Cat In this example, the generated QA pair are not relevant to the context scope, as the passage does not discuss the specific names of lemma words. The question itself is unclear, and the answer does not reflect a meaningful understanding of the question. This highlights a limitation in the tool’s ability to analyse the context and generate accurate QA pairs that reflect the passage content.

• Passage: The goal of classification is to take a single observation, extract some useful features, and thereby classify the observation into one of a set of discrete classes. One method for classifying text is to use handwritten rules. There are many areas of language processing where handwritten rule-based classifiers constitute a state-of-the-art system, or at least part of it. Generated Question: What is the goal of classification? Generated Answer: A single observation. The answer in this example is incomplete. It lacks the necessary details to fully convey the comprehensive goal of classification described in the passage, which can be summarised as ‘classifying the observation into one of a set of discrete classes’.

• Passage: If a chatbot is human-like, users are also more likely to disclose private information, and less likely to worry about the harm of this disclosure (Ischen et al. 2019). In general, chatbots that are trained on transcripts of human–human or human–machine conversation must anonymise personally identifiable information. Generated Question: Who is less likely to worry about the harm of a chatbot? Generated Answer: Ischen et al. 2019. The question generated is poorly constructed and lacks clarity and precision. The answer, ‘Ischen et al. 2019’, indicates that the tool had difficulty accurately analysing the reference in the passage. The reference in parentheses was mistakenly interpreted as being integral to the sentence’s meaning, revealing a limitation in the tool’s capability to handle citations. As a result of this misinterpretation, an incorrect QA pair was generated.

#### 5.2. Evolution to large language model-based educational chatbot

• Prompts: This is essentially the main component for communicating with and guiding the behaviour of AI’s LLMs. It consists of natural language text that incorporates the user’s input (question) and instructions for the LLM on how to process the provided input in order to generate a desired response. A prompt may include a one-shot or a set of few-shot examples to direct the language model towards improved performance. LangChain offers several categories of specialised prompt templates for generating prompts for language models. A prompt template is a predefined method of creating a prompt for the model. It can include specific instructions for the language model, a few-shot example, and a given context along with the user’s questions.

• Models: There are three main types of models used in LangChain: LLMs, chat models, and text embedding models. LLMs are the main class of models used in LangChain. These models take a text string as input and produce a text string as output. Chat models are a more structured API that works with Chat Messages as input and output. Finally, the text embedding model takes the input as text and converts it into a list of numbers (floats) to create a numerical representation of the provided text.

• Chains: In LangChain, the term ‘chains’ refers to the technique of creating a series of operations by combining LLMs with other components to form a unified application. These chains can connect one or multiple LLMs to a user prompt, allowing interaction with the provided text or other data in a specific manner. This approach is particularly useful for streamlining the development of intricate applications that involve chaining LLMs, either with each other or with other components. As depicted in Fig. 5, a simple chain may consist of a user input that is formatted using a specified prompt template and then processed using a language model to generate the desired output. For more complex tasks, multiple chains can be combined, with the output of one chain serving as the input for the next chain.

• Memory: In LangChain, the memory component enables LLM applications to store and retrieve information from previous interactions. The memory system is essential for developing a conversational interface (‘chatbots’) that can maintain context throughout a conversation and respond appropriately to follow-up questions. LLMs themselves are stateless, meaning that each request is handled independently of other interactions. Therefore, a memory component is required to provide LLMs with the user’s previous requests, which will be processed alongside the user’s new query.

Download: Download high-res image (145KB)

Download: Download full-size image

Fig. 5. Simple chain structure.

##### 5.2.1. Design and implementation

• Load: We used LangChain’s Unstructured-PDFLoader to load our data, which included lecture transcripts and textbook chapters provided as PDFs.

• Splitting Data to Chunks: Typically, the context window of LLMs requires breaking long texts into smaller, semantically meaningful chunks that fit within the model’s token limit. The context window of an LLM refers to the number of tokens it can accept as input to generate responses. Tokens can be characters, words, sentences, or other segments of text. To facilitate easier processing, the PDFs were segmented into smaller chunks using LangChain’s CharacterTextSplitter.

• Embeddings: LLMs require text embeddings as a fundamental building component. These serve as a link between the neural network of the language model and the raw text input. Embeddings are numerical representations of words or phrases that capture their semantics and context, enabling the language model to understand the meaning and relationship of the given text in order to generate coherent and meaningful responses that mimic natural human communication. We utilised OpenAI Embeddings ‘text-embedding-ada-002’, which is recommended by OpenAI for its improved performance, cost-effectiveness, and ease of use. OpenAI Embeddings measure the relatedness of texts in various contexts for purposes such as text search, clustering, or classification. These embeddings are stored using a vector store, and for storing and retrieving embeddings, we used the Facebook AI Similarity Search (FAISS) Library. This library allows developers to quickly search for embeddings of multimedia documents that are similar to each other (Meta, 2023). When a user submits a question, the same model is used to embed the query, and relevant chunks with context are retrieved. Subsequently, the retrieved chunks are concatenated with the query and fed to the LLM chain to generate an answer.

• Retrieval: Upon receiving a question from a user, its embedding is calculated, and relevant segments are retrieved from the FAISS database using vector retrieval. These retrieved segments, along with the question, are then sent to the LLM to generate contextually appropriate answers to user queries.

Download: Download high-res image (167KB)

Download: Download full-size image

Fig. 6. Retrieval-augmented generation-based chatbot framework.

Download: Download high-res image (109KB)

Download: Download full-size image

Download: Download high-res image (73KB)

Download: Download full-size image

##### Human evaluation.

Table 3. Example 1 of automatic evaluation with GPT-4.

Question | What is the process of text normalisation?
Reference answer | Normalising text means converting it to a more convenient, standard form. The main steps in text normalisation are tokenisation, lemmatisation, stemming, sentence segmentation, and Parts-of-Speech (POS) tagging.
Predicted answer | 
Evaluation | 
Score | 8

Table 4. Example 2 of automatic evaluation with GPT-4.

Question | What are the different approaches for extracting relations among entities in natural language processing?
Reference answer | Relations among entities can be extracted by pattern-based approaches, supervised learning methods when annotated training data is available, lightly supervised bootstrapping methods when small numbers of seed tuples or seed patterns are available, distant supervision when a database of relations is available, and unsupervised or Open IE methods.
Predicted answer | 
Evaluation | 
Score | 6

Table 5. Human evaluation results for retrieval-augmented generation–based chatbot.

Metric | Percentage
Correctness | 4.7
Relevance | 4.9
Accuracy | 4.63
Clarity | 4.78
Depth of thought | 4.65
Overall helpful | 4.88
Overall Average ≈ 4.76

### 6. Discussion and future directions

Table 6. Example of complex question.

Question | What are the fundamental differences between generative classifiers like naive Bayes and discriminative classifiers like logistic regression in the context of machine learning for text classification?
Predicted answer | 

Table 7. Comparison of intent-based vs. retrieval-augmented generation approaches.

Aspect | Intent-based approach | Retrieval-augmented generation approach
Foundation | Primarily relies on predefined intents and corresponding responses, limiting the scope of educational content. | Combines retrieval and generation mechanisms, allowing access to a broader range of educational content.
Flexibility | Limited flexibility as responses are based on predefined intents, which may not address all educational topics. | Highly flexible, adapts to a wide range of student queries through retrieval, handling various educational topics.
Adaptability | Struggles with handling queries outside predefined intents, potentially not considering complex educational queries. | Adaptable to diverse educational queries by retrieving and augmenting relevant information, providing comprehensive answers.
User interaction | Students need to conform to predefined intents for effective interaction, which may limit their engagement and exploration. | Allows more natural and context-aware interactions, encouraging deeper student engagement with educational material.
Knowledge base | Requires a well-defined set of intents and associated responses, which may become outdated and limited in educational scope. | Knowledge base can be expanded by retrieving information as needed, ensuring that educational content is up-to-date and comprehensive.
Development complexity | Generally simpler development due to predefined intents, facilitating the development process but resulting in less dynamic educational applications. | May require more complex development, especially in designing prompts and integrating retrieval, but offers richer educational interactions.
Handling new information | Challenges in handling queries that do not align with predefined intents, limiting the ability to address new or emerging educational queries. | More proficient at handling novel queries by retrieving and generating relevant educational information.
Use of artificial intelligence models | May involve AI models for intent recognition and response mapping, which could be limited in educational adaptability. | Integrates AI models for both retrieval and generation, combining their strengths to offer more robust educational responses.
Scalability | Scalability may be limited by the need for constant intent expansion, which can be resource-intensive and slow to adapt to new educational content. | Potentially more scalable, as new educational content can be much more easily embedded.
Context awareness | Limited context awareness as responses are typically based on current intent, which can limit the ability to provide context-rich educational experiences. | Improved context awareness as responses can be augmented by retrieved information, facilitating deeper and more context-rich educational interactions.

### Appendix. Data mining and text analytics lecture transcripts

• Text pre-processing transcript.

• Data mining and text analytics online communities and applications transcript.

• Text classification transcript.

• N-grams transcript.

• Tagging POS and NER transcript.

• Scaling to big data transcript.

• Word meanings transcript.

• Machine Translation: Challenges and Approaches transcript.

• Information Extraction: Extracting Named Entities and Relations from Text transcript.

• Cheat, NLTK, SpaCy: Text Analytics in Python transcript.

• Coursework report: produce an applied text analytics research proposal transcript.

• Chatbots and Dialogue Systems transcript.

• University student surveys using chatbots: Artificial Intelligence conversational agents transcript.

• Information retrieval and web search transcript.

• Multi-word expressions transcript.

• Deep learning of text understanding: Google’s BERT transcript.

#### Based on reading popularity

Research article Open access Using Social Network Analysis to gain insight into social creativity while designing digital mathematics books Christian Bokhove, …, Manolis Mavrikis Social Sciences & Humanities Open • Volume 8, Issue 1 • 2023 • Article 100497 View PDF

Research article Open access Conceptual commonsense-aware attentive modeling with pre-trained masked language models for humor recognition Yuta Sasaki, …, Yuhki Shiraishi Natural Language Processing Journal • Volume 9 • 2024 • Article 100117 View PDF

Research article Full text access Mapping student-AI interaction dynamics in multi-agent learning environments: Supporting personalized learning and reducing performance gaps Zhanxin Hao, …, Yu Zhang Computers & Education • Volume 241 • 2026 • Article 105472 View PDF

Research article Open access Scholarly recommendation system for NIH funded grants based on biomedical word embedding models Zitong Zhang, …, Hulin Wu Natural Language Processing Journal • Volume 8 • 2024 • Article 100095 View PDF

Research article Open access Pre-service teachers' perceptions and intentions regarding the use of chatbots through statistical and lag sequential analysis Tzu-Chi Yang, Jian-Hua Chen Computers and Education: Artificial Intelligence • Volume 4 • 2023 • Article 100119 View PDF

Research article Open access Human-GenAI interaction for active learning in STEM education: State-of-the-art and future directions Sofie Otto, …, Lykke Brogaard Bertel Computers & Education • Volume 239 • 2025 • Article 105444 View PDF

### Cited by (91)

Research article Open access Empowering preservice teachers’ AI literacy: Current understanding, influential factors, and strategies for improvement Pei B., …, Jing X. Computers and Education: Artificial Intelligence • Volume 8 • 2025 • Article 100406 Show abstract Artificial Intelligence (AI) holds significant potential in transforming future educational practices by enhancing teaching and learning. However, its full realization heavily depends on teachers' AI literacy, which significantly influences their engagement levels with AI technologies and their abilities to adopt AI technologies effectively in similar settings. In this study, we conduct a holistic analysis examining pre-service teachers' AI literacy for providing insights about current understanding of AI technologies, perceptions of the applications of AI in education, ethical issues and strategies for effectively enhancing AI literacy. Guided by Bloom's Taxonomy, a comprehensive, layered survey was designed to systematically evaluate pre-service teachers' AI literacy competencies. The Technology Acceptance Model 3 (TAM3) was mapped onto each layer to design questions that identify factors influencing pre-service teachers' AI literacy proficiency. The survey was administered to a sample of 200 pre-service teachers in a large public university. Descriptive analysis and ANOVA were conducted to examine how the influential factors influence AI literacy within and across layers. We also conducted a thematic analysis to identify the most preferred strategies to enhance pre-service teachers' AI literacy. The analytical results revealed a significant gap in understanding levels of AI mechanisms among pre-service teachers and highlighted its positive associations with their engagement, perceptions and ethical considerations of AI in educational settings. The findings also underscored the importance of hands-on, practical training and in-person collaborative learning for enhancing pre-service teachers' AI literacy. Finally, we discussed practical implications regarding implementing training and professional development programs for fostering pre-service teachers' AI literacy.

A Systematic Literature Review of Retrieval-Augmented Generation: Techniques, Metrics, and Challenges Brown A., …, Devereux B. Big Data and Cognitive Computing • Volume 9 • 2025 • Article 320

AI-Powered Educational Agents: Opportunities, Innovations, and Ethical Challenges Córdova-Esparza D.-M. Information (Switzerland) • Volume 16 • 2025 • Article 469

PAIGE: Examining Learning Outcomes and Experiences with Personalized AI-Generated Educational Podcasts Do T.D., …, Sarda N. Conference on Human Factors in Computing Systems - Proceedings • 2025 • Article 896

LPITutor: An LLM based personalized intelligent tutoring system using RAG and prompt engineering Liu Z., …, Verma P.K. PeerJ Computer Science • Volume 11 • 2025 • Article e2991

A Comprehensive Survey of Retrieval-Augmented Large Language Models for Decision Making in Agriculture: Unsolved Problems and Research Opportunities Vizniuk A., …, Smola̧g J. Journal of Artificial Intelligence and Soft Computing Research • Volume 15 • 2024

#### Citations

Citation Indexes 89

Policy Citations 3

#### Captures

Mendeley Readers 249

#### Mentions

News Mentions 1

---

## An LLM-Driven Chatbot in Higher Education for Databases and Information Systems

**Autores:** Alexander Tobias Neumann, Yue Yin, Sulayman Sowe, Stefan Decker, Matthias Jarke  
**Publicação:** IEEE Transactions on Education · 2025  
**DOI:** https://doi.org/10.1109/TE.2024.3467912  
**Fonte:** ieee — https://ieeexplore.ieee.org/document/10706931  
**Citações:** 165  
**Keywords:** Chatbots, Education, Computer science, Databases, Accuracy, Mentoring, Information technology, Information systems, Adaptation models, Vectors, Information System, Interactive, Usability, Learning Process, Computer Science, Teaching Process, Perceived Usefulness, Self-regulated Learning, Help-seeking Behavior, Learning Management System, Cronbach’s Alpha, Educational Settings, User Experience, Confusion Matrix, Behavioral Intention, Response Accuracy, Student Engagement, User Behavior, Internal Variability, User Input, Perceived Ease Of Use, Aachen University, Lecture Content, Shaping Students, Artificial Intelligence Tools, Student Feedback, Text Generation, External Variables, User Satisfaction, Exam Preparation, Chatbots, higher education, large language model (LLM), moodle, moodlebot  

**TL;DR:** The findings indicate that educational chatbots are suitable for integration into courses to improve personalized learning and reduce teacher administrative burden, although improvements in automated fact-checking are needed.

**Abstract:**

Contribution: This research explores the benefits and challenges of developing, deploying, and evaluating a large language model (LLM) chatbot, MoodleBot, in computer science classroom settings. It highlights the potential of integrating LLMs into LMSs like Moodle to support self-regulated learning (SRL) and help-seeking behavior. Background: Computer science educators face immense challenges incorporating novel tools into LMSs to create a supportive and engaging learning environment. MoodleBot addresses this challenge by offering an interactive platform for both students and teachers. Research Questions: Despite issues like bias, hallucinations, and teachers’ and educators’ resistance to embracing new (AI) technologies, this research investigates two questions: (RQ1) To what extent do students accept MoodleBot as a valuable tool for learning support? (RQ2) How accurately does MoodleBot churn out responses, and how congruent are these with the established course content? Methodology: This study reviews pedagogical literature on AI-driven chatbots and adopts the retrieval-augmented generation (RAG) approach for MoodleBot’s design and data processing. The technology acceptance model (TAM) evaluates user acceptance through constructs like perceived usefulness (PU) and Ease of Use. Forty-six students participated, with 30 completing the TAM questionnaire. Findings: LLM-based chatbots like MoodleBot can significantly improve the teaching and learning process. This study revealed a high accuracy rate (88%) in providing course-related assistance. Positive responses from students attest to the efficacy and applicability of AI-driven educational tools. These findings indicate that educational chatbots are suitable for integration into courses to improve personalized learning and reduce teacher administrative burden, although improvements in automated fact-checking are needed.

**Texto completo** — HTML do editor (ieeexplore.ieee.org)

### Article text

Alerts Alerts Manage Content Alerts Add to Citation Alerts

### Alerts

Download PDF

Download References

Request Permissions

Save to

Alerts

### Introduction

In the rapidly evolving technological landscape, Artificial Intelligence (AI) has carved a niche in various sectors, including education. Chatbots, especially AI-driven chatbots, have become a prominent educational tool [1], [2]. They are software applications designed to simulate human conversation through predetermined scripts or, increasingly, more sophisticated natural language processing (NLP) algorithms [3]. Their capacity to generate human-like responses showcases the influence AI on the broader educational paradigm. The growing complexity and diversity of data within learning management systems (LMS) present unique challenges, hindering their effectiveness. Former iterations of AI-driven chatbots face challenges, gaining acceptance and achieving widespread success in educational settings. These challenges primarily revolve around their limited understanding of context, rigid script-based interactions, and suboptimal user experiences [2]. However, the advent of large language models (LLMs), including technologies, such as ChatGPT, marks a significant evolution from these earlier AI-driven bots [4]. This is where LLM-driven solutions promise transformative change. Throughout this article, AI-driven chatbots are defined as the AI solutions for chatbots before the advent of LLM, which are characterized as LLM-driven chatbots enabling more dynamic and contextually aware interactions. LLM-driven chatbots can fill information gaps and significantly improve user experiences in such environments. For instance, chatbots can serve as relentless academic aides when integrated into an LMS [5]. They can help students find pertinent course materials or resolve organizational issues by employing similarity searches over the course content. Their unique capacity to provide on-demand explanations and entertain follow-up queries positions them as virtual tutors. With rapid, anytime-available support, these systems potentially eliminate the need for students to repeatedly reinforce already understood materials, thus enhancing their learning progress and overall motivation [6].

This article presents MoodleBot, an open-source chatbot designed to provide feedback on lecture content and tasks tailored for self-regulated learning (SRL). Moodle, 1 the platform for which MoodleBot is developed, is a widely used LMS in higher education and used by the RWTH Aachen University. The study focuses on its deployment among students from the lecture on “Databases and Information Systems” at the RWTH Aachen University, a mandatory bachelor’s computer science lecture with over 700 participants. With its human-like conversational process, MoodleBot offers students an experience similar to interacting with a real tutor but with the advantages of immediate responses and round-the-clock availability. This article addresses the following research questions.

RQ1: To what extent do students accept MoodleBot as a valuable tool for learning support?

##### RQ1:

To what extent do students accept MoodleBot as a valuable tool for learning support?

RQ2: How accurately does MoodleBot churn out responses, and how congruent are these with the established course content?

##### RQ2:

How accurately does MoodleBot churn out responses, and how congruent are these with the established course content?

The implications of the findings extend beyond academic discourse, holding value for educators, administrators, and software developers by shedding light on the dynamics and potential of LLM-augmented tools in educational settings.

### Background and Related Work

AI-driven chatbots in educational contexts have seen significant advances in their application within academia. These chatbots fulfill diverse functions, including providing instant feedback on assignments [2], [7], [8], assisting with course-related queries [2], [9], [10], streamlining enrollment processes [10], [11], and disseminating campus information [10], [12], [13]. Mentoring bots, a specialized subset, offer 24/7 instructional and support services [6], notably easing the workload of teachers and teaching assistant (TA) [14]. Conversational agents show promise for delivering personalized tutoring in educational contexts [15], [16]. Some studies demonstrate the efficacy of mentoring chatbots in providing individualized learning support [17]. Recent work explores using chatbots to tailor tutoring to each learner’s needs and characteristics [18]. Such bots can be seamlessly integrated into online courses [5], [6]. They can enhance student engagement within the learning community [19]. The output accuracy of most educational chatbots highly depends on the input data [20]. Personalized hybrid e-learning models are suggested to consider a student’s personality, tailoring the chatbot’s interactions accordingly [21]. Another application of chatbots is in teaching programming languages, with findings indicating a significant uptick in user satisfaction when social dialogue is incorporated [22].

#### A. Self-Regulated Learning

SRL is a paradigm that enables learners to enhance their education by setting specific goals, monitoring performance, and adjusting behaviors through cognitive, metacognitive, and motivational strategies to optimize outcomes [23]. The three-layer model of SRL includes the regulation of processing modes, learning processes, and the self, emphasizing the dynamic interplay between these elements [24]. Self-regulation enhances academic performance by integrating cognitive strategies and metacognition [25], as well as motivation, engagement, and social support [26]. Integrating chatbots in e-learning platforms can reduce feelings of isolation and detachment while boosting intrinsic motivation and perceived competence [27], especially when combined with traditional teacher support [28]. Deploying AI-driven chatbots, guided by pedagogical strategies, such as goal setting and personalized feedback, can enhance learners’ SRL skills [29]. These chatbots can support goal articulation [30] and pose strategic questions to facilitate SRL [31]. The application of LLM exemplifies this dynamic, as these tools deliver immediate, contextually appropriate information and support learners in reflective and self-regulatory practices [32]. LLM can simultaneously challenge and support the development of SRL skills. Learners can benefit from receiving alternative solutions, being exposed to diverse perspectives, and encouraging critical thinking. However, it is important to note that excessive use of LLM may diminish the learner’s capacity for SRL. Therefore, educators must design interventions that balance the facilitation and disruption of self-regulation [33].

#### B. Students’ Help-Seeking Behaviors

While engaging in SRL, students may encounter challenges or identify gaps in their knowledge and skills. Help-seeking is an essential academic strategy for self-regulation that facilitates learning [34]. It is considered an important form of behavioral self-regulation that can cognitively, behaviorally, and emotionally engage learners [35]. However, many students, particularly adolescents, avoid seeking help even when they need it [36]. This help avoidance behavior can be attributed to various factors, including competence concerns (fear of appearing incompetent) and autonomy concerns (desire to work independently) [36]. Students with low self-efficacy (SE) or those focused on performance goals are particularly prone to avoiding help-seeking due to concerns about negative judgments from teachers or peers [36]. Effective help-seeking is timely and context-dependent, with early help-seeking in problem-solving associated with better learning outcomes [37]. In online environments, it is beneficial to seek help on challenging steps; however, overuse can reduce learning outcomes [38]. Effective help-seeking behaviors include asking precise questions and persisting in seeking help, while effective help-giving involves providing detailed explanations and monitoring student understanding [39]. Chatbots, as AI-driven educational tools, have the potential to address these concerns and alleviate help avoidance behavior. They provide a private, nonjudgmental space for students to ask questions without fear of embarrassment in front of peers or teachers [36]. Regarding accessibility, office hours are essential for addressing students’ queries about assignments [40], course content, and administrative issues. Integrating LLM can enhance these interactions by offering real-time, accessible solutions and promoting more proactive and effective engagement with learning resources.

#### C. LLM-Driven Education

In the domain of natural language generation (NLG), LLM represent a significant advancement, particularly those founded on the transformer architecture with self-attention mechanisms [41]. These models are distinguished by their capability to produce contextually relevant and coherent human-like text [42]. The generative pretrained transformer (GPT) series, a family of models, has gained recognition in this space. Among these, ChatGPT, a specialized chat model developed by OpenAI, is built on the architecture of specific GPT versions and tailored for interactive applications. 2 OpenAI offers specialized fine-tuning for the GPT models, facilitating deployment across diverse domains and applications.

LLM offer versatile support in education, facilitating tasks, such as providing comprehensive feedback on assignments, discussing intricate concepts, annotating code to highlight errors, and generating exercises along with sample solutions [43]. The research presented in this article builds upon these capabilities, providing comprehensive mentoring support to students, addressing their needs ranging from organizational queries to conceptual discussions and exercise generation for exam preparation. This holistic approach sets the presented work in this article apart from studies [44], [45], which focus primarily on content support and administrative queries.

However, challenges remain, including control over its responses [44], [46] and occasional “hallucinations,” where it produces incorrect content [47], [48], [49], [50]. The presented solution in this article adopts an retrieval-augmented generation (RAG) approach [51] that can enhance the accuracy and correctness of responses [44], [52]. Similar works offer either administrative and content support [45], [52], exercise support [53], [54], [55] or exercise generation [56], [57], but not both in one package. Furthermore, instead of using a pool of tasks only [44], [50], this approach involves assessing students’ acceptance of the tool using technology acceptance model (TAM). While existing studies often discuss the accuracy of such models [44], [45], [48], [52], [54], [56], [57], none of them conduct a TAM analysis. Despite students’ awareness of these models [58], only a few explored their willingness to adopt them in their current state [52], [59]. Moreover, while the technical scalability is frequently mentioned [46], [50], [52], [60], [61], only one examined the associated costs [52]. Among the reviewed studies, one notable paper addresses a similar database course utilizing an RAG approach [44]. However, their validation process is limited to the course instructor’s assessment, omitting a comprehensive evaluation of student acceptance and feedback. In contrast, the approach presented in this article extends the validation to include studies on student engagement and acceptance, providing a more holistic understanding of the educational impact and practical efficacy of integrating chatbots in academic settings.

### MoodleBot

MoodleBot was developed by the authors as part of the tech4compKI project, 3 a German research project aimed at supporting personalized learning and skill development through hybrid AI mentoring. MoodleBot represents a pioneering effort in integrating an advanced LLM-driven chatbot into the RWTH academic course framework. The open-source integration 4 of the chatbot MoodleBot into Moodle targets two interrelated use cases relevant to enhancing pedagogical and operational support for academic environments. Today’s academic courses often overwhelm students with a vast amount of information [62], sometimes causing them to lose track of essential organizational details [5], [63]. MoodleBot is a reference point that helps learners to find and reconcile this information quickly. Beyond this organizational assistance, the chatbot’s pedagogical role is to serve as an always-available tutor [7], particularly during intense periods, such as exam preparation [63]. The primary goal of MoodleBot is to dynamically generate exercises and solve questions by deploying these chains and using Python-based functions. The bot aids students in clarifying doubts and comprehending complex lecture content. MoodleBot’s response accuracy is paramount, as misinformation can significantly affect the learner’s progress [64]. Concurrently, the benefits of MoodleBot extend to educators. Traditional Q&A forums, while beneficial, often become overloaded with repetitive and basic inquiries [5]. Educators can focus on more complicated, content-related questions by delegating most of these routine questions to MoodleBot. This enhances efficiency and elevates the quality of discourse within these forums. It is important to mention MoodleBot’s fallibility. Traditional forums remain crucial, as they serve as channels for substantive discussions that may be beyond the scope of the chatbot and ensure a holistic educational experience.

#### A. Architecture

MoodleBot’s design is not a generic, one-size-fits-all solution. Instead, it is a specialized, adaptive system engineered to meet a single course’s specific needs and learning objectives. This approach requires an own instance of MoodleBot with its personalized agent for each course. It is fed with tailored materials, such as lecture slides, supplementary resources, and course-specific lecture notes. The architecture of MoodleBot, as illustrated in Fig. 1, integrates various tools and frameworks. OpenAI’s pretrained models are utilized for optimal performance. They can be enhanced by compatible frameworks, such as LangChain 5 and LlamaIndex. 6 The following describes the core components and their functionalities:

System overview of MoodleBot’s architecture.

Show All

Data Acquisition: MoodleBot can source its data from PDFs, including lecture notes, lecture slides, and exercise sheets.

Data Vectorization: Once acquired, the raw data undergoes a transformation process where it is converted into vectors. These vectors are then stored in a Weaviate database. 7

Moodle Integration: MoodleBot seamlessly integrates with Moodle’s native chat interface and forums. This ensures users experience a consistent interface while benefiting from the enhanced capabilities of MoodleBot.

LangChain Agent: MoodleBot utilizes LangChain agents equipped with modular tools to improve functionality. Initially, the chatbot uses two tools, a Question Generator and a Answer Generator. The Question Generator assists in formulating relevant questions based on the content. In contrast, the Answer Generator provides accurate answers to user queries by tapping into the stored vectorized data. The LangChain agent is backed by advanced LLMs, specifically GPT-4 [4].

Cost and Chat History: A MongoDB 8 instance stores all associated costs and chat histories with MoodleBot to maintain transparency and aid in future optimizations.

#### B. Data Ingestion and Retrieval

The chatbot needs knowledge from a lecture to provide support. A Weaviate vector database is created with LangChain and LlamaIndex to take documents from various sources in various formats. A document loader transfers lecture notes to the vector database. This ensures systematic indexing of the information and its subsequent retrievability. The application utilizes LangChain’s text splitter to break down longer text into manageable chunks. Each piece of text is then processed by the OpenAI Embedding model, which is accessible through LlamaIndex. This model converts the content into high-dimensional vectors, an essential step for efficient similarity search and information extraction.

#### C. Langchain Agent

The LangChain agent is a mediator bridging the gap between user input and the sophisticated functionalities of the LLM. Its role is to determine the actions following a user’s interaction. The agent formulates a request that bundles the agent’s prompt and the given user input, subsequently sending it to the LLM. The LLM then evaluates the information provided and checks whether the user’s input, in conjunction with the agent’s prompt, is sufficient for an immediate response. If it determines that it is sufficient, it returns a final response. If, on the other hand, it determines that additional context or data is required, the LLM responds with further instructions for the agent. Typically, these instructions cause the agent to leverage various tools to extract or derive additional context. After this information retrieval process, the LLM is invoked again with a more extensive dataset. At this point, the LLM will either generate a comprehensive response for the user or conclude that the existing context remains insufficient, thereby instructing the agent to utilize the tools again.

##### 1) Agent Prompt:

To ensure optimal results, effective prompts are needed. A prompt should clearly and concisely convey knowledge, incorporating four key components: 1) instruction; 2) context; 3) input data; and 4) output indicator [65]. Together, these components ensure that the LLM understands and processes the request to deliver optimal results. Below, more details are provided about these components’ nuances and how they were integrated into the Moodle LangChain agent. The instructions should be expressed clearly and comprehensibly so that the LLM can provide accurate responses. The context, which should be brief and directly relevant to the task at hand, is shaped by the agent’s role and goal. The agent is tailored to specific use cases, increasing its efficiency and relevance [65].

A LangChain agent prompt consists of multiple components, including the agent’s instruction, background context, user input, and an output indicator. It already adheres to the suggested prompt pattern. The instruction consists of the personality, the goal of the agent/tool, its tasks and the limitations. The background context is an additional source of information that can be manually inserted into the prompt or retrieved from the vector database. User input is a query submitted by the user, and the output indicator marks the beginning of the generated text. LangChain provides various prompt templates to use. The ChatPromptTemplate is tailored to the conversational context and is divided into four parts: 1) System Prompt; 2) Chat History; 3) User Input; and 4) Agent Scratchpad. The System Prompt section specifies the agent’s personality and must be tailored to the specific case. For MoodleBot, the System Prompt is as follows.

You are a tutor for the lecture Databases and Information Systems at RWTH Aachen University. Your goal is to support the students during the lecture and to answer questions about the lecture by having a conversation with them. You can generate exercises for the students and correct their answers. Since the lecture is held in German, you should also answer in German. You can only answer questions about the lecture. You should refuse to answer any content not part of the lecture. Always be friendly, and if you cannot answer a question, admit it. In summary, the tutor is a powerful system that can help with various tasks and provide valuable insight and information on various topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Tutor is here to help.

The agent acts as a tool during a lecture, facilitating answering questions and automatically generating exercises. Therefore, the agent focuses on the lecture’s content and is designed to ignore irrelevant or off-topic queries. Each sentence is tested for optimal outcomes using contextual information and a chain of thought [66]. User input is treated as an input variable, and the LLM temperature determines the randomness of the outputs. The temperature is set to zero to avoid incorrect terms in an educational context.

##### 2) Agent Type:

BaseMultiActionAgent was chosen as the most appropriate agent type for MoodleBot. This choice derives from the requirements that the bot should be able to use multiple tools with different functionalities and have interactive dialogues with students. Since the purpose is to chat, a chat model is necessary. During the implementation phase, two leading LLMs: 1) gpt-3.5-turbo and 2) gpt-4 were tested. After manually comparing some generated answers, gpt-4 showed superior ability in formulating answers and explaining lecture material. Unlike gpt-3.5-turbo, gpt-4 can identify the need for a tool with ease. Therefore, the chat model for the agent uses gpt-4 as its LLM.

##### 3) Tools:

An agent uses tools to perform specific tasks efficiently. These tools can range from simple utilities to more complex entities, such as the composition of multiple chains.

##### a) Answer Generation Based on Context:

LangChain’s create-stuff-documents-chain was adopted to generate answers in a particular lecture context. The retrieval mechanism relies on the Weaviate vector index containing embedded lecture data. The system searches the database using similarity and retrieves the most relevant documents. This search is facilitated using the same embedding model used when the database was initially set up. LangChain provides multiple chain types: stuff, refine, reduce, map-reduce and map-rerank. The stuff chain is designed to accept a list of collected documents, integrate them into a provided prompt, and then forward them to the target LLM. It is also faster in processing than its counterparts. However, to ensure both efficiency in similarity search and low costs, the number of documents fed into the process is limited to five. 9 The following custom prompt is configured to ensure that the create-stuff-documents-chain returns the best possible response.

As a tutor for the lecture databases and information systems, your goal is to provide accurate and helpful information about the lecture. You should answer the user’s inquiries as best as possible based on the context and chat history provided and avoid making up answers. If you do not know the answer, simply state that you do not know. Answer the question in German.

The LLM tool generates results derived from concise prompts and the context of data retrieval. It is capable of answering both organizational and content questions about lectures. The scenario depicted in Fig. 2 exemplifies the answering of an organizational question.

User is inquiring about the process for obtaining admission to take an exam.

Show All

##### b) Question Generation:

To act like a tutor and support learners, the QAGeneration-Chain is used to generate rudimentary practice exercises for students. These can be useful to review the lecture content and have a similar effect as flashcards. The MongoDB database contains 170 question-answer pairs. Within this dataset, repetitions were identified, with ten pairs flagged as organizational and 20 as inaccurate. These incorrect entries were manually removed from the database. This tool is programmed to retrieve questions at a faster rate than generating them at runtime. As shown in Fig. 3, it responds with random exercise questions, which are helpful for students to learn from, and helps them comprehend the topic by providing an answer. While it ensures prompt delivery of answers, the basic nature of the generated questions could limit their applicability in advanced practice sheets or other specialized scenarios.

User has requested an exercise question, and MoodleBot is assisting with the solution.

Show All

##### c) Specific Question Generation:

The Question Generation tool can only generate random questions, and the quality of the generated questions is inferior to that produced by the creates-stuff-documents-chain using a customized prompt to generate specific questions. The prompt for the Specific Question Generation tool looks as follows.

You will assist students with practice tasks as a tutor for databases and information systems. The student will request a practice exercise on a particular subject. You will come up with a question that is pertinent to the subject. The questions should be in German.

Although the generation takes longer, the results are superior to those of the Question Generation tool mentioned above.

### Evaluation

In this section, the technology acceptance model (TAM) was utilized to assess how effectively the chatbot addresses the acceptance of MoodleBot as a valuable tool for learning support among students [67]. This is accomplished by examining hypotheses H1–H10 in Tables IV and V as part of answering RQ1. The technical evaluation focuses on output precision and a token-generation cost analysis for API calls to analyze the accuracy of MoodleBot’s responses and its congruency with the established course content as stated in RQ2.

#### A. Conceptual Framework

The TAM, proposed by Davis [67], is a widely used theoretical framework for predicting users’ acceptance and adoption of new technology. The individual’s technology acceptance is determined by two variables, perceived usefulness (PU) and perceived ease of use (PEOU). PU is defined as the extent to which the user believes a particular system would enhance their job performance, and PEOU refers to the degree to which the user acknowledges that using a specific system would be free of effort [67]. Both affect the user’s Attitude (AT) toward the technology directly and indirectly affect their behavioral intention (BI) [67], [68]. As external variables, SE refers to the individual’s perception of their ability to fulfill a particular task and system accessibility (SA) to the perceived ease of accessibility and interaction with the specific system [67], [68]. TAM is a valuable tool for researchers and practitioners interested in studying students’ acceptance of learning technologies [69], [70], [71]. It helps educators gain insights into improving the effectiveness of technology-based learning environments. This study assesses the users’ perceptions of the usefulness and ease of use of MoodleBot. Measuring the six key areas, PU, PEOU, AT toward the MoodleBot, BI, SE, and SA, provide insights into the likelihood of adoption and potential areas for improvement to enhance users’ acceptance toward LLM-driven chatbots in higher education. The validity of the constructs was assessed through an explorative factor analysis utilizing principal component analysis (PCA), reducing the dimensionality of the dataset while preserving the variance and ensuring that the constructs measured what they were intended to. The reliability of the constructs was evaluated using Cronbach’s alpha, confirming the internal consistency of the measurement items.

#### B. Evaluation Setup

Since students may accept the answers of these tools as a general truth, leading to the propagation of misinformation [48], 46 students who already passed the course participated voluntarily in this study. The participants, ranging in age from 20 to 31, were granted access to a live system within a controlled environment and were supervised throughout the study to ensure high-quality feedback. Of these, 30 answered the questionnaire, and 28 identified as male, while one preferred not to disclose their gender. All participants are either enrolled in or have completed a computer science program. The selection criterion emphasized that students should be familiar with the chatbot’s content, ensuring their capability to evaluate its content accuracy. Having undergone the lecture titled Databases and Information Systems, they possess the requisite background to evaluate the chatbot’s content accuracy. While 28 of the participants had previous interactions with chatbots, only 17 have used them in an educational setting. Despite their familiarity, they were initially unaware of MoodleBot’s capabilities. After a brief orientation to MoodleBot’s functionalities, they navigated the chatbot interactions more confidently. Ultimately, they were asked to complete the TAM questionnaire.

#### C. Evaluation Results

Table I illustrates the average responses and standard deviations from participants (N = 30) based on a Likert scale of 1–5, with 1 being “Strongly Disagree” and 5 as “Strongly Agree.” In general, participants indicated a favorable perspective toward interacting with the MoodleBot. From the PEOU category, the statement with the highest average score, 4. 6 ¯ ¯ ¯, was P E O U 3, indicating participants found its operation straightforward. In terms of PU, the statement “The MoodleBot could make it easier to study course content” (P U 7) recorded the highest mean of 4.4 6 ¯ ¯ ¯, while “The learning questions asked by the MoodleBot were always good” (P U 5) received the lowest mean of 3.9 3 ¯ ¯ ¯. Within the AT section, participants expressed the most positive sentiment with the statement “The bot is a good complement to traditional learning methods” (A T 2), yielding an average of 4.7 3 ¯ ¯ ¯. When discussing BI to use MoodleBot, the statement “I would continue to use the MoodleBot in the future as part of other courses” (B I 3) garnered a high score of 4.2 3 ¯ ¯ ¯. However, the average score for participants’ preference for interacting with the MoodleBot instead of a real tutor was only 2.7 (B I 1). SE contained items with averages around the mid-range, suggesting that while participants generally felt confident using the MoodleBot and saw its societal value, there were still some reservations. Lastly, the SA category had a high mean value of 4. 3 ¯ ¯ ¯ for S A 1, indicating that participants did not find difficulty accessing and using the MoodleBot within the Moodle course. Since no other factors affect the bot’s accessibility, this single question captures the key aspect of SA and accurately reflects users’ experience.

##### 1) Reliability and Validity:

The reliability of the variables gauged on a Likert scale was determined using Cronbach’s alpha, and the results are presented in Table II. The Cronbach’s alpha values range from 0.688 (for BI) to 0.802 (for PU) which can be described as reasonable [72]. Notably, the Cronbach’s Alpha for AT was 0.800. Only the coefficients that exceed the 0.6 threshold were considered, suggesting that the questionnaire items for these coefficients present satisfactory reliability since values below are questionable [72]. Furthermore, the Kaiser-Meyer–Olkin (KMO) measure verified the good sampling adequacy for the analysis, with a KMO of 0.7041 [73]. It is noteworthy that values closer to 1 are more suitable for factor analysis. The Bartlett’s test of sphericity was significant with χ 2 = 227.780, d f = 13, and p = 0.000. This indicates that the correlations between items were sufficiently large for factor analysis.

Table III presents the outcomes of the explorative factor analysis, revealing the necessity to remove specific items based on a threshold of 0.6, which is acceptable for samples less than 100 [74]. Selecting components with eigenvalues greater than 1 resulted in three components with eigenvalues of 5.625, 1.72, and 1.469, explaining 67% of total variance [75]. The Cronbach’s alpha coefficients for these components were 0.864, 0.806, and 0.751, suggesting satisfactory reliability. In terms of communalities, the items P U 1, P U 4, P U 6, P U 7, A T 3, and B I 3 were greater than 0.6 and the items A T 2 and B I 1 were slightly below the threshold. This indicates that most items retained in the components have a moderate degree of variance, underlining the trustworthiness of the measurement model.

##### 2) Regression Analysis:

Multiple linear regression analyses were conducted as shown in Fig. 4. This aimed to determine the strength and direction of the relationships between various internal and external variables and their impact on user behavior and perceptions. Tables IV and V summarize the tested hypotheses and their outcomes.

Analysis result model of the hypothesis test (β = Standardized Coefficients; t = Test Statistics; p = Significance Probability (p-value)).

Show All

##### a) Internal Variables:

Table IV presents the internal variables and their correlation with user attitudes and behaviors. Among the variables assessed, AT and PU proved to be a significant predictor of BI, with an R 2 value of 1.0699 and a standard error of 0.245. The hypothesized relationship between PU and BI could be confirmed, as evidenced by a R 2 value of 0.6678 and a standard error of 0.247. A statistical correlation was noticed between PEOU and PU with p-values below the threshold of 0.05. Furthermore, the derived R 2 value of 0.4636 and the associated standard error (σ x ¯ ¯ ¯ = 0.140) underlines the positive effect of PU to AT. This is consistent with the expected influence of PEOU on AT as evidenced by an R 2 value of 0.3384 and an standard error σ x ¯ ¯ ¯ of 0.152. The acceptable range for the t-value depends on both the p-value and the degrees of freedom [76].

##### b) External Variables:

In the context of the TAM, the PU and PEOU may be influenced by various external variables, including age, gender, academic degree, prior experience with educational chatbots, SE, and system accessibility, SA [77]. Due to the homogeneous nature of responses in the dataset, factors like age, gender, and academic degree were excluded from the analysis. From an in-depth examination of the data in Tablet V and as visualized in Fig. 4, it is evident that SA is a significant predictor of PEOU, registering an R 2 value of 0.3333 and a standard error of 0.095. Conversely, experience with educational chatbots showed no observable influence on either PU or PEOU. SE exhibited a positive correlation with PU (with R 2 = 0.4052 and σ x ¯ ¯ ¯ = 0.136) and PEOU (with R 2 = 0.3506 and σ x ¯ ¯ ¯ = 0.141). While SA had an impact on PEOU, it did not show a significant correlation with PU, as indicated by an R 2 value of 0.1723 and a standard error of 0.109. Interestingly, prior experience with educational chatbots provided minimal explanatory power for both PU (with R 2 = − 0.1658 and σ x ¯ ¯ ¯ = 0.196) and PEOU (with R 2 = − 0.1220 and σ x ¯ ¯ ¯ = 0.197).

#### D. Correctness and Fact-Checking

Following the evaluation of the acceptance and utility of MoodleBot, the accuracy of its responses emerges as a critical factor. To scrutinize the congruence of MoodleBot’s responses with the established course content, the results were manually verified by a TA and subjected to a LangChain-based fact-checker chain, the LLMSummarization-CheckerChain.

##### 1) Correctness of Generated Outputs:

To evaluate the user-perceived accuracy of MoodleBot’s generated outputs, manual evaluations and student feedback were employed to assess the quality. Content answers were scrutinized for factual accuracy by the TA, while students provided feedback on each answer’s utility and perceived correctness. It is important to note that feedback from students who completed the lecture over a year prior was excluded, particularly for answers they could not verify or those irrelevant to the lecture content. Of the total evaluations, a TA manually reviewed 65 responses and obtained feedback for each of them from the students. A confusion matrix, detailed in Table VI, classifies the results (including accuracy, precision, sensitivity, and specificity [78]). Using the confusion matrix, 53 out of 65 responses were accurate. However, some users were unhappy with the answers when looking at feedback from 17 chatbot responses. They said MoodleBot sometimes gave repetitive, unhelpful, or too much confusing information.

To assess the congruency of MoodleBot’s responses, the TA conducted a thorough evaluation to verify the factual accuracy and relevance of the generated outputs. This process involved cross-referencing MoodleBot’s responses with the course materials, including the syllabus and lecture notes, to ensure that the answers provided aligned with the course’s intended content. The TA also examined the contextual appropriateness of MoodleBot’s responses, ensuring they maintained consistency with the ongoing lecture topics and reflected the expected depth of understanding. A part of this evaluation included documenting any errors or discrepancies found in MoodleBot’s responses. This documentation identifies common issues, such as the mix-up of terms like “Wertebereich (Domäne, Domain)” and “Wertedomäne,” highlighting the need for more precise handling of specific terminology. In addition, student feedback played a crucial role in assessing congruency. Feedback from recent course completers was analyzed to understand areas where MoodleBot’s responses might have been repetitive, overly complex, or unhelpful.

Another aspect of the evaluation involved assessing how MoodleBot handled incorrect student input. While MoodleBot sometimes missed specific errors, its feedback was still useful, as it often pointed out other mistakes, helping students learn through iterative feedback. For example, in an SQL task, MoodleBot caught a keyword error but missed an ID number mistake.

Upon examination, no further significant discrepancies or issues were found. As a result, the responses generated by MoodleBot can be inferred to be congruent with the course content. While MoodleBot is right about 81% of the time, there is still room for improvement.

##### 2) Automated Fact-Checking:

In the implementation phase, to avoid disrupting interaction flow, responses from the LMS Chatbot Service were stored in a MongoDB database for subsequent review. In addressing RQ2, the aim was to determine whether the quality and congruence of MoodleBot’s responses could be measured automatically rather than relying solely on manual verification. Therefore, each was manually verified by a TA to ensure accuracy, with 88% of 100 responses deemed correct. Redundant answers, such as greetings and organizational queries, were excluded, resulting in approximately 160 content-specific questions. Each response was passed through a fact-checker chain to automate this process using the gpt-3.5-turbo model. The outputs of this fact-checker were compared against the TA‘s manual evaluations to assess the tool’s utility and accuracy. Only the first 100 responses, which were also previously checked by the TA, underwent the fact-checker chain to maintain cost efficiency, detailed further in Section IV-E. As seen in Table VII similar to Section IV-D1, a confusion matrix was established to evaluate the bot’s performance.

In the evaluation, the model achieved an accuracy of 82%, a precision of 88.04%, and high sensitivity values, suggesting proficient identification of true assertions while minimizing false positives. It should be noted that the same LLM handles both fact-checking and answer generation, which might bias it against detecting false statements, as evidenced by the Negative Predictive Value of 12.5%. The specificity, which measures the ratio of correctly identified negative instances to all negative instances, stands at 8%, indicating a deficiency in detecting negative instances. Moreover, the evaluation does not account for instances where the agent’s generated answers deviate from lecture content, such as verbose responses to queries about briefly mentioned topics. While this could assist students in understanding broader content, it might also lead to misconceptions about exam relevance or misuse. Despite the 88% accuracy in generating correct answers, the fact-checking service falls short in identifying erroneous responses, which is crucial for a checker. Thus, the performance of the fact-checker chain combined with LLM is suboptimal, and relying on LLM for accuracy verification to produce precise responses is not recommended.

##### 3) Summary of Fact-Checking:

In relation to RQ2, the analysis indicates that 88 out of 100 GPT-generated responses, when measured against a predetermined confusion matrix, were accurate. Despite this significant accuracy rate, there is an evident need for refinement. Feedback from student evaluations provides valuable insight into GPT’s reliability and user satisfaction. Notably, GPT exhibits limitations in identifying false assertions. The current fact-checking system, relying exclusively on LLMChain from LangChain, lacks integration with lecture slide data, potentially affecting response accuracy. In the educational domain, ensuring the integrity of information is paramount. Fact-checking enhancement could benefit from integrating LLMs trained in educational content or refining the overarching answer-generation process. Considering precision, employing multiple LLM agents and cross-referencing their outputs might optimize response accuracy.

#### E. Cost Calculation

OpenAI’s API platform offers a suite of LLMs, each designed for specific tasks and associated with distinct pricing. The API usage fees can be calculated with the processed token amount and the selected model version. 10 Standard models can process up to 4096 tokens, which is approximately equivalent to 3000 words 11 (costs are assessed per 1000 tokens). For the cost calculation, the following equation is utilized: C (n τ, c m) = n τ ∗ c m 1000. (1) View Source \begin{equation*} C(n_{\tau },c_{m}) = n_{\tau }*\frac {c_{m}}{1000}. \tag {1}\end{equation*} where C is the total cost, n τ is the number of tokens, and c m is the cost for the chosen model.

##### 1) Database Setup:

The text-embedding-ada-002 model from OpenAI was employed for the Weaviate database setup. It required approximately 280 000 tokens to embed lecture slides and exercise texts C Embedding = C (280000, $ 0.0001) = $ 0.028. (2) View Source \begin{equation*} C_{\text {Embedding}} = C(280000, {\$}0.0001) = {\$}0.028. \tag {2}\end{equation*}

##### 2) Similarity Search Embeddings:

A similarity search to retrieve information from the vector database requires embeddings for each query, which adds computational cost. During the evaluation phase, embeddings did not surpass 1000 tokens per query. Utilizing the text-embedding-ada-002 model this results in $ 0.0001 per query C (1000, $ 0.0001) = $ 0.0001. (3) View Source \begin{equation*} C(1000, {\$}0.0001) = {\$}0.0001. \tag {3}\end{equation*}

##### 3) Chat:

Answer generation based on context is similar to forwarding a prompt to the LLM, implying that costs involve more than just the embedding. During the evaluation, the token count per chat message ranged from 327 (319 In and 8 Out) to 71981 (66187 In and 5794 Out) tokens per student. Since only a limited student cohort was present, the GPT-4 model with an 8 K context was employed for the best user experience. 12 It is important to highlight that when using GPT models for conversations, both input and output tokens must be considered, which results in the following cost calculation per chat message: C (319, $ 0.03) + C (8, $ 0.06) ≈ $ 0.01 ≤ C message ≤ C (66187, $ 0.03) + C (5794, $ 0.06) ≈ $ 2.33. (4) View Source \begin{align*}& C(319, {\$}0.03) + C(8, {\$}0.06) \approx {\$}0.01 \\& \; \leq C_{\text {message}} \tag {4}\\& \; \leq C(66187, {\$}0.03) + C(5794, {\$}0.06) \approx {\$}2.33.\end{align*} The upper token bound for chat messages stems from the fact that, in such a conversational scenario, up to four prior turns (equating to 8 messages) were used to be retained for context. This history storage, the current message, and its corresponding response can lead to higher token values. Post-evaluation, the aggregate expenses were approximately $ 41.15, averaging to ≈ $ 1.65 per participant. The observed post-evaluation costs are notably lower than the projected range. This discrepancy can be attributed to the fact that, during the evaluation phase, most students did not fully utilize the stipulated 100-message cap with MoodleBot. Only a restricted amount of lecture questions were asked, and a specific number of exercises were generated, with a maximum of 34 conversation turns. For subsequent courses, employing a self-hosted LLM or utilizing a more cost-effective LLM, such as GPT-3.5-turbo, within a 16 K context is recommended.

#### F. Discussion and Implications

This study aimed to investigate the effectiveness of a Moodle-integrated chatbot in an academic setting tailored explicitly for students enrolled in a course on databases and information systems. While other studies have effectively encouraged the use of similar tools by embedding them within course policies, thus indirectly increasing participation rates [52], the presented approach in this article was voluntary and contained only students who had completed the course. This decision prevented unforeseen misuse or misinformation propagation, as related studies highlighted [48], [58]. In contrast to the study by [57], this research utilized the TAM to assess student perceptions. The evaluation encompassed an in-depth questionnaire to gauge the quality, utility, and suitability of MoodleBot’s responses while examining students’ AT and BI. A comprehensive analysis of the quantitative feedback obtained from participants showcased high average scores across the assessed metrics, indicating a favorable acceptance of MoodleBot. As hypothesized in RQ1, students viewed MoodleBot as a helpful tool enhancing their educational journey. Nonetheless, certain constraints were evident. Despite MoodleBot’s natural communication, students still prefer a human tutor when choosing, as reflected in the modest BI scores, indicating that chatbots should be used to complement rather than replace traditional teaching methods. Evaluation of the external variables revealed unexpected insights. While prior experience with chatbots had minimal impact on PU and PEOU, SA of the system and SE proved to be relevant factors for PEOU. This underscores the importance of easy access to LMS in shaping students’ academic interactions. As outline in TAM [67], a positive correlation exists between PU, PEOU and AT. For users with technical expertise, PU and PEOU are not always the most important factors for adoption, as the significance of these factors can vary depending on the nature of the task [79]. Factors, such as SE, subjective norm, enjoyment, computer anxiety, and experience often shape students’ PEOU, and PU, particularly in e-learning contexts [80]. The high acceptance rates and positive student perceptions of MoodleBot demonstrate the readiness to use LLM-based chatbot technologies. This suggests that integrating these technologies within educational platforms can increase student engagement by providing timely and accessible support outside regular instructional hours.

In efforts to affirm MoodleBot’s accuracy (RQ2), the fact-checker chain function showed an accuracy rate of 88%, aligning with the results reported by other studies [52]. The accuracy evaluated in this study depends on both the context and usefulness of the answer, supporting the findings of similar research that focused solely on the answer’s context [44]. TAs may consider the generated output more accurate and valuable. However, some students may be dissatisfied with the answer and require a more detailed explanation or description of the solution, resulting in a lower accuracy value of 69.23% in the assessment of both the TA and the students. However, it became clear that detecting inaccurate statements generated during the answer formulation requires improvement. Certain discrepancies where MoodleBot’s responses differed from lecture notes underscored this requirement. Therefore, introducing a more sophisticated fact-checking mechanism may further optimize accuracy. When integrating chatbots into learning environments, educators should ensure accurate responses and contextually relevant information to maintain educational integrity. They should encourage students to verify information and critically assess the generated responses, emphasizing the role of chatbots as supplementary tools rather than definitive sources of knowledge.

Another consideration is the cumulative cost associated with using the API for MoodleBot responses increases with long-term use. The direct integration into an educational course should consider integrating a self-hosted LLM or exploring cost-effective alternatives that maintain high performance. It is noteworthy that the presented approach has demonstrated comparable cost-efficiency ($ 1.65 per student) to those reported by others ($ 1.90 per student) and is quite fair regarding costs per student [52]. A more extended observation period could offer deeper insights into users’ perceptions. In addition, expanding the sample to include a broader range of genders and demographic backgrounds would provide a more holistic view of MoodleBot’s utility.

Overall, this approach holds promise in addressing the shortage of specialists in higher education and providing valuable support. Both pupils and students will increasingly engage with chatbots, and the prevalence of pilot projects utilizing LLM for learning support is expected to rise. 13

### Limitations

These constraints imposed by course policies and German GDPR likely contributed to the lower participation rate. Consequently, the sample size was relatively small, with 46 students, out of which 30 participated in the survey, leading to a small number of responses for which feedback was received. The voluntary nature of participation may have introduced a selection bias, as those who chose to participate might have had a predisposition toward the technology, affecting the generalization of the results. Voluntary participation is a common challenge [81], yet it remains a significant limitation in drawing broad conclusions. Furthermore, as the students who have completed the course are already acquainted with the course content, they will likely possess a more profound grasp of the course material and terminology, enabling them to pose more precise and targeted questions. Conversely, students who have yet to complete the course may require assistance employing the correct terminology, which could potentially result in more general and ambiguous prompts, thus yielding less informative responses. These disparities bear substantial implications for educational chatbots’ design and operational effectiveness, such as adaptive responses with learner stage recognition. Regarding feedback, the manual evaluation is done by a sole TA, which could lead to incorrect feedback for complex responses.

Another limitation of the study is using the gpt-4 model for the chatbot implementation. The presented study does not compare its performance with other contemporary LLMs. While gpt-4 demonstrated a high accuracy rate and provided valuable support to students, other models might offer different advantages regarding response accuracy, processing speed, or cost-effectiveness. Future research should explore and compare various LLMs to determine the most effective and efficient options for educational chatbots.

### Conclusion

The pervasiveness of AI tools and associated technologies like LLMs continues to revolutionize how tutors teach and support students in their SRL and help-seeking behavior. The promise is to usher in an AI-enabled instructional environment and make serendipitous learning more enjoyable for students. However, the complicated setup of many modern LMSs in higher education, increasing student numbers, the size and variety of educational material, information overload, and the problems of recruiting competent teachers or lecturers present fundamental challenges when developing and deploying AI tools, especially in computer science education settings.

This article addressed some of these challenges by presenting an LLM-driven chatbot called MoodleBot. A discussion on the pedagogical justification for the development of MoodleBot was followed by the architectural design and the integration of MoodleBot into the Moodle LMS of RWTH Aachen University. Two research questions concerning the acceptance and efficacy of MoodleBot as a learning support tool (RQ1), and the accuracy of MoodleBot’s responses concerning the established coursework (RQ2) were addressed.

Regarding RQ1, six measures of the TAM were used to evaluate the MoodleBot. These measures are PU, PEOU, users’ Attitude (AT), BI, SE, and SA. The evaluation shed light on the beneficial impact of MoodleBot on the student’s learning process, with the chatbot receiving favorable PU and PEOU feedback from the students. These results confirm MoodleBot’s potential to enhance learning by providing immediate assistance and enabling SRL.

However, despite the natural-language communication offered by MoodleBot, students still preferred a human tutor, indicating room for enhancing MoodleBot’s human-like interaction and tutoring capability. The results also emphasize the positive influence of LLMs on students’ academic engagement. The overall student acceptance of MoodleBot signifies the potential of AI-driven chatbots in educational settings.

As for RQ2, while MoodleBot demonstrated an accuracy rate of 88% when using the fact-checker function and proven congruent to the course materials by TAs, it is challenging for MoodleBot to detect inaccurate statements generated during the answer formulation process.

Despite the limitations (course or teaching policies, small number and voluntary nature of participants, etc.) enumerated below, the research can conclude with a caution that LLMs in general, and LLM-driven chatbots in particular, can effectively be used to personalize and support students throughout their learning journeys and foster SRL.

For educators, including but not limited to electrical and electronic engineering, computer engineering, and computer science, AI tools, such as LLMs can reduce administrative burdens and provide supplementary assistance, allowing more focus on instruction. Educators should use AI tools or chatbots to complement, not replace, human instruction. Continuous monitoring and evaluation of AI-enabled teaching and learning technologies, such as the MoodleBot presented in this research has the potential to impact students’ learning and engagement. Institutions can benefit from LLM-driven chatbots’ scalable and cost-effective nature to make quality education more accessible and efficient.

### Future Work

However, future research could still optimize the performance and usability of MoodleBot. This includes improving its fact-checking ability and accuracy of responses and exploring other (self-hosted) LLMs to reduce its reliance on (expensive) proprietary APIs. Furthermore, employing a more extensive and diverse sample of users for evaluation would offer robust insights into MoodleBot’s utility and acceptance. As with any pioneering technology, the ongoing refinement of these educational tools, as informed by qualitative and quantitative assessments, will be crucial in maximizing their potential value to learners and educators. In conclusion, LLM-powered educational chatbots, such as MoodleBot, promise to revolutionize traditional learning paradigms, equipping learners with accessible, instantaneous, and personalized learning support. Continuous improvements in AI capabilities will lead to even more effective and reliable educational chatbots, further integrating them into everyday learning and teaching processes.

#### ACKNOWLEDGMENT

The authors would like to express their sincere gratitude to the editor, associate editor, and reviewers for their valuable comments and constructive suggestions, which have significantly improved the quality of this work.

### More Like This

2025 4th International Conference on Sentiment Analysis and Deep Learning (ICSADL)

Published: 2025

2018 International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)

Published: 2018

---

## LAMB: An open-source software framework to create artificial intelligence assistants deployed and integrated into learning management systems

**Autores:** Marc Alier, Juanan Pereira, Francisco José García-Peñalvo, Maria Jose Casañ, Jose Cabré  
**Publicação:** Computer Standards &amp; Interfaces · 2025  
**DOI:** https://doi.org/10.1016/j.csi.2024.103940  
**Fonte:** sciencedirect — https://www.sciencedirect.com/science/article/pii/S0920548924001090  
**Citações:** 43  
**Keywords:** learning assistants, virtual learning environments, retrieval-augmented generation, prompt engineering, knowledge base, large language models, generative AI in education, hallucination mitigation, personalized learning, open source software, artificial intelligence in education, lecture transcription, student engagement, knowledge distillation  

**Abstract:**

• A learning assistant is a software tool that combines traditional software engineering with generative AI and retrieval augmented generation (RAG) to deliver a new class of educational applications. • This paper introduces the LAMB framework. LAMB allows creating and deploying learning assistants based on custom educational content, such as textbooks, lecture notes, and video recordings. • LAMB allows for creating and managing knowledge bases for RAG, as well as prompt engineering and plugins to define the behavior of the learning assistants. • The learning assistants created with LAMB run seamlessly within the context of the learning management system of the learning institution via the IMS LTI interoperability protocol. • The learning assistants created with LAMB provide accurate responses based on their knowledge base, providing references, and are less prone to hallucinations than regular LLM-based chatbots. This paper presents LAMB (Learning Assistant Manager and Builder), an innovative open-source software framework designed to create AI-powered Learning Assistants tailored for integration into learning management systems. LAMB addresses critical gaps in existing educational AI solutions by providing a framework specifically designed for the unique requirements of the education sector. It introduces novel features, including a modular architecture for seamless integration of AI assistants into existing LMS platforms and an intuitive interface for educators to create custom AI assistants without coding skills. Unlike existing AI tools in education, LAMB provides a comprehensive framework that addresses privacy concerns, ensures alignment with institutional policies, and promotes using authoritative sources. LAMB leverages the capabilities of large language models and associated generative artificial intelligence technologies to create generative intelligent learning assistants that enhance educational experiences by providing personalized learning support based on clear directions and authoritative fonts of information. Key features of LAMB include its modular architecture, which supports prompt engineering, retrieval-augmented generation, and the creation of extensive knowledge bases from diverse educational content, including video sources. The development and deployment of LAMB were iteratively refined using a minimum viable product approach, exemplified by the learning assistant: “Macroeconomics Study Coach,” which effectively integrated lecture transcriptions and other course materials to support student inquiries. Initial validations in various educational settings demonstrate the potential that learning assistants created with LAMB have to enhance teaching methodologies, increase student engagement, and provide personalized learning experiences. The system's usability, scalability, security, and interoperability with existing LMS platforms make it a robust solution for integrating artificial intelligence into educational environments. LAMB's open-source nature encourages collaboration and innovation among educators, researchers, and developers, fostering a community dedicated to advancing the role of artificial intelligence in education. This paper outlines the system architecture, implementation details, use cases, and the significant benefits and challenges encountered, offering valuable insights for future developments in artificial intelligence assistants for any sector.

**Texto completo** — HTML do editor (www.sciencedirect.com)

### Highlights

• A learning assistant is a software tool that combines traditional software engineering with generative AI and retrieval augmented generation (RAG) to deliver a new class of educational applications.

• This paper introduces the LAMB framework. LAMB allows creating and deploying learning assistants based on custom educational content, such as textbooks, lecture notes, and video recordings.

• LAMB allows for creating and managing knowledge bases for RAG, as well as prompt engineering and plugins to define the behavior of the learning assistants.

• The learning assistants created with LAMB run seamlessly within the context of the learning management system of the learning institution via the IMS LTI interoperability protocol.

• The learning assistants created with LAMB provide accurate responses based on their knowledge base, providing references, and are less prone to hallucinations than regular LLM-based chatbots.

### Keywords

Previous article in this issue

Next article in this issue

### 1. Introduction

1. A novel open-source framework, LAMB, designed for educators to create AI-powered learning assistants without requiring programming knowledge.

2. A modular architecture that enables seamless integration with Learning Management Systems (LMS) through the IMS Learning Tools Interoperability (LTI) standard.

3. A robust focus on privacy, ethical AI usage, and adherence to institutional policies to ensure safe deployment in educational environments.

4. A validated case study, the "Macroeconomics Study Coach," which demonstrates the practical application and benefits of the LAMB framework in real-world educational settings.

#### 1.1. Background

Table 1. Main characteristics of LLM-based chatbots.

Characteristic | Description
Advanced Natural Language Processing Abilities | Shows understanding of the user's input, quality of text generated, summarization, and synthesis abilities
Few-shot Learning | LLMs can quickly adapt to new tasks with minimal examples, learning effectively from limited interaction data
Chain-of-Thought Reasoning | LLMs can articulate step-by-step reasoning processes, enhancing their ability to handle complex tasks by mimicking the way humans explain their thought processes
Unforeseen Skills (Emerging Capabilities) | Including programming, arithmetic, correcting misconceptions, and answering exam questions across various domains, improving as the model size increases
Internal Representations | LLMs show internal representations allowing for abstract reasoning beyond mere linguistic structure, such as understanding colors, geography, object properties, and game states
Misconception Differentiation | They can distinguish between misconceptions and facts, showing an internal calibration of truth likelihood
Common-Sense Reasoning | LLMs pass tests like the Winograd Schema Challenge [7], indicating a sophisticated level of common-sense reasoning beyond textual clues
Privacy Concerns | Privacy is an issue in most LLMs provided as a service; for example, only Enterprise or Team ChatGPT customers have guaranteed confidentiality under the terms of service
Multimodality | Since 2023, LLMs have been able to handle inputs and generate outputs in the combined form of images, audio, and even video
Hallucinations | LLM responses are always peppered with the chance of hallucinations or incorrect answers, which the LLM delivers with the same confidence as correct answers

#### 1.2. Artificial intelligence assistants

Table 2. Technologies involved in the creation of an AI assistant (in addition to LLMs).

Technology | Description
Retrieval-Augmented Generation (RAG) | RAG combines LLM's ability to generate responses and pull information from external databases or documents, improving the accuracy and relevance of responses. The retrieved data is inserted in the conversation with the LLM, usually called Context, so the LLM can use it to generate an accurate response [27]
Semantic Search in Embeddings Databases | Utilizes embeddings to organize and retrieve information semantically, improving the assistant's ability to understand and respond to queries accurately across different modalities. An embedding is a numerical representation of data that captures its meaning and relationships in a high-dimensional space. An embeddings database can perform a similarity search and retrieve semantic-related objects to a given query. With RAG embeddings, databases confer an AI assistant capable of effectively using large amounts of unstructured information [28]
Very Large Contexts | Modern LLMs have started to allow for extensive contexts. The context is the window of attention of LLM to a conversation. LLMs have displayed the emerging ability to learn new skills from the information and examples provided in a conversation.
Code Interpreters | The LLMs are not designed to perform calculations or complex tasks. While they can fake it with reasonable accuracy, especially the larger models, they are prone to error and hallucination. However, LLMs are increasingly proficient at generating code that can be passed to an interpreter, and they then use the execution output to complete their response
Function Calling | Function calling is a feature introduced by OpenAI in June 2023 [26]. It provides the LLM with the option to respond with an invocation to the function of an API defined in the context. Function calling enables the LLM to interact with external information systems based on user commands
Prompt Engineering | Prompt engineering [29] refers to crafting and optimizing prompts to guide the LLM responses, improving the quality and relevance of generated content
Evaluation Frameworks and Metrics | Utilizing tools and techniques for assessing assistant performance, including monitoring systems, accuracy metrics, and benchmark datasets, to ensure reliability and effectiveness.
Fine Tuning | Refers to retraining the underlying LLM on specific datasets to enhance its performance in particular domains or tasks [30, 31]

#### 1.3. Research goals

• A learning assistant must be interoperable with the Learning Management Systems (LMS) and presented to students and teachers as part of the educational institution's software tools and processes.

• Substantial compliance with the educational institution's privacy policies is a legal requirement in the education sector.

• Alignment of the learning assistant with the educational institution culture, using only authoritative sources of information and tools for content generation, providing proper citations and transparency.

#### 3.1. Architecture overview

• The AI infrastructure. This provides access to embeddings models and LLM inference. Vendors like OpenAI, Google, Anthropic, or Mistral can provide the AI infrastructure or can provide it by running open-source models like Llama3 or Mixtral in one's infrastructure.

• The institutional ecosystem. The LMS is a virtual campus used in learning institutions like Moodle, Sakai, Canvas, or Blackboard.

Download: Download high-res image (695KB)

Download: Download full-size image

Fig. 1. LAMB architecture schema.

Download: Download high-res image (177KB)

Download: Download full-size image

Fig. 2. Sequence diagram of the creation of the “Macroeconomics Study Coach”.

• Prompt engineering. This component allows the user to create, test, and manage prompts used to define the behavior of the assistants. The prompts are parameterized for the RAG Engine and the Augmentation Plugins. Prompt engineering allows testing and evaluating the assistant in an iterative design process. When considered suitable, the user can publish the learning assistant via the LAMB LTI Integration by defining an Assistant Key.

• Content library manager. This component allows users to create and manage learning materials (video transcripts, documents, webpages, etc.) in libraries. The learning assistants will use the contents as authoritative sources of information (ground truth). In an "ingestion process,” the Content Library Manager breaks down the sources into relevant chunks of data and metadata, encoded as embeddings, creating Knowledge Bases. The chunking strategies are critical to refine the effectiveness of the RAG [40]. Hence, LAMB allows plugins for chunking strategy.

• REST API. It provides access to the learning assistants through various endpoints implementing the OpenAI API call structure. The REST API will require the Assistant Key to authorize using a learning assistant.

• Pipeline manager (PM). This is invoked by the REST API, which provides a learning assistant identifier for the messages received. The PM handles the pipeline of execution of the learning assistant, according to its configuration (done at the Prompt Engineering module), using retrieved chunks from the LAMB Knowledge Base, the Augmentation Plugins, and the LLM Integration Layer. Next, the output of the LLM will be processed and returned to the REST API.

• Retrieval Augmented Generation (RAG) engine. It retrieves appropriate information from the Knowledge Base to produce more accurate and contextually relevant responses from the LLM.

• Augmentation plugins. LAMB allows the definition of custom Augmentation Plugins to shape the behavior of the learning assistant in the PM.

• LLM integration layer. This layer manages the interaction with the chosen LLM, sending prompts and receiving generated responses. It supports multiple LLMs and infrastructure provider configurations. Users can set up their AI infrastructure configurations, including API URLs, API Keys, and models.

• LTI integration. It creates an LTI Learning Tool for each assistant in the LAMB LTI Provider, assigning the proper Assistant key. The LAMB LTI Integration can also be used by the Augmentation Plugins to send grades, participation reports, and feedback to the LMS.

• Web-based user interface and administration.

• Scalability: The architecture supports multiple instances of AI assistants and large content libraries, ensuring smooth performance even as user demand grows.

• Security: The system employs robust security measures, including Assistant Keys that protect access to learning assistants, ensuring compliance with institutional data privacy policies.

• Extensibility: The modular structure allows for the easy integration of new LLMs, features, and plugins, enabling the system to evolve alongside advances in AI technologies.

### 4. Implementing the macroeconomics study coach on LAMB

1. With the Content Library Manager, he will create a library with all the transcriptions of his lectures. The metadata will include the URL where each video is available for streaming. He will make a Knowledge Base with all the videos, plus a PDF file with some lecture notes.

2. He will create prompt templates for his learning assistant with the Prompt Engineering module. Then, he will test and refine the prompts and the assistant. After that, the assistant was published. Finally, LAMB Core will create an Assistant Key and a LAMB LTI Tool provider and show Jose the required parameters to set up an IMS LTI activity on his LMS (Moodle).

3. Now acting as a teacher (see Fig. 3), Jose will open his macroeconomics course on the Moodle instance of his university, adding an External Tool Activity (Macroeconomics Study Coach) with the parameters he received in step 2. He will enter the activity and define the privacy policies and requirements. Download: Download high-res image (163KB) Download: Download full-size image Fig. 3. The teacher creates the LTI Activity that wraps the LAMB Learning Assistant.

Download: Download high-res image (163KB)

Download: Download full-size image

Fig. 3. The teacher creates the LTI Activity that wraps the LAMB Learning Assistant.

4. Jose's students will interact with the “Macroeconomics Study Coach” (see Fig. 4). On the first time they enter, they will have to accept the terms and conditions (if any are set up) and choose their confidentiality settings, like deciding whether they want to share their names with the “Macroeconomics Study Coach” or allow or not their activity with the learning assistant to be anonymously accessed by learning analytics processes. Then, they will be redirected to the LAMB chatbot user interface, where they will interact with the learning assistant and ask questions. Download: Download high-res image (214KB) Download: Download full-size image Fig. 4. The student integration with the chatbot via the LMS and the LAMB LTI Tool.

Download: Download high-res image (214KB)

Download: Download full-size image

Fig. 4. The student integration with the chatbot via the LMS and the LAMB LTI Tool.

5. To answer those questions, the LAMB Core accesses the Knowledge Base and the LLM infrastructure to send back any response to the chatbot user interface.

6. On the chatbot user interface, the “Macroeconomics Study Coach” will answer the students’ questions using the Knowledge Base as ground truth and provide excerpts of the sources used and links to the streaming videos of the lectures where the questions are answered.

#### 5.1. The learning assistant is the expert

Download: Download high-res image (207KB)

Download: Download full-size image

Fig. 5.. Answers to the questions about the helpfulness of the assistant (left) and the usefulness of the additional questions suggested by the system. The survey aggregates 36 answers from students in the two courses participating.

#### 5.2. The teacher's assistant

Download: Download high-res image (192KB)

Download: Download full-size image

Fig. 6. Survey on the perceived usefulness of a learning assistant as an educational tool.

• Consistency and Alignment: Experts emphasized the chatbot's consistent performance, noting its ability to stay within the provided knowledge base and avoid generating irrelevant information. For example, one expert stated: "At the moment, the chatbot seems very consistent in its responses: it doesn't say anything it shouldn't, and it uses the documentation we have provided, almost always referencing it as a source."

• Reduced workload: Experts believed the learning assistant could handle repetitive student queries about course procedures and deadlines, freeing their time for more complex tasks.

• Enhanced student learning: In the case of the expert-based learning assistant, professors observed a noticeable improvement in the depth and quality of student reports compared to previous semesters. They attributed this improvement to the assistant's ability to provide students with access to expert knowledge and facilitate more profound engagement with the case study.

• Promoting student autonomy: Some experts saw the potential of learning assistants to encourage students to develop their independence and digital competencies by providing them with a tool for independent learning and exploration.

• Potential misuse and over-reliance: Concerns were raised about students using the assistant as a shortcut to avoid engaging with core course materials or accepting information uncritically. One expert highlighted the need for clear guidance and training for students to ensure proper use.

• Integration and usability: Suggestions were made to improve the integration of the chatbot interface within the LMS to create a more seamless user experience. For example, one expert suggested: "Another type of interaction: for questions for which it has not been trained and does not have information, you could add an option to make a query to the teacher of the course (e.g., "I cannot answer that question, do you want me to send the query to the teacher of the course? They will answer you through the messaging…")."

• Language support: One expert mentioned the need for the assistant to support minority languages, like Basque or Catalan, particularly for contexts with diverse student populations.

### 6. Running costs of LAMB

Table 3. Running costs of the learning assistant macroeconomics study coach with GPT-3.5.

Prompts per Student | Input Tokens | Output Tokens | Input Cost | Output Cost | Cost per 100 Students | Cost per Student
0.5 | 123,750 | 41,250 | $0.06 | $0.06 | $0.12 | $0.001
1 | 247,500 | 82,500 | $0.12 | $0.12 | $0.25 | $0.002
2 | 495,000 | 165,000 | $0.25 | $0.25 | $0.50 | $0.005
4 | 990,000 | 330,000 | $0.50 | $0.50 | $0.99 | $0.010
8 | 1980,000 | 660,000 | $0.99 | $0.99 | $1.98 | $0.020
12 | 2970,000 | 990,000 | $1.49 | $1.49 | $2.97 | $0.030
20 | 4950,000 | 1650,000 | $2.48 | $2.48 | $4.95 | $0.050
50 | 12,375,000 | 4125,000 | $6.19 | $6.19 | $12.38 | $0.124

Table 4. Running costs of the learning assistant macroeconomics study coach with GPT-4o.

Prompts per Student | Input Tokens | Output Tokens | Input Cost | Output Cost | Total per 100 Students | Total per Student
0.5 | 123,750 | 41,250 | $0.62 | $0.62 | $1.24 | $0.01
1 | 247,500 | 82,500 | $1.24 | $1.24 | $2.48 | $0.02
2 | 495,000 | 165,000 | $2.48 | $2.48 | $4.95 | $0.05
4 | 990,000 | 330,000 | $4.95 | $4.95 | $9.90 | $0.10
8 | 1980,000 | 660,000 | $9.90 | $9.90 | $19.80 | $0.20
12 | 2970,000 | 990,000 | $14.85 | $14.85 | $29.70 | $0.30
20 | 4950,000 | 1650,000 | $24.75 | $24.75 | $49.50 | $0.50
50 | 12,375,000 | 4125,000 | $61.88 | $61.88 | $123.75 | $1.24

#### 6.1. Cost of creation of a learning assistant

• Cost of pre-processing documentation. For instance, processing the “Macroeconomics Study Coach” video lectures involved several steps. The Whisper 3 model, which can be run locally, transcribes the lectures. Diarization models were employed to separate the professor's speech from the students’ questions and responses in the recordings. Additionally, the transcriptions were processed using GPT-4 to enhance the clarity of the text. Notably, the total cost of the GPT-4 API for this purpose was only $3.

• Cost of computing embeddings during ingestion. Embeddings can be locally calculated with small models that do not even require GPU. However, one lesson learned is that the learning assistant benefits significantly from using the best and most expensive embeddings model. For example, the OpenAI embeddings model “text-embedding-3-small” could not recognize technical terms like “stagflation” and would perform poorly if the user switched to the Catalan language on queries. The solution was to use “text-embedings-3-large,” which significantly improved the results in English and Spanish and performed well with queries in Catalan. While the first model costs (1/62,500$) = $0.000016/page of text, the second (1/9200$) = $0.0001/page of text. Since ingestion occurs only once for a knowledge base, the cost of embeddings is considered negligible even with the top embedding models. (https://d66z.short.gy/nRVZUo).

#### 6.2. Cost of running a learning assistant

Table 5. Average token usage for the Macroeconomics Learning Coach activity as measured on system logs.

Number of Students | 100
Input tokens per augmented prompt | 2475
Output tokens | 825
GPT-3.5 input $/M tokens | 0,5
GPT-3.5 output $/M Tokens | 1,5
GPT-4o input $/M tokens | 5
GPT-4o output $/M Tokens | 15

### 7. Discussion

• Breaking the access gap to AI in Education. LAMB empowers educators, regardless of their technical expertise, to harness the potential of AI. This democratization of AI technology can bridge the gap between cutting-edge research and practical classroom application.

• Contextualized learning support. Unlike generic AI chatbots, like ChatGPT, LAMB-powered assistants are deeply integrated with course content through their knowledge bases. This ensures student interactions are grounded in accurate, relevant, and authoritative information, minimizing the risk of AI hallucinations and promoting a more reliable and trustworthy learning experience.

• Flexibility and customization. The modular design of LAMB, particularly the prompt engineering module, enables educators to tailor learning assistants to their specific pedagogical approaches, course objectives, and student needs. This flexibility fosters a more personalized and adaptive learning environment.

• Personalized learning. LAMB facilitates the creation of personalized learning paths for individual students. Learning assistants can adapt to different learning styles, paces, and levels of understanding, providing customized support and guidance.

• Enhanced student engagement. The interactive nature of learning assistants, coupled with their ability to provide immediate feedback and answer student queries conversationally, fosters greater student engagement with course material. This can lead to a deeper understanding of concepts and increased learning motivation.

• We are empowering educators. By automating routine tasks such as answering frequently asked questions and providing essential explanations, LAMB frees up valuable time for educators. This allows them to focus on higher-order teaching activities, such as facilitating discussions, mentoring students, and developing engaging learning materials.

• Data-driven insights. LAMB's ability to track and analyze student interactions with learning assistants offers valuable insights into learning patterns, common misconceptions, and areas where students struggle. This data can inform pedagogical strategies, curriculum development, and interventions to improve learning outcomes.

### 8. Conclusions and future work

1. Expanding LAMB's capabilities to incorporate multimodal inputs and outputs, enhancing the versatility of learning assistants in various educational scenarios.

2. Integrating advanced LLM features such as code interpreters and function calling to extend the functionality of learning assistants.

3. Implementing robust learning analytics integration to provide educators with valuable insights into student learning patterns and outcomes.

4. Integrating Spaced Repetition Based Adaptive E-Learning techniques to enhance long-term retention by personalizing review sessions based on individual student needs and progress.

#### Based on reading popularity

Research article Full text access Enriching teachers’ assessments of rhythmic Forró dance skills by modelling motion sensor data Augusto Dias Pereira dos Santos, …, Roberto Martinez-Maldonado International Journal of Human-Computer Studies • Volume 161 • 2022 • Article 102776 View PDF

Research article Full text access Knowledge interaction enhanced sequential modeling for interpretable learner knowledge diagnosis in intelligent tutoring systems Wenbin Gan, …, Yi Sun Neurocomputing • Volume 488 • 2022 • Pages 36-53 View PDF

Research article Full text access Investigating students’ academic language-related challenges and their interplay with English proficiency and self-efficacy on EMI success in Transnational Education (TNE) programs in China Xiao Cui, Ishamina Athirah Gardiner English for Specific Purposes • Volume 78 • 2025 • Pages 53-69 View PDF

Short communication Full text access Promoting problem refining, analyzing and solving abilities through active learning in Polymer Chemistry and Physics teaching: A prospective framework for free radical suspension polymerization Peng Liu Education for Chemical Engineers • Volume 39 • 2022 • Pages 15-18 View PDF

Research article Full text access Empowering Futures: The Impact of Surgical Research Pipeline Programs on Undergraduate Career Development Ashba Allahwasaya, …, Andrea Gillis Journal of Surgical Education • Volume 82, Issue 2 • 2025 • Article 103393 View PDF

Research article Full text access Breast cancer diagnosis through serious gaming: Clinical reasoning, AI-driven character morphing, and emotional engagement Rafael Garcia Barbosa, Maria Andréia Formico Rodrigues Entertainment Computing • Volume 52 • 2025 • Article 100863 View PDF

### Cited by (53)

Research article Open access Enhancing textile heritage engagement through generative AI-based virtual assistants in virtual reality museums Ariya P., …, Puritat K. Computers and Education: X Reality • Volume 7 • 2025 • Article 100112 Show abstract This study investigates how generative AI-based virtual assistants embedded within immersive virtual reality (VR) environments can enhance user engagement and cultural learning in virtual museums. Situated at the Wieng Yong House Museum in Thailand, the research addresses the challenge of preserving and promoting textile heritage in the digital age. The study aims to design, implement, and evaluate an AI-driven virtual docent capable of delivering personalized, multilingual, and real-time cultural information through interactive voice-based engagement. Using a purposive sampling technique, 25 university students participated in a convergent parallel mixed-methods study combining structured questionnaires and open-ended feedback. Quantitative findings from structured questionnaires revealed high user satisfaction, with mean scores of 4.40 for visual quality and 4.20 for ease of interaction, while response latency and voice clarity received lower ratings of 3.36 and 3.62 respectively, indicating areas for improvement. Qualitative analysis revealed four key themes: user experience with the system, communication quality, response effectiveness, and suggestions for improvement. The results demonstrate both the transformative potential and current limitations of generative AI in digital heritage settings. This study contributes to the development of more inclusive and engaging virtual museum experiences for the teaching and learning of cultural heritage, offering practical design insights for educators, curators, and developers.

Review article Open access Retrieval-augmented generation for educational application: A systematic survey Li Z., …, Wang F.L. Computers and Education: Artificial Intelligence • Volume 8 • 2025 • Article 100417 Show abstract Advancements in large language models (LLMs) have transformed AI-driven education, enabling innovative applications across various learning and teaching domains. However, LLMs still face several challenges, including hallucination and static internal knowledge, which hinder their reliability in educational settings. Retrieval-Augmented Generation (RAG) enhances LLMs by retrieving relevant information from an external knowledge base and incorporating it into the LLM's generation process. This approach improves factual accuracy and enables dynamic knowledge updates, making LLMs particularly suitable for educational applications. In this paper, we comprehensively review existing research that integrates RAG into educational scenarios. We first clarify the definition and workflow of RAG, and following the indexing mechanism of RAG, we introduce different types of retrievers and generation optimization methods. As the main focus of this work, we explore the practical applications of RAG in education, covering interactive learning systems, generation and assessment of educational content, and large-scale deployment in educational ecosystems. Based on our comprehensive review, this paper discusses existing challenges and future directions, including mitigating hallucinations, ensuring the completeness and timeliness of retrieved knowledge, reducing computational costs, and enhancing multimodal support for RAG-based educational applications.

The Impact of Adaptive Learning Technologies, Personalized Feedback, and Interactive AI Tools on Student Engagement: The Moderating Role of Digital Literacy Yaseen H., …, Sharbati A.-A.A. Sustainability (Switzerland) • Volume 17 • 2025 • Article 1133

GenAI as a Learning Buddy for Non-English Majors: Effects on Listening and Writing Performance Zheldibayeva R. Educational Process: International Journal • Volume 14 • 2025 • Article e2025051

The ethics of generative artificial intelligence in education under debate. A perspective from the development of a theoretical-practical case study García-Peñalvo F.-J., …, Pereira-Varela J.-A. Revista Espanola de Pedagogia • Volume 83 • 2025

Exploring AI to Automate EFL Corrective Written Feedback in the First Language Hirschel R., Horai K. Technology in Language Teaching and Learning • Volume 7 • 2025 • Article 2208

#### Citations

Citation Indexes 52

#### Captures

Mendeley Readers 341

#### Mentions

News Mentions 14

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

**Texto completo** — HTML do editor (dl.acm.org)

#### AI-Generated Summary (Experimental)

This summary was generated using automated tools and was not authored or reviewed by the article's author(s). It is provided to support discovery, help readers assess relevance, and assist readers from adjacent research areas in understanding the work. It is intended to complement the author-supplied abstract, which remains the primary summary of the paper. The full article remains the authoritative version of record. Click here to learn more.

Click here to comment on the accuracy, clarity, and usefulness of this summary. Doing so will help inform refinements and future regenerated versions.

AI-generated summary

Generated by an automated system based on the published article text.

Version created on December 9, 2025.

The research paper introduces CyberBOT, an ontology-grounded retrieval-augmented generation (RAG) system designed to provide reliable and context-aware cybersecurity education. The key aspects of the system are:

Intent interpreter: CyberBOT uses an intent interpreter to capture the user's underlying intent from the multi-turn conversational history, allowing it to reformulate the query into a more knowledge-intensive version for effective retrieval.

Retrieval-augmented generation: Based on the interpreted intent, CyberBOT retrieves relevant course-specific documents from a curated knowledge base to serve as the contextual foundation for generating responses using large language models (LLMs).

Ontology-based validation: CyberBOT employs a domain-specific cybersecurity ontology to validate the generated answers, ensuring semantic alignment with authoritative knowledge and filtering out potentially unsafe or hallucinated content.

The paper describes the deployment of CyberBOT in a graduate-level cloud computing course at Arizona State University, with over 100 students interacting with the system. This real-world application provides valuable insights into the practical utility and pedagogical effectiveness of the ontology-informed validation approach.

Quantitative evaluation using the CyberQ dataset demonstrates that CyberBOT achieves strong performance across both QA-based metrics (e.g., BERTScore) and RAG-based metrics (e.g., Answer Relevancy, Context Precision, and Context Recall), highlighting the system's ability to generate high-quality, contextually relevant, and domain-appropriate responses.

The paper concludes by discussing the potential of specialized natural language processing systems, such as CyberBOT, in advancing cybersecurity education and the future work on enhancing the system with personalized learning capabilities.

### Formats available

You can view the full content in the following formats:

### Cited By

Chaudhary K Zhao C Zhang F Agrawal G Deng Y Liu H (2026) EssayCBM: Transparent Essay Scoring via Rubric-Aligned Concept Bottlenecks Machine Learning and Knowledge Discovery in Databases. Applied Data Science Track, Demo Track and Industrial Track 10.1007/978-3-032-37685-5_22 (302-305) Online publication date: 8-Sep-2026 https://doi.org/10.1007/978-3-032-37685-5_22

Gensale A Cagliero L Basile C Garza P Ferrua L (2026) Efficient Retrieval-Augmented Generation for Vulnerability Assessment and Penetration Testing in Automotive Engineering Algorithms 10.3390/a19070555 19:7 (555) Online publication date: 7-Jul-2026 https://doi.org/10.3390/a19070555

Arpaci I Khan N Qayyum S Baloglu M (2026) Generative AI and Cybersecurity Education, Training, and Awareness: A Systematic Mapping Study IEEE Access 10.1109/ACCESS.2026.3738195 14 (150806-150827) Online publication date: 2026 https://doi.org/10.1109/ACCESS.2026.3738195

Show More Cited By

### Index Terms

CyberBOT: Ontology-Grounded Retrieval Augmented Generation for Reliable Cybersecurity Education Computing methodologies Artificial intelligence Natural language processing Natural language generation

Computing methodologies Artificial intelligence Natural language processing Natural language generation

Computing methodologies

Artificial intelligence Natural language processing Natural language generation

Artificial intelligence

Natural language processing Natural language generation

Natural language processing

Natural language generation

Natural language generation

### Recommendations

MoRSE: Bridging the Gap in Cybersecurity Expertise with Retrieval Augmented Generation SAC '25: Proceedings of the 40th ACM/SIGAPP Symposium on Applied Computing In this paper, we introduce MoRSE (Mixture of RAGs Security Experts), the first specialised AI chatbot for cybersecurity. MoRSE aims to provide comprehensive and complete knowledge about cybersecurity. MoRSE uses two RAG (Retrieval Augmented Generation)... Read More

#### MoRSE: Bridging the Gap in Cybersecurity Expertise with Retrieval Augmented Generation

In this paper, we introduce MoRSE (Mixture of RAGs Security Experts), the first specialised AI chatbot for cybersecurity. MoRSE aims to provide comprehensive and complete knowledge about cybersecurity. MoRSE uses two RAG (Retrieval Augmented Generation)...

Enhancing Cybersecurity Education Using POGIL (Abstract Only) SIGCSE '17: Proceedings of the 2017 ACM SIGCSE Technical Symposium on Computer Science Education This poster presents our NSF collaborative project "Enhancing Cybersecurity Education Using POGIL". Although the POGIL (Process Oriented Guided Inquiry Learning) instructional approach has been used and evaluated in science and engineering disciplines,... Read More

#### Enhancing Cybersecurity Education Using POGIL (Abstract Only)

This poster presents our NSF collaborative project "Enhancing Cybersecurity Education Using POGIL". Although the POGIL (Process Oriented Guided Inquiry Learning) instructional approach has been used and evaluated in science and engineering disciplines,...

Shaping Curricular Guidelines for Associate-Degree Cybersecurity Programs SIGCSE '19: Proceedings of the 50th ACM Technical Symposium on Computer Science Education As projections of the shortage of cybersecurity workers grow [4], the spotlight is on cybersecurity education. In December of 2017, the Joint Task Force on Cybersecurity Education published Cybersecurity Curricula 2017: Curriculum Guidelines for Post-... Read More

#### Shaping Curricular Guidelines for Associate-Degree Cybersecurity Programs

As projections of the shortage of cybersecurity workers grow [4], the spotlight is on cybersecurity education. In December of 2017, the Joint Task Force on Cybersecurity Education published Cybersecurity Curricula 2017: Curriculum Guidelines for Post-...

##### Published In

General Chairs:

Meeyoung Cha,

Chanyoung Park,

+ 8

##### Sponsors

SIGIR: ACM Special Interest Group on Information Retrieval

SIGWEB: ACM Special Interest Group on Hypertext, Hypermedia, and Web

##### Publisher

Association for Computing Machinery

New York, NY, United States

##### Author Tags

cybersecurity education

large language model

question answering

retrieval augmented generation

##### Qualifiers

Short-paper

##### Funding Sources

National Science Foundation

National Science Foundation

##### Conference

SIGIR

SIGWEB

##### Upcoming Conference

Sponsor:

sigir

sigir

##### Article Metrics

5 Total Citations View Citations

461 Total Downloads

Downloads (Last 12 months) 461

Downloads (Last 6 weeks) 51

##### Data Visualization

Citations

Downloads

Total

First 90 Days

Last 6 Months

Last 12 Months

PNG

CSV

Facebook

X

Linkedin

Threads

Bluesky

WeChat

Email

##### Geographical Distribution of Downloads

Downloads

### Cited By

Chaudhary K Zhao C Zhang F Agrawal G Deng Y Liu H (2026) EssayCBM: Transparent Essay Scoring via Rubric-Aligned Concept Bottlenecks Machine Learning and Knowledge Discovery in Databases. Applied Data Science Track, Demo Track and Industrial Track 10.1007/978-3-032-37685-5_22 (302-305) Online publication date: 8-Sep-2026 https://doi.org/10.1007/978-3-032-37685-5_22

Gensale A Cagliero L Basile C Garza P Ferrua L (2026) Efficient Retrieval-Augmented Generation for Vulnerability Assessment and Penetration Testing in Automotive Engineering Algorithms 10.3390/a19070555 19:7 (555) Online publication date: 7-Jul-2026 https://doi.org/10.3390/a19070555

Arpaci I Khan N Qayyum S Baloglu M (2026) Generative AI and Cybersecurity Education, Training, and Awareness: A Systematic Mapping Study IEEE Access 10.1109/ACCESS.2026.3738195 14 (150806-150827) Online publication date: 2026 https://doi.org/10.1109/ACCESS.2026.3738195

Yang C Roy S Li Z Kamps J Cha M Park C Park N (2025) Report on the 34th ACM Conference on Information and Knowledge Management (CIKM 2025) ACM SIGIR Forum 10.1145/3799914.3799932 59:2 (1-14) Online publication date: 1-Dec-2025 https://dl.acm.org/doi/10.1145/3799914.3799932

Artayasa P Kusuma A Sugiartawan P (2025) Enhancing Academic Chatbot Accuracy With Retrieval-Augmented Generation in Higher Education 2025 IEEE International Symposium on Consumer Technology (ISCT) 10.1109/ISCT66099.2025.11297210 (427-432) Online publication date: 16-Sep-2025 https://doi.org/10.1109/ISCT66099.2025.11297210

##### PDF

View or Download as a PDF file.

##### eReader

View online with eReader.

##### Share this Publication link

https://dl.acm.org/doi/10.1145/3746252.3761478

Copied!

Copying failed.

---

## A Teacher-Driven Framework for Reliable and Personalised AITutors

**Autores:** Stefano Valtolina, Ricardo Anibal Matamoros Aragon, Francesco Epifania  
**Publicação:** Proceedings of the 16th Biannual Conference of the Italian SIGCHI Chapter · 2025  
**DOI:** https://doi.org/10.1145/3750069.3750121  
**Fonte:** acm — https://dl.acm.org/doi/10.1145/3750069.3750121  
**Citações:** 1  
**Keywords:** chatbots, teacher agency, retrieval-augmented generation, VARK learning styles, adaptive tutoring, human-centered AI, artificial intelligence in education, cognitive load, usability, UTAUT  

**TL;DR:** A software framework that enables teachers to design reliable, personalised conversational agents tailored to their pedagogical goals and student learning preferences and supports the development of human-centred AI tutors that are transparent, configurable, and grounded in teacher expertise is presented.

**Abstract:**

This paper presents a software framework that enables teachers to design reliable, personalised conversational agents tailored to their pedagogical goals and student learning preferences. The system combines a Retrieval-Augmented Generation (RAG) architecture with a visual configuration environment, allowing educators to upload, validate, and organise domain-specific teaching materials into a teacher-curated content corpus. Educators can configure adaptive tutoring strategies based on the VARK model (Visual, Auditory, Reading/Writing, Kinesthetic), allowing the conversational agents to address diverse learning preferences and educational contexts. Unlike fully autonomous or black-box educational AI systems, this approach foregrounds teacher agency and pedagogical alignment, enabling intuitive control over content and interaction style. A preliminary evaluation with university educators assessed usability (SUS), perceived utility (UTAUT), cognitive load (NASA-TLX), and creative-technical capacity (CTS), revealing promising results and informing future design directions. The system supports the development of human-centred AI tutors that are transparent, configurable, and grounded in teacher expertise.

**Texto completo** — HTML do editor (dl.acm.org)

#### AI-Generated Summary (Experimental)

This summary was generated using automated tools and was not authored or reviewed by the article's author(s). It is provided to support discovery, help readers assess relevance, and assist readers from adjacent research areas in understanding the work. It is intended to complement the author-supplied abstract, which remains the primary summary of the paper. The full article remains the authoritative version of record. Click here to learn more.

Click here to comment on the accuracy, clarity, and usefulness of this summary. Doing so will help inform refinements and future regenerated versions.

AI-generated summary

Generated by an automated system based on the published article text.

Version created on December 10, 2025.

This paper presents a software framework that empowers teachers to design reliable and personalized conversational AI tutors without requiring technical expertise. The system combines Retrieval-Augmented Generation architecture with a visual configuration interface, enabling educators to upload, validate, and organize domain-specific teaching materials into curated content repositories. The framework allows teachers to configure adaptive tutoring strategies based on the VARK model, which categorizes learners as Visual, Auditory, Reading/Writing, or Kinesthetic, ensuring conversational agents can address diverse learning preferences across different educational contexts.

Unlike fully autonomous or opaque educational AI systems, this approach prioritizes teacher agency and pedagogical alignment, providing intuitive control over both content and interaction style. The system features two main components: a content generation interface for creating AI-assisted teaching materials like slide presentations, and a chatbot deployment module for configuring course-specific conversational agents. Teachers can define core chatbot metadata, upload and organize reference materials thematically, and use an interactive calendar to schedule topics throughout the course. The underlying technical architecture employs semantic segmentation of documents into manageable fragments, which are encoded into vector representations using transformer-based models. When students submit questions, the system retrieves the most semantically similar content fragments and applies personalization based on the student's learning style preference before generating responses through a large language model.

The framework was evaluated through a formative study with six university educators representing diverse academic roles and technical expertise. Participants interacted with the system, authored tutoring agents, and assessed its effectiveness using validated instruments including the System Usability Scale, Unified Theory of Acceptance and Use of Technology questionnaire, NASA Task Load Index, and a Cognitive Task Scaffolding scale. Results revealed strong usability with an average SUS score of 79.1, well above the acceptability threshold. Participants rated the system highly on performance expectancy and perceived it as manageable with moderate cognitive demand. However, abstraction-oriented tasks like formulating reusable strategies across different chatbots were perceived as more challenging, even by experienced users, indicating the need for additional scaffolding.

The research contributes to human-centered AI in education by demonstrating that with appropriate tools and metaphors, non-technical educators can effectively configure intelligent educational technologies. The modular architecture allows independent updates to content, personalization templates, and scheduling without retraining the entire system. Future work will include broader classroom deployments with diverse student populations, measurement of learning outcomes, and integration of learning analytics features to support iterative refinement across multiple semesters.

#### 4.1 Content Generator for Pedagogical Presentations

User interface of the AI-powered content generator for educational courses. Panel (A) allows the user to select the content source (e.g., Wikipedia), (B) to choose the output format (e.g., Google Slides or HTML), (C) to upload supporting documents either from local files or Google Drive, and (D) to configure automatic layout preferences (visual, textual, kinesthetic). The interface supports flexible slide content and structure configuration, allowing educators to customise AI-generated presentations to pedagogical needs.

#### 4.2 Chatbot Deployment Interface

Main steps in the configuration of a course-specific educational chatbot. Panel (A) shows the initial setup screen where users define the chatbot's name, course metadata, and instructional guidelines. Panel (B) illustrates topic creation and uploads reference material for each module. Panel (C) displays an interactive calendar for scheduling the topics throughout the course duration. The interface promotes a structured workflow for creating course-aligned conversational agents.

### 6 Evaluation Plan

Variables | Average | Std. Dev | Variables | Average | Std. Dev | Variables | Average | Std. Dev | Variables | Average | Std. Dev
Effort Expectancy (EE) | Performance Expectancy (PE) | Social Influence (SI) | Facilitating Conditions (FC)
EE1 | 3.80 | 0.80 | PE1 | 4.33 | 1.40 | SI1 | 3.10 | 1.20 | FC1 | 2.86 | 0.56
EE2 | 4.30 | 2.15 | PE2 | 3.88 | 0.70 | SI2 | 2.90 | 0.9 | FC2 | 3.55 | 0.59
EE3 | 5.33 | 0.6 | PE3 | 3.80 | 0.50 | SI3 | 2.50 | 1.80 | FC3 | 3.33 | 1.25
 | PE4 | 3.0 | 0.60 |  | FC4 | 3.23 | 1.25
PE5 | 4.70 | 0.70 | 
Trust (T) | User Satisfaction (US) | Behavioural Intention (BI)
T1 | 4.73 | 1.00 | US1 | 5.04 | 0.7 | BI1 | 4.00 | 1.04
T2 | 3.77 | 0.61 | US2 | 5.03 | 1.10 | BI2 | 4.12 | 0.80
T3 | 4.00 | 0.54 | US3 | 5.02 | 0.60 | 

The table contains the average and standard deviation of the answers to the questions of the UTAUT questionnaire.

 | Professors | Researchers | Phd Students
Abstractions | 4.7 | 4.3 | 3.2
Decomposition | 3.2 | 3.9 | 2.1
Algorithm Design | 4.1 | 3.0 | 4.2
Generalisation | 4.0 | 3.7 | 3.4
Evaluation | 4.4 | 4.4 | 3.0

Descriptive Statistics (Means) of the Five-Dimensional CT Scores (Scale: 1-5).

### References

a [...] configuration of intelligent systems

b [...]]. However, existing research

c [...] interfaces without programming skills

a [...] our system incorporates the VARK model

b [...] preferences and needs. The VARK model

a [...] configuration of intelligent systems

b [...] interfaces without programming skills

a [...] traceability, and pedagogical alignment

b [...] principles in educational technology design

a [...] including the System Usability Scale (SUS)

b [...] the System Usability Scale (SUS)

a [...] of Acceptance and Use of Technology (UTAUT)

b [...] and Use of Technology (UTAUT) questionnaire

a [...]], NASA Task Load Index (NASA-TLX)

b [...]], the NASA Task Load Index (NASA-TLX)

a [...] Creativity and Technical Skills (CTS) scale

b [...] the Cognitive Task Scaffolding (CTS) scale

c [...] the Cognitive Task Scaffolding (CTS) scale

a [...] potential to support learning environments

b [...] with generative response capabilities

a [...] to specific, indexed source material

b [...] metaphors, and domain-specific abstractions

a [...] potential to support learning environments

b [...] sequences or tailor content delivery

a [...] planning support, and motivational prompts

b [...] sequences or tailor content delivery

a [...] planning support, and motivational prompts

b [...] to shape how AI tools operate and behave

a [...] to shape how AI tools operate and behave

b [...] in End-User Development frameworks

### Index Terms

A Teacher-Driven Framework for Reliable and Personalised AITutors Applied computing Education Computer-managed instruction Interactive learning environments Computing methodologies Artificial intelligence Distributed artificial intelligence Human-centered computing Human computer interaction (HCI) Interaction paradigms Interaction design Interaction design process and methods User interface design

Applied computing Education Computer-managed instruction Interactive learning environments

Applied computing

Education Computer-managed instruction Interactive learning environments

Education

Computer-managed instruction

Computer-managed instruction

Interactive learning environments

Interactive learning environments

Computing methodologies Artificial intelligence Distributed artificial intelligence

Computing methodologies

Artificial intelligence Distributed artificial intelligence

Artificial intelligence

Distributed artificial intelligence

Distributed artificial intelligence

Human-centered computing Human computer interaction (HCI) Interaction paradigms Interaction design Interaction design process and methods User interface design

Human-centered computing

Human computer interaction (HCI) Interaction paradigms

Human computer interaction (HCI)

Interaction paradigms

Interaction paradigms

Interaction design Interaction design process and methods User interface design

Interaction design

Interaction design process and methods User interface design

Interaction design process and methods

User interface design

User interface design

### Recommendations

Design of a conversational recommender system in education Abstract In recent years, we have seen a significant proliferation of e-learning platforms. E-learning platforms allow teachers to create digital courses in a more effective and time-saving way, but several flaws hinder their actual success. One main... Read More

#### Design of a conversational recommender system in education

In recent years, we have seen a significant proliferation of e-learning platforms. E-learning platforms allow teachers to create digital courses in a more effective and time-saving way, but several flaws hinder their actual success. One main...

Personalization in OELEs: Developing a Data-Driven Framework to Model and Scaffold SRL Processes Artificial Intelligence in Education Abstract This research focuses on developing a data-driven framework for modeling and scaffolding learners’ self-regulated learning (SRL) processes in open-ended learning environments (OELE). The aim of this work is to offer a personalized and productive... Read More

#### Personalization in OELEs: Developing a Data-Driven Framework to Model and Scaffold SRL Processes

This research focuses on developing a data-driven framework for modeling and scaffolding learners’ self-regulated learning (SRL) processes in open-ended learning environments (OELE). The aim of this work is to offer a personalized and productive...

Artificial Intelligence-Driven Personalized Learning Pathways in Vocational Education: Enhancing Competence, Engagement, and Outcomes GAIDMA '25: Proceedings of the 2025 International Conference on Generative AI and Digital Media Arts Artificial intelligence-driven personalized learning pathways (AI-PLPs) leverage adaptive algorithms and learner analytics to deliver individualized educational experiences. Although earlier studies have acknowledged the value of these systems in... Read More

#### Artificial Intelligence-Driven Personalized Learning Pathways in Vocational Education: Enhancing Competence, Engagement, and Outcomes

Artificial intelligence-driven personalized learning pathways (AI-PLPs) leverage adaptive algorithms and learner analytics to deliver individualized educational experiences. Although earlier studies have acknowledged the value of these systems in...

##### Publisher

Association for Computing Machinery

New York, NY, United States

##### Author Tags

Acceptability and Usability

Conversational interface

End User Development objects

Machine learning for education

##### Qualifiers

Research-article

##### Article Metrics

0 Total Citations

1,097 Total Downloads

Downloads (Last 12 months) 1,097

Downloads (Last 6 weeks) 93

##### Data Visualization

Citations

Downloads

Total

First 90 Days

Last 6 Months

Last 12 Months

PNG

CSV

Facebook

X

Linkedin

Threads

Bluesky

WeChat

Email

##### Geographical Distribution of Downloads

Downloads

##### PDF

View or Download as a PDF file.

##### XML

Download text as an XML file.

##### eReader

View online with eReader.

##### Share this Publication link

https://dl.acm.org/doi/10.1145/3750069.3750121

Copied!

Copying failed.

##### References

a [...] configuration of intelligent systems

b [...]]. However, existing research

c [...] interfaces without programming skills

a [...] our system incorporates the VARK model

b [...] preferences and needs. The VARK model

a [...] configuration of intelligent systems

b [...] interfaces without programming skills

a [...] traceability, and pedagogical alignment

b [...] principles in educational technology design

a [...] including the System Usability Scale (SUS)

b [...] the System Usability Scale (SUS)

a [...] of Acceptance and Use of Technology (UTAUT)

b [...] and Use of Technology (UTAUT) questionnaire

a [...]], NASA Task Load Index (NASA-TLX)

b [...]], the NASA Task Load Index (NASA-TLX)

a [...] Creativity and Technical Skills (CTS) scale

b [...] the Cognitive Task Scaffolding (CTS) scale

c [...] the Cognitive Task Scaffolding (CTS) scale

a [...] potential to support learning environments

b [...] with generative response capabilities

a [...] to specific, indexed source material

b [...] metaphors, and domain-specific abstractions

a [...] potential to support learning environments

b [...] sequences or tailor content delivery

a [...] planning support, and motivational prompts

b [...] sequences or tailor content delivery

a [...] planning support, and motivational prompts

b [...] to shape how AI tools operate and behave

a [...] to shape how AI tools operate and behave

b [...] in End-User Development frameworks

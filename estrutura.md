# EAP — Desenvolvimento iterativo da solução

```mermaid
%%{init: {"theme":"base","flowchart":{"nodeSpacing":24,"rankSpacing":34,"useMaxWidth":true},"themeVariables":{"fontFamily":"Arial, sans-serif","primaryTextColor":"#172033","lineColor":"#94A3B8"}}}%%
%%{init: {"theme":"base","flowchart":{"nodeSpacing":20,"rankSpacing":28,"useMaxWidth":true,"curve":"linear"},"themeVariables":{"fontFamily":"Arial, sans-serif","primaryTextColor":"#172033","lineColor":"#94A3B8"}}}%%
flowchart TB
    P["<b>Projeto de dissertação</b>"]
    A["<b>1.1 Compreensão do problema</b><br/>1.1.1 Problema e contexto caracterizados<br/>1.1.2 Utilizadores e partes interessadas identificados<br/>1.1.3 Objetivos e resultados pretendidos definidos<br/>1.1.4 Critérios de sucesso definidos"]
    B["<b>1.2 Requisitos e story map</b><br/>1.2.1 Necessidades dos utilizadores identificadas<br/>1.2.2 Atividades principais mapeadas<br/>1.2.3 Tarefas e funcionalidades associadas<br/>1.2.4 Story map revisto e validado<br/>1.2.5 MVP e incrementos seguintes delimitados"]
    C["<b>1.3 Backlog do produto no Jira</b><br/>1.3.1 Épicos criados para as áreas principais<br/>1.3.2 Stories criadas a partir das necessidades<br/>1.3.3 Subtarefas técnicas identificadas quando necessário<br/>1.3.4 Critérios de aceitação definidos<br/>1.3.5 Valor, prioridade, esforço e dificuldade estimados<br/>1.3.6 Dependências e riscos registados<br/>1.3.7 Backlog ordenado e revisto"]
    D["<b>1.4 Desenvolvimento iterativo</b><br/>1.4.1 Incremento planeado a partir do backlog prioritário<br/>1.4.2 Funcionalidades implementadas<br/>1.4.3 Incremento verificado face aos critérios de aceitação<br/>1.4.4 Incremento demonstrado e integrado<br/>1.4.5 Próximo incremento ajustado com base no progresso"]
    E["<b>1.5 Avaliação e evolução</b><br/>1.5.1 MVP demonstrado a utilizadores ou avaliadores<br/>1.5.2 Feedback recolhido e analisado<br/>1.5.3 Backlog repriorizado com base no feedback<br/>1.5.4 Melhorias prioritárias implementadas<br/>1.5.5 Resultados avaliados face aos critérios de sucesso"]
    F["<b>1.6 Conclusão da dissertação</b><br/>1.6.1 Solução e processo documentados<br/>1.6.2 Resultados e limitações descritos<br/>1.6.3 Dissertação finalizada e submetida"]
    P["Projeto de dissertação"]
    A["1.1 Compreensão do problema"]
    B["1.2 Requisitos e story map"]
    C["1.3 Backlog do produto no Jira"]
    D["1.4 Desenvolvimento iterativo"]
    E["1.5 Avaliação e evolução"]
    F["1.6 Conclusão da dissertação"]

    P --> A --> B --> C --> D --> E --> F

    A --> A1["1.1.1 Problema e contexto caracterizados"]
    A --> A2["1.1.2 Utilizadores e partes interessadas identificados"]
    A --> A3["1.1.3 Objetivos e resultados pretendidos definidos"]
    A --> A4["1.1.4 Critérios de sucesso definidos"]
    A1 ~~~ A2 ~~~ A3 ~~~ A4

    B --> B1["1.2.1 Necessidades dos utilizadores identificadas"]
    B --> B2["1.2.2 Atividades principais mapeadas"]
    B --> B3["1.2.3 Tarefas e funcionalidades associadas"]
    B --> B4["1.2.4 Story map revisto e validado"]
    B --> B5["1.2.5 MVP e incrementos seguintes delimitados"]
    B1 ~~~ B2 ~~~ B3 ~~~ B4 ~~~ B5

    C --> C1["1.3.1 Épicos criados para as áreas principais"]
    C --> C2["1.3.2 Stories criadas a partir das necessidades"]
    C --> C3["1.3.3 Subtarefas técnicas identificadas quando necessário"]
    C --> C4["1.3.4 Critérios de aceitação definidos"]
    C --> C5["1.3.5 Valor, prioridade, esforço e dificuldade estimados"]
    C --> C6["1.3.6 Dependências e riscos registados"]
    C --> C7["1.3.7 Backlog ordenado e revisto"]
    C1 ~~~ C2 ~~~ C3 ~~~ C4 ~~~ C5 ~~~ C6 ~~~ C7

    D --> D1["1.4.1 Incremento planeado a partir do backlog prioritário"]
    D --> D2["1.4.2 Funcionalidades implementadas"]
    D --> D3["1.4.3 Incremento verificado face aos critérios de aceitação"]
    D --> D4["1.4.4 Incremento demonstrado e integrado"]
    D --> D5["1.4.5 Próximo incremento ajustado com base no progresso"]
    D1 ~~~ D2 ~~~ D3 ~~~ D4 ~~~ D5

    E --> E1["1.5.1 MVP demonstrado a utilizadores ou avaliadores"]
    E --> E2["1.5.2 Feedback recolhido e analisado"]
    E --> E3["1.5.3 Backlog repriorizado com base no feedback"]
    E --> E4["1.5.4 Melhorias prioritárias implementadas"]
    E --> E5["1.5.5 Resultados avaliados face aos critérios de sucesso"]
    E1 ~~~ E2 ~~~ E3 ~~~ E4 ~~~ E5

    F --> F1["1.6.1 Solução e processo documentados"]
    F --> F2["1.6.2 Resultados e limitações descritos"]
    F --> F3["1.6.3 Dissertação finalizada e submetida"]
    F1 ~~~ F2 ~~~ F3

    classDef root fill:#17324D,color:#FFFFFF,stroke:#17324D,stroke-width:3px,font-size:20px,font-weight:bold;
    classDef analysis fill:#DCEBFF,color:#172033,stroke:#8BB8F0,stroke-width:2px;
    classDef mapping fill:#DDF5E7,color:#172033,stroke:#79C99A,stroke-width:2px;
    classDef backlog fill:#FFF0D5,color:#172033,stroke:#E9B958,stroke-width:2px;
    classDef build fill:#E9E1FF,color:#172033,stroke:#A78BFA,stroke-width:2px;
    classDef review fill:#D9F2F2,color:#172033,stroke:#67BFC0,stroke-width:2px;
    classDef closeout fill:#FFE3E3,color:#172033,stroke:#E69A9A,stroke-width:2px;

    class P root;
    class A analysis;
    class B mapping;
    class C backlog;
    class D build;
    class E review;
    class F closeout;
    class A,A1,A2,A3,A4 analysis;
    class B,B1,B2,B3,B4,B5 mapping;
    class C,C1,C2,C3,C4,C5,C6,C7 backlog;
    class D,D1,D2,D3,D4,D5 build;
    class E,E1,E2,E3,E4,E5 review;
    class F,F1,F2,F3 closeout;

    linkStyle 0,1,2,3,4,5 stroke:#94A3B8,stroke-width:2px;
```

As ligações verticais entre as atividades irmãs servem apenas para manter o desenho compacto; não indicam dependência nem ordem de execução.

> Os incrementos são planeados progressivamente. O respetivo conteúdo pode mudar quando o backlog é revisto após implementação e feedback.
Os incrementos são planeados progressivamente. O respetivo conteúdo pode mudar quando o backlog é revisto após implementação e feedback.
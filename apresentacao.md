# Roteiro de Defesa — TaxaJurosPro (versão enxuta)

> Alinhado 1:1 com os 27 slides ativos do index.html. Tempo-alvo: ~19 min (margem para arguição).
> **(pausa)** = pequena pausa para respirar.

---

## Slide 1 — Capa / Abertura (≈ 40 s)

Bom dia. Agradeço à banca pelo tempo dedicado a este trabalho. **(pausa)**

Meu nome é Kossi Sedjro Mawuli Dominique Houessou, e apresento o "TaxaJurosPro: um sistema web para redução da assimetria informacional no mercado de crédito brasileiro por meio dos dados abertos do Banco Central", sob orientação do Dr. Thiago Iachiley Araújo de Souza. **(pausa)**

Vou mostrar como dados públicos, hoje pouco acessíveis, podem virar uma ferramenta prática de apoio à decisão financeira.

---

## Slide 2 — Sumário · O percurso da apresentação (≈ 35 s)

A apresentação segue cinco atos. **(pausa)**

"A Tensão": o problema. "O Enquadramento": a fundamentação teórica e a metodologia. "A Solução": o sistema e suas funcionalidades. "A Prova": a validação técnica e a avaliação com usuários. E "O Fechamento": objetivos, contribuições e trabalhos futuros. **(pausa)**

A tese central é simples: transformar dados abertos em informação acessível é viável e socialmente relevante.

---

## Slide 3 — § 01 · A Tensão · O paradoxo do crédito brasileiro (≈ 45 s)

O problema central é um paradoxo. **(pausa)**

O Banco Central publica gratuitamente uma enorme quantidade de dados sobre o crédito: centenas de instituições, várias modalidades, milhares de registros. Do ponto de vista da transparência, a informação existe. **(pausa)**

Mas ela é entregue em formato técnico, por uma API OData que retorna JSON e exige saber programar. Ou seja, a transparência existe para quem tem conhecimento técnico, não para quem precisa decidir sobre crédito. Foi essa distância que motivou o trabalho.

---

## Slide 4 — § 02 · A Tensão · Três números tornam o problema irrefutável (≈ 45 s)

Três números oficiais dimensionam o problema. **(pausa)**

Primeiro: o crédito às famílias ultrapassa 4 trilhões de reais, um dos maiores mercados da economia. Segundo: o letramento financeiro do brasileiro, segundo o Banco Central e a OCDE, está distante do ideal. Terceiro: pouca gente consegue fazer cálculos simples de juros. **(pausa)**

Ou seja, o problema não é a disponibilidade do dado, e sim a forma como ele chega ao usuário. É essa lacuna que o TaxaJurosPro preenche.

---

## Slide 5 — § 03 · A Tensão · Pergunta de pesquisa e objetivo geral (≈ 40 s)

Daí a pergunta de pesquisa: **(pausa)** como uma plataforma web integrada à API de dados abertos do Banco Central pode ajudar pessoas físicas a comparar taxas e decidir melhor sobre crédito, reduzindo a assimetria informacional? **(pausa)**

O objetivo geral foi desenvolver essa plataforma: consumir os dados oficiais, processá-los e apresentá-los de forma simples e útil. Os objetivos específicos vão da integração com a API até a consulta, comparação, simulação e a validação da solução.

---

## Slide 6 — § 04 · O Enquadramento · Assimetria informacional (≈ 45 s)

O conceito que fundamenta o trabalho é a assimetria informacional: quando as duas partes de uma negociação têm níveis diferentes de informação. **(pausa)**

No crédito, de um lado o consumidor conhece só a parcela ou a taxa da propaganda. Do outro, a instituição tem modelos de risco, histórico e estatísticas. Esse desequilíbrio faz o consumidor decidir com menos informação. **(pausa)**

O fenômeno foi estudado por Akerlof e ampliado por Stiglitz e Weiss. O TaxaJurosPro não decide pelo usuário: ele reduz essa diferença, organizando dados oficiais de forma clara.

---

## Slide 7 — § 05 · O Enquadramento · Dado publicado não é dado apropriado (≈ 35 s)

Um ponto-chave: publicar dado não é o mesmo que torná-lo acessível. **(pausa)**

Os dados do Banco Central são abertos, mas distribuídos por uma API técnica, com endpoints, OData e JSON. Simples para um desenvolvedor, inacessível para a maioria. **(pausa)**

Existe uma barreira entre o dado publicado e o conhecimento usável. O TaxaJurosPro é a camada intermediária que converte esses registros em informação clara, comparável e acionável.

---

## Slide 8 — § 06 · O Enquadramento · Dados Abertos × Open Finance (≈ 35 s)

Um esclarecimento importante, porque gera dúvida: dados abertos não são Open Finance. **(pausa)**

O TaxaJurosPro usa só dados abertos: públicos, agregados, sem cadastro nem autorização. Já o Open Finance lida com dados individuais do cliente, que exigem consentimento. **(pausa)**

Portanto, o sistema nunca acessa contas, saldos ou dados pessoais. Trabalha apenas com informação pública oficial, o que garante simplicidade e privacidade.

---

## Slide 9 — § 07 · O Enquadramento · Ferramenta de política pública (≈ 30 s)

O trabalho também tem dimensão social. **(pausa)**

Ao transformar dado técnico em informação compreensível, ele aproxima o cidadão das informações do próprio Estado. Isso dialoga com a Estratégia Nacional de Educação Financeira e com os Objetivos de Desenvolvimento Sustentável da Agenda 2030, ligados à redução das desigualdades e ao fortalecimento das instituições.

---

## Slide 10 — § 08 · O Enquadramento · Design Science e trabalhos relacionados (≈ 1 min)

A metodologia foi a Design Science Research, usada quando o objetivo é criar um artefato para resolver um problema real. Aqui, a contribuição científica é o próprio sistema desenvolvido, implementado e validado. **(pausa)**

À direita, o posicionamento na literatura. Nascimento e colaboradores, 2021, compararam instituições manualmente; eu automatizo via API do Banco Central. **(pausa)** Ornelas e Pécora, num Working Paper do Banco Central de 2022, estudaram o impacto das fintechs; meu diferencial é ser voltado ao consumidor final. **(pausa)** Caciatori Junior, 2020, analisou a concentração bancária em nível macro; o TaxaJurosPro desce ao nível prático, com comparação por instituição. E Freitas e Reis, 2022, propuseram uma plataforma conceitual; aqui é uma implementação real com dados oficiais. **(pausa)**

Na revisão, não encontrei nenhum comparador de taxas com dados abertos do Banco Central voltado ao cidadão. É nessa lacuna que o trabalho se posiciona.

---

## Slide 11 — § 10 · A Solução · Requisitos e processo de desenvolvimento (≈ 40 s)

Passando à solução. O desenvolvimento partiu de um levantamento de requisitos, seguindo Sommerville. **(pausa)**

Os requisitos funcionais: consultar taxas, comparar instituições, simular pelo Price e espelhar condições. Os não funcionais: usabilidade, desempenho, acessibilidade e integração confiável com a API. **(pausa)**

O processo foi incremental: cada funcionalidade foi validada antes da próxima, reduzindo riscos.

---

## Slide 12 — § 11 · A Solução · Modalidades de crédito cobertas (≈ 30 s)

O escopo foi delimitado a operações pré-fixadas de pessoa física, as mais presentes no dia a dia. **(pausa)**

São seis grupos: cartão de crédito, cheque especial, consignado, crédito pessoal, financiamento de bens e desconto de cheques. Um recorte deliberado, focado no que mais afeta o consumidor.

---

## Slide 13 — § 12 · A Solução · Arquitetura em três camadas (≈ 40 s)

A arquitetura segue a separação de responsabilidades, em três camadas. **(pausa)**

Apresentação: componentes React, com TanStack Router e Tailwind mais Radix UI. Lógica de negócio: hooks customizados com o processamento e os cálculos financeiros. E acesso a dados: comunicação com a API pela Fetch API, com o TanStack Query gerenciando cache e sincronização. **(pausa)**

Isso facilita manutenção, reuso e evolução.

---

## Slide 14 — § 13 · A Solução · Fluxo de dados, da API ao usuário (≈ 40 s)

Este é o caminho do dado até o usuário. **(pausa)**

Começa na API do Banco Central, que retorna cerca de mil registros, obtidos pela Fetch API. Como a API deixou de oferecer filtros durante o projeto, a filtragem passou a ser feita no navegador. **(pausa)** Depois os dados vão para cache no TanStack Query e no localStorage, e só então alimentam as páginas de consulta, comparação e simulação. Isso reduz requisições e melhora o desempenho.

---

## Slide 15 — Funcionalidade 01 · Consulta de taxas (≈ 30 s)

Passo às funcionalidades, na jornada descobrir, comparar e decidir. **(pausa)**

A primeira é a consulta de taxas: todas as instituições reguladas em uma tabela filtrável. O usuário escolhe a modalidade e vê as taxas organizadas. O que antes exigia ler JSON de uma API vira uma consulta visual simples.

---

## Slide 16 — Funcionalidade 02 · Comparação entre instituições (≈ 40 s)

A segunda funcionalidade é o comparador. **(pausa)**

O usuário escolhe a modalidade e duas instituições; o sistema mostra as taxas lado a lado e destaca a menor. **(pausa)** Uma diferença que parece pequena vira um impacto grande ao longo de um financiamento. A funcionalidade transforma centenas de registros em uma resposta objetiva.

---

## Slide 17 — Funcionalidade 03 · Simulador de empréstimos (≈ 45 s)

A terceira, e mais útil, é o simulador. **(pausa)**

O usuário informa valor e número de parcelas; o sistema aplica o Sistema Price, de amortização francesa com parcela fixa, sobre as taxas de cada banco e calcula as prestações, ordenadas da menor para a maior. **(pausa)** Além da parcela, mostra os juros totais. Assim o usuário enxerga o impacto real da taxa no bolso, não só o percentual.

---

## Slide 18 — Funcionalidade 04 · Espelhamento de condições (≈ 30 s)

A quarta funcionalidade é o espelhamento, com base na Resolução CMN 4.292 de 2013, sobre portabilidade de crédito. **(pausa)**

Ela funciona como um mecanismo de descoberta: a partir de uma condição conhecida, ajuda o usuário a encontrar instituições com condições equivalentes ou melhores, conectando a tecnologia ao direito do consumidor de migrar seu crédito.

---

## Slide 19 — § 14 · A Prova · Validação técnica (≈ 40 s)

A validação teve quatro frentes. **(pausa)**

Testes funcionais das funcionalidades; conferência dos dados contra a API oficial; comparação dos cálculos com calculadoras de referência, com diferença só de centavos por arredondamento; e testes de responsividade e compatibilidade no Chrome, Firefox e Edge. **(pausa)** Tudo confirmou que o sistema atende aos requisitos técnicos.

---

## Slide 20 — § 15 · A Prova · Avaliação de usabilidade (≈ 50 s)

Também avaliei a usabilidade com usuários reais. **(pausa)**

Apliquei um questionário próprio, no Google Forms, com escala Likert de cinco pontos ancorada na ISO 9241-11. Foram nove participantes, respondendo dez afirmações após usar o sistema. **(pausa)** A média global foi 4,77 de 5, numa faixa estreita de 4,67 a 4,89, indicando que acharam o sistema fácil e intuitivo. **(pausa)**

Optei deliberadamente por um instrumento próprio, e não o SUS, pelo caráter formativo desta etapa; o SUS com amostra maior fica como trabalho futuro. A amostra é pequena, mas dá evidências iniciais sólidas.

---

## Slide 21 — § 16 · A Prova · Limitações reconhecidas (≈ 40 s)

Nomear os limites faz parte do rigor. **(pausa)**

No método: nove participantes revelam problemas, mas não generalizam; recrutamento por conveniência; instrumento próprio, não o SUS. No escopo: só o Price, sem SAC; sem o CET completo; só pré-fixadas de pessoa física. E no processo: a dependência da API do Banco Central, que mudou durante o projeto. **(pausa)** Foram recortes conscientes, coerentes com o escopo.

---

## Slide 22 — § 17 · A Prova · O que prova, e o que não prova (≈ 35 s)

É importante ser preciso sobre a evidência. **(pausa)**

Fica demonstrada a viabilidade técnica e a percepção de utilidade e clareza pelos usuários: o sistema reduz a barreira de acesso à informação. **(pausa)** O que não afirmo é que ele leve, de forma causal, a escolhas mais vantajosas — isso exigiria um estudo experimental. O trabalho cria as condições para decisões mais informadas, e deixa a prova de impacto para o futuro.

---

## Slide 23 — § 18 · O Fechamento · Alcance dos objetivos (≈ 25 s)

Os seis objetivos específicos foram cumpridos. **(pausa)**

A plataforma está funcional e integrada à API, permite consultar, comparar e simular com dados oficiais, tem interface responsiva e cache, e teve boa aceitação na avaliação. Cada objetivo virou uma entrega concreta.

---

## Slide 24 — § 19 · O Fechamento · Contribuições (≈ 35 s)

As contribuições vêm em três frentes. **(pausa)**

Técnica: uma arquitetura de referência para integrar dados abertos, replicável em outros contextos. Social: reduzir a barreira de acesso à informação de crédito. E acadêmica: um estudo de caso completo em Design Science, do requisito ao artefato validado.

---

## Slide 25 — § 20 · O Fechamento · Trabalhos futuros (≈ 35 s)

A continuidade tem duas frentes. **(pausa)**

Funcional: Sistema SAC, o CET completo, gráficos históricos, pessoa jurídica e uma área autenticada, sugerida pelos próprios usuários. **(pausa)** Científica: avaliação com amostra maior usando o SUS, medidas objetivas de desempenho e um estudo experimental para verificar o impacto real nas decisões.

---

## Slide 26 — § 21 · O Fechamento · Considerações finais (≈ 40 s)

Concluindo: o trabalho mostrou que transformar dados abertos em informação acessível é viável e útil para apoiar decisões de crédito. **(pausa)**

Embora as taxas sejam públicas, o formato técnico afasta o cidadão. O TaxaJurosPro reúne consulta, comparação e simulação numa só plataforma, com dados oficiais. **(pausa)** A pergunta foi respondida, os seis objetivos atingidos com o sistema em produção, e as limitações foram deliberadas. Os objetivos da pesquisa foram alcançados, unindo Engenharia de Software, Desenvolvimento Web e Educação Financeira.

---

## Slide 27 — Obrigado (≈ 15 s)

Encerro por aqui. Agradeço à banca e fico à disposição para as perguntas. **(pausa)** Obrigado.

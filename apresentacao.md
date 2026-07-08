# Roteiro de Defesa — TaxaJurosPro

> Alinhado 1:1 com os 29 slides do index.html, na ordem exata da apresentação.
> Tempo-alvo total: 25 a 30 minutos.
> **(pausa)** = pequena pausa para respirar e não se perder na leitura.

---

## Slide 1 — Capa / Abertura (≈ 1 min)

Bom dia. **(pausa)**

Antes de iniciar, gostaria de agradecer aos professores da banca pelo tempo dedicado à avaliação deste trabalho. **(pausa)** É uma satisfação poder apresentar o resultado desta pesquisa e compartilhar com os senhores um projeto que reuniu conhecimentos de engenharia de software, desenvolvimento web, sistemas de informação e educação financeira. **(pausa)**

Meu nome é Kossi Sedjro Mawuli Dominique Houessou **(pausa)** e o trabalho que apresento hoje tem como título "TaxaJurosPro: Desenvolvimento de um Sistema Web para Redução da Assimetria Informacional no Mercado de Crédito Brasileiro por meio da Integração com Dados Abertos do Banco Central", **(pausa)** desenvolvido sob orientação do Dr. Thiago Iachiley Araújo de Souza. **(pausa)**

Durante esta apresentação, vou mostrar como dados públicos, que atualmente são pouco acessíveis para a maioria da população, podem ser transformados em uma ferramenta prática para apoiar decisões financeiras mais conscientes. **(pausa)** Também apresentarei a fundamentação teórica da pesquisa, as decisões de desenvolvimento adotadas, a validação realizada e os principais resultados obtidos.

---

## Slide 2 — Sumário · O percurso da apresentação (≈ 1 min)

Antes de entrarmos no desenvolvimento do trabalho, gostaria de apresentar rapidamente o percurso que seguiremos durante esta defesa. **(pausa)**

Estruturei a apresentação em cinco momentos, cada um respondendo a uma pergunta importante da pesquisa. **(pausa)**

No primeiro ato, "A Tensão", vou mostrar qual foi o problema que motivou este trabalho e por que ele merece atenção. Veremos que existe um paradoxo: os dados sobre taxas de juros são públicos, mas continuam pouco acessíveis para a maior parte da população. **(pausa)**

Em seguida, em "O Enquadramento", apresentarei a fundamentação teórica que sustenta a pesquisa, abordando conceitos como assimetria informacional, dados abertos e Design Science Research, que orientou o desenvolvimento da solução. **(pausa)**

No terceiro momento, "A Solução", mostrarei o TaxaJurosPro, sua arquitetura, os requisitos definidos e as funcionalidades implementadas. **(pausa)**

Depois, em "A Prova", apresentarei como o sistema foi validado, incluindo os testes técnicos e a avaliação de usabilidade com usuários, além das limitações identificadas durante a pesquisa. **(pausa)**

Por fim, em "O Fechamento", retomarei os objetivos do trabalho, apresentarei as contribuições alcançadas e discutirei possíveis evoluções futuras. **(pausa)**

Ao longo de toda a apresentação, buscarei demonstrar a tese central desta pesquisa: que transformar dados abertos em informação acessível é não apenas tecnicamente viável, mas também socialmente relevante.

---

## Slide 3 — § 01 · A Tensão · O paradoxo do crédito brasileiro (≈ 1 min 10 s)

Gostaria de começar apresentando o problema central desta pesquisa. **(pausa)**

Hoje vivemos uma situação bastante curiosa. O Banco Central do Brasil disponibiliza gratuitamente uma enorme quantidade de informações sobre o mercado de crédito. São centenas de instituições financeiras, diversas modalidades de empréstimo e milhares de registros atualizados periodicamente. **(pausa)**

Ou seja, do ponto de vista da transparência pública, essas informações existem e estão disponíveis para qualquer pessoa. **(pausa)**

Entretanto, existe um paradoxo. **(pausa)** Embora os dados sejam públicos, eles permanecem praticamente inacessíveis para o cidadão comum. Isso acontece porque são disponibilizados em um formato essencialmente técnico, por meio de uma API baseada no padrão OData, retornando arquivos JSON que exigem conhecimento de programação para serem consultados e interpretados. **(pausa)**

Na prática, a transparência existe para quem possui conhecimento técnico, mas não necessariamente para quem realmente precisa utilizar essas informações para tomar decisões financeiras. **(pausa)**

Foi justamente essa distância entre a existência do dado público e sua utilização efetiva que motivou o desenvolvimento deste trabalho.

---

## Slide 4 — § 02 · A Tensão · Três números tornam o problema irrefutável (≈ 1 min 10 s)

Para compreender melhor a importância desse problema, gostaria de destacar três números provenientes de fontes oficiais do Banco Central. **(pausa)**

O primeiro é o volume do mercado de crédito brasileiro destinado às famílias, que ultrapassa 4 trilhões de reais. Estamos falando de um dos maiores mercados da economia nacional. **(pausa)**

O segundo dado está relacionado ao letramento financeiro. Segundo estudos do próprio Banco Central e da OCDE, o índice médio de educação financeira da população brasileira ainda está distante do ideal, indicando dificuldades para compreender conceitos básicos relacionados ao crédito e aos juros. **(pausa)**

O terceiro dado é ainda mais preocupante. Uma parcela muito pequena da população consegue realizar corretamente cálculos simples envolvendo juros. Isso significa que, mesmo quando as informações estão disponíveis, muitas pessoas não conseguem interpretá-las adequadamente para comparar diferentes opções de crédito. **(pausa)**

Esses números mostram que o problema não está apenas na disponibilidade dos dados, mas principalmente na forma como eles chegam ao usuário final. **(pausa)** E foi exatamente essa lacuna que o TaxaJurosPro buscou preencher.

---

## Slide 5 — § 03 · A Tensão · Pergunta de pesquisa e objetivo geral (≈ 1 min)

Diante desse cenário, surgiu a seguinte pergunta de pesquisa: **(pausa)**

Como uma plataforma web integrada à API de dados abertos do Banco Central pode auxiliar pessoas físicas a comparar taxas de juros e tomar decisões mais informadas sobre operações de crédito, contribuindo para reduzir a assimetria informacional existente nesse mercado? **(pausa)**

Para responder a essa pergunta, defini como objetivo geral desenvolver uma plataforma web capaz de consumir automaticamente os dados oficiais do Banco Central, processá-los e apresentá-los de forma simples, intuitiva e útil ao usuário. **(pausa)**

A partir desse objetivo geral foram estabelecidos os objetivos específicos, que envolveram desde a integração com a API oficial até a implementação das funcionalidades de consulta, comparação e simulação de crédito, além da validação técnica e da avaliação de usabilidade da solução desenvolvida. **(pausa)**

Ao longo da apresentação, mostrarei como cada um desses objetivos foi efetivamente alcançado e como eles contribuíram para responder à pergunta que motivou esta pesquisa.

---

## Slide 6 — § 04 · O Enquadramento · O nome técnico da dor: assimetria informacional (≈ 1 min 20 s)

Antes de apresentar a solução desenvolvida, é importante entender o conceito que fundamenta toda esta pesquisa: a assimetria informacional. **(pausa)**

Esse termo descreve uma situação em que duas partes de uma negociação possuem níveis diferentes de informação. No mercado de crédito, isso acontece de forma bastante evidente. **(pausa)**

De um lado está o consumidor, que normalmente conhece apenas o valor da parcela ou a taxa apresentada em uma propaganda. Muitas vezes ele não consegue comparar diferentes ofertas nem compreender o impacto dos juros ao longo do tempo. **(pausa)**

Do outro lado estão as instituições financeiras, que possuem acesso a uma grande quantidade de informações: modelos de risco, histórico de crédito dos clientes, estatísticas do mercado e conhecimento detalhado sobre seus próprios produtos. **(pausa)**

Esse desequilíbrio cria um ambiente em que o consumidor tende a tomar decisões com menos informação do que a instituição financeira. **(pausa)**

Esse fenômeno foi estudado inicialmente por George Akerlof, em seu clássico trabalho sobre mercados com informação imperfeita, e posteriormente ampliado por Stiglitz e Weiss para o contexto do mercado de crédito. **(pausa)**

O TaxaJurosPro não pretende substituir a decisão do usuário. **(pausa)** Seu objetivo é reduzir essa diferença de informação, oferecendo dados oficiais organizados de forma clara para que o consumidor possa tomar decisões mais conscientes.

---

## Slide 7 — § 05 · O Enquadramento · Dado publicado não é dado apropriado (≈ 1 min)

Um ponto muito importante desta pesquisa é compreender que publicar dados não significa necessariamente torná-los acessíveis. **(pausa)**

Hoje o Banco Central disponibiliza uma enorme quantidade de informações em formato aberto. No entanto, esses dados são distribuídos por meio de uma API técnica, utilizando estruturas como endpoints, parâmetros OData e arquivos JSON. **(pausa)**

Para um desenvolvedor, isso é relativamente simples. Mas para a maioria da população, esse formato é completamente inacessível. **(pausa)**

Existe, portanto, uma barreira entre o dado publicado e o conhecimento efetivamente utilizado pelo cidadão. **(pausa)**

Diversos autores que estudam dados abertos afirmam exatamente isso: disponibilizar informação é apenas o primeiro passo. É necessário transformá-la em algo compreensível, útil e capaz de apoiar decisões. **(pausa)**

Foi justamente essa transformação que procurei realizar neste trabalho. Em outras palavras, o TaxaJurosPro funciona como uma camada intermediária entre os dados técnicos do Banco Central e o usuário final, convertendo registros complexos em informações claras, comparáveis e acionáveis.

---

## Slide 8 — § 06 · O Enquadramento · Que tipo de dado aberto o sistema usa (Dados Abertos × Open Finance) (≈ 1 min)

Neste ponto, gostaria de esclarecer uma distinção importante, porque é uma dúvida bastante comum. **(pausa)** Muitas pessoas confundem Dados Abertos com Open Finance, mas são iniciativas completamente diferentes. **(pausa)**

O TaxaJurosPro utiliza exclusivamente dados abertos do Banco Central. Esses dados são públicos, agregados e podem ser acessados por qualquer pessoa sem necessidade de autenticação, cadastro ou autorização do usuário. **(pausa)**

Já o Open Finance trabalha com informações individuais dos clientes. Nesse modelo, os dados bancários pertencem ao usuário e só podem ser compartilhados mediante seu consentimento explícito. **(pausa)**

Portanto, em nenhum momento o TaxaJurosPro acessa informações pessoais, contas bancárias, saldos, extratos ou qualquer dado sensível. **(pausa)**

Toda a aplicação trabalha apenas com informações públicas disponibilizadas oficialmente pelo Banco Central, garantindo simplicidade de utilização e respeito à privacidade dos usuários.

---

## Slide 9 — § 07 · O Enquadramento · Mais que um sistema: ferramenta de política pública (≈ 1 min)

Além do aspecto tecnológico, este trabalho também possui uma dimensão social. **(pausa)** A proposta está alinhada com iniciativas governamentais voltadas para educação financeira e transparência pública. **(pausa)**

Ao transformar dados técnicos em informações compreensíveis, o sistema contribui para aproximar o cidadão das informações produzidas pelo próprio Estado. **(pausa)**

Isso vai ao encontro da Estratégia Nacional de Educação Financeira, que incentiva o desenvolvimento de ferramentas capazes de melhorar o conhecimento financeiro da população. **(pausa)**

Da mesma forma, a pesquisa dialoga com os Objetivos de Desenvolvimento Sustentável da Agenda 2030, especialmente aqueles relacionados à redução das desigualdades, à promoção do trabalho decente e ao fortalecimento das instituições. **(pausa)**

Embora seja uma aplicação tecnológica, seu impacto potencial vai além da engenharia de software, pois busca facilitar o acesso da população a informações relevantes para decisões financeiras do cotidiano.

---

## Slide 10 — § 08 · O Enquadramento · Design Science: o artefato como contribuição (≈ 1 min 20 s)

Passando agora para a metodologia, a pesquisa foi conduzida utilizando a abordagem Design Science Research, bastante utilizada em Sistemas de Informação quando o objetivo é desenvolver um artefato tecnológico para resolver um problema real. **(pausa)**

Diferentemente de pesquisas puramente descritivas ou experimentais, na Design Science o principal resultado científico é justamente o artefato desenvolvido. **(pausa)** Ou seja, neste trabalho, a contribuição científica não é apenas discutir a assimetria informacional ou analisar dados do mercado de crédito. A principal contribuição é o desenvolvimento, a implementação e a validação de uma solução capaz de enfrentar esse problema na prática. **(pausa)**

O processo iniciou com o levantamento bibliográfico e documental, seguido pela identificação dos requisitos do sistema, desenvolvimento incremental da aplicação, validação técnica e, por fim, pela avaliação de usabilidade com usuários reais. **(pausa)**

À direita, posiciono o trabalho frente à literatura. **(pausa)** Nascimento e colaboradores, em 2021, fizeram uma comparação entre instituições, porém de forma manual, consultando sites; o TaxaJurosPro automatiza essa comparação consumindo diretamente a API do Banco Central. **(pausa)** Ornelas e Pécora, em um Working Paper do próprio Banco Central de 2022, estudaram o impacto das fintechs no crédito; a diferença é que o meu trabalho entrega uma ferramenta voltada diretamente ao consumidor final. **(pausa)** Caciatori Junior, em 2020, analisou a concentração e a competitividade bancária em nível macro; o TaxaJurosPro desce ao nível prático, permitindo a comparação granular entre instituições. **(pausa)** E Freitas e Reis, em 2022, propuseram uma plataforma de educação financeira, mas em caráter conceitual; aqui a proposta é uma implementação real, funcional, com dados oficiais. **(pausa)**

Ou seja, durante a revisão da literatura não identifiquei nenhum comparador de taxas voltado ao cidadão que utilizasse os dados abertos do Banco Central. É justamente nessa lacuna que o TaxaJurosPro se posiciona: não se limita a análises conceituais ou protótipos, mas entrega uma aplicação funcional, em produção e alimentada continuamente por dados oficiais.

---

## Slide 11 — § 09 · A Solução · TaxaJurosPro em uma frase (≈ 45 s)

Feita a fundamentação, passo agora à solução propriamente dita. **(pausa)**

Se eu tivesse que resumir o TaxaJurosPro em uma única frase, diria que é uma plataforma web que transforma os dados brutos da API do Banco Central em informação acionável para o cidadão. **(pausa)**

E, para o usuário, essa transformação se traduz em uma jornada simples de três passos: primeiro descobrir as taxas praticadas no mercado, depois comparar as instituições e, por fim, decidir com base em uma simulação concreta. **(pausa)**

Descobrir, comparar e decidir. É em torno dessa jornada que todas as funcionalidades foram organizadas. **(pausa)** O sistema, aliás, está publicado e em produção, acessível no endereço taxajurospro.com.br.

---

## Slide 12 — § 10 · A Solução · Requisitos e processo de desenvolvimento (≈ 1 min)

Antes de escrever qualquer linha de código, realizei um levantamento estruturado de requisitos, seguindo as boas práticas de engenharia de software descritas por Sommerville. **(pausa)**

Os requisitos funcionais definiram o que o sistema deveria fazer: consultar taxas por instituição e modalidade, comparar instituições diretamente, simular empréstimos pelo Sistema Price e espelhar condições de crédito. **(pausa)**

Já os requisitos não funcionais trataram de como o sistema deveria se comportar: usabilidade da interface, desempenho no processamento dos dados, acessibilidade em diferentes dispositivos e integração confiável com o serviço externo da API do Banco Central. **(pausa)**

O desenvolvimento seguiu um processo incremental: cada incremento agregou uma funcionalidade e foi validado antes de se avançar para o próximo. Isso reduziu riscos e facilitou correções ao longo do desenvolvimento.

---

## Slide 13 — § 11 · A Solução · As modalidades de crédito cobertas (≈ 50 s)

Um ponto importante do trabalho foi delimitar o escopo de cobertura do sistema. **(pausa)**

O TaxaJurosPro trabalha com operações de crédito pré-fixadas destinadas a pessoas físicas, com recursos livres, que são justamente as formas de financiamento mais presentes no cotidiano do consumidor. **(pausa)**

Na prática, o sistema cobre seis grandes grupos de modalidades: cartão de crédito, nas modalidades rotativo e parcelado; cheque especial; crédito consignado, incluindo INSS, setor público e privado; crédito pessoal não consignado; financiamento de bens, como veículos e eletrônicos; e desconto de cheques. **(pausa)**

Esse foi um recorte deliberado: concentrar a solução nas operações que mais afetam o dia a dia das pessoas físicas.

---

## Slide 14 — § 12 · A Solução · Arquitetura em três camadas (≈ 1 min)

Nesta etapa apresento a arquitetura utilizada no desenvolvimento. **(pausa)**

A aplicação foi organizada em três camadas principais, seguindo o princípio da separação de responsabilidades. **(pausa)**

Na camada de apresentação estão os componentes React responsáveis pela interface do usuário, apoiados pelo TanStack Router para a navegação e pelo Tailwind com Radix UI para um design acessível. **(pausa)**

Na camada de lógica de negócio encontram-se os hooks customizados, responsáveis pelo processamento dos dados e pelos cálculos financeiros, mantendo as regras de negócio separadas da interface. **(pausa)**

Por fim, a camada de acesso aos dados realiza a comunicação com a API do Banco Central utilizando a Fetch API, enquanto o TanStack Query gerencia o cache e a sincronização dos dados. **(pausa)**

Essa separação facilita a manutenção, a reutilização de código e a evolução futura do sistema.

---

## Slide 15 — § 13 · A Solução · Fluxo de dados, da API ao usuário (≈ 1 min)

Este diagrama mostra o caminho percorrido pelos dados até chegarem ao usuário. **(pausa)**

Tudo começa na API oficial do Banco Central, que retorna aproximadamente mil registros contendo informações de pessoas físicas e jurídicas. Esses dados são obtidos utilizando a Fetch API. **(pausa)**

Um ponto que merece destaque: como a API deixou de oferecer filtros por categoria durante o desenvolvimento do projeto, a filtragem passou a ser realizada no próprio navegador, do lado do cliente. **(pausa)**

Após esse processamento, os dados são armazenados em cache utilizando o TanStack Query e também persistidos no localStorage, para acelerar acessos futuros. **(pausa)**

Somente então essas informações são disponibilizadas para as páginas de consulta, comparação e simulação. **(pausa)**

Esse fluxo reduz requisições desnecessárias e melhora significativamente o desempenho percebido pelo usuário.

---

## Slide 16 — Funcionalidade 01 · Descobrir · Consulta de taxas (≈ 50 s)

Com a arquitetura apresentada, passo agora a demonstrar as funcionalidades, seguindo aquela jornada de descobrir, comparar e decidir. **(pausa)**

A primeira funcionalidade é a consulta de taxas. Aqui o sistema reúne todas as instituições reguladas em uma única tabela filtrável. **(pausa)**

O usuário seleciona a modalidade de crédito desejada e o sistema exibe, de forma organizada, as taxas praticadas pelas diferentes instituições financeiras, a partir dos dados oficiais do Banco Central. **(pausa)**

O que antes exigia consultar uma API técnica e interpretar arquivos JSON passa a ser uma simples consulta visual, ao alcance de qualquer pessoa.

---

## Slide 17 — Funcionalidade 02 · Comparar · Comparação entre instituições (≈ 1 min)

Depois de descobrir as taxas, a segunda funcionalidade do sistema é o comparador de instituições financeiras. **(pausa)**

A ideia aqui é simples: permitir que o usuário compare duas instituições para uma mesma modalidade de crédito. **(pausa)**

Primeiro, o usuário escolhe o tipo de crédito, por exemplo crédito pessoal não consignado. Em seguida, seleciona duas instituições financeiras disponíveis na base do Banco Central. **(pausa)**

O sistema então apresenta as duas taxas lado a lado e destaca automaticamente qual instituição possui a menor taxa. **(pausa)**

Embora a diferença entre duas taxas possa parecer pequena, ela representa um impacto financeiro significativo quando aplicada durante vários meses em um financiamento. **(pausa)**

Essa funcionalidade reduz o tempo necessário para comparar ofertas e transforma centenas de registros da API em uma informação objetiva, permitindo que o usuário identifique rapidamente a alternativa mais vantajosa.

---

## Slide 18 — Funcionalidade 03 · Decidir · Simulador de empréstimos (≈ 1 min)

A terceira funcionalidade é o simulador de empréstimos, que considero a mais útil para o usuário final. **(pausa)**

Depois de escolher a modalidade de crédito, o usuário informa apenas o valor desejado e o número de parcelas. **(pausa)**

O sistema utiliza as taxas de cada instituição financeira e aplica o Sistema Price para calcular automaticamente o valor das parcelas. **(pausa)**

Os resultados são apresentados ordenados pela menor prestação, permitindo que o usuário visualize imediatamente quais bancos oferecem a condição mais econômica. **(pausa)**

Além da parcela mensal, também são apresentados os juros totais pagos durante todo o financiamento. **(pausa)**

Assim, o usuário deixa de comparar apenas percentuais de juros e passa a visualizar o impacto financeiro real daquela taxa sobre o seu bolso.

---

## Slide 19 — Aprofundamento técnico · A matemática por trás do simulador (≈ 50 s)

Vale detalhar rapidamente a matemática que sustenta o simulador. **(pausa)**

O cálculo utiliza o Sistema Price, também conhecido como sistema de amortização francesa. A característica principal desse sistema é a parcela fixa: o valor pago a cada mês permanece constante do início ao fim do financiamento. **(pausa)**

Essa parcela fixa embute juros compostos, e sua composição muda ao longo do tempo: no começo, a maior parte da parcela corresponde a juros; ao final, a maior parte corresponde à amortização do valor principal. **(pausa)**

Implementar esse motor de cálculo corretamente foi essencial para garantir que as simulações refletissem a realidade das operações de crédito e fossem confiáveis para apoiar a decisão do usuário.

---

## Slide 20 — Funcionalidade 04 · Continuar · Espelhamento de condições (≈ 50 s)

A quarta funcionalidade é o espelhamento de condições, que possui um enquadramento jurídico importante. **(pausa)**

Ela se apoia na Resolução CMN 4.292, de 2013, que trata da portabilidade de crédito e do direito do consumidor de buscar condições mais vantajosas em outras instituições. **(pausa)**

Na prática, essa funcionalidade atua como um mecanismo de descoberta de alternativas: a partir de uma condição de crédito conhecida, o sistema ajuda o usuário a identificar outras instituições que poderiam oferecer condições equivalentes ou melhores. **(pausa)**

É uma funcionalidade que conecta a dimensão técnica da solução ao direito real do consumidor de renegociar e migrar seu crédito.

---

## Slide 21 — § 14 · A Prova · Validação técnica em quatro dimensões (≈ 1 min)

Após a implementação, iniciou-se a etapa de validação do sistema, organizada em quatro dimensões. **(pausa)**

Primeiro, foram realizados testes funcionais para verificar se todas as funcionalidades operavam conforme os requisitos definidos. **(pausa)**

Segundo, foi feita a conferência dos dados apresentados na aplicação, comparando-os diretamente com os dados retornados pela API oficial do Banco Central. **(pausa)**

Terceiro, os cálculos financeiros implementados no simulador foram comparados com calculadoras financeiras de referência, apresentando precisão compatível, com diferenças apenas na ordem de centavos, decorrentes de arredondamentos. **(pausa)**

E quarto, foram realizados testes de responsividade em diferentes tamanhos de tela e testes de compatibilidade nos navegadores Google Chrome, Mozilla Firefox e Microsoft Edge. **(pausa)**

Esses procedimentos permitiram confirmar que o sistema atende aos requisitos técnicos estabelecidos durante a fase de análise.

---

## Slide 22 — § 15 · A Prova · Avaliação de usabilidade com usuários (≈ 1 min 10 s)

Além da validação técnica, foi realizada uma avaliação de usabilidade com usuários reais. **(pausa)**

Para isso, elaborei um questionário próprio, disponibilizado por meio do Google Forms, com afirmações respondidas em uma escala Likert de cinco pontos, ancorada nos critérios de usabilidade da norma ISO 9241-11. **(pausa)**

O questionário foi aplicado a nove participantes, que utilizaram livremente as funcionalidades do TaxaJurosPro antes de responder às dez afirmações da escala. **(pausa)**

O resultado foi bastante positivo: a média global foi de 4,77 em 5, com as afirmações variando numa faixa estreita, entre 4,67 e 4,89. Isso indica que os participantes perceberam o sistema como fácil de aprender, intuitivo e simples de utilizar. **(pausa)**

É importante esclarecer que optei deliberadamente por um instrumento sob medida, e não pela escala SUS. **(pausa)** A escolha se justifica pelo caráter formativo da avaliação nesta etapa: eu queria investigar aspectos específicos da interface do TaxaJurosPro. A aplicação do SUS, com uma amostra maior, está prevista como trabalho futuro. **(pausa)**

Embora a amostra seja pequena e não permita generalizações estatísticas, ela fornece evidências iniciais importantes sobre a qualidade da experiência oferecida pela aplicação.

---

## Slide 23 — § 16 · A Prova · Limitações reconhecidas como escolhas conscientes (≈ 1 min)

Toda pesquisa tem limites, e nomeá-los faz parte do rigor científico. Organizei as limitações em três grupos. **(pausa)**

No método: a amostra de nove participantes é suficiente para revelar problemas de usabilidade, como aponta Nielsen, mas não para generalizar estatisticamente. O recrutamento foi por conveniência, típico de uma avaliação formativa em estágio inicial. E, como comentei, o instrumento foi um questionário próprio, uma escolha deliberada, e não o SUS. **(pausa)**

No escopo: o simulador implementa apenas o Sistema Price, ficando o Sistema SAC como trabalho futuro. O Custo Efetivo Total completo, com tarifas e seguros, não foi implementado. E o sistema cobre apenas operações pré-fixadas de pessoa física, com a ampliação para pessoa jurídica prevista no roadmap. **(pausa)**

E no processo: a principal limitação foi a dependência de um serviço externo, a API do Banco Central, que mudou de comportamento durante o desenvolvimento. **(pausa)**

O ponto central aqui é que essas limitações não foram acidentes: foram recortes conscientes, coerentes com o escopo informacional do trabalho.

---

## Slide 24 — § 17 · A Prova · O que este trabalho prova, e o que não prova (≈ 1 min)

Ainda no espírito do rigor científico, é importante ser preciso sobre onde a evidência termina. **(pausa)**

O que fica demonstrado é a viabilidade técnica da solução e a percepção de utilidade e clareza por parte dos usuários. A plataforma reduz, de fato, a barreira de acesso e de interpretação dos dados de taxas. **(pausa)**

O que este trabalho não afirma é que o uso do sistema conduza, de forma causal, a escolhas economicamente mais vantajosas. Comprovar isso exigiria um estudo longitudinal ou experimental, que está fora do escopo informacional que delimitei. **(pausa)**

Em outras palavras, o trabalho responde à dimensão de impacto de maneira indireta: ele cria as condições necessárias para decisões mais informadas, deixando a confirmação empírica desses ganhos como uma investigação futura.

---

## Slide 25 — § 18 · O Fechamento · Alcance dos objetivos específicos (≈ 50 s)

Entrando no fechamento, retomo os objetivos específicos apresentados no início da pesquisa, para mostrar que todos os seis foram efetivamente cumpridos. **(pausa)**

Foi desenvolvida uma plataforma web funcional, integrada diretamente à API oficial do Banco Central. O sistema permite consultar centenas de instituições financeiras, comparar taxas de diferentes modalidades e simular financiamentos com dados oficiais. **(pausa)**

A aplicação apresenta interface responsiva, desempenho satisfatório e mecanismos de cache que reduzem o tempo de carregamento em acessos posteriores. E a avaliação de usabilidade indicou boa aceitação pelos participantes. **(pausa)**

Cada objetivo específico definido no início encontrou correspondência direta em uma entrega concreta do sistema.

---

## Slide 26 — § 19 · O Fechamento · Contribuições em três frentes (≈ 50 s)

As contribuições deste trabalho se organizam em três frentes. **(pausa)**

A primeira é técnica: uma arquitetura de referência para integração com dados abertos governamentais, com decisões de caching e de processamento no lado do cliente que podem ser replicadas em outros contextos. **(pausa)**

A segunda é social: ao transformar dados técnicos em informação acessível, o trabalho aproxima o cidadão das informações produzidas pelo Estado e contribui para a educação financeira. **(pausa)**

A terceira é acadêmica: um estudo de caso completo, documentado sob a ótica da Design Science, indo do levantamento de requisitos até o artefato validado, servindo de base para estudos futuros.

---

## Slide 27 — § 20 · O Fechamento · Trabalhos futuros (≈ 50 s)

A pesquisa abre continuidade em duas frentes. **(pausa)**

Na frente funcional, entre as evoluções do sistema estão: o Sistema SAC como complemento ao Price, o cálculo integral do Custo Efetivo Total incluindo tarifas, seguros e IOF, gráficos históricos de evolução das taxas, a ampliação para pessoa jurídica e uma área autenticada, que foi diretamente sugerida pelos usuários no campo aberto do questionário. **(pausa)**

Na frente científica, entre as evoluções da pesquisa estão: uma avaliação com amostra maior utilizando o instrumento SUS, testes com medidas objetivas de desempenho, a validação do espelhamento com usuários reais e, principalmente, um estudo longitudinal ou experimental para verificar o impacto do sistema em decisões efetivas de crédito.

---

## Slide 28 — § 21 · O Fechamento · Considerações finais (≈ 1 min)

Como consideração final, este trabalho demonstrou que a transformação de dados abertos governamentais em informação acessível é tecnicamente viável e possui potencial para apoiar decisões de crédito mais informadas. **(pausa)**

Embora as informações sobre taxas de juros estejam disponíveis publicamente, sua apresentação em formato técnico dificulta a utilização pelo cidadão comum. O TaxaJurosPro reduz essa barreira ao reunir consulta, comparação e simulação em uma única plataforma, utilizando exclusivamente dados oficiais do Banco Central. **(pausa)**

Retomando os pilares da pesquisa: a pergunta foi respondida dentro do enquadramento de Design Science; os seis objetivos específicos foram atingidos, com o sistema em produção; e as limitações foram recortes deliberados, com continuidade já planejada. **(pausa)**

Considero, portanto, que os objetivos definidos no início foram atingidos e que o TaxaJurosPro representa uma aplicação prática dos conhecimentos adquiridos ao longo da graduação, unindo Engenharia de Software, Desenvolvimento Web e Educação Financeira para resolver um problema real.

---

## Slide 29 — Obrigado (≈ 20 s)

Com isso, encerro a apresentação. **(pausa)**

Agradeço mais uma vez à banca pela atenção e fico à disposição para as arguições e para responder às perguntas dos senhores. **(pausa)**

Obrigado.

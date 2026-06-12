# Gerenciador-de-Senhas-Preferenciais01

# Descrição do Projeto
O Sistema de Gerenciamento de Senhas foi desenvolvido com o objetivo de organizar e controlar filas de atendimento de forma prática e intuitiva. O programa permite a emissão de senhas para diferentes tipos de prioridade, o gerenciamento da fila de espera e o acompanhamento do histórico de atendimentos.
A aplicação foi desenvolvida em Python utilizando a biblioteca CustomTkinter para a construção da interface gráfica, proporcionando uma experiência moderna, organizada e acessível ao usuário.

# Objetivos
- Organizar o fluxo de atendimento.
- Gerenciar filas por ordem de prioridade.
- Registrar histórico das senhas chamadas.
- Facilitar a visualização dos atendimentos em andamento.
- Aplicar conceitos de estruturas de dados e lógica de programação.

# Funcionalidades

Emissão de Senhas
O sistema permite gerar senhas para três categorias:
- Normal
- Preferencial
- Urgente
Cada senha recebe um código único baseado no nome do usuário e na categoria escolhida.

Gerenciamento de Fila
As senhas são inseridas automaticamente na fila respeitando a ordem de prioridade:
1. Urgente
2. Preferencial
3. Normal
Dessa forma, atendimentos mais importantes são realizados primeiro.

Chamada de Senhas
O atendente pode chamar a próxima senha da fila através de um botão específico. A senha chamada passa a ser exibida na área principal do sistema.

Histórico
O sistema mantém um histórico das últimas 20 senhas atendidas, permitindo consultar atendimentos recentes.

Estatísticas
Também são exibidas informações como:
- Quantidade de pessoas na fila.
- Total de senhas chamadas.
- Controle de atendimentos por tipo e serviço.

Acessibilidade
O sistema possui um modo daltônico, alterando as cores da interface para facilitar a visualização por pessoas com deficiência na percepção de cores.

# Estruturas de Dados Utilizadas
Durante o desenvolvimento foram utilizadas:
- Listas
- Matrizes
- Dicionários
- Variáveis globais
- Estruturas condicionais
- Estruturas de repetição
Essas estruturas foram fundamentais para o controle da fila, histórico e estatísticas do sistema.

# Desenvolvimento das Funções
Durante o desenvolvimento do projeto, buscamos criar nossas próprias funções sem usar utilizar funções prontas da linguagem Python. Como objetivo de aprendizado.
Ao invés de utilizar diretamente alguns métodos já existentes na linguagem, implementamos funções próprias para exercitar a lógica de programação e reforçar o conhecimento sobre estruturas de dados, laços de repetição e manipulação de textos e listas.
Entre as funções desenvolvidas pela equipe estão:
- Conversão de letras maiúsculas para minúsculas;
- Remoção de espaços em textos;
- Remoção de espaços no início e no fim de palavras;
- Inserção de elementos em posições específicas de listas;
- Remoção do primeiro e do último elemento de uma lista;
- Verificação de números pares e ímpares;
- Seleção dos primeiros caracteres de uma string.
Essa abordagem permitiu compreender melhor como essas operações são realizadas internamente, contribuindo para o desenvolvimento do raciocínio lógico e para o aprendizado dos conceitos fundamentais da programação.

# Tecnologias Utilizadas
- Python
- CustomTkinter
- Tkinter

# Como executar
1. Instale a dependência:
- install customtkinter

2. Execute o arquivo:
- python gerenciador_de_senhas.py

# Conclusão
O desenvolvimento deste projeto permitiu aplicar conceitos importantes de programação, interface gráfica, estruturas de dados e algoritmos. Além de resolver um problema real de organização de atendimentos, o projeto também contribuiu para o aprofundamento dos conhecimentos da equipe, especialmente pela implementação manual de diversas funções que normalmente seriam fornecidas pela própria linguagem Python. Dessa forma, o sistema serviu tanto como solução prática quanto como ferramenta de aprendizado e desenvolvimento técnico.

# Design e Documentação Visual

Fluxo de Navegação
[Sistema de senhas Ofc 01.pdf](https://github.com/user-attachments/files/28884041/Sistema.de.senhas.Ofc.01.pdf)

Sitemap
[Sistema de senhas Sitemap Ofc 01.pdf](https://github.com/user-attachments/files/28884067/Sistema.de.senhas.Sitemap.Ofc.01.pdf)

Wireframes
[Link do Figma](https://www.figma.com/design/bbSwGR3TzLlerjZGBn9ZVW/Sem-t%C3%ADtulo?node-id=0-1&t=QW9W58btnDhr3GA7-1)

Protótipo
[Link do Figma](https://www.figma.com/design/TjsC8iuKscaoEIctWjq1Dz/Prototipa%C3%A7%C3%A3o?node-id=0-1&t=VpALaA4sZmV9iTEp-1)

# Equipe 
Marcus Aurélio Teixeira Carvalho 
RA: 1012612628

Pedro Costa Malheiros 
RA: 1012613222

Guilherme Rian Sales Silva 
RA: 1012616605

João Pedro Veiga Silva
RA: 10126110650

Natan Nunes Pinto Costa 
RA: 1012616108

Ronald Emanuel Magalhães Costa
RA: 1012510065

Farley Souza Silva de Oliveira
RA: 10126110763

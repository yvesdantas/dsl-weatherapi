# Linguagem de Domínio Específico - WeatherAPI

Desenvolvimento de DSL para formatação de consulta de dados climáticos.

## Usabilidade

O arquivo <code>Clima.xtext</code> descreve a Gramática para a DSL implementada. Para "Cidade", qualquer entrada é válida, não há verificação ou validação. "Data início" e "Data fim" são do tipo "DATA", definido por dia, dois dígitos, mês, dois dígitos e ano, quatro dígitos, "DD/MM/AAAA". A DSL verifica se dia está entre 01 e 31, se mês está entre 01 e 12 e, se ano está entre 2000 e 2021. Além disso, verifica se os separadores são somente "/". Caso o usuário não obedeça as especificações, o compilador emite alerta, a DSL não valida os dados e não gera o arquivo de saída;

O arquivo <code>ClimaGenerator.xtend</code> consiste no gerador do arquivo com a extensão <code>.json</code> a partir das entradas realizadas pelo usuário. O arquivo <code>Clima.wht</code> consiste em um exemplo de código para utilização da DSL e possíveis entradas de dados pelo usuário, as quais podem ser preenchidas com o nome da cidade, data início e data fim. O arquivo gerado pela DSL (exemplo <code>dadosClimaticos.json</code>) é utilizada como input para o script em python <code>wheaterapi.py</code>, o qual retorna a saída <code>output.csv</code>. O arquivo <code>wheaterapi.pdf</code> mostra um exemplo da utilização dos dados retornados com a ferramenta Power BI.

<div style="text-align:center"><img src="/static/weatherapi.png" /></div>

Este trabalho foi elaborado pelos alunos Lucas Novais Assunção e Yves Dantas Neves sob orientação do prof. Sérgio Medeiros no contexto da disciplina Linguagens de Domínio Específico do Mestrado Profissional do Programa de Pós-graduação em Tecnologia da Informação (PPgTI) do Instituto Metrópole Digital (IMD) da Universidade Federal do Rio Grande do Norte (UFRN).

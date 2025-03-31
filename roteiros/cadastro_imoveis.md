[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

# SPIUnet
Os valores que vão para o SIAFI são os do RIP Utilização (e não o RIP Imóveis), somando o terreno com a benfeitoria.
Após é necessário lançar a ratificação.

No Laudo, há a seção CONCLUSÃO onde o perito atribui os novos valores ao imóvel.

## Dados prévios do Laudo e do SIAFI
- RIP Imóvel
- RIP Utilização
- Data do laudo
- Valor do terreno
- Fração da utilização
- Valor das benfeitorias
- Somatório dos valores
- Documento sei do Laudo

## Lançamento de atualização dos valores do terreno
1. Entrar em Cadastramento > Imóvel

![Cadastro Imóvel](https://github.com/Mateus-cpa/manual-material/blob/main/img/1%20-%20Tela%20Cadastramento%20-%20Terrenos.PNG)

2. Informar o RIP Imóvel

![Informa RIP imóvel](https://github.com/Mateus-cpa/manual-material/blob/main/img/2%20-%20inserir%20RIP%20Im%C3%B3vel.PNG)

3. Ir para a Seção Dados do Terreno
4. Se mantiver a quantidade de m², 
    - Apagar Valor m² (R$)
    - Lançar o Valor do Terreno (R$)
    - Quando se preenche um, o outro é preenchido automaticamente após a gravação dos dados.

![Dados do Terreno](https://github.com/Mateus-cpa/manual-material/blob/main/img/3%20-%20Dados%20do%20terreno.PNG)

5. Lançar Data Avaliação: data do laudo.
    - Nível de Rigor é sempre Rigorosa (6 meses), conforme Portaria Conjunta 010/2023 - SPU/STN.
    - Prazo Validade é calculado automaticamente.

![Data Laudo](https://github.com/Mateus-cpa/manual-material/blob/main/img/4%20-%20Dados%20do%20im%C3%B3vel%20-%20data%20laudo.PNG)

6. Botão Avançar
7. Conferir Dados imóvel
8. Botão Gravar
9. Msg: 0101 - Alteração efetuada com sucesso

## Lançamento de atualização dos valores das benfeitorias
10. Entrar em Cadastramento > Utilização

![Cadastra Utilização](https://github.com/Mateus-cpa/manual-material/blob/main/img/5%20-%20Tela%20cadastramento%20-%20Utiliza%C3%A7%C3%A3o%20(para%20lan%C3%A7ar%20benfeitorias).PNG)

11. Informar o RIP Utilização
12. Na primeira tela ele apresenta os dados do imóvel
13. Ir para Dados da Benfeitoria da Utilização
14. Apagar CUB para o sistema calcular posteriormente
15. Lançar Valor da Benfeitoria (R$)

![Valor da benfeitoria](https://github.com/Mateus-cpa/manual-material/blob/main/img/6%20-%20Valor%20da%20benfeitoria.PNG)

16. Lançar Data Avaliação: data do laudo.
    - Nível de Rigor é sempre Rigorosa (6 meses), conforme Portaria Conjunta 010/2023 - SPU/STN.
    - Prazo Validade é calculado automaticamente.
17. Valor da Utilização (R$) : Soma dos valores de:
    - terreno (se for o responsável), e 
    - benfeitorias (multiplicado pela fração)
18. Observação da Utilização:
    - Adicionar linhas acima do texto atual;
    - Atualização em [data do lançamento] conforme [Laudo SEI] (nº SEI), conforme Portaria Conjunta 010/2023 - SPU/STN.

![Dados da Avaliação](https://github.com/Mateus-cpa/manual-material/blob/main/img/7%20-%20Valor%20da%20utiliza%C3%A7%C3%A3o%20e%20Observa%C3%A7%C3%A3o.PNG)

19. Botão Avançar
20. No campo Data Fim: Atualizar para 5 anos após a emissão do Laudo

![Data Fim](https://github.com/Mateus-cpa/manual-material/blob/main/img/8%20-%20Data%20Fim.PNG)

21. Botão Avançar
22. Conferir em Envio ao SIAFI a Reavaliação (diferença do saldo anterior em relação ao Laudo atual).
23. Capturar a Tela a NL

![Lançar NL](https://github.com/Mateus-cpa/manual-material/blob/main/img/9%20-%20Confirma%C3%A7%C3%A3o%20NL.PNG)

24. Evento 541730 para reavaliação positiva
25. Conferir saldo na conta de controle 899912401 - CONTROLE REGISTRO SPIUNET A RATIFICAR

![Saldo conta controle](https://github.com/Mateus-cpa/manual-material/blob/main/img/10%20-%20Saldo%20conta%20controle.PNG)

## Lançamento no SIAFI
26. Ratificar o valor no SIAFI utilizando o INCDH (incluir documento hábil) tipo PA:
    - Situação IMB134
    - Conta corrente: RIP utilização (não do Imóvel)

![INCDH](https://github.com/Mateus-cpa/manual-material/blob/main/img/11%20-%20lan%C3%A7ar%20PA%20siafi.PNG)


27. Evidenciar o histórico mensal das reavaliações utilizando o INCDH tipo PA:
    - Se saldo na conta 899912403
    - Situação LDV147 - Registro de Baixa do Controle da Reavaliação de Bens Imóveis - RIP - Saldo credor (ou LDV146 para saldo devedor), conforme Macrofunção 02.10.06, item 4.3.4 e subitem 4.3.5.2
    

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
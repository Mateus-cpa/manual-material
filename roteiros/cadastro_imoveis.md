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
2. Informar o RIP Imóvel
3. Ir para a Seção Dados do Terreno
4. Se mantiver a quantidade de m², 
    - Apagar Valor m² (R$)
    - Lançar o Valor do Terreno (R$)
    - Quando se preenche um, o outro é preenchido automaticamente após a gravação dos dados.
5. Lançar Data Avaliação: data do laudo.
    - Nível de Rigor é sempre Rigorosa (6 meses), conforme Portaria Conjunta 010/2023 - SPU/STN.
    - Prazo Validade é calculado automaticamente.
6. Botão Avançar
7. Conferir Dados imóvel
8. Botão Gravar
9. Msg: 0101 - Alteração efetuada com sucesso

## Lançamento de atualização dos valores das benfeitorias
10. Entrar em Cadastramento > Utilização
11. Informar o RIP Utilização
12. Na primeira tela ele apresenta os dados do imóvel
13. Ir para Dados da Benfeitoria da Utilização
14. Apagar CUB para o sistema calcular posteriormente
15. Lançar Data Avaliação: data do laudo.
    - Nível de Rigor é sempre Rigorosa (6 meses), conforme Portaria Conjunta 010/2023 - SPU/STN.
    - Prazo Validade é calculado automaticamente.
16. Valor da Utilização (R$) : Soma dos valores de:
    - terreno (se for o responsável), e 
    - benfeitorias (multiplicado pela fração)
17. Observação da Utilização:
    - Adicionar linhas acima do texto atual;
    - Atualização em [data do lançamento] conforme [Laudo SEI] (nº SEI), conforme Portaria Conjunta 010/2023 - SPU/STN.
18. Botão Avançar
19. No campo Data Fim: Atualizar para 5 anos após a emissão do Laudo
20. Botão Avançar
21. Conferir em Envio ao SIAFI a Reavaliação (diferença do saldo anterior em relação ao Laudo atual).
22. Capturar a Tela a NL
23. Evento 541730 para reavaliação positiva
24. Conferir saldo na conta de controle 899912401 - CONTROLE REGISTRO SPIUNET A RATIFICAR

## Lançamento no SIAFI
25. Ratificar o valor no SIAFI utilizando o tipo PA:
    - Situação IMB134
    - Conta corrente: RIP utilização (não do Imóvel)


[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)
# Conciliação de contas e Relatório mensal
## Preparar pasta dos arquivos
Copiar última pasta gerada e seu conteúdo:
![copiar pasta](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/01%20-%20copiar%20pasta%20do%20m%C3%AAs%20anterior.png)


Alterar o nome dos documentos par aa data atual
![alterar nome](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/02%20-%20alterar%20nomes.png)

Alterar o nome da pasta para o mês de referência do relatório (geralmente o mês anterior)
![renomear pasta](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/03%20-%20renomear%20pasta.png)

Na sequência, avaliar contas contábeis e relatórios mensais.

Existem 4 níveis de avaliação do patrimônio:

- Almoxarifado
- Materiais permanentes
- Bens intangíveis
- Imóveis

## eLog > RMA

>Sipac>Almoxarifado>Relatórios>RMA Sintético

- Selecionar o mês anterior. 
- Selecionar apenas a UG Patrimonial.
- **IMPORTANTE**: Não selecionar o Almoxarifado, caso contrário não retornará os lançamentos de outros Almoxarifados de sua UG (de munições do GAT/DREX ou dos NOs/Delegacias descentralizadas)

![emitir rma](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/04%20-%20rma%20sint%C3%A9tico.png)


### Siafi > conrazao 115610100
Abrir o SIAFI operacional, atualmente após logar no SAIFI web.

Abrir o comando >CONRAZAO
![conrazao](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/07%20-%20conrazao.png)



Indicar dados:
- Conta Contabil 115610100
- Mes MMM igual do RMA

![conta 115610100](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/08%20-%20conrazao%20115610100.png)


### Comparar contas
Verificar se o saldo total e das contas correntes no SIAFI estão iguais aos saldos de 
![compara rma x 115610100](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/09%20-%20rma%20x%20conrazao.png)

### Contas com valores diferentes

Em caso de erro nas contas, avaliar a movimentação do siafi colocando o cursor ao lado o "P" da conta corrente com diferença e pressionando F2. Utilize o F7 (retornar) e F8 (Avançar) para navegar nos lançamentos da conta e F2 para detalhar.

No eLog, avalie o RMA analítico da para observar as:
- **entradas**: Nota Fiscal, recebimento de estoque, entrada avulsa, e
- **saídas**: Envio de estoque, atendimento de requisição, saída avulsa, baixa.

### Salvar tela do RMA e do CONRAZAO

Em caso de conciliação das contas e do eLog, salvar em pdf a tela do conrazao e do RMA, substituindo o arquivo anterior.

![salvar rma](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/05%20-%20imprimir%20rma%20e%20salvar%20substituindo%20anterior.png)

Verá que o arquivo tem a data de alteração do dia atual.
![ver arquivo atualizado](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/05%20-%20imprimir%20rma%20e%20salvar%20substituindo%20anterior.png)


## Materiais permanentes
Avaliar os saldos contábeis e confrontar com Relatórios mensais sintéticos do e-Log (saldo bruto e depreciação).

### Siafi > balancete

No menu principal do SIAFI, digitar o comando >conrazao

Preencha os campos conforme a sua UG e a imagem abaixo:
![balancete 12311](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/10%20-%20balancete%2012311.png)

## Balancete x RMB sintético (Valor Bruto)

> Caminho: SIPAC > Patrimônio > Relatórios > RMB sintético

![balancete 12311 x rmb](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/11%20-%20rmb%20x%20balancete%2012311.png)

Compare o total do saldo bruto com o valor de consolidação do balancete.

### Avaliação de erros nas contas no eLog
Pode decorrer de:
- Termo de Transferência (Envio ou recepção de bens entre UGs);
- Termo de Alienação/Baixa;
- Nota de Recebimento (Incorporação);
- Termo de Localização;
- TBNL (Termo de Baixa por Não Localização?);
- Desmembramento.

No SIAFI, navegue mas contas que deram diferença.

## Balancete x RMB sintético (Depreciação)

Realize os mesmos procedimentos para as contas 12381 no balancete e cvompare com o total da coluna Depreciação Acumulada.

![balancete 12381 x rmb](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/12%20-%20rmb%20x%20balancete%2012381.png)


### Avaliar documentos de lançamento no eLog
1. Extrair  o relatório analítico do grupo de bens analisando as movimentações individuais de cada bem impactado.

2. Verificar possível alteração de saldo anterior do grupo de bens, através do relatório analítico e sintético do sistema e-Log.

1. ENTRADA
- Notas de Recebimento
- Termos de Bens Localização
- Guias de movimentação para outras UGs
2. SAÍDA
- Termos de Bens Não localizados
- Guias de movimentação para outras UGs
- Termos de Baixa/Alienação

#### Indicar a possível causa e apontar a consequência
Ex: Um resumo contábil de saída por transferência registrado em duplicidade no SIAFI, resulta numa divergência de saldo no e-Log a **MAIOR**.

### Salvar RMB e Balancete
Baixe o arquivo em pdf e substitua os arquivos anteriores.

![salvar rmb](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/15%20-%20salvar%20rmb.png)

## Balancete x RMI sintético (Valor bruto)

Os procedimentos são semelhantes aos executados no RMB, mas emitindo o RMI sintético e o balancete das contas 12411:

![balancete 12411 x rmi](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/12%20-%20rmb%20x%20balancete%2012381.png)

## Balancete x RMI sintético (Depreciação)

Os procedimentos são semelhantes aos executados no RMB, mas avaliando a Amortização Acumulada do RMI sintético e o balancete das contas 12481:

![balancete 12481 x rmi](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/14%20-%20rmi%20x%20balancete%2012481.png)

## RIP Utilização x Balancete 12321

Entrar no SPIUNT e extrair o relatório de RIP Utilização:

> Caminho: Consulta > UG > 

![spiunet](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/16%20-%20spiunet.png)

Emitir relatório de RIP Utilização
![consultar ug](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/17%20-%20consulta%20ug.png)

Consultas saldo do Balancete 12321, da mesma forma dos outros relatórios:
![balancete 12321 x spiunet](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/18%20-%20spiunet%20x%20balancete%2012321.png)


## Relatar fechamento mensal das contas
Compactar arquivos de pdf gerados em um arquivo.
![compactar arquivos](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/19%20-%20compactar%20arquivos.png)

Copiar informação anterior, se quiser.
![copiar informação](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/20%20-%20Copiar%20informacao%20anterior.png)

Editar o relatório de contas.
![relatorio de contas](https://raw.githubusercontent.com/Mateus-cpa/manual-material/refs/heads/main/img/conciliacao/21%20-%20relatorio%20de%20contas.png)

Não precisa manter a tabela de contas ma Informação.

#### Ferramentas
1. eLog: Relatório sintético dos bens RMB, RMI, RMA;

2. Tesouro gerencial: saldo de D-1;

3. SIAFI operacional: >CONRAZAO

4. eLog: Relatório analítico da classe de bens com divergência.

5. eLog: Extrato de Movimentação


#### Dicas
1. Qualquer bem no sistema de controle com saldo (-) negativo é indicação de erro.

2. Jamais a **DEPRECIAÇÃO** poderá ser superior ao valor do bem.


[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)


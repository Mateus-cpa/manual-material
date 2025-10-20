[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

# Tombamento por licitação/contrato

## Comprasnet
### Apropriar instrumento de cobrança
> Caminho: [Comprasnet contratos](https://contratos.comprasnet.gov.br/login) > Gestão financeira > Apropriar instrumento de cobrança

- Selecionar a Nota Fiscal a apropriar.

![Selecionar intrumento de cobrança](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/01%20-%20Selecionar%20Instrumento%20de%20Cobran%C3%A7a.png)

### Dados básicos

- Tipo de DH: NP - Nota de Pagamento

- Observação: Incluir Objeto da aquisição, o processo Sei e a Nota Fiscal, se necessário.

![Apropriar Nota - Dados básicos](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/02%20-%20Apropriar%20Nota%20-%20dados%20b%C3%A1sicos.png)

### Principal com orçamento

1. Situação:

- DSP101: Aquisição de materiais para **estoque** 
- DSP102: Aquisição de materiais para **consumo imediato** 
- DSP201: Aquisição de bens **móveis**
- DSP205: Despesas com aquisição de **imóveis, obras e instalações** 

2. Se tem contrato, conta de contratos:
- 81231**02**01: Fornecimento de serviços
- 81231**04**01: Fornecimento de materiais
- Favorecido do contrato: CNPJ da empresa ou Inscrição Genérica (neste caso, consultar Setor de Contratos) 

3. Conta de bens móveis: Conta patrimonial, porém, nesta data, o sistema bloqueia a conta 123110801.

4. Contas a pagar: 
- 213110**1**00: Equipamentos de área finalística
- 213110**4**00: Outras aquisições

![Apropriar Nota - Principal com orçamento](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/03%20-%20Apropriar%20Nota%20-%20principal%20com%20or%C3%A7amento.png)

Conferir Nota de Sistema e Documento Hábil gerados

![Apropriar Nota - NP gerada](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/04%20-%20Apropriar%20Nota%20-%20NP%20gerado.png)

## SIAFI operacional (tela preta)

Conferir lançamento na conta intermediária 123110801 - ESTOQUE INTERNO:

> Caminho: >conrazao

![Conrazao 123110801](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/07%20-%20Conrazao%20conta%20123110801.png)

## SIAFI Web

> Caminho: [Siafi web](https://siafi.tesouro.gov.br/senha/) > INCDH

Tipo de documento: PA

### Dados básicos

- Valor do documento: valor da apropriação
- Exemplo de Observação: Reclassificação da aquisição de xxx para uso das Unidades xxx, conforme Nota Fiscal xxx, processo sei xxx.

![PA reclassificação - dados básicos](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/05%20-%20PA%20reclassificacao%20-%20dados%20b%C3%A1sicos.png)

### Outros Lançamentos

- Situação: **IMB050** - RECLASSIFICAÇÃO DE BENS MÓVEIS EM ALMOXARIFADO PARA BENS MÓVEIS C/C007

- subitem da despesa: Igual à conta corrente de 123110801

- Bens móveis em uso: Conta contábil de bens móveis correta a reclassificar

- Bens móveis em almoxarifado: 123110801

![PA reclassificação - Outros lançamentos](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/06%20-%20PA%20reclassificacao%20-%20outros%20lancamentos.png)

![eLog módulo Orçamento](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/08%20-%20cadastra%20empenho.png)

![Conferir Plano Interno](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/09%20-%20Conferir%20Plano%20Interno.png)

![Registrar NE](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/10%20-%20eLog%20-%20Registrar%20NE.png)

![Registrar NE - outros](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/11%20-%20eLog%20-%20Registrar%20NE.png)

![Dados de empenho](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/12%20-%20eLog%20-%20dados%20do%20empenho.png)

![Centro de custos](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/13%20-%20eLog%20-%20centro%20de%20custos.png)

![Confirmar empenho](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/14%20-%20eLog%20-%20confirmar%20empenho.png)

![Modulo patrimonio](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/15%20-%20eLog%20-%20m%C3%B3dulo%20patrim%C3%B4nio.png)

![Cadastrar NF](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/16%20-%20eLog%20-%20cadastrar%20NF.png)

![Cadastra dados NF](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/17%20-%20eLog%20-%20cadastra%20dados%20da%20NF.png)

![Dados NF](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/17%20-%20eLog%20-%20cadastra%20dados%20da%20NF.png)

![Confirma tombamento](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/18%20-%20eLog%20-%20confirma%20NE%20-%20tombamento.png)

![Cadastrar itens](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/19%20-%20eLog%20-%20cadastrar%20itens.png)

![eLog descritores](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/20%20-%20eLog%20-%20descritores.png)

![Descritores](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/21%20-%20eLog%20-%20descritores%20individuais.png)

![Nota de Recebimento](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/22%20-%20eLog%20-%20nota%20de%20recebimento.png)

![Nota de Recebimento](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/22%20-%20eLog%20-%20nota%20de%20recebimento.png)

![Gerar etiquetas](https://github.com/Mateus-cpa/manual-material/blob/main/img/incorporacao_compra/24%20-%20gerar%20etiquetas.png)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
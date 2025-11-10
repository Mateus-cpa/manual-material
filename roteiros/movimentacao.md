[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)
# Movimentação

## Enviar bens
Para realizar as atividades deste menu, é necessário possuir o perfil de GESTOR LOCAL ou ser Chefe ou substituto de uma Unidade Organizacional.

### Entrar no sistema patrimonial

Realizar entrada no sistema patrimonial 
![SIPAC](https://sistemas.dpf.gov.br/sipac/)

![Entrar no sistema patrimônio](https://github.com/Mateus-cpa/manual-material/blob/main/img/01%20-%20Entrar%20no%20sistema%20eLog.PNG)

### Entrar no menu Gerência/Enviar Bens

![Entrar em Enviar Bens](https://github.com/Mateus-cpa/manual-material/blob/main/img/02%20-%20Entrar%20no%20menu%20Enviar%20Bens.PNG)

### Localizar Unidade de Destino

Clique na lupa para abrir o quadro de pesquisa das Unidades da PF.

![Localizar Unidade de Destino](https://github.com/Mateus-cpa/manual-material/blob/main/img/03%20-%20Localizar%20Unidade%20de%20Destino.PNG)

### Transportar a Unidade para a guia de envio de materiais

Clique na seta verde para selecionar a Unidade Organizacional para onde será enviada.

![Transportar a Unidade para a guia de envio de materiais](https://github.com/Mateus-cpa/manual-material/blob/main/img/04%20-%20Transportar%20a%20Unidade%20para%20a%20guia%20de%20envio%20de%20materiais.PNG)

### Selecionar a localidade de destino

Selecione uma sala de destino. Esta etapa é importante, pois caso contrário o a lista de bens será transferido para o "limbo" dentro da Unidade. Estes bens não saem em todos relatórios da localidade.

![Selecionar a localidade de destino](https://github.com/Mateus-cpa/manual-material/blob/main/img/05%20-%20Selecionar%20a%20loclaidade%20de%20destino.PNG)

### Adicionar descrição de movimentação

SEMPRE que possível informe o processo SEI relacionado à movimentação.

![Adicionar descrição de movimentação](https://github.com/Mateus-cpa/manual-material/blob/main/img/06%20-%20Adicionar%20descri%C3%A7%C3%A3o%20de%20movimenta%C3%A7%C3%A3o.PNG)

### Entrada de patrimônio

Liste os patrimônios conforme a necessidade
    
a) Entrada por número de patrimônio ou faixa de patrimônios

![Entrada de patrimônio](https://github.com/Mateus-cpa/manual-material/blob/main/img/07a%20-%20Entrada%20de%20patrim%C3%B4nio.PNG)

b) Entrada por arquivo .txt com lista de patrimônios

![Entrada de patrimônio por lote](https://github.com/Mateus-cpa/manual-material/blob/main/img/07b%20-%20Entrada%20de%20patrim%C3%B4nio%20por%20lote.PNG)

### Adicionar bens na guia de movimentação

Adicione quantos bens precisar para a guia de movimentação.

![Adicionar bens na guia de movimentação](https://github.com/Mateus-cpa/manual-material/blob/main/img/08%20-%20Adicionar%20bens%20na%20guia%20de%20movimenta%C3%A7%C3%A3o.PNG)

### Concluir guia
Após listar todos os bens à guia de movimentação, conclua com o botão "Confirmar".

![Concluir guia](https://github.com/Mateus-cpa/manual-material/blob/main/img/09%20-%20Concluir%20guia.PNG)

## Recebimento imediato
Após o envio, aparece um botão de recebimento imediato, onde é possível o servidor realizar imediatamente o recebimento, solicitando o login e senha de qualquer servidor **lotado no local de destino**.

# Receber Bens

## 10. Abrir o menu Receber bens

>Caminho: sipac/Patrimônio/Gerência/Movimentações/Receber bens.

O número indica a quantidade de bens a receber.

![Abrir o menu Receber bens](https://github.com/Mateus-cpa/manual-material/blob/main/img/10%20-%20Abrir%20o%20menu%20Receber%20bens.PNG)

## 11. Selecionar guia de recebimento

![Selecionar guia de recebimento](https://github.com/Mateus-cpa/manual-material/blob/main/img/11%20-%20Selecionar%20guia%20de%20recebimento.PNG)

# Unidade de Material: Validação (quando movimentação entre UGs)

Cadastrar Documento Hábil no Siafi. Através da integração, ele envia o DH Lançamento Patrimonial (PA). 
- IMB046 - Transferência/doação de bens móveis - sem colocar bem em trânsito (valor bruto)
- IMB044 - Transf de deprec/exaust/amortz acumulada (depreciação)

# Movimentação de Bens para outros Órgãos
O Termo de Responsabilidade lastreia a mudança de responsabilidade sobre o bem. Pode ser:
- Interna: Dentro da Unidade Gestora.
- Externa: Entre Unidades Gestoras. 
- Externa: Também para outras Unidades Gestoras de outros Órgãos. A parte do SIAFI é manual no valor líquido.


#  Transferência externa - Outros Órgãos Federais
## SIPAC
> Caminho: sipac/patrimônio/gerência/movimentações para outros órgãos

![Movimentação para outros Órgãos](https://github.com/Mateus-cpa/manual-material/blob/main/img/Transfer%C3%8Ancia%20externa%20outros%20%C3%B3rg%C3%A3os.PNG)

Modalidade de desfazimento: 
- Cessão: Empréstimo com previsão de retorno
- Transferência externa: Doação definitiva

Toda alienação é precedida de uma avaliação por comissão formada.

**IMPORTANTÍSSIMO**: Termo de Recebimento deve ser impresso e anexado ao SEI 
### SIAFI
- Tipo: PA
- Dados básicos: UG e valor bruto
- Outros Lançamentos
#### Situação (repetir para cada conta): 
- IMB041 - confirma recebimento em transferência/doação de bens imobilizados em trânsito
- IMB040 - Transferência/doação de bens imobilizados em trânsito
- IMB010 - Apuração de valor contábil líquido de bens imóveis pela baixa da depreciação.
Lançar a conta patrimonial de referência do bem
- Conta de bens recebidos 



[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
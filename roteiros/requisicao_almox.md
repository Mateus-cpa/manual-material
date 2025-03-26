[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)
# Requisição de bens de Almoxarifado

## Solicitante
> Caminho: sipac/Portal Administrativo/Requisições/Material/Almoxarifado/Cadastrar requisição

**!imagem**

1. Solicitar CORRETAMENTE ao:
- Almoxarifado de **municao** da SR/PF/**[SUA UG]** (Eletrônico): para requisição de munições gerenciadas pelos GATs
- Almoxarifado da SR/PF/**[SUA UG]** (Eletrônico): para demais casos.

2. Listar materiais da requisição


3. Selecionar materiais da requisição


4. Incluir material na requisição

    - É possível solicitar vários materiais de almoxarifado na mesma Requisição, basta repetir os passos 2 a 4.

5. Finalizar listagem
Caso não precise incluir mais materiais, clique em continuar

6. Finalizar Requisição.
No campo **observações**:
    - Sempre que se referir a um processo SEI, informe-o neste campo. 
    - Se for retirado por outra pessoa, informe-o.
    - Se for aplicável, informar data e horário de previsão para retirada.

Unidades bloqueadoas (sem recebimento de materiais permanentes após X dias) não têm permissão para solicitar materiais.

### Projeto futuro
Criar formulário de solicitação para compras futuras com:
- Informações do material de consumo
- Unidade de solicitação
- Contato

## NUMAT
> Caminho: sipac/Almoxarifado/Requisições/Atendimento de Requisições

1. Clicar em atender requisição daquela a ser atendida.
2. Informar a quantidade de saída de cada item solicitado.
3. Após informar todas quantidades atendidas, clicar no botÂo "Finalizar Atendimento".
4. Informar Servidor Recebedor.
5. Imprimir documento de Requisição de Material.
6. Realizar Lançamento no SIAFI.
 - 6.1. Informar CPF, senha e Código de Centro de Custos
 - 6.2. Registrar nº da NS no documento de Requisição
7. Conferir no SIAFI se lançamento foi realizado.
- 7.1. [Siafiweb](siafi.tesouro.gov.br)
- 7.2. Comando `CONDH`
- 7.3. Tipo: `PA`, 
- 7.4. Data de Emissão De: `data atual` Até: `data atual`
- 7.5. Verificar se estão corretos os dados lançados, tais quais: Observação,  cada Código no eLog e cada Situação ETQ001 em Outros Lançamentos do SIAFI.
- 7.6. Registrar o nº da PA no documento de Requisição
8. Separar material ficisamente.

## Solicitante
1. Verificar se a solicitação foi atendida.
2. Conferir e Retirar o material.
3. Assinar recibo. 

> IMPORTANTE: Requisições não atendidas no ano serão automaticamente apagadas.


[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
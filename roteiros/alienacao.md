[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)

[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)
# Alienação (baixa) de bens

Conforme o 8.2.2., por padrão o valor de mercado pode ser utilizado ao invés do atual. Valor de mercado para licitação é diferente para cotação por pessoa física.

## Doação
Quando o destinatário tem proveito.

```
Art. 6º Os bens móveis inservíveis ociosos e os recuperáveis poderão ser reaproveitados, mediante transferência interna ou externa.
```


## Destinação
**Descarte**: Quando não há mais proveito do bem. Conforme Decreto 9373/18:

```
Art. 7º Os bens móveis inservíveis cujo reaproveitamento seja considerado inconveniente ou inoportuno serão alienados em conformidade com a legislação aplicável às licitações e aos contratos no âmbito da administração pública federal direta, autárquica e fundacional, indispensável a avaliação prévia. 

Parágrafo único. Verificada a impossibilidade ou a inconveniência da alienação do bem classificado como irrecuperável, a autoridade competente determinará sua destinação ou disposição final ambientalmente adequada, nos termos da Lei nº 12.305, de 2010.
```
### Veículos
Laudo de Avaliação de Veículos - realizado pela Utran.

Faz uma avaliação a valor de mercado, no caso das viaturas.

Modelo SETRAN/DIFRO:

Identificação | Informação 
:------- | ----: 
Marca/Modelo | xxx
Fabricação | xxx
Placa Oficial | xxx
Carga Patrimonial | xxx
Tempo de uso | xxx
Rodagem | xxx
Histórico de Manutenção | xxx
Orçamento para ficar em condições de rodagem | xxx
Valor do bem pela tabela FIPE | xxx
Valor do bem no sistema eLog | xxx

 Cálculo de índice de Antieconomicidade
 
Dado  | Fórmula
 :------- | ----:
Valor Fipe (R$) | Fipe
Histórico de manutenções | Hm
Manutenções necessárias | Mn
Custo acumulado de manutenção | Cam = Hm + Mn
Índice de antieconomicidade | Ia = Cam/Fipe

Cálculo de Valor de REferÊncia
Dado  | Fórmula
 :------- | ----:
Valor Fipe | Fipe
Valor patrimonial depreciado no eLog | Vpd
Manutenções necessárias | Mn
Valor de referÊncia | Vr = (Fipe+Vpd)/2-Mn

Compara o valor calculado por fórmula com o eLog e utiliza o valor menor.

Para viaturas, conforme a IN, preferencialmente veículos as alienações são por Leilão.

Os servidores da unidade de transporte podem fazer de ofício para dar suporte à unidade de Material.

## Bens específicos
Comissão especial com no mínimo 3 servidores da unidade de utilização do bem para realizar a destruição.

SIP, DRE, NEPOM, NTI, GAT, UTRAN.

## Bens de uso comum
Laudo de Avaliação Patrimonial é emitido pela Unidade de Material para (macrofunção STN 02.03.30) 

Pode ser Comissão de Avaliação fixa para bens de uso comum.

### No SEI (comissão)
> Laudo de Avaliação Patrimonial

### No SEI (Ordenador)
> Autorizar a alienação

### No eLog ((Unidade de Material))
Realizar Ajuste de Gerência/Ajuste de Valor Contábil

> Execução da Alienação
Caminho: sipac/patrimônio/Cadastro/Gerência/Alienação/Baixa/Registrar/ Alienar Baixa
> Dados de recebedor de alienador: 
- Tipo do Fornecedor:	Pessoa Física / Pessoa Jurídica / Unidade Gestora / Estrangeiro
- Razão Social:
- Nome Fantasia:	
- CPF/CNPJ:	
- Representante:	
- Endereço:	
- Bairro:	
- Cidade:	
- CEP:	
- Email:	
- Fone:	
- Fax:	
- NIT ou PIS/PASEP
> Pessoas físicas apenas para leilão ou para semoventes (indicado pelo cuidador).

Cadastre-se primeiramente o destinatário:

![Cadastro Destinatário](https://github.com/Mateus-cpa/manual-material/blob/main/img/registrar-alienar%20baixa.PNG)

Após elenque os bens a serem destinados:

![Cadastro Bens](https://github.com/Mateus-cpa/manual-material/blob/main/img/registrar-alienar%20baixa2.PNG)

Verifique se foi lançado o PA no SIAFI.


[Retornar para Roteiros](https://github.com/Mateus-cpa/manual-material/blob/main/roteiros.md)

[Retornar ao menu principal](https://github.com/Mateus-cpa/manual-material/blob/main/README.md)
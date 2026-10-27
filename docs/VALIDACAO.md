# Validação privada do plugin

Use uma empresa de teste com dados apropriados. Nunca use uma empresa real para experimentar gravações ou estornos sem intenção explícita do responsável. Não anexe credenciais ou dados contábeis às evidências públicas.

## Pacote

- Execute `python3 scripts/plugin.py check` e `python3 scripts/plugin.py package`.
- Com Claude Code disponível, execute `claude plugin validate .`.
- Faça upload do ZIP no Claude e confirme o nome **noLivro** e as dez skills.
- Abra **Connectors**, conecte pelo OAuth e confira as empresas exibidas.

## Jornadas

| Jornada | Resultado esperado |
| --- | --- |
| Descoberta | Claude identifica as skills e encontra as ferramentas do noLivro |
| Consulta | Lista somente as empresas autorizadas; resolve ambiguidades antes de prosseguir |
| Contexto | Seleciona empresa e período sem inventar IDs |
| Lançamento | Valida, apresenta problemas, salva com a mesma prévia e distingue rascunho de contabilizado |
| Ação simples | Renomeia um período de teste sem exigir prévia inexistente |
| Confirmação | Respeita aceitar/recusar conforme a política do cliente; não alega clique não observado |
| Arquivo | Usa bytes reais ou referência temporária; análise não é apresentada como importação concluída |
| Relatório | Respeita paginação e exibe competências em MM/AAAA |
| Falha | Não repete gravação automaticamente após timeout; informa resultado indeterminado quando necessário |
| Desconexão | Não consegue continuar chamando ferramentas com acesso revogado; oferece reconexão |

Registre versão do pacote, superfície do Claude, configuração de confirmação, data e resultado de cada jornada. “Não executado” é diferente de “aprovado”. Os testes do conector e uma consulta pelo ChatGPT não homologam este pacote no Claude.

## Atualização das skills

As dez skills foram adaptadas das skills do MCP público do noLivro. Os nomes das ferramentas devem continuar correspondendo ao catálogo servido pelo conector. Quando o catálogo mudar, revise os argumentos, o fluxo e a recuperação de cada skill e aumente a versão do manifesto antes de distribuir outra edição.

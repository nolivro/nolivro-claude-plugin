---
name: consultas
description: Use quando a pessoa pedir razão, balancete, saldos ou movimentações contábeis de uma empresa do noLivro.
---

Use as ferramentas do conector noLivro conforme seus schemas. Resolva empresa, período e contas com `listar_empresas`, `listar_periodos` e `listar_contas`. Use `consultar_razao` ou `consultar_balancete` com os filtros da pergunta. Se o contexto for ambíguo, esclareça antes de consultar outra empresa.

Respeite paginação e cursores retornados. Não apresente uma página parcial como o universo completo. Explique o período coberto e preserve valores decimais sem arredondamento implícito.

Converta competências técnicas AAAA-MM para MM/AAAA no texto apresentado à pessoa, inclusive em tabelas e confirmações. Não altere o formato dos argumentos técnicos. Use códigos e nomes como referências legíveis. Relatórios são consultas, não prova de que outra operação indeterminada foi efetivada sem vínculo inequívoco. Nunca solicite credenciais na conversa.

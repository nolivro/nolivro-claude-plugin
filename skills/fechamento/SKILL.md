---
name: fechamento
description: Use quando a pessoa quiser preparar ou executar fechamento contábil no noLivro, consultar revisões ou retificar um período.
---

Use as ferramentas do conector noLivro conforme seus schemas. Resolva empresa e período com `listar_empresas` e `listar_periodos`. Consulte `consultar_configuracao_resultado`; use `configurar_apuracao_resultado` somente quando houver pedido de alteração das contas.

Chame `preparar_fechamento` com o conjunto de demonstrações escolhido. Apresente pendências, lacunas e alterações do conjunto. Use `fechar_periodo` com o hash e dados correspondentes. Confirmações de lacunas ou alteração do conjunto exigem intenção da pessoa; não as marque apenas para superar uma recusa.

A confirmação de chamada ocorre no cliente de IA, sem proposta do chat interno. A API revalida o fechamento. Não trate a preparação como bloqueio de concorrência nem promessa de aprovação.

Consulte `listar_fechamentos` e `consultar_fechamento` para identificar a revisão efetiva. Em timeout, não repita o fechamento antes de verificar evidência suficiente. Para retificar, obtenha motivo e use `retificar_periodo`; não simule retificação alterando lançamentos diretamente.

Apresente competências como MM/AAAA e identifique empresa, período e revisão na resposta. Não declare execução antes do resultado confiável. Nunca solicite credenciais na conversa.

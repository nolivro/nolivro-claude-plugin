---
name: escrituracao
description: Use quando a pessoa quiser consultar, validar, salvar, contabilizar ou estornar lançamentos contábeis no noLivro.
---

Use as ferramentas do conector noLivro e os schemas disponíveis na conexão. Resolva a empresa com `listar_empresas`, o período com `listar_periodos` e as contas com `listar_contas`. Peça esclarecimento quando houver mais de uma correspondência. Use IDs somente nos argumentos técnicos e nomes/códigos nas respostas.

Para criar um ou vários lançamentos, use `validar_lancamentos`. Explique os problemas retornados e corrija os dados antes de continuar. Em seguida use `salvar_lancamentos` com os mesmos dados, a `previa_id` recebida e uma chave de idempotência estável. A confirmação de execução pertence ao cliente de IA; não declare que a pessoa clicou em aprovar sem evidência.

Se os dados mudarem, valide novamente. A prévia expira e pode desaparecer após reinício. Não reutilize prévia de outra conexão ou empresa. Uma confirmação de saldo invertido deve corresponder à intenção explícita da pessoa e às exigências da API.

Use `listar_lancamentos` para conferir o resultado. Diferencie rascunho salvo e lançamento contabilizado conforme a resposta. Para registros existentes há `contabilizar_lancamento`, `editar_complemento_lancamento`, `alterar_distribuicoes_notas` e `estornar_lancamento`. Preserve histórico anterior e revisão quando exigidos.

Após resultado indeterminado, não repita automaticamente. Preserve a chave original e consulte os registros/vínculos disponíveis. Se a consulta não provar o resultado, diga que ele continua indeterminado. Nunca peça senha ou token na conversa; reconexão ocorre na página do conector. Mostre competências em MM/AAAA, mantendo o formato técnico exigido pelos schemas.

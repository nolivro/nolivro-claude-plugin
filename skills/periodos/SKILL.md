---
name: periodos
description: Use quando a pessoa quiser selecionar, listar, criar ou renomear períodos contábeis no noLivro.
---

Use as ferramentas do conector noLivro conforme os schemas da conexão. Use `listar_empresas` e `listar_periodos` para resolver o contexto. Apresente nomes e datas, não UUIDs. Competências devem aparecer como MM/AAAA, mantendo o formato técnico nos argumentos.

Use `criar_periodo` com nome, início e fim solicitados; deixe a API validar sobreposição. Para mudar apenas o nome, chame `renomear_periodo` diretamente, sem prévia fictícia. O cliente controla sua confirmação de execução.

Uma recusa da API não autoriza buscar outra empresa ou ampliar permissões. Após timeout não idempotente, consulte os períodos e relate a incerteza se não for possível confirmar. Fechamento e retificação usam a skill de fechamento, não renomeação. Se faltar conexão, oriente o login na interface do conector, nunca na conversa.

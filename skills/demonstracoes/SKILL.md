---
name: demonstracoes
description: Use quando a pessoa pedir DRE ou balanço patrimonial do noLivro, consultar prévias e definitivas ou criar e editar templates e trabalhos de demonstrações.
---

Use as ferramentas do conector noLivro conforme os schemas disponíveis. Resolva empresa e período com `listar_empresas` e `listar_periodos`. Para DRE, use `listar_templates_dre`, `consultar_template_dre` e `consultar_contas_elegiveis_dre`. Para balanço, use `listar_templates_balanco`, `consultar_template_balanco` e `consultar_contas_elegiveis_balanco`.

Os ciclos de edição incluem `criar_template_dre`, `editar_template_dre`, `renomear_template_dre`, `duplicar_template_dre`, `arquivar_template_dre` e `excluir_template_dre`; no balanço, `criar_template_balanco`, `editar_template_balanco`, `renomear_template_balanco`, `duplicar_template_balanco`, `arquivar_template_balanco` e `excluir_template_balanco`. Preserve IDs de linhas existentes e relações de composição.

Consulte `consultar_previa_dre` ou `consultar_previa_balanco` indicando template ou trabalho conforme contrato. Demonstrações definitivas usam `consultar_definitiva_dre` e `consultar_definitiva_balanco`; não apresente prévia como definitiva.

Trabalhos são registros editáveis, não jobs: `listar_trabalhos_dre`, `consultar_trabalho_dre`, `editar_trabalho_dre` e os correspondentes `listar_trabalhos_balanco`, `consultar_trabalho_balanco`, `editar_trabalho_balanco`. Informe o período exigido pelo schema; não invente progresso assíncrono.

Preserve decimais e exiba competências como MM/AAAA. Após timeout de escrita, não reenvie automaticamente; consulte o registro e informe a incerteza quando não houver evidência conclusiva. Credenciais pertencem à interface de conexão, não à conversa.

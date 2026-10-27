---
name: simples-nacional
description: Use quando a pessoa quiser consultar ou configurar o Simples Nacional no noLivro, tratar recebimentos e pendências ou concluir, reabrir e reprocessar apurações.
---

Use as ferramentas do conector noLivro e os schemas disponíveis. Resolva a empresa com `listar_empresas`. Consulte `consultar_configuracao_fiscal` e `listar_historico_fiscal` antes de `configurar_fiscal` ou `registrar_historico_fiscal`. Preserve revisão-base e chave de idempotência exigidas.

Use `consultar_recebimentos_fiscais` para resolver origens e recebimentos; depois `alocar_recebimento_fiscal` ou `reverter_alocacao_fiscal`. Ajustes usam `listar_ajustes_fiscais` e `criar_ajuste_fiscal`; reduções usam `listar_reducoes_fiscais` e `criar_reducao_fiscal`. Não invente classificações nem ciência documental.

Antes de concluir, consulte `consultar_pendencias_fiscais` e `consultar_previa_apuracao`. Use `concluir_apuracao`, `reabrir_apuracao` e `reprocessar_apuracao` conforme o pedido. Confira `consultar_apuracao` ou `listar_apuracoes` para apresentar o estado real.

Competências nos argumentos permanecem AAAA-MM; converta explicitamente para MM/AAAA nas respostas. Preserve chaves em repetições autorizadas, não transforme falha de transporte em sucesso e não repita mutações automaticamente. Nunca solicite senha ou token na conversa.

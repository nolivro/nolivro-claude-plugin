---
name: conciliacao
description: Use quando a pessoa quiser importar extrato OFX, consultar movimentos bancários ou conciliar, desfazer ou ignorar movimentos no noLivro.
---

Use as ferramentas do conector noLivro e os schemas disponíveis. Resolva a empresa com `listar_empresas` e a conta com `listar_contas`. Use `importar_extrato` com os bytes originais do OFX e a conta escolhida. Se necessário, ofereça o link de `preparar_envio_arquivo` da empresa. Não invente bytes ou URLs.

Não concilie automaticamente após importar: consulte os movimentos e resolva a partida de cada conciliação. Um timeout de importação não autoriza reenviar o arquivo sem consultar as importações existentes.

Use `listar_extratos`, `consultar_extrato` e `listar_movimentos_bancarios`. Percorra a paginação necessária sem tratar uma página como extrato completo.

Use `consultar_sugestoes_conciliacao` e `consultar_historico_conciliacao` antes de escolher uma partida. Sugestão não significa conciliação concluída. Chame `conciliar_movimento` somente com a partida escolhida.

Outras ações disponíveis são `desfazer_conciliacao`, `ignorar_movimento` com justificativa, `reabrir_movimento` e `criar_rascunho_bancario`. Não acrescente uma etapa de prévia inexistente. Rascunho não equivale a lançamento contabilizado.

Em resultado indeterminado consulte movimento e histórico; não reenvie automaticamente uma mutação. Não solicite credenciais na conversa. Apresente competências em MM/AAAA e referências pelos nomes/códigos.

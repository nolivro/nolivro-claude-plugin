---
name: plano-contas
description: Use quando a pessoa quiser consultar, criar ou editar contas no noLivro, importar um plano contábil ou alterar sua máscara.
---

Use as ferramentas do conector noLivro conforme seus schemas. Selecione a empresa com `listar_empresas`. Consulte `consultar_configuracao_plano` e `listar_contas` antes de resolver códigos e naturezas. Não invente IDs de contas.

`consultar_modelo_plano` baixa o XLSX da empresa. `analisar_importacao_contas` analisa os bytes do XLSX sem persistir; revise os registros retornados e use `criar_contas` para a gravação. Não confunda a referência de prévia com contas já cadastradas. Se precisar de um link de envio, use `preparar_envio_arquivo` para a empresa selecionada.

Use `criar_conta`, `criar_contas` ou `editar_conta` conforme a solicitação. Essas operações não exigem prévia artificial. A API valida hierarquia, código e natureza. Não prometa atomicidade além da resposta do endpoint de lote.

Alteração de máscara exige `simular_mascara_plano` e depois `aplicar_mascara_plano`, mantendo máscara, revisão, prévia e chave de idempotência correspondentes. Mudança de conteúdo requer nova simulação.

A API de máscara usa estado e revisão; receber uma chave não significa recuperar a resposta por essa chave. Após timeout, consulte `consultar_configuracao_plano` e não reenvie automaticamente. Estado coincidente não comprova que essa chamada foi a responsável pela mudança.

Informe somente alterações confirmadas pela API. Em timeout, consulte o código antes de qualquer repetição; existência semelhante não prova autoria da operação. Não invente chamadas ou conteúdo de arquivos nem solicite credenciais na conversa.

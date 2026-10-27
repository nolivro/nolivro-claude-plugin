---
name: notas-parceiros
description: Use quando a pessoa quiser consultar ou cadastrar clientes, fornecedores e notas fiscais no noLivro, importar XML, anexar documentos ou contabilizar notas.
---

Use as ferramentas do conector noLivro e os schemas da conexão. Escolha a empresa com `listar_empresas`. Resolva clientes e fornecedores com `listar_parceiros`; use `criar_parceiro` e `editar_parceiro` quando solicitado. Não deduza parceiro apenas por nome ambíguo.

Quando o cliente não transfere os bytes originais, use `preparar_envio_arquivo` para oferecer um link pontual à pessoa. Depois do envio, passe o objeto com `referencia` no argumento de arquivo. A referência expira e pertence somente à conexão e à empresa selecionadas; não cole a URL em outra conversa.

Para arquivos originais, use `analisar_xml_notas` antes de `importar_xml_notas`, preservando nomes, bytes, hash e referência da prévia. `anexar_arquivo_nota` recebe PDF/XML; `baixar_arquivo_nota` e `baixar_xml_nota` devolvem bytes originais em base64. Nunca invente conteúdo de arquivo nem busque uma URL arbitrária. Se não for possível transferir os bytes ou usar a referência, explique a limitação.

Consulte `listar_notas`, filtre por documento/competência e use `cadastrar_notas_manuais`, `editar_nota` ou `excluir_nota` conforme o pedido. Mostre competências como MM/AAAA, mantendo AAAA-MM nos argumentos.

Cadastro de nota e contabilização são estados distintos. `contabilizar_nota` exige revisão documental, partidas e chave de idempotência; obtenha esses dados da consulta e da intenção da pessoa. Respeite restrições de liquidação e devolução retornadas pela API.

Para cadastrar documentos com os lançamentos correspondentes na operação conjunta existente, use `cadastrar_notas_com_lancamentos`, preservando a correspondência entre notas e contabilizações e a chave de idempotência. Não substitua essa operação por uma sequência de chamadas alegando atomicidade entre elas.

Não repita cadastro após timeout sem confirmar o resultado pelos documentos disponíveis. Não invente ferramentas ausentes no catálogo. Nunca solicite token ou senha para obter um arquivo.

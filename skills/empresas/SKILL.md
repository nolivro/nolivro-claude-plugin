---
name: empresas
description: Use quando a pessoa quiser listar empresas do noLivro, escolher a empresa da conversa, consultar o painel ou cadastrar uma empresa com plano inicial.
---

Use as ferramentas do conector noLivro. Consulte os schemas disponíveis na conexão; não invente ferramentas ausentes. Se o conector estiver desconectado, peça conexão pela aba Connectors, nunca senha ou token na conversa.

Use `listar_empresas` para identificar as empresas pelo nome e CNPJ. A conexão acessa somente o escritório retornado pelo login e as empresas autorizadas. `consultar_painel_operacional` apresenta indicadores dessas empresas. Peça esclarecimento quando houver ambiguidade.

Se o plano inicial vier de uma planilha, obtenha `consultar_modelo_onboarding` e use `analisar_plano_onboarding` com a máscara e os bytes reais do XLSX. A análise não cadastra a empresa. Incorpore apenas as contas revisadas ao cadastro final.

Se o cliente não transfere arquivos, use `preparar_envio_arquivo` sem empresa para o onboarding, quando permitido pelo servidor. Essa referência não pode ser reutilizada para documentos de uma empresa existente.

Para cadastrar, reúna CNPJ, nome, plano inicial, período, configuração fiscal e templates antes de solicitar `criar_empresa`. Não invente preset, contas ou enquadramento fiscal. Respeite recusas do servidor; não suponha que há uma opção granular de permissão na tela de conexão. Mantenha a mesma chave de idempotência e o mesmo conteúdo ao reconciliar uma tentativa autorizada.

O cliente aplica sua política de confirmação antes da chamada. Não afirme criação antes do resultado confiável. Após cadastrar, peça reconexão para incluir a nova empresa; a criação não amplia automaticamente o acesso da conexão. Apresente competências como MM/AAAA e nomes/códigos em vez de UUIDs.

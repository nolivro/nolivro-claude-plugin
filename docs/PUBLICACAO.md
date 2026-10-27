# Publicação no diretório do Claude

## Identidade do pacote

- Repositório: `https://github.com/nolivro/nolivro-claude-plugin`
- Caminho do plugin no repositório: raiz (`.`).
- Identificador permanente: `nolivro`.
- Nome exibido: **noLivro**.
- MCP remoto: `https://mcp.nolivro.com.br/mcp`.
- Logo de origem do produto: `assets/nolivro.svg`. Confira os formatos e tamanhos aceitos pelo portal e gere a imagem solicitada a partir desse arquivo.

## Pendências antes da submissão

- [x] Licença MIT registrada em `LICENSE` e no manifesto, com ressalva sobre marca, logo e serviço hospedado no README.
- [ ] Confirmar uma URL pública de privacidade, termos e canal de suporte do noLivro.
- [ ] Executar o roteiro de `VALIDACAO.md` no Claude e registrar as evidências.
- [ ] Preparar uma conta de avaliação e dados de teste para a revisão do conector, sem colocar acesso neste repositório.
- [ ] Publicar o commit escolhido no GitHub e garantir a visibilidade/acesso exigidos para a revisão.
- [ ] Validar o pacote no portal e corrigir os apontamentos.

## Submissão

1. Abra [o portal de desenvolvedores](https://claude.ai/directory/manage) com uma conta elegível e a organização responsável pelo noLivro.
2. Cadastre o conector MCP e o plugin sob essa organização, conforme os formulários disponíveis.
3. Para o plugin, informe repositório, branch e caminho da raiz; use o commit revisado, não uma pasta do backend.
4. Preencha descrição, imagens e informações sobre dados, suporte e privacidade com informações confirmadas pelo produto.
5. Execute **Validate** no portal e depois envie para revisão.

A preparação local não publica o plugin automaticamente nem garante aprovação. O README é parte da apresentação da listagem; revise-o antes de enviar. Não inclua tokens, senhas ou dados de clientes nos arquivos ou nas imagens da listagem.

Referências oficiais:

- [Estrutura e testes do plugin](https://claude.com/docs/plugins/build)
- [Checklist de submissão](https://claude.com/docs/plugins/pre-submission-checklist.md)
- [Publicação no diretório](https://claude.com/docs/directory/publish.md)

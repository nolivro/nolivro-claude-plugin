# noLivro para Claude

Plugin do [noLivro](https://nolivro.com.br) com dez skills contábeis e conexão ao servidor MCP do produto. Use sua conta do noLivro para consultar empresas, contas, lançamentos e demonstrações, além de executar operações solicitadas pela conversa com Claude.

Este repositório contém o pacote do plugin: manifesto, skills, configuração pública do conector e documentação. As ferramentas são fornecidas pelo servidor remoto; o backend do noLivro não é distribuído aqui.

## Instalação privada

Você precisa de uma conta no [noLivro](https://app.nolivro.com.br) e de acesso à instalação de plugins na sua conta Claude. Em organizações, o administrador pode precisar habilitar o conector.

1. Gere o ZIP conforme a seção **Preparar e validar** abaixo.
2. No Claude, abra **Customize → Plugins → Add → Upload plugin** e escolha `dist/nolivro-claude-plugin-0.1.0.zip`.
3. Abra a aba **Connectors** do plugin e conecte o noLivro.
4. Faça login na página de `mcp.nolivro.com.br` e selecione as empresas da conexão.
5. Em uma nova conversa, habilite o plugin e peça: **“Liste minhas empresas do noLivro.”**

O plugin utiliza `https://mcp.nolivro.com.br/mcp`. Não informe sua senha, token ou segredo na conversa. Se a conexão expirar, refaça o login pela interface do conector.

## Exemplos de uso

- “Liste as contas da empresa que eu selecionar.”
- “Consulte o balancete de janeiro de 2026.”
- “Valide este lançamento antes de salvá-lo.”
- “Quais são as pendências para fechar este período?”
- “Prepare a importação deste XML e mostre o resultado da análise.”

Identifique a empresa e o período antes de uma operação. O Claude usa as ferramentas disponíveis na conexão e segue a política de confirmação configurada no cliente. Consultas e prévias não equivalem a gravação: confirme o estado retornado antes de considerar uma operação concluída. Não repita automaticamente uma gravação após timeout.

## Skills incluídas

| Skill | Uso |
| --- | --- |
| `empresas` | Contexto, painel, cadastro e plano inicial |
| `plano-contas` | Contas, máscara e importação de plano |
| `periodos` | Consulta, criação e renomeação de períodos |
| `escrituracao` | Prévia, gravação, contabilização e estorno |
| `consultas` | Razão e balancete |
| `notas-parceiros` | Parceiros, notas fiscais, XML e anexos |
| `conciliacao` | Extratos OFX e conciliação bancária |
| `demonstracoes` | DRE, balanço, templates e trabalhos |
| `simples-nacional` | Configuração fiscal e apurações |
| `fechamento` | Preparação, fechamento e retificação |

## Dados e conexão

Ao usar uma ferramenta, o Claude envia os argumentos necessários ao servidor do noLivro. Conforme a operação, isso inclui empresa, contas, valores, documentos fiscais ou arquivos enviados por você. O resultado volta ao Claude e pode integrar a conversa. O login acontece na página do noLivro: as credenciais não fazem parte dos arquivos deste plugin nem dos argumentos das ferramentas.

O pacote não instala um banco de dados ou um servidor local. O serviço remoto mantém o estado de autenticação e processa os dados no noLivro. Consulte [Dados e acesso](docs/DADOS.md) para os limites e o fluxo de arquivos. Essa descrição técnica não substitui os termos e a política de privacidade do produto.

## Preparar e validar

Com Python 3.10 ou superior, na raiz deste repositório:

```bash
python3 scripts/plugin.py check
python3 scripts/plugin.py package
```

O ZIP inclui somente os arquivos públicos do plugin, com o manifesto na posição correta. Não inclui `.git`, scripts de desenvolvimento ou segredos locais. A validação local verifica a estrutura; não comprova homologação no Claude.

Se tiver Claude Code instalado:

```bash
claude plugin validate .
claude --plugin-dir .
```

No Claude Code, use `/mcp` para verificar a conexão. No chat, confirme que as skills aparecem e conecte o servidor pela aba **Connectors**. Siga [o roteiro de validação](docs/VALIDACAO.md) antes de solicitar publicação.

## Publicação e licença

O código, as skills, os manifestos e a documentação deste repositório são distribuídos sob a [licença MIT](LICENSE).

A marca noLivro e o logo em `assets/nolivro.svg` não estão abrangidos pela licença MIT. Nenhum direito de marca é concedido por essa licença. A licença do pacote também não se estende ao backend nem concede acesso ao serviço hospedado, que continua sujeito à autenticação e às condições aplicáveis do noLivro.

O pacote está preparado para teste privado. A submissão ao diretório ainda depende de confirmar os canais públicos de suporte e privacidade e validar o plugin no Claude.

O comando `python3 scripts/plugin.py check --release` verifica a estrutura e a declaração de licença; não substitui a validação da Anthropic. Veja [Publicação](docs/PUBLICACAO.md) para as etapas restantes.

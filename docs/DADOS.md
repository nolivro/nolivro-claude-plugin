# Dados e acesso

## Fluxo

1. O Claude carrega as instruções das skills e a URL pública do conector.
2. A pessoa entra no noLivro por OAuth, fora da conversa, e seleciona empresas.
3. O Claude chama as ferramentas com os dados necessários à solicitação.
4. O noLivro valida a sessão, a empresa e as regras da operação. A resposta retorna ao Claude.

Este pacote não contém senhas ou chaves de API. Não coloque credenciais em `.mcp.json`, no Git ou na conversa. As políticas do Claude também se aplicam aos dados que aparecem no chat; evite enviar informações que não sejam necessárias à operação.

## Permissões e gravações

As empresas da conexão delimitam o acesso. Atualmente, o servidor de produção habilita as operações do catálogo para as empresas autorizadas, sem seleção granular entre leitura e escrita na tela de consentimento. As permissões do usuário no backend continuam valendo. A política de confirmação de chamadas pertence ao cliente Claude; não é garantido um novo clique humano antes de cada operação.

Uma skill orienta o uso das ferramentas e não substitui a autorização do servidor. O plugin não amplia automaticamente o consentimento quando uma nova empresa é criada. Refazer a conexão permite incluir a nova empresa.

## Arquivos e sessões

Arquivos podem ser enviados às ferramentas ou por um link temporário gerado pelo próprio conector. A referência pertence à conexão e ao contexto escolhido; não a compartilhe em outra conversa. A prévia de importação não grava o documento. A gravação acontece somente pela operação correspondente.

O serviço remoto armazena o estado OAuth no Redis e protege o token da sessão upstream por cifra. Uploads temporários do conector têm expiração; documentos efetivamente gravados seguem o armazenamento do noLivro. Não confunda expiração de uma referência temporária com exclusão de um documento contábil.

Desconectar o conector invalida seu acesso. Isso não desfaz gravações já concluídas, não apaga conversas e não garante o cancelamento de uma requisição que já tenha sido enviada. Se a sessão expirar, conecte novamente pela interface OAuth.

## Informações públicas ainda necessárias

Antes da submissão ao diretório, o responsável pelo produto deve confirmar a URL da política de privacidade, os termos aplicáveis e o canal de suporte. Este documento descreve o funcionamento técnico; não estabelece prazos legais de retenção, compromissos contratuais ou uma nova política de privacidade.

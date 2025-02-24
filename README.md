
# Guia Rápido de Comandos Git

Este documento fornece uma visão geral dos principais comandos do Git para gerenciamento de repositórios.

Criado para tirar dúvidas configurações e alguns dos principais comandos utilizados.

## Sumário

1. [Configuração Git](#configuracao-git)
2. [Autenticação com GitHub](#aitenticacao-github)
3. [Comandos Básicos](#comandos-básicos)
4. [Trabalhando com Branches](#trabalhando-com-branches)
5. [Repositórios Remotos](#repositórios-remotos)
6. [Visualização de Histórico](#visualização-de-histórico)
7. [Desfazendo Mudanças](#desfazendo-mudanças)
8. [Reset de Commit](#reset-de-commit)

## Configuração Git

Exibe informações de configuração da ferramenta Git e variáveis de configuração.
```
git config
```
Configurações do usuário.
```
-- global
```
Configuração do sistema.
```
-- system
```  
Configuração do repositório.
```
-- local
```

Para configuração do nome e email do usuário, utilizamos o comando.
```
git config --global user.name "nome_do_usuario"
```
```
git config --global user.email "email_usuario"
```

Visualializar configurações
```
git config --list
```

Para configuração da branch padrão
```
git config init.defaultBranch
``` 
Retornando o nome da branch padrão já configurada.
```
git config --global init.defaultBranch nome_branch_padrao
``` 
Alterando o nome da branch padrão globalmente para o nome desejado.

Para mais configurações podemos visitar a página de documentação do git.

[Documentação Git](https://git-scm.com/doc)

## Autenticação com GitHub

- Autenticação via Token

Entrar na página de configuração do seu perfil no GitHub, e ir na aba de Developers Settings > Personal Access Tokens > Tokens (classic) > Generate New Token (Classic).

Ao gerar o token, podemos configurar o tempo de expiração do mesmo e outros escopos de acesso.

O token gerado não será mostrado novamente após o fechamento da página, logo deve se ter cuidado para copia-lo.

- Autenticação via SSH 

[Documentação Autenticação SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)


## Comandos Básicos

#### Inicializar um novo reositório em uma pasta local
Utilizando o GitBash, entramos no diretorio escolhido e usamos o seguinte comando:

```
git init
```

Para vincular esse diretorio a um repositório remoto.
```
git remote add origin URL
``` 

Subistituindo o URL pelo link HTTPS do repositório no GitHub


#### Para clonar um repositório criado no GitHub, utilizamos o comando:
```
git clone URL
```

Sendo URL o link HTTPS encontrado na página do repositório.
Caso deseje renomear o repositório localmente, utiliza-se:
```
git clone URL nome_repositorio"
```

Subistituindo a URL pelo HTTPS do repositorio e "nome_repositorio" pelo nome desejado localmente.

#### Verificar Status do repositório
Mostra a situação dos arquivos no repositório (modificados, preparados para commit, não rastreados).
```
git status
```
#### Adicionar arquivos a área de preparação
Adiciona mudanças nos arquivos à área de preparação para o próximo commit.

```
git add nome_do_arquivo
```

Para adicionar todos os arquivos modificados:

```
git add .
```

#### Confirmar as alterações

Salva as mudanças preparadas no repositório com uma mensagem de commit descritiva

```
git commit -m "mensagem do commit"
```

#### Enviar alterações para o repositório remoto

```
git push origin nome_da_branch
```
#### Baixando alterações do repositório remoto

Atualiza seu repositório local com as alterações do repositório remoto.

```
git pull
```

## Trabalhando com Branches
Branches permitem que você trabalhe em diferentes versões de um repositório ao mesmo tempo. Isso é útil para gerenciar novas funcionalidades, correções de bugs ou experimentos sem afetar a branch principal (geralmente main ou master).

#### Criar uma Nova Branch
Cria uma nova branch a partir da branch atual. Use este comando quando quiser começar a desenvolver uma nova funcionalidade ou corrigir um bug sem interferir na branch atual.
```
git branch <nome-da-branch>
```

#### Mudar para uma Branch
Alterna para a branch especificada. Use este comando quando quiser trocar para outra branch para ver ou continuar o trabalho naquela branch.
```
git checkout <nome-da-branch>
```

#### Criar e Mudar para uma Nova Branch
Cria uma nova branch e muda para ela imediatamente. Use este comando quando quiser criar uma nova branch e começar a trabalhar nela de uma vez.
```
git checkout -b nome_da_branch
```

#### Mesclar uma Branch na Atual
Mescla as alterações de uma branch especificada na branch atual. Use este comando quando quiser incorporar as alterações feitas em uma branch de desenvolvimento ou correção de bugs na branch atual.
```
git merge nome_da_branch
```

#### Deletar uma Branch
Remove uma branch que não está mais em uso. Use este comando quando uma branch foi mesclada ou não é mais necessária, e você deseja manter seu repositório limpo.
```
git branch -d nome_da_branch
```
#### Para forçar a remoção de uma branch que ainda não foi mesclada:
Use este comando com cautela para remover uma branch que possui alterações não mescladas, pois isso pode resultar na perda de trabalho não incorporado em outras branches.
```
git branch -D nome_da_branch
```

## Repositórios Remotos
Repositórios remotos são versões de seu projeto que estão hospedadas na internet ou em uma rede. Eles permitem a colaboração com outros desenvolvedores e o backup de seu trabalho.

#### Adicionar um Repositório Remoto
Adiciona um repositório remoto com um nome especificado. Use este comando quando quiser associar seu repositório local a um repositório remoto, geralmente para começar a compartilhar seu trabalho com outros.
```
git remote add nome_do_remoto URL_remoto
```
#### Verificar os Remotos Configurados
Lista todos os repositórios remotos configurados. Use este comando para ver quais repositórios remotos estão associados ao seu repositório local.
```
git remote -v
```

#### Remover um Repositório Remoto
Remove a associação com um repositório remoto. Use este comando quando um repositório remoto não for mais necessário ou estiver incorreto.
```
git remote remove nome_remoto
```

#### Renomear um Repositório Remoto
Renomeia um repositório remoto. Use este comando quando quiser mudar o nome de um repositório remoto para algo mais descritivo ou adequado.
```
git remote rename nome_antigo nome_novo
```

## Visualização de Histórico
É importante visualizar o histórico de commits para entender a evolução do projeto e acompanhar as mudanças feitas ao longo do tempo.

#### Ver o Histórico de Commits
Mostra uma lista de commits em ordem cronológica inversa. Use este comando para ver detalhes completos de cada commit, incluindo autor, data e mensagem.
```
git log
```

### Ver um Histórico Compacto
Mostra um histórico resumido dos commits, útil para uma visão geral rápida. Use este comando para uma visão simplificada do histórico de commits.
```
git log --oneline
```

#### Ver um Histórico Gráfico
Mostra um gráfico das branches e merges do repositório. Use este comando para visualizar a estrutura do repositório, incluindo como as branches divergem e se unem.
```
git log --graph --oneline --all
```

#### Ver as Alterações de um Commit Específico
Mostra as alterações feitas em um commit específico. Use este comando para inspecionar o que foi modificado em um commit particular.
```
git show hash_commit
```

#### Ver as Alterações entre Commits
Mostra as diferenças entre dois commits. Use este comando para comparar duas versões específicas do projeto e ver o que mudou entre elas.
```
git diff commit1 commit2
```

#### Ver as Alterações desde o Último Commit
Mostra as diferenças entre a árvore de trabalho e o último commit. Use este comando para ver as alterações que ainda não foram commitadas.
```
git diff HEAD
```

## Desfazendo Mudanças
Desfazer mudanças é uma parte crítica do fluxo de trabalho no Git. Existem várias maneiras de desfazer alterações dependendo do que você deseja alcançar.

#### Desfazer Alterações no Arquivo da Árvore de Trabalho
Descarta as mudanças não confirmadas no arquivo e restaura a última versão confirmada. Use este comando para reverter modificações em um arquivo específico que ainda não foram commitadas.
```
git checkout -- <arquivo>
```

#### Desfazer Alterações na Área de Preparação
Remove as mudanças da área de preparação, mas mantém as alterações na árvore de trabalho. Use este comando para tirar um arquivo da área de preparação enquanto mantém suas mudanças no diretório de trabalho.
```
git reset HEAD <arquivo>
```

### Reverter um Commit
Cria um novo commit que desfaz as alterações de um commit anterior. O histórico do commit original é preservado. Use este comando para desfazer as mudanças de um commit sem alterar o histórico do repositório.
```
git revert <hash-do-commit>
```

### Stash 
```git pop```

### Retornar o comit
```
git reset --soft HEAD^
```

## Reset de Commit
### Tipos
1. `--soft`
2. `--mixed` (padrão)
3. `--hard`

### Reset `--soft`

Este modo move o ponteiro do HEAD para o commit especificado, mas deixa a área de preparação (staging area) e a árvore de trabalho (working directory) inalteradas. As alterações do commit que foi "desfeito" permanecem na área de preparação.

Quando usar:
- Quando você quer desfazer um commit, mas deseja manter as alterações na área de preparação para fazer um novo commit imediatamente.

### Reset `--mixed`
Este é o modo padrão. Move o ponteiro do HEAD para o commit especificado e desfaz as mudanças na área de preparação, mas deixa a árvore de trabalho inalterada. As alterações do commit que foi "desfeito" permanecem nos arquivos, mas não estão mais na área de preparação.

Quando usar:
- Quando você quer desfazer um commit e remover as alterações da área de preparação, mas deseja manter as mudanças nos arquivos para revisão ou correção antes de um novo commit.

### Reset `--hard`
Este é o modo mais drástico. Move o ponteiro do HEAD para o commit especificado e desfaz todas as mudanças na área de preparação e na árvore de trabalho. Todas as alterações feitas desde o commit especificado são perdidas permanentemente.

Quando usar:
- Quando você quer desfazer commits e descartar todas as alterações feitas nos arquivos desde esse commit. Use com cuidado, pois as alterações serão perdidas permanentemente.

---

**por: Vinicius Mariath**

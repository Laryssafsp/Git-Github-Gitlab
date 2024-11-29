# GIT
· Git é um sistema de controle de versão,utilizado para desenvolvimento de software. <br>
· Ele é conhecido como um Repositório Local. <br>
· Registra cada operação com um "commit". <br>
. Os projetos Git podem ser hospedados em plataformas como o GitHub. <br>

# GITHUB
. O GitHub e uma plataforma de codigo colaboração baseada em Git. <br>
· Conhecido como Repositório remoto.  <br>
. Ele permite que os desenvolvedores compartilhem seus projetos de software. <br>

# REPOSITÓRIO
Um repositório no GitHub é como uma pasta online onde você pode armazenar e gerenciar todos os arquivos relacionados a um projeto.


- Branch: cópia do repositório/arquivos para que devs possam trabalhar simultaneamente, não "problemas de conflito".
- Pull Request: solicitação para que as mudanças feitas no branch sejam revisadas e, se apropriadas, integradas ao branch MASTER.
-> Revisão de Código: Antes de um merge, outros membros da equipe geralmente revisam.
- Merge: As mudanças podem ser incorporadas (ou "merged") no branch principal. 
- Merge Conflicts: Às vezes, podem ocorrer conflitos de merge se o mesmo trecho de código foi modificado de maneiras diferentes nos dois branches. 
- Commit: comentário sobre as alterações e confirmações
- [Padrões de Commits (Conventional Commits)](https://www.conventionalcommits.org/en/v1.0.0/#specification)
  
---

# Comandos:

`git clone ` =  Copia o repositório
`git checkout ` =  Verificar a branch atual
`git checkout "branch_name" ` =  Troca de branch
`git checkout -b  "branch_name" ` =  Troca de branch
`git fetch ` =  Atualiza suas referências locais em referencias remotas
`git pull ` =  Atualiza sua branch local com a versão atual do git
`git status ` =  Apresenta o status da branch local contra a do git
`git add . ` =  Adiciona todas as suas alterações em um pacote

`git commit -m "Comentário" ` =  Comenta as alterações que serão enviadas
`git push ` =  Envia as alterações adicionadas e comentadas
- a primeiro branch criada via terminal é `git push --set-upstream origin feature/branchnova`
`git checkout -b "branch_name" ` =  Clona suabranch atual com o nome branch_name 
`git merge "branch_name" ` =  Traz as alterações da branch_name para sua branch atual
`git branch -D "branch_atual" ` =  Apaga sua branch localmente
obs: cuidado para não apagar a branch errada - apaga a branch quando finaliza o desejado.


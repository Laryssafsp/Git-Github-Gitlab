# Formacao Gitlab CICD
CI/CD é o coração do DevOps

### Versionamento
1.0 -> Versão Inicial
1.1 -> Atualizações menores (adição de novas features)
1.1.1 -> Patch (correção de um pequeno bug)
1.2 -> Atualizações menores (melhoria de desempenho)
2.0 -> Atualização Importante (troca de layout)
2.0.1 -> Patch (correção na tradução)


### O que é Deploy?
A implantação (Deploy) envolve mover o software de um ambiente controlado para outro. Um ambiente é um subconjunto de infraestrutura de Tl usado para uma finalidade específica.

### O que é Deploy?

Os ambientes mais comuns sao:

**Desenvolvimento (Dev)**: É aqui que os desenvolvedores constroem o código.
**Integração (Staging)**: Aqui, o novo código é combinado e validado para funcionar com o código existente. O papel do ambiente de staging é ser o mais próximo da realidade, ou seja, ele deve ser uma réplica perfeita do ambiente de produção.
**Teste**: É aqui que os testes funcionais e não funcionais são realizados no código mesclado para confirmar que ele atende aos requisitos da organização e do cliente.
**Produção**: É aqui que o software é disponibilizado aos usuários.


### Integração contínua (CI)

A integração contínua é uma prática de desenvolvimento de software em que os desenvolvedores, com frequência, juntam suas alterações de código em um repositório central. Depois disso, criações e testes são executados. Os principais objetivos da integração contínua são encontrar e investigar erros mais rapidamente, melhorar a qualidade do software e
reduzir o tempo necessário para validar e lançar novas atualizações de software.


### Entrega contínua (CD)

A entrega contínua é uma prática de desenvolvimento de software em que alterações de código são criadas, testadas e preparadas automaticamente para liberação para produção. Ela expande com base na integração contínua, pela implantação de todas as alterações de código em um ambiente de teste e/ou ambiente de produção, após o estágio de criação.
Quando a integração contínua for implementada adequadamente, os desenvolvedores sempre terão um artefato de criação pronto para ser implantado, e que passou por um processo de teste padronizado.


## O que é o GitLab?

O GitLab é um repositório Git que fornece repositórios abertos e privados e outros recursos. E uma plataforma completa de DevOps que permite que os profissionais executem todas as tarefas em um projeto, desde o planejamento do projeto, passando pelo gerenciamento do código-fonte até o monitoramento e a segurança.



# Codes

## GITLAB

#### Subir branch para gitlab - e sobe para produção
```
git push --set-upstream origin test
```

#### pode especificar quais jobs serão executados
Por exemplo, executar apenas o job de testes na nova branch criada, então adiciona um parâmetro `only` no scrip. 



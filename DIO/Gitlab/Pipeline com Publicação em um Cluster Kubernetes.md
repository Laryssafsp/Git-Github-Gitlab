# Criando uma MV do tipo Bastion para a gerência do cluster
## Pipeline com Publicação em um Cluster Kubernetes

- a MV será usando o Bastion Host com acesso ao rede onde esta o Cluster (e deploy, sempre estará online.
- e o serviço será automaticamente atualizado por ela e não por uma máquina de terceiro.

- Além do Cluster, precisa de uma máquna virtual: (no exemplo de  GCP)
  - na mesma região que o Cluster ou acesso a rede onde ele esta
  - Informações necessárias - no gitlab:
    -  IP externo (público) de acesso (colocar no putty)
    -  Configurar para acessar (Segurança e acesso) ➡️ Adicionar Item ➡️ [Win] baixar o putty.exe e puttygen.exe (gerador das chaves publica e privada) (alterar o nome de usuario na senha), a SSH_key*** e a IP da máquina

```yml
stages:
  - build
  - deploy_gcp

build_images:
  stage: build
  image: docker:20.10.16

  services:
    - docker: 20.10.16-dind
  
  variables:
    DOCKER_TLS_CERTDIR: "/certs"
  
  before_script:
    - docker login -u $REGISTRY_USER -p $REGISTRY_PASS
  
  script:
    - docker build -t denilsonbonatti/app-cicd-dio:1.0 app/.
    - docker push denilsonbonatti/app-cicd-dio:1.0

deploy_gcp:
  stage: deploy_gcp
  before_script: # arquivo com chave para à MV - puxar no puttygen a private key - tem que ser .pem por ser linux - adicionar a variavel nas configurações no gitlab***
    - chmod 400 $SSh_KEY # puxa a variável configurada no gitlab
  script:
    - ssh -o StrictHostKeyCheching=no -i $SSH_KEY <user@ip> "sudo rm -Rf ./name file/ && sudo gitclone <clone url gitlab> && cd <name file> && cd <file> && sudo chmod +x ./script.sh && ./script.sh" # StrictHostKeyCheching=no  = remove a interação de confirmaçaõ
```

#### arquivo script.sh

```sh
#!/bin/bash

kubectl apply -f deployment.yml
```

#### deployment.yml

```yml
<https://gitlab.com/denilsonbonatti/app-cicd-dio.git> # arquivo com o script
```
    

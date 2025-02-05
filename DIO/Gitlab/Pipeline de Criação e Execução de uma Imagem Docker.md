##Utilizando o girlab runner

```sudo gitlab-runner regitrer```
inserir a url + token + instancia + tags + executor


##Criação do Pipeline e images

- criar pasta ```app``` com o download da imagem baixada no site: [free-css](https://www.free-css.com)
- Caso o download não inicie automaticamente após você clicar no link acima, copie e cole em seu navegador a url abaixo: (https://www.free-css.com/assets/files/free-css-templates/download/page285/bitcypo.zip)

### Arquivo dockerfile dentro do app

```dockerfile
FROM httpd:latest

WORKDIR /usr/local/apache2/htdocs/
COPY . /usr/local/apache2/htdocs/

EXPOSE 80
```

### Criação do gitlab-ci.yml

```yml
stages:
- build
deploy

criar_imagens:
stage: build
tags:
gcp
script:
- docker build -t denilsonbonatti/gcp-projeto1:1.0 app/.
- docker push denilsonbonatti/gcp-projeto1:1.0

executar_imagens :
stage: deploy
needs :
- criar_imagens
tags:
- gcp
script:
- docker run -dti -- name webserver -p 80:80 denilsonbonatti/gcp-projeto1:1.0
```

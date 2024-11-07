<center><h2>Explorando a Colaboração e o Uso do Markdown para Documentação Eficiente</h2></center>

Olá, me chamo Viviani!! O curso foi muito aproveitoso, e proporcionou um grande aprendizado sobre os conceitos de Git e GitHub, informações sobre autenticação, além de fundamentos de coloboração e uso adequado do Markdown para uma documentação clara e objetiva.

<div align="center"><img src="https://inklysaraujo.com.br/wp-content/uploads/2022/10/git-vs-github.png" alt="Git vs GitHub" width="600" height="300"></div>

### Objetivos Realizados:

1. **Criar sua conta no Github:** Conta criada e configurada com autenticação por token para garantir segurança e facilitar o acesso. Perfil disponível em: [github.com/vivianikelly](github.com/vivianikelly).

2. **Criar um Repositório:** Repositório para o desafio criado [desafio-github-markdown](https://github.com/vivianikelly/desafio-github-markdown-vivi) criado com sucesso para armazenar e gerenciar projetos. A edição foi realizada tanto no Visual Studio Code quanto diretamente no GitHub.dev, proporcionando flexibilidade no desenvolvimento.

3. **Colaboração:** Para iniciar a coloboração, foi realizado um *fork* do repositório https://github.com/alinealien/desafio-github-markdown para ter como base nas alterações. 

4. **Formatação com Markdown:** Foi utilizado para estruturar a documentação de forma clara, incluindo títulos, listas, links e imagens para uma apresentação visualmente organizada.

### Tabela: Colaboração com o Github

Tema | Breve Conceito
-|-
Repositório |Local aonde fica os projetos
Branches |Local desenvolvimento separado no controle de versão
Pull Resquest|Propor alterações em um repositório e solicitar que essas alterações sejam revisadas e mescladas
Merge |Operação no controle de versão, com alterações de duas branches diferentes
Fork |É uma cópia de um repositório de outro usuário para o seu próprio espaço no GitHub. 
Issues |Usadas para rastrear tarefas, bugs, melhorias
Wikis |Documentação de projetos, de uma forma mais detalhada
Gists |Úteis para compartilhar pequenos trechos de código, notas ou até mesmo scripts

### Clonagem do Repositório:

Após concluir o fork, foi realizado o clone do repositório para a máquina local com o seguinte comando:

``` 
$ git clone https://github.com/vivianikelly/desafio-github-markdown-vivi.git
Cloning into 'desafio-github-markdown-vivi'... 
```

Para complementar o repositório, foram incluídos alguns scripts Python desenvolvidos na trilha de Programação Python.

### Verificando status do repositório:

```
$ git status
...
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        scripts_python/
```

### Inclusão, Commit e Push das Alterações:

```
$ git add .

$ git commit -m "Meu desafio Github - usando Markdown"
[main 2cfb171] Meu desafio Github - usando Markdown
 9 files changed, 131 insertions(+), 18 deletions(-)
 create mode 100644 scripts_python/funcao_bissexto.py
 create mode 100644 scripts_python/funcao_contador.py
 create mode 100644 scripts_python/funcao_converter_temperatura.py
 create mode 100644 scripts_python/funcao_email.py
 create mode 100644 scripts_python/funcao_impar_par.py
 create mode 100644 "scripts_python/funcao_intersec\303\247\303\243o.py"
 create mode 100644 scripts_python/funcao_pessoa.py
 create mode 100644 scripts_python/funcao_transforma_data.py

$ git push origin main
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 12 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 3.37 KiB | 3.37 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/vivianikelly/desafio-github-markdown-vivi.git
   d85515a..2cfb171  main -> main
```

## Issues no Repositório Fork

- Como o repositório é um fork (cópia) não apresenta o item *Issues*. Assim, foi criado em outro repositório e referenciado aqui: [Melhorar README. #1]( https://github.com/vivianikelly/meu-repositorio-autenticacoes-DIO/issues/1#issue-2640908937)

## README de Perfil

Além do desafio, foi criado um README de perfil disponível em:  [vivianikelly/README.md](https://github.com/vivianikelly/vivianikelly)


<div align="center"><h2> Desafio Concluído 🚀</h2></div>

<div align="center"><img src="https://img.freepik.com/vetores-premium/concluido-conceito-de-trabalho-projeto-concluido-escolha-aprovada-ideia-de-tarefa-concluida-questionario-on-line_675567-1668.jpg" alt="Git vs GitHub" width="600" height="400"></div><br><br>
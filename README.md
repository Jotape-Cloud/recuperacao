# Como fazer Git Clone no VS Code

Este guia explica como baixar (clonar) um repositório do GitHub diretamente no VS Code.

---

## Pre-requisitos

Antes de começar, certifique-se de ter instalado:

- [Git](https://git-scm.com/downloads) — necessário para usar o comando `git clone`
- [Visual Studio Code](https://code.visualstudio.com/)

Para verificar se o Git está instalado, abra o terminal e digite:

```bash
git --version
```

Se aparecer uma versão (ex: `git version 2.45.0`), está tudo certo.

---

## Passo a passo

### 1. Copie o link do repositório

No GitHub, acesse o repositório que deseja clonar, clique no botão verde **"Code"** e copie o link HTTPS:

```
https://github.com/usuario/nome-do-repositorio.git
```

### 2. Abra o VS Code

Abra o Visual Studio Code normalmente.

### 3. Abra o terminal integrado

No menu superior, clique em **Terminal > Novo Terminal** (ou use o atalho `` Ctrl + ` ``).

### 4. Navegue até a pasta onde deseja salvar o projeto

Use o comando `cd` para ir até a pasta desejada. Exemplo:

```bash
cd Documentos
```

### 5. Execute o comando git clone

Cole o link copiado no passo 1:

```bash
git clone https://github.com/usuario/nome-do-repositorio.git
```

Aguarde o download terminar.

### 6. Abra a pasta clonada no VS Code

Após o clone, entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

Em seguida, abra no VS Code:

```bash
code .
```

---

## Alternativa: clonar pela interface do VS Code

Você também pode clonar sem usar o terminal:

1. Pressione `Ctrl + Shift + P` para abrir a paleta de comandos
2. Digite `Git: Clone` e pressione `Enter`
3. Cole o link do repositório e pressione `Enter`
4. Escolha a pasta onde salvar
5. Clique em **"Abrir Repositório"** quando solicitado

---

## Duvidas comuns

**O git clone deu erro de "não reconhecido"?**
Isso significa que o Git não está instalado ou não foi adicionado ao PATH. Reinstale o Git e marque a opção "Add Git to PATH" durante a instalação.

**Pede usuario e senha do GitHub?**
O GitHub não aceita mais senha comum. Use um **token de acesso pessoal** no lugar da senha. Consulte o professor para obter orientações.

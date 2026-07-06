# Python Academy STW

**Pensar primeiro. Construir com proposito.**

Material didatico progressivo de logica de programacao e Python — do primeiro `print` a uma aplicacao completa com banco de dados, organizada em quatro modulos sequenciais.

---

## Sobre o projeto

O **Python Academy STW** e um curso estruturado para ensinar programacao desde a base: antes de frameworks ou ferramentas avancadas, o aluno aprende a **pensar como programador**. Cada modulo parte do anterior, com aulas comentadas, exercicios praticos e um projeto que amarra os conceitos.

A trilha segue uma unica linha evolutiva — o mesmo problema ("guardar e manipular dados") cresce em complexidade a cada etapa:

```
logica e sintaxe  →  funcoes e arquivos  →  classes e objetos  →  sistema em camadas + banco
```

---

## Modulos

| Modulo | Pasta | Foco | Aulas |
|--------|-------|------|-------|
| **01** | `Modulo01PY/` | Fundamentos: variaveis, tipos, condicionais, lacos, colecoes | 51 |
| **02** | `Modulo02PY/` | Funcoes, modularizacao, pastas e persistencia (txt/json) | 15 |
| **03** | `Modulo03PY/` | Orientacao a objetos: classes, encapsulamento, heranca | 15 |
| **04** | `Modulo04PY/` | Aplicacao console em camadas com SQLite | 1 projeto |

Cada modulo contem:

- **`description.txt`** — visao geral, de onde viemos e para onde vamos
- **`Aulas/`** — codigo comentado, pronto para acompanhar em aula
- **`Exercicios/`** — um desafio por aula, com enunciado em comentarios

Consulte o `description.txt` de cada modulo antes de comecar.

---

## Como comecar

**Requisito:** Python 3.10 ou superior ([python.org/downloads](https://www.python.org/downloads/))

```bash
git clone https://github.com/AndreSoftwareTech/PythonAcademySTW.git
cd PythonAcademySTW
```

**Modulo 01** (primeiro passo):

```bash
cd Modulo01PY/Aulas
python aula01.py
```

**Modulo 04** (projeto final):

```bash
cd Modulo04PY
python main.py
```

Siga a ordem dos modulos. Cada `description.txt` explica a conexao com o modulo anterior e o proximo.

---

## Estrutura do repositorio

```
PythonAcademySTW/
├── README.md
├── Modulo01PY/     Aulas/ + Exercicios/     (fundamentos)
├── Modulo02PY/     Aulas/ + Exercicios/     (funcoes e persistencia)
├── Modulo03PY/     Aulas/ + Exercicios/     (orientacao a objetos)
└── Modulo04PY/     aplicacao em camadas     (banco de dados)
```

---

## Para professores

- As aulas foram pensadas para **compartilhamento de tela**: comentarios explicam o *como* e o *porque*.
- Os exercicios validam se o aluno prestou atencao; enunciados sao criativos e progressivos.
- O gabarito do professor fica abaixo da linha `# --- GABARITO DO PROFESSOR ---` em cada exercicio.

---

## Recursos

- [Documentacao oficial Python](https://docs.python.org/3/)
- [Comunidade Python](https://www.python.org/community/)

---

<p align="center">
  <strong>Python Academy STW</strong><br>
  <em>Da logica ao sistema — cada linha tem um proposito.</em>
</p>

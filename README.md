# Análise de Vulnerabilidades com Testes Automatizados

Este projeto demonstra, de forma prática, a exploração e a mitigação da vulnerabilidade SQL Injection em um sistema simples de autenticação desenvolvido em Python. A validação do comportamento da aplicação é realizada por meio de testes automatizados utilizando pytest.

## Objetivo

Simular uma falha de segurança em um sistema de login e aplicar técnicas de proteção para impedir sua exploração, evidenciando a importância de boas práticas no desenvolvimento de software seguro.

## Conceitos Abordados

* SQL Injection
* Segurança em aplicações
* Validação de entrada
* Hash de senha com SHA-256
* Testes automatizados com pytest
* Boas práticas de desenvolvimento seguro

## Estrutura do Projeto

```
.
├── app_vulneravel.py   # Sistema com vulnerabilidade de SQL Injection
├── app_seguro.py       # Sistema protegido com boas práticas de segurança
└── test_login.py       # Testes automatizados com pytest
```

## Versão Vulnerável

A versão vulnerável realiza a autenticação por meio da concatenação direta de strings na construção da consulta SQL:

```python
query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
```

Esse método permite que entradas maliciosas alterem a lógica da consulta, possibilitando ataques como:

```
' OR '1'='1
```

## Versão Segura

A versão segura aplica medidas de proteção para impedir a exploração da vulnerabilidade:

* Uso de consultas parametrizadas
* Validação de entrada com expressões regulares
* Hash de senha com SHA-256

Exemplo de consulta segura:

```python
query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
cursor.execute(query, (usuario, senha_hash))
```

Essas práticas impedem que os dados fornecidos pelo usuário sejam interpretados como comandos SQL.

## Testes Automatizados

Os testes foram implementados com pytest para validar diferentes cenários:

* Autenticação com credenciais válidas
* Tentativa de acesso com credenciais inválidas
* Exploração da vulnerabilidade na versão insegura
* Bloqueio do ataque na versão segura

### Execução dos testes

```bash
python -m pytest
```

### Resultado esperado

```
collected 2 items
test_login.py .. [100%]

2 passed
```

## Resultados

A aplicação vulnerável permitiu autenticação indevida ao receber uma entrada maliciosa, evidenciando a falha de segurança. Em contrapartida, a versão segura bloqueou corretamente a tentativa de ataque, mantendo o funcionamento normal para usuários legítimos.

## Medidas de Segurança Aplicadas

* Consultas parametrizadas
* Validação de entrada
* Hash de senhas com SHA-256
* Testes automatizados

## Referências

* OWASP Foundation. OWASP Testing Guide
* PRESSMAN, R. S.; MAXIM, B. R. Engenharia de Software
* STALLINGS, William. Segurança de Redes
* ANDERSON, Ross. Engenharia de Segurança

## Autoria

Projeto desenvolvido para a disciplina de Projeto Integrador em Análise e Desenvolvimento de Sistemas.

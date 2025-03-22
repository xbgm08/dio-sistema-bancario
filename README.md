# Sistema Bancário

Este é um sistema bancário simples implementado em Python. Ele permite criar clientes, contas, realizar depósitos, saques e exibir extratos.

## Funcionalidades

- Criar cliente
- Criar conta
- Realizar depósito
- Realizar saque
- Exibir extrato
- Listar contas

## Estrutura do Projeto

- `desafio.py`: Contém a implementação do sistema bancário.
- `README.md`: Este arquivo, com informações sobre o projeto.

## Exemplo de Uso

Ao executar o script, você verá um menu com as seguintes opções:

================ MENU ================ 
[d] Depositar 
[s] Sacar 
[e] Extrato 
[nc] Nova conta 
[lc] Listar contas 
[nu] Novo usuário 
[q] Sair =>

Você pode selecionar uma das opções para realizar a operação desejada.

## Classes e Métodos

### Cliente

- `Cliente`: Classe base para clientes.
- `PessoaFisica`: Subclasse de `Cliente` para pessoas físicas.

### Conta

- `Conta`: Classe base para contas.
- `ContaCorrente`: Subclasse de `Conta` para contas correntes.

### Transações

- `Transacao`: Classe abstrata para transações.
- `Saque`: Subclasse de `Transacao` para saques.
- `Deposito`: Subclasse de `Transacao` para depósitos.

### Histórico

- `Historico`: Classe para armazenar o histórico de transações.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

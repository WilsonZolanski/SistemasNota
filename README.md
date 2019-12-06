<h1>Sistemas De Nota — Projeto do Cin, Universidade Federal De Pernambuco</h1> 

> O programa é um simples sistemas de notas para Cadastrar, Remover, Atualizar os cadastros, buscar, Alterar nível de acesso(entre professor e aluno), Ordernar todos por nome, Gerar relatório(em .txt) ou planilha (.csv)

*O projeto é um sistema aberto e de livre escolha do aluno, você pode entender o desenvolvimento, clicando no link> [projeto](https://github.com/WilsonZolanski/SistemasNota/blob/master/Projeto%202019.2.pdf).*

<p float="left">
  <image width=50%, src="./1.gif"/> 
  <image width=50%, src="./2.gif"/> 
</p>

# Mais detalhes [FALTA TERMIANR]

### Instruções de primeiro acesso
Siga os passos a seguir se é o seu primeiro acesso e não sabe como funciona!

```shell
#1 — Abra o Prompt de Comando em seguida tente acessar a pasta onde se encontra "agenda.py", como no gif exemplificado acima. 
#2 — Assim como está no gif, digite o nome do programa "Python" ou "Python3" (dependendo da sua versão) + o nome do arquivo "agenda.py" + comando desejável.
#>>> Exemplo: C:\Users/wilson/downloads/python agenda.py help
#3 — Caso queira entender cada função do programa, digite o comando "help" para entender quais são as funções do programa e como deve manusear o código.
```
### Download
Baixe o programa pelo botão verde (**Clone or Download**) ou se preferir, abra o programa Visual Studio Code, pressione no teclado Ctrl+Shift+P e digite *"Git clone"* e cole (*https://github.com/WilsonZolanski/agenda.git*) para salvar em um repositório local.

# Todos os comandos

### Adicionar:
```shell
>> python agenda.py a (data) (hora) (prioridade) (descrição) (contexto) (projeto)
```
*Observação* = A adição de uma nova tarefa deve seguir exatamente essa ordem, também é possível adicionar apenas a "descrição" da sua tarefa sem os outros dados.
- `Data`: A data deve ser digitada dessa forma "DDMMAAAA" onde "D" é o Dia, "M" o mês e "A" o ano. Exemplo: 14012018 (Isso representa 14/01/2018)
- `Hora`: A hora deve ser digitada dessa forma "HHMM" onde "H" é a hora e "M" o minuto. Exemplo 1030 (Isso representa 10 horas e 30 minutos)
- `Prioridade`: A prioridade da sua tarefa deve ser digitada seguindo a ordem do alfabeto, a ordem será seguida de acordo com alfabeto, em outras palavras a letra "A" terá mais prioridade que a letra "Z". (Caso seja digitado letras maiúsculas e minúsculas, a ordem será seguida da maiúscula para minúscula).
  - **OBS:** Caso o programa seja aberto no ubuntu, a prioridade terá um sistema de cores diferentes.
- `Contexto`: Contexto da tarefa pode ser traduzido também como o local onde será feito a tarefa. Exemplo: @casa.
- `Projeto`: O projeto da tarefa pode ser traduzido também como a finalidade da sua tarefa. Exemplo: +Pesquisa.

### Listar:
O comando "listar" pode ser utilizado também por data, hora, prioridade, contexto ou projeto.
```shell
>> python agenda.py l 
```
### Remover:
O comando "remover" pode ser utilizado pegando o número index que se encontra ao lado de cada tarefa:
```shell
>> python agenda.py r (index da tarefa)
```
### Fazer:
O comando "fazer" pode ser utilizado quando o usuário quiser marcar uma tarefa como concluída.
  - Caso o usuário marque a tarefa como feita, será movida para um novo arquivo "done.txt".
```shell
>> python agenda.py f (index da tarefa)
```
### Prioridade:
O comando "prioridade" pode ser utilizado quando o usuário desejar adicionar ou alterar a prioridade de uma tarefa.
```shell
>> python agenda.py p (Nova prioridade) (Índice da tarefa)
```

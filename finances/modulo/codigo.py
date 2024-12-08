from datetime import datetime
class Transaction:
    """
    Representa uma transação financeira.

    Atributos:
    amount (float): O valor da transação.
    date (datetime): A data da transação.
    category (str): A categoria da transação.
    description (str): A descrição da transação.
    """
    
    def __init__(self, amount: float, date: datetime, category: str, description: str) -> None:
        """
        Inicializa os atributos da transação.

        Parâmetros:
        amount (float): Valor da transação.
        date (datetime): Data da transação.
        category (str): Categoria da transação.
        description (str): Descrição da transação.
        """
        self.amount = amount
        self.date = date or datetime.now()
        self.category = category
        self.description = description

    def __str__(self) -> str:
        """
        Retorna uma string representando a transação.

        Retorna:
        str: Uma representação legível da transação.
        """
        return f"Transação: {self.description}\nR${self.amount:.0.2f}\n{self.category}"

    def update(self, **kwargs) -> None:
        """
        Atualiza os atributos da transação.

        Parâmetros:
        kwargs (dict): Atributos a serem atualizados.
        """
        for atributos in kwargs:
            self.novo_atributo = atributos
        
        self.amount = self.novo_atributo
        self.date = datetime.now()
        self.category = self.novo_atributo
        self.description = self.novo_atributo


class Account:
    """
    Representa uma conta bancária.

    Atributos:
    name (str): Nome da conta.
    balance (float): Saldo atual da conta.
    transactions (list): Lista de transações associadas à conta.
    """
    
    def __init__(self, name: str, balance: float = 0.0) -> None:
        """
        Inicializa uma conta bancária.

        Parâmetros:
        name (str): Nome da conta.
        balance (float): Saldo da conta.
        """
        self.name = name
        self.balance = balance
        self.transactions = []

    def add_transaction(self, amount: float, category: int, description: str = "") -> None:
        """
        Adiciona uma transação à conta.

        Parâmetros:
        amount (float): Valor da transação.
        category (int): Categoria da transação (1-5).
        description (str): Descrição da transação.
        """
        category_type = {
            1: "Transações Operacionais", 
            2: "Transação de Investimento",
            3: "Transação Financiamento", 
            4: "Transação de Capital",
            5: "Transações Não Operacionais"
        }
        category_name = category_type.get(category, "Categoria")
        
        transaction = Transaction(amount, category=category_name, description=description)
        self.transactions.append(transaction)
        self.balance -= amount

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: int = None) -> list:
        """
        Retorna transações de acordo com filtros de data e categoria.

        Parâmetros:
        start_date (datetime): Data inicial para filtrar as transações.
        end_date (datetime): Data final para filtrar as transações.
        category (int): Categoria das transações a serem retornadas.

        Retorna:
        list: Lista de transações filtradas.
        """
        pass

    def client(self, Client):
        """
        Associa um cliente à conta.

        Parâmetros:
        Client (Client): O cliente associado à conta.
        """
        self.Client = Client()


class Investment(Account):
    """
    Representa um investimento financeiro.

    Atributos:
    type (str): Tipo de investimento.
    initial_amount (float): Valor inicial do investimento.
    rate_of_return (float): Taxa de retorno do investimento.
    time (int): Ano de compra do investimento.
    """
    
    def __init__(self, type: str, initial_amount: float, rate_of_return: float, time: int = 2024) -> None:
        """
        Inicializa um investimento.

        Parâmetros:
        type (str): Tipo do investimento.
        initial_amount (float): Valor inicial investido.
        rate_of_return (float): Taxa de retorno do investimento.
        time (int): Ano de compra do investimento.
        """
        self.type = type
        self.initial_amount = initial_amount
        self.rate_of_return = rate_of_return
        self.time = time

    def calculate_value(self) -> float:
        """
        Calcula o valor futuro do investimento com base na taxa de retorno.

        Retorna:
        float: O valor estimado do investimento.
        """
        months = (datetime.now() - datetime(self.time, 1, 1)).days // 30
        future_value = self.initial_amount * (1 + self.rate_of_return) ** months
        return future_value

    def sell(self, account: Account) -> None:
        """
        Vende o investimento e adiciona o valor obtido à conta.

        Parâmetros:
        account (Account): A conta onde o valor será depositado.
        """
        value = self.calculate_value()
        account.balance += value
        account.add_transaction(value, 2, f"Venda de investimento {self.type}")


class Client:
    """
    Representa um cliente bancário.

    Atributos:
    name (str): Nome do cliente.
    accounts (list): Lista de contas do cliente.
    investments (list): Lista de investimentos do cliente.
    """
    
    def __init__(self, name: str) -> None:
        """
        Inicializa o cliente com um nome.

        Parâmetros:
        name (str): Nome do cliente.
        """
        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str, balance: float = 0.0) -> Account:
        """
        Adiciona uma nova conta ao cliente.

        Parâmetros:
        account_name (str): Nome da conta.
        balance (float): Saldo inicial da conta.

        Retorna:
        Account: A conta criada.
        """
        account = Account(account_name, balance)
        self.accounts.append(account)
        return account
        
    def add_investment(self, investment: Investment) -> None:
        """
        Adiciona um investimento ao cliente.

        Parâmetros:
        investment (Investment): O investimento a ser adicionado.
        """
        self.investments.append(investment)

    def get_net_worth(self) -> float:
        """
        Calcula o patrimônio líquido do cliente.

        Retorna:
        float: O valor total do patrimônio (contas + investimentos).
        """
        total_balance = sum(account.balance for account in self.accounts)
        total_investment_value = sum(investment.calculate_value() for investment in self.investments)
        return total_balance + total_investment_value

def future_value_report(client: Client, date: datetime) -> str:
    """
    Gera um relatório sobre o valor futuro dos investimentos de um cliente.

    Parâmetros:
    client (Client): O cliente cujos investimentos serão analisados.
    date (datetime): A data para a projeção futura.

    Retorna:
    str: O relatório com o valor futuro dos investimentos.
    """
    future_reports = []
    
    for investment in client.investments:
        future_value = investment.calculate_value()
        annual_return = investment.rate_of_return
        years_to_project = (date - datetime.now()).days / 365

        future_value *= (1 + annual_return) ** years_to_project
        
        future_reports.append(f"Investimento em {investment.type}, "
                              f"Valor Atual: R$ {investment.initial_amount}, "
                              f"Retorno Estimado: {annual_return*100:.2f}%, "
                              f"Valor futuro em {date.strftime('%d/%m/%Y')}: R$ {future_value:.2f}")
    
    total_future_value = sum(investment.calculate_value() for investment in client.investments)
    future_reports.append(f"Valor total dos investimentos futuros: R$ {total_future_value:.2f}")
    
    return "\n".join(future_reports)

def generate_report(client: Client) -> str:
    """
    Gera um relatório financeiro detalhado do cliente.

    Parâmetros:
    client (Client): O cliente para o qual o relatório será gerado.

    Retorna:
    str: O relatório financeiro do cliente.
    """
    report = [f"Relatório financeiro de {client.name}"]
    total_balance = sum(account.balance for account in client.accounts)
    report.append(f"\nSaldo total: R$ {total_balance:.2f}")
    report.append("\nDetalhamento das contas:")

    for account in client.accounts:
        report.append(f"{account.name}: R$ {account.balance:.2f}")
    
    report.append("\nTransações realizadas:")
    for account in client.accounts:
        for transaction in account.transactions:
            report.append(f"{transaction.description} - {transaction.category}: "
                          f"R$ {transaction.amount:.2f} em {transaction.date.strftime('%d/%m/%Y')}")
    
    report.append("\nInvestimentos:")
    for investment in client.investments:
        current_value = investment.calculate_value()
        report.append(f"{investment.type}: R$ {current_value:.2f}, "
                      f"Valor inicial: R$ {investment.initial_amount:.2f}, "
                      f"Taxa de retorno: {investment.rate_of_return*100:.2f}%")
    
    return "\n".join(report)


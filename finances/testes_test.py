from datetime import datetime
from .modulo import codigo

def test_client():
    """
    Testa a criação de um cliente e valida o nome atribuído ao cliente.
    """
    client = codigo.Client("Elara")
    assert client.name == "Elara"

def test_investment():
    """
    Testa a criação de um investimento e valida seus atributos como 
    valor inicial, taxa de retorno e tipo de investimento.
    """
    investment = codigo.Investment("Ações", 100, 0.5, 2024)
    assert investment.initial_amount == 100
    assert investment.rate_of_return == 0.05
    assert investment.type == "Ações"

def test_account():
    '''
    Testa a criação de uma conta e valida seus atributos como o nome da conta 
    e o saldo inicial.
    '''
    account = codigo.Account("Conta corrente", 34.80)
    assert account.name == "Conta corrente"
    assert account.balance == 34.80

def test_transaction():
    '''
    Testa a criação de uma transação e valida seus atributos como o valor, 
    data, categoria e descrição.
    '''
    transaction = codigo.Transaction(500, date=datetime(2024, 12, 8))
    assert transaction.amount == 500
    assert transaction.date == datetime(2024, 12, 8)
    assert transaction.category == "Transação financeira"
    assert transaction.description == "Compra"

def test_transaction_update():
    '''
    Testa a atualização de uma transação, verificando se o valor, categoria 
    e descrição são alterados corretamente.
    '''
    transaction = codigo.Transaction(500, date=datetime(2024, 12, 8))
    transaction.update(600, date=datetime(2024, 12, 8))
    assert transaction.amount == 600
    assert transaction.category == "Investimento"
    assert transaction.description == "Venda"

def test_investment_future_value():
    '''
    Testa o cálculo do valor futuro de um investimento e verifica se o 
    valor calculado é maior que o valor inicial.
    '''
    investment = codigo.Investment("Ações", 1000, 0.05, 2024)
    future_value = investment.calculate_value()
    assert future_value > 1000

def test_generate_report():
    '''
    Testa a geração de um relatório financeiro, validando se informações 
    como o saldo total e os investimentos estão corretos no relatório gerado.
    '''
    client = codigo.Client("Elara")
    account1 = client.add_account("Conta Corrente", 2000.00)
    account2 = client.add_account("Conta Poupança", 5000.00)
    investment1 = codigo.Investment("Ações", 1000.00, 0.1, 2020)
    investment2 = codigo.Investment("CDB", 5000.00, 0.06, 2021)
    client.add_investment(investment1)
    client.add_investment(investment2)

    report = codigo.generate_report(client)
    assert "Relatório Financeiro de Elara" in report
    assert "Saldo Total: R$ 7000.00" in report
    assert "Investimentos:" in report
    assert "Ações: R$" in report

def test_future_value_report():
    '''
    Testa a geração de um relatório de valor futuro dos investimentos, 
    validando se o valor projetado e o total de investimentos futuros estão corretos.
    '''
    client = codigo.Client("Elara")
    investment1 = codigo.Investment("Ações", 1000.00, 0.1, 2020)
    investment2 = codigo.Investment("CDB", 5000.00, 0.06, 2021)
    client.add_investment(investment1)
    client.add_investment(investment2)

    future_date = datetime(2030, 12, 31)
    report = codigo.future_value_report(client, future_date)
    assert "Relatório de Projeção de Rendimentos Futuros para Elara" in report
    assert "Valor futuro em 31/12/2030" in report
    assert "Valor total dos investimentos futuros" in report


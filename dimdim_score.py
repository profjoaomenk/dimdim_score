#!/usr/bin/env python3
"""
DimDim Bank - Sistema de Pontuação de Clientes
Versão inicial - Calcula a pontuação baseada nas transações mensais
"""

def calcula_pontuacao(cliente):
    """
    Calcula a pontuação básica de um cliente
    
    Args:
        cliente (dict): Dicionário com dados do cliente
            - nome (str): Nome do cliente
            - transacoes (int): Número de transações mensais
    
    Returns:
        int: Pontuação calculada (transações * 10)
    """
    return cliente['transacoes'] * 10

def main():
    """Função principal para demonstrar o sistema"""
    print("DimDim Bank - Sistema de Pontuação")
    print("=" * 40)
    
    # Dados de exemplo dos clientes
    clientes = [
        {'nome': 'Ana Silva', 'transacoes': 6, 'vip': False},
        {'nome': 'Bruno Santos', 'transacoes': 8, 'vip': True},
        {'nome': 'Carla Oliveira', 'transacoes': 12, 'vip': True},
        {'nome': 'Daniel Costa', 'transacoes': 3, 'vip': False}
    ]
    
    print("Pontuação dos Clientes:")
    for cliente in clientes:
        pontos = calcula_pontuacao(cliente)
        print(f"• {cliente['nome']}: {pontos} pontos")

if __name__ == "__main__":
    main()

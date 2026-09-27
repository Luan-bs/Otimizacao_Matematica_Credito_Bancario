"""Ponto de entrada do projeto de otimização de crédito bancário."""

try:
    from .modelo import executar_analise_completa
except ImportError:  # Execução direta via python src/main.py
    from modelo import executar_analise_completa


def main() -> None:
    """Executa a análise completa do modelo de alocação ótima."""
    executar_analise_completa()


if __name__ == "__main__":
    main()
"""Modelo de programação linear para alocação ótima de crédito."""

from __future__ import annotations

from typing import Any

import numpy as np
from scipy.optimize import linprog


def definir_modelo() -> dict[str, Any]:
    """Constroi o modelo de programação linear para a carteira de crédito."""
    nomes_variaveis = [
        "X1 (Empréstimos Pessoais)",
        "X2 (Pensionistas)",
        "X3 (PMEs)",
        "X4 (Admin/Funcionários)",
        "X5 (Adiantamento/Cheque Especial)",
    ]

    lucro_liquido = np.array([0.225, 0.22, 0.235, 0.20, 0.23])
    orcamento_total = 5_000_000.0

    c = -lucro_liquido

    A_ub: list[list[float]] = []
    b_ub: list[float] = []

    A_ub.append([1, 1, 1, 1, 1])
    b_ub.append(orcamento_total)

    A_ub.append([-0.015, -0.01, -0.005, -0.01, 0])
    b_ub.append(0.0)

    A_ub.extend(
        [
            [0.55, -0.45, -0.45, -0.45, -0.45],
            [-0.45, 0.55, -0.45, -0.45, -0.45],
            [-0.45, -0.45, 0.55, -0.45, -0.45],
            [-0.45, -0.45, -0.45, 0.55, -0.45],
            [-0.45, -0.45, -0.45, -0.45, 0.55],
        ]
    )
    b_ub.extend([0.0, 0.0, 0.0, 0.0, 0.0])

    A_ub.append([0, 0.25, -1, 0.25, -1])
    b_ub.append(0.0)

    bounds = [(0, None) for _ in range(5)]

    return {
        "nomes_variaveis": nomes_variaveis,
        "c": c,
        "A_ub": A_ub,
        "b_ub": b_ub,
        "bounds": bounds,
    }


def resolver_modelo(modelo: dict[str, Any], c: np.ndarray | None = None):
    """Resolve o problema de maximização via programação linear."""
    c_usado = modelo["c"] if c is None else c
    resultado = linprog(
        c_usado,
        A_ub=modelo["A_ub"],
        b_ub=modelo["b_ub"],
        bounds=modelo["bounds"],
        method="highs",
    )

    if not resultado.success:
        raise RuntimeError(f"Otimização falhou: {resultado.message}")

    return resultado


def exibir_solucao_otima(modelo: dict[str, Any], resultado) -> None:
    """Exibe a solução ótima do modelo."""
    print("=== SOLUÇÃO ÓTIMA ===")
    for nome, valor in zip(modelo["nomes_variaveis"], resultado.x):
        print(f"{nome}: GH¢ {valor:,.2f}")
    print(f"\nLucro Máximo (P): GH¢ {-resultado.fun:,.2f}\n")


def analise_dualidade(resultado) -> None:
    """Exibe os preços-sombra da solução ótima."""
    print("=== PREÇOS-SOMBRA (DUALIDADE) ===")
    marginais = resultado.ineqlin.marginals
    for i, y_val in enumerate(marginais):
        valor_limpo = 0.0 if abs(y_val) < 1e-10 else abs(y_val)
        print(f"Y{i + 1}: {valor_limpo:.3f}".replace(".", ","))
    print(f"Solução ótima: GH¢ {-resultado.fun:,.2f}\n")


def analise_sensibilidade(modelo: dict[str, Any]) -> None:
    """Executa análise de sensibilidade paramétrica nos lucros."""
    print("=== SENSIBILIDADE (VARIAÇÃO NO LUCRO) ===")
    variacoes = [-0.30, -0.20, -0.10, -0.05, 0.0, 0.05, 0.10, 0.20, 0.30]

    for var in variacoes:
        c_cenario = modelo["c"] * (1 + var)
        resultado_cenario = resolver_modelo(modelo, c=c_cenario)
        print(
            f"{var * 100:+.0f}%: GH¢ {-resultado_cenario.fun:,.2f}".replace(
                ".", ","
            )
        )


def executar_analise_completa() -> None:
    """Executa a solução, dualidade e análise de sensibilidade."""
    modelo = definir_modelo()
    resultado = resolver_modelo(modelo)
    exibir_solucao_otima(modelo, resultado)
    analise_dualidade(resultado)
    analise_sensibilidade(modelo)


if __name__ == "__main__":
    executar_analise_completa()

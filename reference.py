"""AI-assisted synthetic feasibility arithmetic; not author-code reproduction."""
import json
import math

def minimum_cost(costs, lower):
    if len(costs) != len(lower) or not costs:
        raise ValueError("Costs and lower bounds must be nonempty and the same length")
    if not all(math.isfinite(c) and c > 0 for c in costs):
        raise ValueError("Costs must be finite and positive")
    if not all(math.isfinite(x) and x >= 0 for x in lower):
        raise ValueError("Lower bounds must be finite and nonnegative")
    return sum(c*x for c, x in zip(costs, lower))

CASES = [
    ("two-minimums-budget-one", [1,1], [2,2], 1, 4, False),
    ("boundary-feasible", [1,1], [2,2], 4, 4, True),
    ("zero-lower-bounds", [1,1], [0,0], 1, 0, True),
    ("unequal-costs", [1,3], [2,2], 7, 8, False),
    ("four-layers", [3, 1/2, 2, 4], [1, 1, 2, 1], 12, 11.5, True)
]
if __name__ == "__main__":
    rows = []
    for name, costs, lower, budget, expected_min, expected_feasible in CASES:
        result = minimum_cost(costs, lower)
        feasible = budget >= result
        assert result == expected_min and feasible == expected_feasible
        rows.append({"case": name, "costs": costs, "lower": lower, "budget": budget,
                     "minimum_cost": result, "inequality_domain_feasible": feasible})
    alpha, lam, cost = 1, 3, 2
    assert (alpha+lam)*cost == 8
    assert alpha+lam*cost == 7
    print(json.dumps({"cases": rows, "denominator_example": {
        "alpha": alpha, "lambda": lam, "cost": cost,
        "(alpha+lambda)*cost": (alpha+lam)*cost,
        "alpha+lambda*cost": alpha+lam*cost},
        "scope": "synthetic algebra; source commit and author code not verified here"}, indent=2))



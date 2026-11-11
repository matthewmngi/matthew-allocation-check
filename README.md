# Matthew — allocation domain decision check
**Total cap: 60 minutes, within the agreed two-hour total ceiling.** This is a bounded algebra/documentation task. The previously held author-code implementation and compute work remain on hold.

Run `python3 reference.py` with Python 3.10+ and no dependencies.

## What this establishes
For positive unit costs c_i and lower bounds l_i, allocations e_i >= l_i can obey sum(c_i*e_i) <= B only if B >= sum(c_i*l_i). For this simple domain, that condition is also sufficient: e=l is a witness. An equality budget is also attainable for continuous allocations with no upper bounds. Integer allocations can have additional restrictions, which this check does not resolve.

Worked cases (explicitly constructed here):
- Two unit-cost layers, lower bound two each, B=1: minimum cost 4, infeasible.
- Same bounds, B=4: e=[2,2] is feasible.
- Lower bound zero, B=1: e=[0,0] satisfies an inequality budget, e=[1,0] satisfies equality.
- Costs [1,3], lower bounds [2,2], B=7: minimum cost 8, infeasible.

The arithmetic also shows (alpha+lambda)*c and alpha+lambda*c differ: alpha=1, lambda=3, c=2 gives 8 and 7. Which expression belongs in a particular derivation requires its exact objective and variable definitions.

## Source status and task
Your existing November 5 PDF, `Matthew_Allocation_Source_Review_2026-11-05.pdf`, reported a paper/code domain and denominator mismatch. This new package does not contain that source PDF, does not reconstruct its pinned commit, and has not executed the authors' code. Treat its earlier mapping as a claim to check, not an established code defect.

Spend about 15 minutes running/reviewing these four cases and 15 minutes adding one case of your own with a hand-computed minimum. Use up to 30 minutes to write a short decision note: state why the target must specify continuous versus integer allocation, lower bounds, costs, inequality versus equality budget, and how infeasible inputs should be rejected before root-finding. If the earlier PDF is at hand, optionally cite the exact equation/function/commit it names; if not, write 'source not verified' and stop. No fresh search or implementation is required.

## Acceptance rubric and return
Return the output and at most 250 words. Your new case must match a hand computation. Explicitly distinguish this domain precheck from bisection convergence, author-code reproduction, rounded-allocation optimality, and language-model results. Do not spend Modal credits or start solver/author-code implementation.

Actual contributions may use the already agreed credit, 'Implementation and reproducibility checks: Matthew Mungai', only to the extent work actually completed supports it and with permission before public use. Paper authorship remains separate.

## Review and boundaries
This starter was prepared with AI assistance. The supplied checks provide an executable first pass; they are not independent human technical review. Ryan can coordinate receipt and an AI-assisted comparison against the stated rubric. No named technical reviewer or review date has been confirmed. A human technical review is still required before extending this into the previously held experiments, public scientific claims, or a release. Use only the supplied synthetic/reference material, your own laptop CPU, and standard Python. No accounts, network, paid compute, private data, or spending are needed. Stop at the time cap; a precise blocker report is a valid handoff. This is voluntary, and the starter is not a new application or sample request. Only your actual changes and findings should be credited to you.


## Agreement before starting
If this small scope and AI-assisted first-pass review suit you, please reply to accept them and suggest a comfortable handoff day; you can then start this checkpoint. If you prefer to wait for a human reviewer, no extra work is due.

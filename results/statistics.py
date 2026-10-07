import pandas

PERF = "perf"
SOUND = "sound"

STANDARD_OUTCOMES = ["SAT", "UNSAT", "UNKNOWN"]
ERR_OUTCOMES = ["ERR_ENCODING", "ERR_NUNCHAKU"]
SOLVERS = {"cvc5": "cvc5", "smbc": "SMBC", "kodkod": "Kodkod"}

# Result whose rows are not counted towards the per-solver columns
SOLVER_EXCLUDED_RESULT = {PERF: "UNSAT", SOUND: "SAT"}

HEADERS = ["Theory", "Problems", "SAT", "UNSAT", "Unknown", "Error"] + list(SOLVERS.values())

TABLE_META = {
    SOUND: ("Chako's results on correct theorem statements", "tab:exp1"),
    PERF: ("Chako's results on mutated theorem statements", "tab:exp2"),
}

AGGREGATOR = {
    "Array": ["array_basic.csv", "array_lemmas.csv"],
    "BitVec": ["bitvec_basic.csv", "bitvec_lemmas.csv"],
    "Fin": ["fin_basic.csv", "fin_lemmas.csv"],
    "Int": ["int_basic.csv", "int_lemmas.csv"],
    "List": ["list_basic.csv", "list_lemmas.csv"],
    "Nat": ["nat_basic.csv", "nat_lemmas.csv"],
    "Option": ["option_basic.csv", "option_lemmas.csv"],
    "Nat.Gcd": ["nat_gcd.csv"],
    "TreeMap": ["treemap_lemmas.csv"],
}

def load_data(dir_name: str):
    theories = {}
    for (theory, paths) in AGGREGATOR.items():
        dfs = []
        for path in paths:
            df = pandas.read_csv(f"{dir_name}/{path}")
            dfs.append(df)
        theories[theory] = pandas.concat(dfs)
    return theories

def count_stats(data, excluded_result: str):
    """Return problem count and per-column hit counts, keyed like HEADERS[1:]."""
    counts = [len(data)]
    for outcome in STANDARD_OUTCOMES:
        counts.append(int((data["result"] == outcome).sum()))
    counts.append(int(data["result"].isin(ERR_OUTCOMES).sum()))
    included = data["result"] != excluded_result
    for solver in SOLVERS:
        solved = data[solver].astype(str).str.lower() == "true"
        counts.append(int((solved & included).sum()))
    return counts

def fmt_percent(num: int, total: int) -> str:
    s = f"{num / total * 100:.1f}"
    if len(s) == 3:
        s = r"\phantom{0}" + s
    elif len(s) == 5:
        s = rf"\llap{{{s[0]}}}{s[1:]}"
    return s + r"\%"

def phantom(n: int) -> str:
    return rf"\phantom{{{'0' * n}}}" if n > 0 else ""

def analyze_dir(prefix: str):
    theories = load_data(prefix)
    rows = [(theory, count_stats(data, SOLVER_EXCLUDED_RESULT[prefix])) for (theory, data) in theories.items()]
    totals = [sum(col) for col in zip(*(counts for (_, counts) in rows))]
    total = totals[0]

    row_width = max(len(str(counts[0])) for (_, counts) in rows)
    total_pad = max(0, len(str(total)) - row_width)

    print(rf"\newcommand{{\{prefix}NumTotal}}{{{total}}}")
    print()

    caption, label = TABLE_META[prefix]
    lines = [
        r"\begin{table}[tb]",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\maybecentering",
        r"\begin{tabular}{@{}l" + r"@{\enskip}c" * (len(HEADERS) - 1) + "@{}}",
        r"\toprule",
        " & ".join(HEADERS) + r" \\",
        r"\midrule",
    ]
    for (i, (theory, counts)) in enumerate(rows):
        n = counts[0]
        cells = [rf"\cst{{{theory}}}", phantom(row_width - len(str(n))) + str(n)]
        cells += [fmt_percent(c, n) for c in counts[1:]]
        end = r" \\[\jot]" if i == len(rows) - 1 else r" \\"
        lines.append(" & ".join(cells) + end)

    cells = ["Total", str(total) + phantom(total_pad)]
    cells += [fmt_percent(c, total) for c in totals[1:]]
    lines.append(" & ".join(cells) + r" \\")
    lines += [
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]
    print("\n".join(lines))
    print()

def main():
    analyze_dir(PERF)
    analyze_dir(SOUND)

if __name__ == "__main__":
    main()

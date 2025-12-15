import pandas
from matplotlib import pyplot as plt
import glob
from dataclasses import dataclass

PERF = "perf"
SOUND = "sound"

STANDARD_OUTCOMES = ["SAT", "UNSAT", "UNKNOWN", ]
ERR_OUTCOMES = ["ERR_ENCODING", "ERR_NUNCHAKU"]

TABLE_HEADER = \
"""table(
  columns: (auto, auto, auto, auto, auto, auto),
  align: (left, right, right, right, right, right),
  stroke: (x, y) => (
    right: if (x == 0) or (x == 4) { 1pt } else { none },
    top: if y > 0 { 1pt } else { none }
  ),
  table.header(
    [*Theory*], [*SAT*], [*UNSAT*], [*Unknown*], [*Error*], [*Problems*],
  ),
"""

TABLE_FOOTER = \
"""
)
"""

AGGREGATOR = {
    "Array": ["array_basic.csv", "array_lemmas.csv"],
    "BitVec": ["bitvec_basic.csv", "bitvec_lemmas.csv"],
    "Fin": ["fin_basic.csv", "fin_lemmas.csv"],
    "Int": ["int_basic.csv", "int_lemmas.csv"],
    "List": ["list_basic.csv", "list_lemmas.csv"],
    "Nat": ["nat_basic.csv", "nat_lemmas.csv"],
    "Option": ["option_lemmas.csv"],
    "Nat.Gcd": ["nat_gcd.csv"],
    "Option": ["option_basic.csv", "option_lemmas.csv"],
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

def analyze_dir(prefix: str):
    theories = load_data(prefix)
    total = sum(map(len, theories.values()))
    print(f"#let {prefix}_num_total = {total}")
    table = TABLE_HEADER
    total_outcomes = {}
    for (theory, data) in theories.items():
        table += f"  `{theory}`, "
        theory_total = len(data)
        for outcome in STANDARD_OUTCOMES:
            num_outcome = len(data[data["result"] == outcome])
            percent = round((float(num_outcome) / theory_total) * 100, 1)
            table += f"[${percent}%$], "
            total_outcomes[outcome] = total_outcomes.get(outcome, 0) + num_outcome

        num_errors = 0
        for error in ERR_OUTCOMES:
            num_outcome = len(data[data["result"] == error])
            num_errors += num_outcome
        percent = round((float(num_errors) / theory_total) * 100, 1)
        table += f"[${percent}%$], "
        total_outcomes["ERROR"] = total_outcomes.get("ERROR", 0) + num_errors

        table += f"${theory_total}$, "

        table += "\n"

    table += "  [*Total*], "
    for outcome in STANDARD_OUTCOMES:
        num_outcome = total_outcomes[outcome]
        percent = round((float(num_outcome) / total) * 100, 1)
        table += f"[${percent}%$], "

    num_outcome = total_outcomes["ERROR"]
    percent = round((float(num_outcome) / total) * 100, 1)
    table += f"[${percent}%$], "
    table += f"${total}$, "

    table += TABLE_FOOTER
    print(f"#let {prefix}_table = {table}")



def main():
    analyze_dir(PERF)
    analyze_dir(SOUND)

if __name__ == "__main__":
    main()

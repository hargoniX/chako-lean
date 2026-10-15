import Chako
import Std

set_option Elab.async false
set_option maxHeartbeats 200000000

#eval_chako_perf_module Init.Data.Array.Basic "results/artefacts/perf/array_basic.csv"
#eval_chako_perf_module Init.Data.Array.Lemmas "results/artefacts/perf/array_lemmas.csv"

#eval_chako_perf_module Init.Data.BitVec.Basic "results/artefacts/perf/bitvec_basic.csv"
#eval_chako_perf_module Init.Data.BitVec.Lemmas "results/artefacts/perf/bitvec_lemmas.csv"

#eval_chako_perf_module Init.Data.Fin.Basic "results/artefacts/perf/fin_basic.csv"
#eval_chako_perf_module Init.Data.Fin.Lemmas "results/artefacts/perf/fin_lemmas.csv"

#eval_chako_perf_module Init.Data.Int.Basic "results/artefacts/perf/int_basic.csv"
#eval_chako_perf_module Init.Data.Int.Lemmas "results/artefacts/perf/int_lemmas.csv"

#eval_chako_perf_module Init.Data.List.Basic "results/artefacts/perf/list_basic.csv"
#eval_chako_perf_module Init.Data.List.Lemmas "results/artefacts/perf/list_lemmas.csv"

#eval_chako_perf_module Init.Data.Nat.Basic "results/artefacts/perf/nat_basic.csv"
#eval_chako_perf_module Init.Data.Nat.Lemmas "results/artefacts/perf/nat_lemmas.csv"
#eval_chako_perf_module Init.Data.Nat.Gcd "results/artefacts/perf/nat_gcd.csv"

#eval_chako_perf_module Init.Data.Option.Basic "results/artefacts/perf/option_basic.csv"
#eval_chako_perf_module Init.Data.Option.Lemmas "results/artefacts/perf/option_lemmas.csv"

#eval_chako_perf_module Std.Data.TreeMap.Lemmas "results/artefacts/perf/treemap_lemmas.csv"

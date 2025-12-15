import Chako
import Std

set_option Elab.async false
set_option maxHeartbeats 200000000
#exit
#eval_chako_perf_module Init.Data.Array.Basic "results/perf/array_basic.csv"
#eval_chako_perf_module Init.Data.Array.Lemmas "results/perf/array_lemmas.csv"

#eval_chako_perf_module Init.Data.BitVec.Basic "results/perf/bitvec_basic.csv"
#eval_chako_perf_module Init.Data.BitVec.Lemmas "results/perf/bitvec_lemmas.csv"

#eval_chako_perf_module Init.Data.Fin.Basic "results/perf/fin_basic.csv"
#eval_chako_perf_module Init.Data.Fin.Lemmas "results/perf/fin_lemmas.csv"

#eval_chako_perf_module Init.Data.Int.Basic "results/perf/int_basic.csv"
#eval_chako_perf_module Init.Data.Int.Lemmas "results/perf/int_lemmas.csv"

#eval_chako_perf_module Init.Data.List.Basic "results/perf/list_basic.csv"
#eval_chako_perf_module Init.Data.List.Lemmas "results/perf/list_lemmas.csv"

#eval_chako_perf_module Init.Data.Nat.Basic "results/perf/nat_basic.csv"
#eval_chako_perf_module Init.Data.Nat.Lemmas "results/perf/nat_lemmas.csv"
#eval_chako_perf_module Init.Data.Nat.Gcd "results/perf/nat_gcd.csv"

#eval_chako_perf_module Init.Data.Option.Basic "results/perf/option_basic.csv"
#eval_chako_perf_module Init.Data.Option.Lemmas "results/perf/option_lemmas.csv"

#eval_chako_perf_module Std.Data.TreeMap.Lemmas "results/perf/treemap_lemmas.csv"

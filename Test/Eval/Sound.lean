import Chako
import Std

set_option Elab.async false
set_option maxHeartbeats 200000000
#exit
#eval_chako_sound_module Init.Data.Array.Basic "results/sound/array_basic.csv"
#eval_chako_sound_module Init.Data.Array.Lemmas "results/sound/array_lemmas.csv"

#eval_chako_sound_module Init.Data.BitVec.Basic "results/sound/bitvec_basic.csv"
#eval_chako_sound_module Init.Data.BitVec.Lemmas "results/sound/bitvec_lemmas.csv"

#eval_chako_sound_module Init.Data.Fin.Basic "results/sound/fin_basic.csv"
#eval_chako_sound_module Init.Data.Fin.Lemmas "results/sound/fin_lemmas.csv"

#eval_chako_sound_module Init.Data.Int.Basic "results/sound/int_basic.csv"
#eval_chako_sound_module Init.Data.Int.Lemmas "results/sound/int_lemmas.csv"

#eval_chako_sound_module Init.Data.List.Basic "results/sound/list_basic.csv"
#eval_chako_sound_module Init.Data.List.Lemmas "results/sound/list_lemmas.csv"

#eval_chako_sound_module Init.Data.Nat.Basic "results/sound/nat_basic.csv"
#eval_chako_sound_module Init.Data.Nat.Lemmas "results/sound/nat_lemmas.csv"
#eval_chako_sound_module Init.Data.Nat.Gcd "results/sound/nat_gcd.csv"

#eval_chako_sound_module Init.Data.Option.Basic "results/sound/option_basic.csv"
#eval_chako_sound_module Init.Data.Option.Lemmas "results/sound/option_lemmas.csv"

#eval_chako_sound_module Std.Data.TreeMap.Lemmas "results/sound/treemap_lemmas.csv"

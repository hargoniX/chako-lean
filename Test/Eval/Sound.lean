import Chako
import Std

set_option Elab.async false
set_option maxHeartbeats 200000000

#eval_chako_sound_module Init.Data.Array.Basic "results/artefacts/sound/array_basic.csv"
#eval_chako_sound_module Init.Data.Array.Lemmas "results/artefacts/sound/array_lemmas.csv"

#eval_chako_sound_module Init.Data.BitVec.Basic "results/artefacts/sound/bitvec_basic.csv"
#eval_chako_sound_module Init.Data.BitVec.Lemmas "results/artefacts/sound/bitvec_lemmas.csv"

#eval_chako_sound_module Init.Data.Fin.Basic "results/artefacts/sound/fin_basic.csv"
#eval_chako_sound_module Init.Data.Fin.Lemmas "results/artefacts/sound/fin_lemmas.csv"

#eval_chako_sound_module Init.Data.Int.Basic "results/artefacts/sound/int_basic.csv"
#eval_chako_sound_module Init.Data.Int.Lemmas "results/artefacts/sound/int_lemmas.csv"

#eval_chako_sound_module Init.Data.List.Basic "results/artefacts/sound/list_basic.csv"
#eval_chako_sound_module Init.Data.List.Lemmas "results/artefacts/sound/list_lemmas.csv"

#eval_chako_sound_module Init.Data.Nat.Basic "results/artefacts/sound/nat_basic.csv"
#eval_chako_sound_module Init.Data.Nat.Lemmas "results/artefacts/sound/nat_lemmas.csv"
#eval_chako_sound_module Init.Data.Nat.Gcd "results/artefacts/sound/nat_gcd.csv"

#eval_chako_sound_module Init.Data.Option.Basic "results/artefacts/sound/option_basic.csv"
#eval_chako_sound_module Init.Data.Option.Lemmas "results/artefacts/sound/option_lemmas.csv"

#eval_chako_sound_module Std.Data.TreeMap.Lemmas "results/artefacts/sound/treemap_lemmas.csv"

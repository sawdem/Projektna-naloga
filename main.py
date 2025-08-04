import pobiranje_podatkov as pob
import filtriranje as filt

pob.pobiranje_podatkov()

filt.monster_to_csv(filt.izlusci_podatke_monster())

filt.spell_and_trap_to_csv(filt.izlusci_podatke_trap_in_spell())

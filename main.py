from Deck import Deck
from Elixir import Elixir
from tacticaboba import TacticaBoba
from tacticabobaIzquierda import TacticaBobaIzquierda


deck  = Deck()
elixir = Elixir()
tactica = TacticaBoba(deck, elixir)
tactica = TacticaBobaIzquierda(deck, elixir)

tactica.jugar()



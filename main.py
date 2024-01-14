from Deck import Deck
from Elixir import Elixir
from Tactics.TacticaBoba import TacticaBoba

deck  = Deck()
elixir = Elixir()
tactica = TacticaBoba(deck, elixir)

tactica.play()



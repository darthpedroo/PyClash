from Deck import Deck
from Elixir import Elixir
from Gui import Gui

from Tactics.TacticaBoba import TacticaBoba

deck  = Deck()
elixir = Elixir()
gui = Gui()
tactica = TacticaBoba(deck, elixir,gui)

tactica.play()



#One Night in Karazhan Set

def All():
  Cards=Minions()
  Cards+=Spells()
  Cards+=Weapons()
  return Cards

def Minions():
  #[class,mana cost,attack,health,text,tribe,name,rarity]
  Cards=[["Neutral",1,0,2,"Deathrattle: Draw a card.","","Runic Egg","Common"],
         ["Neutral",1,2,1,"Whenever you cast a spell, give this minion +1 Health.","","Arcane Anomaly","Common"],
         ["Neutral",2,3,2,"Taunt","","Pompous Thespian","Common"],
         ["Neutral",2,1,3,"Battlecry: If you're holding a Dragon, Discover a Dragon.","","Netherspite Historian","Common"],
         ["Neutral",3,3,3,"Battlecry: Give a random friendly Beast, Dragon, and Murloc +1/+1.","Mech","Zoobot","Common"],
         ["Neutral",3,4,3,"During your turn, your hero is Immune.","","Violet Illusionist","Common"],
         ["Neutral",3,1,3,"Battlecry: Summon a 1/3 Spider.","Beast","Pantry Spider","Common"],
         ["Neutral",3,1,1,"Stealth. At the end of your turn, summon a 1/1 Steward.","","Moroes","Legendary"],
         ["Neutral",4,3,4,"Battlecry: Summon a 1/1 copy of a random minion in yout deck.","","Barnes","Legendary"],
         ["Neutral",4,3,2,"Battlecry: Summon a 0/5 minion with Taunt.","","Arcanosmith","Common"],
         ["Neutral",5,5,6,"When the game starts, add 5 extra Legendary minions to your deck.","Demon","Prince Malchezaar","Legendary"],
         ["Neutral",5,4,4,"Battlecry: Give a random friendly Beast, Dragon, and Murloc +2/+2.","","Menagerie Magician","Common"],
         ["Neutral",5,3,6,"Battlecry: If you control a Secret, gain +1/+1 and Taunt.","","Avian Watcher","Rare"],
         ["Neutral",6,3,3,"Battlecry: Destroy a minion. Deathrattle: Resummon it.","","Moat Lurker","Rare"],
         ["Neutral",6,3,6,"Battlecry: If you're holding a Dragon, destroy an enemy minion with 3 or less Attack.","Dragon","Book Wyrm","Rare"],
         ["Neutral",7,4,6,"Taunt. Battlecry: draw a Beast, Dragon, and Murloc from your deck.","Mech","The Curator"],
         ["Neutral",8,7,7,"Battlecry: Equip Atiesh Greatstaff of the Guardian.","","Medivh, the Guardian","Legendary"],
         ["Neutral",12,8,8,"Costs (1) less for each spell you've cast this game.","","Arcane Giant","Epic"],
         ["Druid",1,2,2,"","Beast","Enchanted Raven","Common"],
         ["Druid",6,5,5,"Battlecry: Choose a friendly Beast. Summon a copy of it.","","Menagerie Warden","Common"],
         ["Hunter",2,1,1,"Deathrattle: Summon a 3/2 Big Bad Wolf.","Beast","Kindly Grandmother","Common"],
         ["Hunter",3,3,4,"Your Secrets cost (0).","","Cloaked Huntress","Common"],
         ["Mage",1,1,1,"Battlecry: Add a random Mage Spell to your hand.","","Babbling Book","Rare"],
         ["Mage",2,2,3,"Battlecry: If you control a Secret, deal 3 damage.","","Medivh's Valet","Common"],
         ["Paladin",3,2,3,"Battlecry: If you're holding a Dragon, summon two 1/1 Whelps.","","Nightbane Templar","Common"],
         ["Paladin",6,4,4,"Battlecry: Discover a spell. Restore ealth to your hero equal to its Cost.","","Ivory Knight","Rare"],
         ["Priest",4,3,6,"Whenever you cast a spell, restore 3 Health to your hero.","","Priest of the Feast","Common"],
         ["Priest",5,3,4,"Battlecry: Summon a friendly minion that died this game.","","Onyx Bishop","Rare"],
         ["Rogue",1,1,1,"Battlecry: Add a random class card to your hand (from your opponent's class).","Pirate","Swashburglar","Common"],
         ["Rogue",3,3,2,"Deathrattle: Add a 3/2 weapon to your hand.","","Deadly Fork","Common"],
         ["Rogue",5,5,6,"Battlecry: Reduce the Cost of cards in your hand from other classes by (2).","Ethereal Peddler","Rare"],
         ["Shaman",4,3,4,"Whenever you cast a spell, summon a random basic Totem.","","Wicked Witchdoctor","Common"],
         ["Warlock",1,1,3,"Whenever you discard a card, draw a card.","Demon","Melchezaar's Imp","Common"],
         ["Warlock",3,3,3,"If you discard this minion, summon it.","","Silverware Golem","Rare"]
    ]
  return Cards

def Spells():
  #[class,mana cost,text,name,rarity]
  Cards=[["Druid",6,"Restore 6 Health. Summon a random 6-Cost minion.","Moonglade Portal","Rare"],
         ["Hunter",2,"Secret After your opponent casts a spell, summon a 4/2 Panther with Stealth.","Cat Trick","Rare"],
         ["Mage",7,"Deal 5 damage. Summon a random 5-Cost minion.","Firelands Portal","Common"],
         ["Paladin",4,"Give a minion +2/+2. Summon a random 2-Cost minion.","Silvermoon Portal","Common"],
         ["Priest",2,"Silence a friendly minion. Draw a card.","Common"],
         ["Shaman",2,"Deal 1 damage to all enemy minions. Summon a random 1-Cost minion.","Maelstrom Portal","Rare"],
         ["Warlock",5,"Summon a 1/1 Candle, 2/2 Broom and 3/3 Teapot.","Kara Kazham!","Common"],
         ["Warrior",3,"For each enemy minion, summon a 1/1 Pawn with Taunt.","Protect the King","Rare"],
         ["Warrior",5,"Gain 4 Armor. Summon a random 4-Cost minion.","Ironforge Portal","Common"]
    ]
  return Cards

def Weapons():
  #[class,mana cost,attack,durability,text,name,rarity]
  Cards=[["Shaman",1,1,3,"Has +2 Attack while you have Spell Damage.","Spirit Claws","Common"],
         ["Warrior",5,3,4,"Unlimited attacks each turn. Can't attack heroes.","Fool's Bane","Common"]
    ]
  return Cards

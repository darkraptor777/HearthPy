#Blackrock Mountain Set

def All():
  Cards=Minions()
  Cards+=Spells()
  Cards+=Weapons()
  return Cards


def Minions():
  #[class,mana cost,attack,health,text,tribe,name,rarity]
  Cards=[["Neutral",1,0,2,"Whenever this minion takes damage, summon a 2/1 Whelp.","","Dragon Egg","Rare"],
         ["Neutral",3,2,4,"Battlecry: If you're holding a Dragon, gain +1/+1.","","Blackwing Technician","Common"],
         ["Neutral",4,5,6,"Battlecry: Summon a random 1-Cost minion for your opponent.","Dragon","Hungry Dragon","Common"],
         ["Neutral",4,3,5,"Whenever you target this minion with a spell, gain +1/+1.","Dragon","Dragonkin Sorcerer","Common"],
         ["Neutral",5,3,3,"Whenever this minion survives damage, summon another Grim Patron.","","Grim Patron","Rare"],
         ["Neutral",5,5,4,"Battlecry: If you're holding a Dragon, deal 3 damage.","","Blackwing Corruptor","Common"],
         ["Neutral",6,6,4,"Costs (1) less for each minion that died this turn.","Dragon","Volcanic Drake","Common"],
         ["Neutral",6,5,5,"At the end of your turn, reduce the Cost of cards in your hand by (1).","","Emperor Thaurissan","Legendary"],
         ["Neutral",6,6,6,"Battlecry: If your opponent has 15 or less Health, gain +3/+3.","Dragon","Drakonid Crusher","Common"],
         ["Neutral",7,8,4,"Battlecry: If you're holding a Dragon, destroy a Legendary minion.","","Rend Blackhand","Legendary"],
         ["Neutral",8,6,8,"Whenever you draw a card, put another copy into your hand.","Dragon","Chromaggus","Legendary"],
         ["Neutral",9,8,8,"Battlecry: Add 2 random spells to your hand (from your opponent's class).","Dragon","Nefarian","Legendary"],
         ["Neutral",9,9,7,"Deathrattle: Replace your hero with Ragnaros, the Firelord.","","Majordomo Executus","Legendary"],
         ["Druid",3,2,2,"Choose One- Transform into a 5/2 minion; or a 2/5 minion.","","Druid of the Flame","Common"],
         ["Druid",9,7,8,"Taunt. Costs (1) less for each minion that died this turn.","","Volcanic Lumberer","Rare"],
         ["Hunter",4,4,4,"Battlecry: If your hand is empty, gain +3/+3.","Beast","Core Rager","Rare"],
         ["Mage",3,2,4,"After you cast a spell, deal 2 damage randomly split among all enemies.","","Flamewaker","Rare"],
         ["Paladin",5,5,5,"Battlecry: The next Dragon you play costs (2) less.","Dragon","Dragon Consort","Rare"],
         ["Priest",1,2,1,"Battlecry: If you're holding a Dragon, gain +2 Health.","Dragon","Twilight Whelp","Common"],
         ["Rogue",5,4,3,"Battlecry: Deal 2 damage to all undamaged enemy minions.","","Dark Iron Skulker","Rare"],
         ["Shaman",4,3,6,"Battlecry: Gain 1-4 Attack. Overload: (1)","","Fireguard Destroyer","Common"],
         ["Warlock",3,2,4,"Whenever this minion takes damage, summon a 1/1 Imp.","Demon","Imp Gang Boss","Common"],
         ["Warrior",4,2,5,"Whenever this minion takes damage, deal 2 damage to the enemy hero.","","Axe Flinger","Common"]
    ]
  return Cards

def Spells():
  #[class,mana cost,text,name,rarity]
  Cards=[["Hunter",2,"Deal 3 damage. If your hand is empty, draw a card.","Quick Shot","Common"],
         ["Mage",5,"Deal 4 damage. Costs (1) less for ech minion that died this turn.","Dragon's Breath","Common"],
         ["Paladin",5,"Draw 2 cards. Costs (1) less for each minion that died this turn.","Solemn Vigil","Common"],
         ["Priest",2,"Summon a random minion that died this game.","Resurrect","Rare"],
         ["Rogue",2,"Choose a minion. Shuffle 3 copies of it into your deck.","Gang Up","Common"],
         ["Shaman",2,"Deal 2 damage. Unlock your Overloaded Mana Crystals.","Lava Shock","Rare"],
         ["Warlock",3,"Deal 2 damage to all non-Demon minions.","Demonwrath","Rare"],
         ["Warrior",2,"Deal 1 damage to all minions. If you have 12 or less Health, deal 3 damage instead.","Revenge","Rare"]
    ]
  return Cards

def Weapons():
  #[class,mana cost,attack,durability,text,name,rarity]
  Cards=[
    ]
  return Cards

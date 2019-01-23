#Naxxramus Set

def All():
  Cards=Minions()
  Cards+=Spells()
  Cards+=Weapons()
  return Cards

def Minions():
  #[class,mana cost,attack,health,text,tribe,name,rarity]
  Cards=[["Neutral",1,2,3,"Deathrattle: Restore 5 Health to the enemy hero.","","Zombie Chow","Common"],
         ["Neutral",1,1,2,"Whenever you summon a minion with Deathrattle, gain +1 Attack.","","Undertaker","Common"],
         ["Neutral",2,1,3,"Taunt. Deathrattle: Deal 1 damage to all minions.","","Unstable Ghoul","Common"],
         ["Neutral",2,0,2,"Deathrattle: Summon a 4/4 Nerubian.","","Nerubian Egg","Rare"],
         ["Neutral",2,1,4,"Minions with Battlecry cost (2) more.","","Nerub'ar Weblord","Common"],
         ["Neutral",2,2,2,"Deathrattle: Put a Secret from your deck into the battlefield.","","Mad Scientist","Common"],
         ["Neutral",2,1,2,"Deathrattle: Summon two 1/1 Spectral Spiders.","Beast","Haunted Creeper","Common"],
         ["Neutral",2,1,2,"Battlecry: Summon an exact copy of this minion at the end of the turn.","","Echoing Ooze","Epic"],
         ["Neutral",3,1,4,"At the start of your turn, restore this minion to full Health.","","Stoneskin Gargoyle","Common"],
         ["Neutral",3,2,2,"Stealth. At the start of your turn, gain +1/+1.","","Shade of Naxxramas","Epic"],
         ["Neutral",3,2,8,"Taunt. Deathrattle: Your opponent puts a minion from their deck into the battlefield.","","Deathlord","Rare"],
         ["Neutral",3,4,4,"Deathrattle: Your opponent draws a cards.","","Dancing Swords","Common"],
         ["Neutral",4,3,5,"Battlecry: Silence yout other minions.","","Wailing Soul","Rare"],
         ["Neutral",4,1,7,"Your minions trigger their Deathrattles twice.","","Baron Rivendare","Legendary"],
         ["Neutral",5,7,4,"Deathrattle: If Feugan also died this game, summon Thaddius.","","Stalagg","Legendary"],
         ["Neutral",5,4,6,"Can't be targeted by spells or Hero Powers.","","Spectral Knight","Common"],
         ["Neutral",5,3,5,"Taunt. Deathrattle: Summon a 1/2 Slime with Taunt.","","Sludge Belcher","Rare"],
         ["Neutral",5,5,5,"Battlecry: Enemy spells cost (5) more next turn.","","Loatheb","Legendary"],
         ["Neutral",5,4,7,"Deathrattle: If Stalagg also died this game, summon Thaddius.","","Feugen","Legendary"],
         ["Neutral",6,2,8,"Destroy any minion damaged by this minion.","Beast","Maexxna","Legendary"],
         ["Neutral",8,6,8,"At the end of each turn summon all friendly minions that died this turn.","","Kel'Thuzad"],
         ["Hunter",1,1,1,"Deathrattle: Add a random Beast card to your hand.","Beast","Webspinner","Common"],
         ["Priest",3,3,4,"Deathrattle: Give a random friendly minion +3 Health.","","Dark Cultist","Common"],
         ["Rogue",4,5,5,"Deathrattle: Return a random friendly minion to your hand.","","Anub'ar Ambusher","Common"],
         ["Warlock",4,3,4,"Deathrattle: Put a random Demon from your hand into the battlefield.","Demon","Voidcaller","Common"]
    ]
  return Cards

def Spells():
  #[class,mana cost,text,name,rarity]
  Cards=[["Druid",4,"Destroy all minions and summon 2/2 Treants to replace them.","Poison Seeds","Common"],
         ["Mage",3,"Secret: When a friendly minion dies, put 2 copies of it into your hand.","Duplicate","Common"],
         ["Paladin",1,"Secret: When one of your minions dies, give a random friendly minion +3/+2.","Avenge","Common"],
         ["Shaman",2,"Destroy a minion, then return it to life with with full Health.","Reincarnate","Common"]
    ]

  return Cards

def Weapons():
  #[class,mana cost,attack,durability,text,name,rarity]
  Cards=[["Warrior",4,4,2,"Deathrattle: Deal 1 damage to all minions.","Death's Bite","Common"]
    ]
  return Cards

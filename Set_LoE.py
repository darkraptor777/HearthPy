#League of Explorers Set

def All():
  Cards=Minions()
  Cards+=Spells()
  Cards+=Weapons()
  return Cards

def Minions():
  #[class,mana cost,attack,health,text,tribe,name,rarity]
  Cards=[["Neutral",0,1,1,"","Murloc","Murloc Tinyfin","Common"],
         ["Neutral",1,1,3,"Battlecry: Discover a new basic Hero Power.","Murloc","Sir Finley Mrrgglton","Legendary"],
         ["Neutral",2,1,1,"Battlecry: Discover a 3-Cost card.","Beast","Jeweled Scarab","Common"],
         ["Neutral",2,3,2,"Deathrattle: Deal 1 damage to a random enemy.","Beast","Huge Toad","Common"],
         ["Neutral",3,2,4,"Your Battlecries trigger twice.","","Brann Bronzebeard","Legendary"],
         ["Neutral",4,3,3,"Battlecry: Discover a Beast.","Beast","Tomb Spider","Common"],
         ["Neutral",4,3,4,"Battlecry: If you control another Mech, Discover a Mech.","Mech","Gorillabot A-3","Common"],
         ["Neutral",4,3,5,"Battlecry: Shuffle the 'Map to the Golden Monkey' into your deck.","","Elise Starseeker","Legendary"],
         ["Neutral",4,7,7,"Can't attack unless it's the only minion in the battlefield.","","Eerie Statue","Rare"],
         ["Neutral",4,7,4,"Battlecry: Shuffle an 'Ancient Curse' into your deck that deal 7 damage to you when drawn.","","Ancient Shade","Rare"],
         ["Neutral",5,0,6,"Whenever you cast a spell, summon a random minion of the same Cost.","","Summoning Stone","Rare"],
         ["Neutral",5,5,5,"Your cards cost(5).","","Naga Sea Witch","Epic"],
         ["Neutral",5,4,6,"After you cast a spell on another firendly minion, cast a s#copy of it on this one.","","Djinni of Zephyrs","Epic"],
         ["Neutral",5,4,4,"Deathrattle: Give a random friendly minion +3/+3.","","Anubisath Sentinel","Common"],
         ["Neutral",6,2,6,"Deathrattle: Summon three 2/2 Runts.","","Wobbling Runts","Rare"],
         ["Neutral",6,4,6,"Battlecry: If your deck contains no more than 1 of any card, fully heal your hero.","","Reno Jackson","Legendary"],
         ["Neutral",8,8,8,"Battlecry: If you control a Beast, gain Taunt.","","Fossilized Devilsaur","Common"],
         ["Neutral",9,7,8,"Battlecry: Discover a powerful Artifact.","","Arch-Thief Rafaam","Legendary"],
         ["Druid",3,3,2,"Deathrattle: Summon a random 1-Cost minion.","Beast","Mounted Raptor","Common"],
         ["Druid",4,4,4,"Both players have Spell Damage +2.","Beast","Jungle Moonkin","Rare"],
         ["Hunter",3,2,4,"Battlecry: Put a 1-Cost minion from each deck into the battlefield.","Beast","Desert Camel","Common"],
         ["Mage",4,4,4,"Your hero can only take 1 damage at a time.","","Animated Armor","Rare"],
         ["Mage",5,6,3,"Battlecry: Discover a spell.","","Ethereal Conjurer","Common"],
         ["Paladin",4,3,4,"Battlecry: Set a minion's Attack and Health to 3.","","Keeper of Uldaman","Common"],
         ["Priest",2,1,2,"Battlecry: Discover a Deathrattle card.","","Museum Curator","Common"],
         ["Rogue",1,2,1,"Destroy any minion damaged by this minion.","Beast","Pit Snake","Common"],
         ["Rogue",3,3,4,"Battlecry: Choose a friendly minion. Gain a copy of its Deathrattle effect.","","Unearthed Raptor","Rare"],
         ["Rogue",4,5,4,"Deathrattle: Add a Coin to your hand.","","Tomb Pillager","Common"],
         ["Shaman",1,1,3,"Whenever you Overload, gain +1 Attack per locked Mana Crystal.","","Tunnel Trogg","Common"],
         ["Shaman",4,2,6,"After you play a Battlecry minion, deal 2 damage to a random enemy.","","Rumbling Elemental","Common"],
         ["Warlock",1,1,1,"Battlecry: If you have 6 other minions, gain +4/+4.","","Reliquary Seeker","Rare"],
         ["Warlock",2,2,2,"Battlecry: Discover a 1-Cost card.","","Darl Peddler","Common"],
         ["Warrior",3,3,4,"Taunt","Beast","Fierce Monkey","Common"],
         ["Warrior",7,7,7,"At the end of your turn, summon a 1/1 Scarab with Taunt.","","Obsidian Destroyer","Common"]
    ]
  return Cards

def Spells():
  #[class,mana cost,text,name,rarity]
  Cards=[["Druid",1,"Choose One - Discover a minion; or Discover a spell.","Raven Idol","Common"],
         ["Hunter",2,'Give a minion +1/+1 and "Deathrattle: Add an Explorer'+"'s"+' Hat to your hand."',"Explorer's Hat","Rare"],
         ["Hunter",2,"Secret: After an opposing Hero Power is used, deal 5 damage to a random enemy.","Dart Trap","Common"],
         ["Mage",3,"Deal 3 damage. Shuffle a 'Roaring Torch' into your deck that deals 6 damage.","Forgotten Torch","Common"],
         ["Paladin",1,"Secret: After your opponent has at least 3 minions and plays another, destroy it.","Sacred Trial","Common"],
         ["Paladin",10,"Summon 7 Murlocs that died this game.","Anyfin Can Happen","Rare"],
         ["Priest",5,"Deal 3 damage to al minions. Shuffle this card into your opponent's deck.","Excavated Evil","Rare"],
         ["Priest",6,"Choose an enemy minion. Shuffle it into your deck.","Entomb","Common"],
         ["Shaman",7,"Give your minions +2/+2. Costs (1) less for each Murloc you control.","Everyfin is Awesome","Rare"],
         ["Warlock",2,"Give your opponent a 'Cursed!' card. While they hold it, they take 2 damage on their turn.","Curse of Rafaam","Common"]
    ]
  return Cards

def Weapons():
  #[class,mana cost,attack,durability,text,name,rarity]
  Cards=[["Warrior",1,2,3,"Double all damage dealth to your hero.","Cursed Blade","Rare"]
    ]
  return Cards

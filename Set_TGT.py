#The Grand Tournament Set

def All():
  Cards=Minions()
  Cards+=Spells()
  Cards+=Weapons()
  return Cards

def Minions():
  #[class,mana cost,attack,health,text,tribe,name,rarity]
  Cards=[["Neutral",1,2,1,"Taunt","","Tournament Attendee","Common"],
         ["Neutral",1,1,2,"Inspire: Gain +1 Attack.","","Lowly Squire","Common"],
         ["Neutral",1,2,4,"Battlecry: Deal 3 damage to this minion.","","Injured Kvaldir","Rare"],
         ["Neutral",1,1,2,"Battlecry: Reveal a minion in each deck. If yours costs more, gain +1/+1.","","Gadgetzan Jouster","Common"],
         ["Neutral",2,1,2,"Battlecry: Give a friendly minion +2 Attack.","","Lance Carrier","Common"],
         ["Neutral",2,2,3,"You can use your Hero Power twice a turn.","","Garrison Commander","Epic"],
         ["Neutral",2,2,3,"Battlecry: Deal 1 damage to a random enemy.","","Flame Juggler","Common"],
         ["Neutral",2,3,2,"Inspire: Gain +1 Health.","","Boneguard Lietenant","Common"],
         ["Neutral",2,2,4,"Can't attack. Inspire: Can attack as normal this turn.","","Argent Watchman","Rare"],
         ["Neutral",3,3,3,"Inspire: Summon a 1/1 Silver Hand Recruit.","","Silver Hand Regent","Common"],
         ["Neutral",3,2,2,"Stealth. Divine Shield.","","Silent Knight","Common"],
         ["Neutral",3,4,3,"Battlecry: Your opponent's Hero Power costs (5) more next turn.","","Saboteur","Rare"],
         ["Neutral",3,4,2,"Battlecry: If you have a minion with Spell Damage, gain +2/+2.","","Master of Ceremonies","Epic"],
         ["Neutral",3,4,3,"Battlecry: Silence a Demon.","","Light's Champion","Rare"],
         ["Neutral",3,5,2,"","","Ice Rager","Common"],
         ["Neutral",3,3,4,"Whenever you target this minion with a spell, gain Divine Shield.","","Fjola Lightbane","Legendary"],
         ["Neutral",3,2,2,"Battlecry: The next time you use your Hero Power it costs (2) less.","","Fencing Coach","Rare"],
         ["Neutral",3,3,4,"Whenever your target this minion with a spell, deal 3 damage to a random enemy.","","Eydis Darkbane","Legendary"],
         ["Neutral",3,3,3,"Inspire: Gain Windfury this turn.","","Dragonhawk Rider","Common"],
         ["Neutral",3,2,5,"Inspire: Return this minion to your hand.","","Coliseum Manager","Rare"],
         ["Neutral",3,2,1,"Charge. Divine Shield.","","Argent Horserider","Common"],
         ["Neutral",4,2,6,"Battlecry: If you're holding a Dragon, gain +1 Attack and Taunt.","Dragon","Twilight Guardian","Epic"],
         ["Neutral",4,1,8,"Inspire: Restore 2 Health to your hero.","","Tournament Medic","Common"],
         ["Neutral",4,3,5,"Battlecry: Restore 4 Health to each hero.","","Refreshment Vendor","Common"],
         ["Neutral",4,2,6,"Your Hero Power costs (1).","","Maiden of the Lake","Common"],
         ["Neutral",4,4,4,"Battlecry: If you have at least 4 other minions, deal 4 damage.","","Gormo the Impaler","Legendary"],
         ["Neutral",4,2,6,"Spell Damage +1","","Frigid Snobold","Common"],
         ["Neutral",4,5,4,"Taunt","","Evil Heckler","Common"],
         ["Neutral",4,4,4,"Whenever your play a card with Battlecry:, gain +1/+1.","","Crowd Favourite","Epic"],
         ["Neutral",4,5,3,"Battlecry: Reveal a minion in each deck. If yours costs more, gain Charge.","Beast","Armored Warhorse","Rare"],
         ["Neutral",5,5,4,"Inspire: Add a 2/2 Squire to your hand.","","Recruiter","Epic"],
         ["Neutral",5,5,6,"","","Pit Fighter","Common"],
         ["Neutral",5,4,5,"Inspire: Add a random spell to your hand.","","Nexus-Champion Saraad","Legendary"],
         ["Neutral",5,4,3,"Inspire: Give your other minions +1/+1.","Beast","Mukla's Champion","Common"],
         ["Neutral",5,4,4,"Inspire: Gain +2/+2.","","Kvaldir Raider","Common"],
         ["Neutral",5,5,5,"Battlecry: Give a friendly Mech +1/+1.","Mech","Clockwork Knight","Common"],
         ["Neutral",6,7,4,"Deathrattle: Reveal a minion in each deck. If yours costs more, return this to your hand.","","The Skeleton Knight","Legendary"],
         ["Neutral",6,6,5,"Battlecry: Copy your opponent's Hero Power.","","Sideshow Spelleater","Epic"],
         ["Druid",2,2,1,"Choose One - Transform to gain Charge; or +1/+1 and Stealth.","","Druid of the Saber","Common"],
         ["Druid",2,2,3,"Battlecry: Gain an empty Mana Crystal. Deathrattle: Lose a Mana Crystal.","","Darnassus Aspirant","Rare"],
         ["Druid",4,4,4,"Battlecry: Give a friendly Beast +3 Health.","","Wildwalker","Common"],
         ["Druid",4,5,4,"Inspire: Give your hero +2 Attack this turn.","Beast","Savage Combatant","Rare"],
         ["Druid",7,6,6,"Whenever you summon a Beast, reduce the Cost of this card by (1).","","Kinght of the Wild","Rare"],
         ["Druid",9,5,5,"Your minions cost (1).","","Aviana","Legendary"],
         ["Hunter",1,2,1,"Inspire: If your hand is empty, deal 2 damage to the enemy hero.","","Brave Archer","Common"],
         ["Hunter",2,3,2,"Battlecry: Reveal a minion in each deck. If yours costs more, draw it.","Beast","King's Elekk","Common"],
         ["Hunter",3,4,2,"Battlecry: Give a friendly Beast Immune this turn.","","Stablemaster","Epic"],
         ["Hunter",3,4,2,"At the end of your turn, deal 1 damage to all other minions.","Beast","Dreadscale","Legendary"],
         ["Hunter",5,3,3,"Battlecry: If you have a Beast, summon a random Beast.","","Ram Wrangler","Rare"],
         ["Hunter",7,4,2,"Whenever another minion takes damage, destroy it.","Beast","Acidmaw","Legendary"],
         ["Mage",2,3,2,"Your Hero Power deals 1 extra damage.","","Fallen Hero","Rare"],
         ["Mage",3,3,4,"Battlecry: Add a random spell to each player's hand.","","Spellslinger","Common"],
         ["Mage",4,3,5,"Inspire: Gain Spell Damage +1.","","Dalaran Aspirant","Common"],
         ["Mage",6,6,6,"You can use your Hero Power any number of times.","Dragon","Coldarra Drake","Epic"],
         ["Mage",8,7,7,"Deathrattle: Add 3 copies of Arcane Missiles to your hand.","","Rhonin","Legendary"],
         ["Paladin",3,2,4,"Your Silver Hand Recruits have +1 Attack.","","Warhorse Trainer","Common"],
         ["Paladin",4,3,4,"Inspire: Summon a random Murloc.","Murloc","Murloc Knight","Common"],
         ["Paladin",5,5,5,"Battlecry: Reveal a minion in each deck. If yours costs more, restore 7 Health to your hero.","","Tuskarr Jouster","Rare"],
         ["Paladin",6,6,6,"Battlecry: Put one of each Secret from your deck into the battlefield.","","Mysterious Challenger","Epic"],
         ["Paladin",7,3,7,"Battlecry: Change all enemy minions' Attack to 1.","","Eadric the Pure","Legendary"],
         ["Priest",2,1,4,"Battlecry: If you're holding a Dragon, gain +1 Attack and Taunt.","","Wyrmrest Agent","Rare"],
         ["Priest",3,3,3,"Whenever your draw a card, reduce its Cost by (1).","","Shadowfiend","Epic"],
         ["Priest",4,5,4,"Inspire: Deal 4 damage to each hero.","","Spawn of Shadows","Rare"],
         ["Priest",4,3,5,"Whenever a character is healed, gain +2 Attack.","","Holy Champion","Common"],
         ["Priest",7,5,4,"Inspire: Summon a random Legendary minion.","","Confessor Paletress","Legendary"],
         ["Rogue",1,2,1,"Whenever you equip a weapon, give it +1 Attack.","Pirate","Buccaneer","Common"],
         ["Rogue",2,3,2,"Combo: Deal 1 damage.","","Undercity Valiant","Common"],
         ["Rogue",2,2,2,"Whenever this minion attacks a hero, add the Coin to your hand.","","Cutpurse","Rare"],
         ["Rogue",3,4,3,"Battlecry: If you have a Pirate, gain +1/+1.","","Shady Dealer","Rare"],
         ["Rogue",5,3,7,"Combo: Gain +3 Attack.","","Shado-pan Rider","Common"],
         ["Rogue",9,8,4,"Deathrattle: Return this to your hand and summon a 4/4 Nerubian.","","Anub'arak","Legendary"],
         ["Shaman",2,3,4,"Overload: (1).","Totem","Totem Golem","Common"],
         ["Shaman",3,3,2,"Battlecry: Summon a random basic Totem.","","Tuskarr Totemic","Common"],
         ["Shaman",4,4,4,"Battlecry: Gain +1/+1 for each friendly Totem.","","Draenei Totemcarver","Rare"],
         ["Shaman",5,3,6,"Inspire: Give your Totems +2 Attack.","","Thunder Bluff Valiant","Rare"],
         ["Shaman",6,4,4,"Battlecry:Give all minions in your hand and deck +1/+1.","","The Mistcaller","Legendary"],
         ["Warlock",2,4,3,"Whenever this minion takes damage, also deal that amount to your hero.","Demon","Wrathguard","Common"],
         ["Warlock",2,3,2,"Whenever you discard a card, gain +1/+1.","Demon","Tiny Knight of Evil","Rare"],
         ["Warlock",4,1,1,"Deathrattle: Summon a Dreadsteed.","Demon","Dreadsteed","Epic"],
         ["Warlock",6,4,4,"Cards you draw from your Hero Power cost (0).","","Wilfred Fizzlebang","Legendary"],
         ["Warlock",6,5,4,"Inspire: Destroy a random minion for each player.","Demon","Void Crusher","Rare"],
         ["Warlock",7,6,8,"","Demon","Fearsome Doomguard","Common"],
         ["Warrior",2,3,2,"Taunt. Battlecry: Give a minion Taunt.","","Sparring Partner","Rare"],
         ["Warrior",2,2,3,"Battlecry: If you're holding a Dragon, gain +1 Attack and Charge.","","Alexstraza's Champion","Rare"],
         ["Warrior",3,3,3,"Inspire: Give your weapon +1 Attack.","","Orgrimmar Aspirant","Common"],
         ["Warrior",4,5,3,"Also damages the minions next to whomever he attacks.","","Magnataur Alpha","Epic"],
         ["Warrior",6,6,7,"When you draw this, deal 1 damage to your minions.","","Sea Reaver","Epic"],
         ["Warrior",10,7,7,"Battlecry: Draw 3 cards. Put any minions you drew directly into the battlefield.","","Varian Wrynn","Legendary"]
    ]
  return Cards

def Spells():
  #[class,mana cost,text,name,rarity]
  Cards=[["Druid",1,"Choose One- Deal 2 damage; or Summon two 1/1 Saplings.","Living Roots","Common"],
         ["Druid",3,"Destroy a minion. Add a random minion to your opponent's hand.","Mulch","Epic"],
         ["Druid",4,"Gain 10 Mana Crystals. Discard your hand.","Astral Communion","Epic"],
         ["Hunter",2,"Each time you cast a spell this turn, add a random Hunter card to your hand.","Lock and Load","Epic"],
         ["Hunter",2,"Secret: After your hero is attacked, summon a 3/3 Bear with Taunt.","Bear Trap","Common"],
         ["Hunter",3,"Deal 2 damage to a minion and the minions next to it.","Powershot","Rare"],
         ["Hunter",6,"Summon three 1/1 Webspinners.","Ball of Spiders","Rare"],
         ["Mage",1,"Deal 2 damage to a minion. This spell gets double bonus from Spell Damage.","Arcane Blast","Epic"],
         ["Mage",3,"Transform a minion into a 4/2 Boar with Charge.","Polymoph: Boar","Rare"],
         ["Mage",3,"Secret: When a friendly minion dies, summon a random minion with the same Cost.","Effigy","Rare"],
         ["Mage",5,"Deal 8 damage to a minion.","Flame Lance","Common"],
         ["Paladin",1,"Secret: When your turn starts, give your minions +1/+1.","Competitive Spirit","Rare"],
         ["Paladin",3,"Give a minion +3 Attack and Divine Shield.","Seal of Champions","Common"],
         ["Paladin",6,"Destroy all minion except each player's highest Attack minion.","Enter the Coliseum","Epic"],
         ["Priest",1,"Choose a minion. Whenever it attacks, restore 4 Health to your hero.","Power Word: Glory","Common"],
         ["Priest",1,"Restore 5 Health.","Flash Heal","Common"],
         ["Priest",2,"Put a copy of an enemy minion into your hand.","Convert","Rare"],
         ["Priest",2,"Swap the Attack and Health of all minions.","Confuse","Epic"],
         ["Rogue",3,"Add 2 random class cards to your hand (from your opponent's class).","Burgle","Rare"],
         ["Rogue",3,"Shuffle 3 Ambushes into your opponent's deck. When drawn, you summon a 4/4 Nerubian.","Beneath the Grounds","Epic"],
         ["Shaman",2,"Draw 2 cards. Overload: (2).","Ancestral Knowledge","Common"],
         ["Shaman",3,"Restore 7 Health. Reveal a minion in each deck. If yours costs more, Restore 14 instead.","Healing Wave","Rare"],
         ["Shaman",3,"Deal 4-5 damage to all minions. Overload: (5).","Elemental Destruction","Epic"],
         ["Warlock",4,"When you play or discard this, deal 4 damage to a random enemmy.","Fist of Jaraxxus","Rare"],
         ["Warlock",6,"Destroy 2 random enemy minions. Discard 2 random cards.","Dark Bargain","Epic"],
         ["Warrior",2,"Give your Taunt minions +2/+2.","Bolster","Common"],
         ["Warrior",3,"Deal 3 damage. Gain 3 Armor.","Bash","Common"]
    ]
  return Cards

def Weapons():
  #[class,mana cost,attack,durability,text,name,rarity]
  Cards=[["Paladin",2,2,2,"Battlecry: Reveal a minion in each deck. If yours costs more, +1 Durability.","Argent Lance","Rare"],
         ["Rogue",4,1,3,"Your Hero Power gives this weapon +1 Attack instead of replacing it.","Poisoned Blade","Epic"],
         ["Shaman",4,2,4,"Deathrattle: Your Hero Power becomes 'Deal 2 damage.'","Charged Hammer","Epic"],
         ["Warrior",3,3,2,"Battlecry: If you have a minion with Taunt, gain +1 Durability.","King's Defender","Rare"]
    ]
  return Cards

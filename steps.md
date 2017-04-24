1. Download page 1-6

curl -s -o out.txt http://tappedout.net/users/commandersbrew/mtg-decks/?&p=1&page=1

2. Find decks
grep -o 'mtg-decks/.*/"' out.txt

3. clean trailing quote
3a. dedupe list

4. Curl deck

http://tappedout.net/mtg-decks/06-11-15-wort-the-raidmother/

5. Parse TCG Player link

grep -o 'http://store.tcgplayer.com/massentry?partner=TPPDOUT&amp;c=.*&amp;'

6. Clean data

http://store.tcgplayer.com/massentry?partner=TPPDOUT&amp;c=1 Apocalypse Hydra||1 Archetype of Aggression||1 Armed / Dangerous||1 Artifact Mutation||1 Avenger of Zendikar||1 Bestial Menace||1 Blighted Woodland||1 Clan Defiance||1 Comet Storm||1 Commander&#39;s Sphere||1 Deus of Calamity||1 Elemental Bond||1 Evolving Wilds||1 Explosive Vegetation||1 Far Wanderings||1 Feral Incarnation||1 Fires of Yavimaya||1 Garruk&#39;s Packleader||1 Giant Trap Door Spider||1 Gruul Guildgate||1 Gruul Signet||1 Gruul Turf||1 Gruul War Chant||1 Gruul War Plow||1 Harmonize||1 Harrow||1 Hellkite Hatchling||1 Hull Breach||1 Increasing Vengeance||1 Journey of Discovery||1 Jund Panorama||1 Kazandu Refuge||1 Mountain Valley||1 Myriad Landscape||1 Naya Panorama||1 Nissa&#39;s Expedition||1 Nissa&#39;s Renewal||1 Omnath, Locus of Rage||1 Oran-Rief Hydra||1 Outpost Siege||1 Polis Crusher||1 Primal Growth||1 Rampaging Baloths||1 Revel of the Fallen God||1 Rubblebelt Raiders||1 Rubblehulk||1 Rugged Highlands||1 Rumbling Slum||1 Rupture Spire||1 Ruric Thar, the Unbowed||1 Savage Twister||1 Savage Ventmaw||1 Savageborn Hydra||1 Scuzzback Marauders||1 Searing Wind||1 Siege Behemoth||1 Skarrg Guildmage||1 Sol Ring||1 Stampeding Elk Herd||1 Stonebrow, Krosan Hero||1 Terramorphic Expanse||1 Transguild Promenade||1 Ulasht, the Hate Seed||1 Vandalblast||1 Vengeful Rebirth||1 Vithian Renegades||1 Volcanic Geyser||1 Voracious Cobra||1 Wild Ricochet||1 Wilderness Elemental||1 Winds of Qal Sisma||1 Xenagos, God of Revels||1 Zendikar Incarnate||1 Zhur-Taa Ancient&amp;

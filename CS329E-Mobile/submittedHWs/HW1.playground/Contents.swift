// Project: MaYixing-HW1
// EID: ym7653
// Course: CS329E

class Weapon {
    // include as a parameter a String that identifies the weapon type
    var weaponType: String
    init(weaponType: String) {
        self.weaponType = weaponType
    }
    
    // change a weapon to a string
    func toString() -> String {
        if weaponType == "dagger"{
            return "dagger"
        }
        if weaponType == "axe" {
            return "axe"
        }
        if weaponType == "staff" {
            return "staff"
        }
        if weaponType == "sword" {
            return "sword"
        }
        if weaponType == "none" {
            return "none"
        }
        return ""
    }
    
    // weapon's damage
    func damage() -> Int {
        if weaponType == "dagger"{
            return -4
        }
        if weaponType == "axe" {
            return -6
        }
        if weaponType == "staff" {
            return -6
        }
        if weaponType == "sword" {
            return -10
        }
        if weaponType == "none" {
            return -1
        }
        return 0
    }
}


class Armor {
    var armorType: String
    // include as a parameter a String that identifies the armor type
    init(armorType: String) {
        self.armorType = armorType
    }
    
    func toString() -> String {
        if armorType == "plate" {
            return "plate"
        }
        if armorType == "chain" {
            return "chain"
        }
        if armorType == "leather" {
            return "leather"
        }
        if armorType == "none" {
            return "none"
        }
        return ""
    }
    
    // protect points
    func protect() -> Int {
        if armorType == "plate" {
            return 2
        }
        if armorType == "chain" {
            return 5
        }
        if armorType == "leather" {
            return 8
        }
        if armorType == "none" {
            return 10
        }
        return 0
    }
}

class RPGCharacter {
    var name: String
    var health: Int
    // make name the parameter, health to be the optional parameter
    init(name: String, health: Int? = nil) {
        self.name = name
        self.health = health != nil ? health! : 0
    }
    
    func unwield() {
        print("\(name) is no longer wielding anything")
    }
    
    func takeOffArmor(){
        print("\(name) is no longer wearing anything")
    }
}

class Wizard: RPGCharacter {
    var spellName: String
    var armor: Armor
    var weapon: Weapon
    var spellPoint: Int
    
    override init(name: String, health: Int? = 16){
        self.spellName = ""
        self.armor = Armor(armorType: "none")
        self.weapon = Weapon(weaponType: "none")
        self.spellPoint = 20
        super.init(name: name, health: 16)
    }

    func wield(weaponObject: Weapon) {
        if weaponObject.weaponType == "dagger" || weaponObject.weaponType == "none" || weaponObject.weaponType == "staff" {
            self.weapon = weaponObject
            print("\(name) is now wielding a(n) \(weapon.toString())")
        }
    }
    
    func putOnArmor(armorObject: Armor) {
        print("Armor not allowed for this character class")
    }
    
    func fight(opponent: Fighter){
        print("\(name) attacks \(opponent.name) with a(n) \(weapon.toString())")
        
        // opponent's heath after attacking
        var currentHealth: Int
            currentHealth = opponent.health + weapon.damage()
        var positivedamage: Int
        positivedamage = (-1) * weapon.damage()
        print("\(name) does \(positivedamage) damage to \(opponent.name)")
        print("\(opponent.name) is now down to \(currentHealth) health")
        opponent.health = currentHealth
        // check if the opponent is defeated
        checkForDefeat(character: opponent)
    }
    
    // show all the attributes of the wizard
    func show(){
        print("\(name)")
        print("  Current Health: \(health)")
        print("  Current Spell Points: \(spellPoint)")
        print("  Wielding: \(weapon.toString())")
        print("  Wearing: none" )
        print("  Armor class: \(armor.protect())")
    }
    
    func checkForDefeat(character: Fighter){
        if character.health <= 0 {
            print("\(character.name) has been defeated!")
        }
    }

    
    func castSpell(spellName: String, target: RPGCharacter){
        var delta: Int
        delta = 6
        var currentSpellPoint: Int
        var currentHealth: Int
        var myHealth: Int
        var prevhealth: Int
        
        if spellName == "Fireball"{
            // cost 3
            currentSpellPoint = spellPoint - 3
            self.spellPoint = currentSpellPoint
            if spellPoint < 0 {
                print("Insufficient spell points")
            }
            else {
                print("\(name) casts \(spellName) at \(target.name)")
            }
            // effect 5
            currentHealth = target.health - 5
            target.health = currentHealth
            print("\(name) does 5 damage to \(target.name)")
            print("\(target.name) is now down to \(target.health) health")
        }
        
        else if spellName == "Lightning Bolt"{
            // cost 10
            currentSpellPoint = spellPoint - 10
            self.spellPoint = currentSpellPoint
            if spellPoint < 0 {
                print("Insufficient spell points")
                return
            }
            else {
                print("\(name) casts \(spellName) at \(target.name)")
            }
            // effect 10
            currentHealth = target.health - 10
            target.health = currentHealth
            print("\(name) does 10 damage to \(target.name)")
            print("\(target.name) is now down to \(target.health) health")
            
        }
        
        else if spellName == "Heal"{
            // cost 6
            currentSpellPoint = spellPoint - 6
            self.spellPoint = currentSpellPoint
            if spellPoint < 0 {
                print("Insufficient spell points")
            }
            else {
                print("\(name) casts \(spellName) at \(target.name)")
                // effect 6
                prevhealth = health
                myHealth = health + 6
                self.health = myHealth
                
                // the maximum of health is 16
                if health > 16 {
                    self.health = 16
                    delta = 16 - prevhealth
                }
                print("\(name) heals \(target.name) for \(delta) health points")
                print("\(name) is now at \(health) health")
            }
        }
        else {
            print("Unknown spell name, spell failed.")
        }
    }
    
}
class Fighter: RPGCharacter {
    var armor: Armor
    var weapon: Weapon
    var spellPoint: Int
    
    override init(name: String, health: Int? = 40){
        self.armor = Armor(armorType: "none")
        self.weapon = Weapon(weaponType: "none")
        self.spellPoint = 0
        super.init(name: name, health: 40)
    }
    
    // fighers are allowed to use any weapon type
    func wield(weaponObject: Weapon) {
        self.weapon = weaponObject
        print("\(name) is now wielding a(n) \(weapon.toString())" )
    }

    // fighers are allowed to wear any type of armor
    func putOnArmor(armorObject: Armor){
        self.armor = armorObject
        print("\(name) is now wearing \(armor.toString())")
    }
    
    
    func fight(opponent: Wizard){
        print("\(name) attacks \(opponent.name) with a(n) \(weapon.toString())")
        
        // opponent's health after attacking
        var currentHealth: Int
            currentHealth = opponent.health + weapon.damage()
        var positivedamage: Int
        positivedamage = (-1) *  weapon.damage()
        print("\(name) does \(positivedamage) damge to \(opponent.name)")
        print("\(opponent.name) is now down to \(currentHealth) health")
        opponent.health = currentHealth
        // check if the opponent is defeated
        checkForDefeat(character: opponent)
    }
    
    func checkForDefeat(character: Wizard){
        if character.health <= 0 {
            print("\(character.name) has been defeated!")
        }
    }
    
    // show all the attibutes of the fighter
    func show(){
        print("\(name)")
        print("  Current Health: \(health)")
        print("  Current Spell Points: \(spellPoint)")
        print("  Wielding: \(weapon.toString())")
        print("  Wearing: \(armor.toString())" )
        print("  Armor class: \(armor.protect())")
    }
}


// top level code

let plateMail = Armor(armorType: "plate")
let chainMail = Armor(armorType: "chain")
let sword = Weapon(weaponType: "sword")
let staff = Weapon(weaponType: "staff")
let axe = Weapon(weaponType: "axe")

let gandalf = Wizard(name: "Gandalf the Grey");
gandalf.wield(weaponObject: staff)

let aragorn = Fighter(name: "Aragorn")

aragorn.putOnArmor(armorObject: plateMail)

aragorn.wield(weaponObject: axe)

gandalf.show()

aragorn.show()

gandalf.castSpell(spellName: "Fireball", target: aragorn)

aragorn.fight(opponent: gandalf)

gandalf.show()

aragorn.show()

gandalf.castSpell(spellName: "Lightning Bolt", target: aragorn)

aragorn.wield(weaponObject: sword)

gandalf.show()

aragorn.show()

gandalf.castSpell(spellName: "Heal", target: gandalf)

aragorn.fight(opponent: gandalf)

gandalf.fight(opponent: aragorn)

aragorn.fight(opponent: gandalf)

gandalf.show()

aragorn.show()


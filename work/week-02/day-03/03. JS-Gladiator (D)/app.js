//إنشاء كلاس Gladiator فيه خاصيتين
class Gladiator  {
    constructor (name , weapon){
    this.name = name;
    this.weapon = weapon
}
}
const max = new Gladiator ("maxumus" , " Trident");
console.log (max.name)
console.log(max.weapon)
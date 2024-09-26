//variables to define the numbers
let powerSupply = 600;
const homes = 12; // number of homes
//power needed per home in units
const powerPerHome = 60;
// Checking if the power supplied to every home is sufficient
if (powerSupply >= homes * powerPerHome);{
    console.log("Power supplied to every home is sufficient!");
} else {
    console.log("Power supplied to every home is not sufficient!");
}
//using if statement to simulate power distribution to each home
for (let i = 1; i <= homes; i++){
    if (powerSupply >= powerPerHome);
{
        console.log(`Home ${i} receives ${powerPerHome} units of power.`);
        powerSupply -= powerPerHome;
    } 
    else {
    console.log(`Home ${i} receives ${powerSupply} units of power, and the rest will not receive any power.`);
    powerSupply = 0;
}
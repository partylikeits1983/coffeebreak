// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;


// remember the time I worked at SBUX? 
contract coffeeMachine {

   struct mastrena {
       
        uint size;
        string shots;
        string roast;
        string milk;
        bool paid;
    
   }
   
   mapping(address => mastrena) public drinks;
   
   function orderDrink(uint size, string memory shots, string memory roast, string memory milk) public {
       
       drinks[msg.sender].size = size;
       drinks[msg.sender].shots = shots;
       drinks[msg.sender].roast = roast;
       drinks[msg.sender].milk = milk;
       drinks[msg.sender].paid = false;
       
   }
   
   
   function makeDrink() public payable {
       
       require(drinks[msg.sender].size != 0);
       
       uint price;
       
       if (drinks[msg.sender].size == 1) {
           price = 1;
       }
       else if (drinks[msg.sender].size == 2) {
           price = 2;
       }
       else {
           price = 3;
       }
       
       require(msg.value >= price);
       
       drinks[msg.sender].paid = true;

       
   }
   
}


    

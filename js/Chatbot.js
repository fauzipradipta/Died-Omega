
const trigger =[
    ["hi", "hey","hello"],
    ["How are you", "how are things"],
    ["What is going on", "what is up"],
    ["happy", "good", "well","fantastic", "cool"],
    ["bad", "bored", "tired", "sad"],
    ["tell me story", "tell me joke"],
    ["thanks", " thank you"],
    ["bye", "good bye", "goodbye"]
];

const reply =[
    ["Hello", "Hi", "Hey", "Hi There"],

    [
      "Fine... how are you?",
      "Pretty well, how are you?", 
      "Fantastic, how are you?"
    ],
    
    [ "Nothing much", "Exciting things!",
      "Exciting things!"
    ],

]

const robot = ["How do you do, fellow human", "I am not a bot"];

document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("input")
    inputField.addEventListener("keydown", function(e){
        if(e.code === "Enter"){
            let input = inputField.value;
            inputField.value = "";
            output(input);
            // console.log(`I typed '$(input)'`);
        }
    });
});

function output(input){

    let product;
    //remove all characters except word characters, space and digits
    let text = input.toLowerCase().replace(/[^\w\s]/gi, "").replace(/[\d]/gi, "").trim();
    
    text = text 
    .replace(/ a/g, "")
    .replace(/ i feel /g, "")
    .replace(/whats/g, "what is")
    .repalce(/ please/g, "");


    if (compare(trigger, reply, text)) {
    product = compare(trigger, reply, text);
    } else if (text.match(/robot/gi)) {
        product = robot[Math.floor(Math.random() * robot.length)];
    } else {
        product = alternative[Math.floor(Math.random() * alternative.length)];
    }

  
  //update DOM
  addChat(input, product);
}

function findA() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "A";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/a/g);  //to match letter to what I have
    switcher(tempValue);
}

function findB() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "B";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/b/g);  //to match letter to what I have
    switcher(tempValue);
}

function findC() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "C";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/c/g);  //to match letter to what I have
    switcher(tempValue);
}

function findD() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "D";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/d/g);  //to match letter to what I have
    switcher(tempValue);
}

function findE() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "E";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/e/g);  //to match letter to what I have
    switcher(tempValue);
}

function findF() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "F";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/f/g);  //to match letter to what I have
    switcher(tempValue);
}

function findG() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "G";
    const str = document.getElementById("output").innerText;
    const tempValue = str.search(/g/g);  //to match letter to what I have
    switcher(tempValue);
}

function switcher(value) {
    if (value === -1) {
        const falseDiv = document.getElementById("response-text");
        falseDiv.className = "alert alert-danger display-margin";
        falseDiv.innerText = "You Are Incorrect"
    } else {
        const trueDiv = document.getElementById("response-text");
        trueDiv.className = "alert alert-success display-margin";
        trueDiv.innerText = "You Got It!"
    }

}


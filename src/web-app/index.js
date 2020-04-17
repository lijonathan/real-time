function readTextFile() {
    let i = 0;
    while(i < 1000) {
        const rawFile = new XMLHttpRequest();
        rawFile.open("GET", 'hand_data.txt', true);
        rawFile.onreadystatechange = function () {
            if (rawFile.readyState === 4) {
                if (rawFile.status === 200 || rawFile.status == 0) {
                    const allText = rawFile.responseText;
                    const textAreaTag = document.getElementById("output");
                    textAreaTag.innerHTML = allText
                }
            }
        };
        rawFile.send(null);
        ++i;
    }
}

function findA() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: A";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/a/g);  //to match letter to what I have
    switcher(tempValue);
}

function findB() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: B";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/b/g);  //to match letter to what I have
    switcher(tempValue);
}

function findC() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: C";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/c/g);  //to match letter to what I have
    switcher(tempValue);
}

function findD() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: D";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/d/g);  //to match letter to what I have
    switcher(tempValue);
}

function findE() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: E";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/e/g);  //to match letter to what I have
    switcher(tempValue);
}

function findF() {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: F";
    const str = document.getElementById("output").innerText;
    // const switcher = str.search(/true/g);
    const tempValue = str.search(/f/g);  //to match letter to what I have
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

function clearWindow() {
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerText = "";
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter:";
    const messageDiv = document.getElementById("response-text");
    messageDiv.className = "alert alert-warning display-margin";
    messageDiv.innerText = "Waiting For Response";
    const fs = require('fs')
    fs.truncate('hand_data.txt', 0, function(){console.log('done')})
}

function sendOnCommand() {
    const jqXHR = $.ajax({
        type: "POST",
        url: "../../glove/glove_start.py",
        async: false,
    });
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerHTML = jqXHR.responseText

}

function sendOffCommand() {
    const jqXHR = $.ajax({
        type: "POST",
        url: "../../glove/glove_stop.py",
        async: false,
    });
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerHTML = jqXHR.responseText

}

function callbackFunc(response) {
    console.log(response);
}

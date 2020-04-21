
function findLetter(temp) {
    console.log("Start");
    let i = 0;
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = temp;
    const str = document.getElementById("output").innerText;
    const lowerTemp = temp.toLowerCase();
    const re = new RegExp(lowerTemp, 'g');
    while (i < 300000) {
        const tempValue = str.search(re);  //to match letter to what I have
        switcher(tempValue);
        i++;
    }
    console.log("Stop")
}
//  Try to set window internal on this too
// function findLetter(temp) {
//     console.log("Start");
//     const rawFile = new XMLHttpRequest();
//     rawFile.open("GET", 'hand_data.txt', true);
//     rawFile.onreadystatechange = function () {
//         if (rawFile.readyState === 4) {
//             if (rawFile.status === 200 || rawFile.status == 0) {
//                 const allText = rawFile.responseText;
//                 const textAreaTag = document.getElementById("output");
//                 textAreaTag.innerHTML = allText
//             }
//         }
//     };
//     rawFile.send(null);
//     for(var i=0; i<1000;++i){}
//     const numGenHeader = document.getElementById("letter-generator");
//     numGenHeader.innerText = temp;
//     const str = document.getElementById("output").innerText;
//     const lowerTemp = temp.toLowerCase();
//     const re = new RegExp(lowerTemp, 'g');
//         const tempValue = str.search(re);  //to match letter to what I have
//         switcher(tempValue);
//     console.log("Stop");
// }

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
    const letterTag = document.getElementById("letter-generator");
    letterTag.innerText = "";
    const messageDiv = document.getElementById("response-text");
    messageDiv.className = "alert alert-warning display-margin";
    messageDiv.innerText = "Waiting For Response";
    clearFile();
};


function clearFile() {

    const fs = require('fs');
    fs.writeFile('../hand_data.txt', 'This is my text', function (err) {
        if (err) throw err;
        console.log('Replaced!');
    });
};

// function displayOutput() {
//     const rawFile = new XMLHttpRequest();
//     rawFile.open("GET", 'hand_data.txt', true);
//     rawFile.onreadystatechange = function () {
//         if (rawFile.readyState === 4) {
//             if (rawFile.status === 200 || rawFile.status == 0) {
//                 const allText = rawFile.responseText;
//                 const textAreaTag = document.getElementById("output");
//                 textAreaTag.innerHTML = allText
//             }
//         }
//     };
//     rawFile.send(null);
// };

window.setInterval(function () {
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
}, 2000);


function findLetter(temp) {
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = temp;
    const str = document.getElementById("output").innerText;
    const lowerTemp = temp.toLowerCase();
    const re = new RegExp(lowerTemp, 'g');
    const tempValue = str.search(re);  //to match letter to what I have
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

// function mainLetterFind(temp) {
//     const rawFile = new XMLHttpRequest();
//     let allText = '';
//     rawFile.open("GET", 'hand_data.txt', true);
//     rawFile.onreadystatechange = function () {
//         if (rawFile.readyState === 4) {
//             if (rawFile.status === 200 || rawFile.status === 0) {
//                 allText = rawFile.responseText;
//                 const textAreaTag = document.getElementById("output");
//                 textAreaTag.innerHTML = allText;
//                 console.log("allText = " + allText);
//                 console.log("temp = " + temp);
//                 if (allText === temp) {
//                     switcher(0);
//                     console.log("Matched In Time")
//                 } else {
//                     switcher(-1);
//                     console.log("Did Not Matched In Time")
//                 }
//             }
//         }
//     };
//     rawFile.send(null);
// };

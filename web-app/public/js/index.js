// window.setInterval(function () {
//     const waitMessage = document.getElementById("wait-message");
//     waitMessage.innerText = "Receiving, please wait..."
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
//     waitMessage.innerText = "Ready To Play"
// }, 2000);

function subscribeStart() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/subscribe-start",
        crossDomain:true,
        error: function(result) {
            alert('Error starting subscription service!');
        }
    });
}

function cloudStart() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/cloud-start",
        crossDomain:true,
        error: function(result) {
            alert('Error sending cloud start topic!');
        }
    });
}

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

function mainLetterFind(temp) {
    const rawFile = new XMLHttpRequest();
    let allText = '';
    rawFile.open("GET", 'hand_data.txt', true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status === 0) {
                allText = rawFile.responseText;
                const textAreaTag = document.getElementById("output");
                textAreaTag.innerHTML = allText;
                const re = new RegExp(temp, 'g')
                temp = allText.search(re);
                switcher(temp);
            }
        }
    };
    rawFile.send(null);
};

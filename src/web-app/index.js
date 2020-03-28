function readTextFile() {
    letterGenerator();
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
}

function findTrue() {
    const str = document.getElementById("output").innerText;
    const switcher = str.search(/true/g);
    // const switcher = str.search(/"letter": a/g);  //to match letter to what I have
    if(switcher === -1){
        const falseDiv = document.getElementById("response-text");
        falseDiv.className = "alert alert-danger display-margin";
        falseDiv.innerText = "You Are Incorrect"
    } else{
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

function letterGenerator(){
    const numGenHeader = document.getElementById("letter-generator");
    numGenHeader.innerText = "Sign The Letter: A";

}

function callbackFunc(response) {
    console.log(response);
}

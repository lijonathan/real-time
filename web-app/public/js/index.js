
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

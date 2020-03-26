function readTextFile() {
    const rawFile = new XMLHttpRequest();
    rawFile.open("GET", 'hand_data.txt', true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                const allText = rawFile.responseText;
                var patt = /true/g;
                var switcher = allText.match(patt);
                if(switcher == "true"){
                    alert("true")
                }else {
                    alert("false")
                }
                // const textAreaTag = document.getElementById("output");
                // textAreaTag.innerHTML = allText
            }
        }
    }
    rawFile.send(null);
}
function clearWindow() {
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerText = ""
}

function sendOnCommand() {
    $.ajax({
        type: "GET",
        url: "../../glove/glove_start.py",
        success: callbackFunc
    });

}
function sendOffCommand() {
    $.ajax({
        type: "POST",
        url: "../../glove/glove_stop.py",
        success: callbackFunc
    });

}

function callbackFunc(response) {
    console.log(response);
}

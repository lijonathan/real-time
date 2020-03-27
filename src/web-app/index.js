function readTextFile() {
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
    }
    rawFile.send(null);
}

// function readTextFile() {
//     jQuery.get("hand_data.txt", function (returnedData) {
//         $("#output").text(returnedData);
//     }, "text/plain");
// };

function findTrue() {
    const str = document.getElementById("output").innerText;
    const switcher = str.search(/true/g);
    if(switcher === -1){
        alert("False")
        document.getElementById("indicator").style.fill = "red";
    } else{
        alert("True")
        document.getElementById("indicator").style.fill = "green";
    }
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

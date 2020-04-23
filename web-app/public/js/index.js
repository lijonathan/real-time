function subscribeStart() {
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/subscribe-start",
        crossDomain: true,
        success: function () {
            const subButton = document.getElementById("subscribe-button");
            subButton.className = "btn btn-primary button-position disabled"
            setTimeout(readyToPlay, 3000);
        },
        error: function () {
            const waitMessage = document.getElementById("wait-message");
            waitMessage.style.color = 'red';
            waitMessage.innerText = "Error Starting Subscription Service"
        }
    });
}

function readyToPlay() {
    const waitMessage = document.getElementById("wait-message");
    waitMessage.style.color = 'green';
    waitMessage.innerText = "Ready To Play";
}


function cloudStart(temp) {
    const trueDiv = document.getElementById("response-text");
    trueDiv.className = "alert alert-warning display-margin";
    trueDiv.innerText = "Waiting For Response"
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/cloud-start",
        crossDomain: true,
        success: function (data) {
            setTimeout(function () {
                mainLetterFind(temp)
            }, 5000);
            console.log(data);
            console.log("Inside success for Cloud Start")
        },
        error: function (result) {
            const waitMessage = document.getElementById("wait-message");
            waitMessage.style.color = 'red';
            waitMessage.innerText = "Error Starting Subscription Service"
        },

    });

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
    console.log("Inside Main Letter Find")
    let allText = '';
    rawFile.open("GET", 'hand_data.txt', true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status === 0) {
                console.log("Found txt file")
                allText = rawFile.responseText;
                const textAreaTag = document.getElementById("output");
                textAreaTag.innerHTML = allText;
                const re = new RegExp(temp, 'g');
                temp = allText.search(re);
                switcher(temp);
            }
        }
        console.log(rawFile.status)
    };
    rawFile.send(null);
};

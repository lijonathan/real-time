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
}, 1000);

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

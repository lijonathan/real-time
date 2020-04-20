function clearWindow() {
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerText = "";
    const messageDiv = document.getElementById("response-text");
    messageDiv.className = "alert alert-warning display-margin";
    messageDiv.innerText = "Waiting For Response";
    clearFile();
};

require(['clearFile']), function clearFile() {
    const fs = require('fs');
    fs.writeFile('../hand_data.txt', 'This is my text', function (err) {
        if (err) throw err;
        console.log('Replaced!');
    });
};

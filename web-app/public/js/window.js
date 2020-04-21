// import {PythonShell} from 'python-shell';
let {PythonShell} = require('python-shell')

function sendOnCommand() {

    PythonShell.run('../../../glove/glove_start.py', null, function (err) {
        if (err) throw err;
        console.log('finished');
    });

    // var xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange = function() {
    //     if (this.readyState == 4 && this.status == 200) {
    //         // Typical action to be performed when the document is ready:
    //     }
    // };
    // xhttp.open("GET", "../index.php", true);
    // xhttp.send();
    // // const execSync = require('child_process').execSync;
    // // const output = execSync('python ../../../glove/glove_start.py')
    // // $.ajax({
    // //     type: "POST",
    // //     url: "../../../glove/glove_start.py",
    // //     async: false,
    // // });
    // // const textAreaTag = document.getElementById("output");
    // // textAreaTag.innerHTML = output.responseText
    // $.ajax({
    //     type: "POST",
    //     url: "../../../glove/glove_start.py",
    //     data: { param: ''}
    // }).done(function( o ) {
    //     // do something
    //     console.log('We Done')
    // });


}

// window.setInterval(function () {
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
// }, 2000);

// define(function (require) {
//     var child_process = require('child_process');
// });

function sendOffCommand() {
    const jqXHR = $.ajax({
        type: "POST",
        url: "../../../glove/glove_stop.py",
        async: true,
    });
    const textAreaTag = document.getElementById("output");
    textAreaTag.innerHTML = jqXHR.responseText

}

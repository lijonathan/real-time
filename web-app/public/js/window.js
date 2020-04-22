


// function sendOnCommand() {
//     // var shell = new ActiveXObject("WScript.Shell");
//     // shell.run("ls");
//     const myPythonScriptPath = '../../../glove/glove_start.py';
//
// // Use python shell
//     const PythonShell = require('python-shell');
//     var pyshell = new PythonShell(myPythonScriptPath);
//
//     pyshell.on('message', function (message) {
//         // received a message sent from the Python script (a simple "print" statement)
//         console.log(message);
//     });
//
// // end the input stream and allow the process to exit
//     pyshell.end(function (err) {
//         if (err) {
//             throw err;
//         }
//         ;
//
//         console.log('finished');
//     });
// };

function sendOnCommand(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            xhttp.open("GET", "../index.php", true);
            // Typical action to be performed when the document is ready:
            console.log("complete")
        }
    };
    xhttp.open("GET", "../index.php", true);
    xhttp.send();
}

// define(function (require) {
//     var child_process = require('child_process');
// });
//
// var shell = new ActiveXObject("WScript.Shell");
// shell.run("ls");

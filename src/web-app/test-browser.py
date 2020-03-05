from browser import document, alert


def greet(event):
    alert("Hello " + document["name-box"].value + "!")


document["greet-button"].bind("click", greet)

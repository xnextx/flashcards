/*
 *
 * Configuration and variables
 *
 */
$('#card').css('cursor', 'pointer');
$("#second").hide();

var question;
var answer;
var progress = 0;
var idontknow = idontknow_global;
var queue = 1;
function fill_card(question, answer) {
    $('#first').text(question);
    $('#second').text(answer);
}
function clear_undefined() { //deleting empty values with array (
    idontknow = idontknow.filter(function (n) {
        return n != undefined
    });
}
function counter() {
    $('#counter').text(progress+1 + "/" + idontknow.length + " " + "queue: " + queue);
}
function parse_card() {
    if ($("#second").is(":visible") == true) {
        switch_card();
    }
    // console.log(idontknow.length);
    if (idontknow[progress] != undefined && idontknow != []) {
        question = idontknow[progress].question;
        answer = idontknow[progress].answer;
        fill_card(question, answer);

    } else if (idontknow.length == 0) {
        fill_card("Finish", "Finish");
        answer = "";
        question = "";
    }
    counter();
}

function iknow_click() {

    if (progress <= idontknow.length - 1) {
        delete idontknow[progress];

        if (progress == idontknow.length - 1) {
            clear_undefined(); //deleting empty values with array

            console.log("Umiane");
            console.log("Elementów w liście nieumianych: " + (idontknow.length));
            console.log("Elementów w liście umianych: " + "brak danych");
            console.log("umiane: ");
            console.log("drak danych");
            console.log("nieumiane: ");
            console.log(idontknow);
            progress = 0;
            queue++;
        } else {
            progress++;
        }

        parse_card();
    } else {
        progress = 0;
    }


}
function idontknow_click() {
    if (progress <= idontknow.length - 1) {

        if (progress == idontknow.length - 1) {
            clear_undefined(); //deleting empty values with array

            console.log("Umiane");
            console.log("Elementów w liście nieumianych: " + (idontknow.length));
            console.log("Elementów w liście umianych: " + "brak danych");
            console.log("umiane: ");
            console.log("drak danych");
            console.log("nieumiane: ");
            console.log(idontknow);
            progress = 0;
            queue++;
        } else {
            progress++;
        }

        parse_card();
    }

}

function speech() {
    if ($("#first").is(":visible") == true) {
        var msg = new SpeechSynthesisUtterance(question);
        msg.lang = 'pl-PL';
        window.speechSynthesis.speak(msg);
    } else {
        var msg = new SpeechSynthesisUtterance(answer);
        var voices = window.speechSynthesis.getVoices();
        console.log(voices);
        msg.voice = voices[4];
        msg.lang = 'en-US';
        window.speechSynthesis.speak(msg);
    }
}

function switch_card() {
    if ($("#first").is(":visible") == true) {
        $("#first").hide();
    } else {
        $("#first").show();
    }
    if ($("#second").is(":visible") == true) {
        $("#second").hide();
    } else {
        $("#second").show();
        speech();
    }
}


parse_card();

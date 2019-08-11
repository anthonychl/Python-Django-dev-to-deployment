const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// set the alert messages from register or login to fade out after 3 seconds if the user doesnt close them
setTimeout(
    //first parameter
    function(){ 
        $('#message').fadeOut('slow');
    },
    // second parameter, the time (miliseconds)
    3000
);

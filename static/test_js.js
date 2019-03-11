function watch() {
    var today = new Date();

    var year = today.getFullYear();
    var month = today.getMonth();
    var day = today.getDate();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var second = today.getSeconds();

    document.getElementById("timer").innerHTML = year+'/'+month+'/'+day+' '+hour+':'+minute+':'+second;

    setTimeout("watch()", 1000);
}
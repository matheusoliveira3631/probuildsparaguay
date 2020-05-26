function Pesquisa() {
    var x = document.getElementById("pesquisa").value;
    var y = window.location.href;
    return location.assign("http://127.0.0.1:8000/camp/" + x.charAt(0).toUpperCase() + x.slice(1));
}
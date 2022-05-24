import * as data from '../../hosts.json'
html = "";
jsonData = JSON.parse(data);
console.log("test")
obj = {
    "192.168.1.42" : "Benjamin",
    "192.168.1.61": "Kien",
    "3" : "Tommy",
    "4" : "Tobias",
    "192.168.1.128": "Geir",
    "6" : "Stian"
}
for(var key in obj) {
    html += "<option value=" + key  + ">" + obj[key] + "</option>"
}
document.getElementById("clients").innerHTML = html;
document.getElementById("test").innerHTML = jsonData;
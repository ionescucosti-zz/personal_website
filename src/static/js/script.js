        function color(x) {
        document.getElementById("portrait").style.webkitFilter = "grayscale(0%)";
        document.getElementById("portrait").style.webkitTransition = "1s";
        x.style.width = "330px";
        x.style.height = "330px";
        x.style.cursor = "pointer";
        }
        function noColor(x) {
        document.getElementById("portrait").style.webkitFilter = "grayscale(100%)";
        x.style.width = "320px";
        x.style.height = "320px";
        }
        function active1(x) {
        x.style.border = "10px solid #23AD76";
        }
        function inactive1(x) {
        x.style.border = "10px solid #2ED190";
        x.style.background = "#2ED190";
        }
        function active2(x) {
        x.style.border = "10px solid #AD235A";
        }
        function inactive2(x) {
        x.style.border = "10px solid #D12E6F";
        x.style.background = "#D12E6F";
        }
        function active3(x) {
        x.style.border = "10px solid #9FAD23";
        }
        function inactive3(x) {
        x.style.border = "10px solid #C1D12E";
        x.style.background = "#C1D12E";
        }
        
function myFunction() {
    alert("Your message has been sent succesfull!");
}
        
const menu = document.getElementById("menu");
const menuBtn = document.getElementById("menuBtn");
const closeBtn = document.getElementById("closeBtn");

menuBtn.addEventListener('click',function () {
    menu.style.top="0";
});
closeBtn.addEventListener('click',function () {
    menu.style.top="-100vh";

});
window.addEventListener('load', function() {
    var video = document.getElementById('homeBg');
    video.play(); // Ensures the video plays when the page loads
});
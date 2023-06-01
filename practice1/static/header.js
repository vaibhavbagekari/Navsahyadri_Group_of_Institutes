function showModel() {
    document.querySelector('.overlay').classList.add('showoverlay');
    document.querySelector('.loginform').classList.add('showloginform');
}
function closModel() {
    document.querySelector('.overlay').classList.remove('showoverlay');
    document.querySelector('.loginform').classList.remove('showloginform');
}
function showModel2() {
    document.querySelector('.overlay2').classList.add('showoverlay2');
    document.querySelector('.loginform2').classList.add('showloginform2');
}

function closModel2() {
    document.querySelector('.overlay2').classList.remove('showoverlay2');
    document.querySelector('.loginform2').classList.remove('showloginform2');
}
function droupdown(){
    let box=document.getElementById('nav1');
    box.classList.toggle("navigation2");
    let btn=document.getElementById('navbtn');
    let btn2=document.getElementById('navbtn2');
    btn.classList.toggle("b2");
    btn2.classList.toggle("snav12");
}
function wellcome(){
    let b=document.getElementById("in1").value;
    alert("well come "+b);
    let c=document.getElementById("in2").value;
    alert("well come "+c);
}
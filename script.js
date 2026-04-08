// SLIDER

function scrollRow(id,amount){

const row=document.getElementById(id)

row.scrollBy({
left:amount,
behavior:"smooth"
})

}



// VIDEO HOVER PREVIEW

document.querySelectorAll(".video-card").forEach(card=>{

const video=card.querySelector("video")

card.addEventListener("mouseenter",()=>video.play())

card.addEventListener("mouseleave",()=>video.pause())

})



// FULLSCREEN VIEWER

function openViewer(src){

document.getElementById("viewer").style.display="flex"
document.getElementById("viewerImg").src=src

}

function closeViewer(){

document.getElementById("viewer").style.display="none"

}



// MUSIC

const music=document.getElementById("bgMusic")

function toggleMusic(){

if(music.paused){

music.play()

}else{

music.pause()

}

}



// SCROLL ANIMATION

const observer=new IntersectionObserver(entries=>{

entries.forEach(entry=>{

if(entry.isIntersecting){

entry.target.style.opacity=1
entry.target.style.transform="translateY(0)"

}

})

})

document.querySelectorAll(".section").forEach(section=>{

section.style.opacity=0
section.style.transform="translateY(50px)"
section.style.transition="1s"

observer.observe(section)

})

function toggleSong(id){

const audio = document.getElementById(id);

if(audio.paused){
audio.play();
}else{
audio.pause();
}

}

let currentAudio = null;

function playMemoryMusic(id, element){

const audio = document.getElementById(id);
const icon = element.querySelector("i");

/* stop other music */
if(currentAudio && currentAudio !== audio){
currentAudio.pause();
document.querySelectorAll(".music-control i").forEach(i=>{
i.classList.remove("fa-pause");
i.classList.add("fa-play");
});
}

/* play or pause */
if(audio.paused){

audio.play();
icon.classList.remove("fa-play");
icon.classList.add("fa-pause");
currentAudio = audio;

}else{

audio.pause();
icon.classList.remove("fa-pause");
icon.classList.add("fa-play");
currentAudio = null;

}

}

function toggleMenu(){

const menu=document.querySelector(".nav-links")
menu.classList.toggle("show")

}

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {

let current = "";

sections.forEach(section => {

const sectionTop = section.offsetTop - 100;
const sectionHeight = section.offsetHeight;

if (
window.scrollY >= sectionTop &&
window.scrollY < sectionTop + sectionHeight
){
current = section.getAttribute("id");
}

});

navLinks.forEach(link => {

link.classList.remove("active");

if(link.getAttribute("href") === "#" + current){
link.classList.add("active");
}

});

});
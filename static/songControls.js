var isPlay = false;
var currSong = document.querySelector('.HS1');
var prevSong = currSong;
let playBtn = document.querySelector(".play-btn");
var TotalMusics = document.querySelectorAll(".TotalMusics");
var NoMusic = TotalMusics[0].value;

function playSong(classs) {
    console.log(classs);
    currSong = document.querySelector('.' + classs);
    if (classs[0] == 'H')
        NoMusic = TotalMusics[0].value;
    else if (classs[0] == 'B')
        NoMusic = TotalMusics[1].value;
    else if (classs[0] == 'P')
        NoMusic = TotalMusics[2].value;
    else
        NoMusic = TotalMusics[3].value;
    if (isPlay) {
        if (currSong != prevSong) {
            currSong.play();
            prevSong.pause();
            playBtn.innerText = '❚❚';
            isPlay = true;
        }
        else {
            currSong.pause();
            playBtn.innerText = '▷';
            isPlay = false;
        }
    }
    else {
        currSong.play();
        playBtn.innerText = '❚❚';
        isPlay = true;
    }
    prevSong = currSong;
    copyCurrSong(classs);
}


function copyCurrSong(classs) {
    let musicDiv = document.querySelector(`.music${classs}`);
    let songDetails = document.querySelector(".details");
    let musicThumbnail = document.querySelector(".imgmusicThumbnail");
    let audio = document.querySelector(".audio");
    let end = document.querySelector("#end-time");
    songDetails.innerHTML = musicDiv.childNodes[3].innerHTML
    musicThumbnail.src = musicDiv.childNodes[1].src
    audio.src = musicDiv.childNodes[5].src
    end.innerText = (currSong.duration / 60).toFixed(2);
}
window.onload = function () {
    let main=document.querySelector("main");
    let loading=document.querySelector(".loading");
    main.classList.add("show-block");
    loading.classList.add("hide");
    copyCurrSong('HS1');
}


function playPauseSong() {
    if (isPlay) {
        currSong.pause();
        playBtn.innerText = '▷';
        isPlay = false;
    } else {
        currSong.play();
        playBtn.innerText = '❚❚';
        isPlay = true;
    }
}

function mute() {
    let mute = document.querySelector(".mute");
    if (mute.innerText == '🔊') {
        currSong.volume = true;
        mute.innerText = '🔇';
    } else {
        currSong.volume = false;
        mute.innerText = '🔊';
    }
}

let repeat = false;
function repeatSong() {
    let repeatBnt = document.querySelector(".repeat");
    if (repeatBnt.innerText == '↻') {
        repeat = true;
        repeatBnt.innerText = '⇆';
    } else {
        repeat = false;
        repeatBnt.innerText = '↻';
    }
}

function nextSong() {
    console.log("next");
    let cl = currSong.className.slice(0, 2);
    let n = Number(currSong.className.slice(2));
    n++;
    let now = cl + n;
    if (n <= NoMusic)
        playSong(now);
}

function PrevSong() {
    console.log("prev");
    let cl = currSong.className.slice(0, 2);
    let n = Number(currSong.className.slice(2));
    n--;
    let now = cl + n;
    if (n >= 1)
        playSong(now);
}

let timeLine = document.querySelector(".timeLine");
timeLine.onchange = function () {
    console.log("Change");
    let ChangeTime = timeLine.value;
    currSong.currentTime = (ChangeTime / 100) * currSong.duration;
}

setInterval(() => {
    if (isPlay) {
        timeLine.value = (currSong.currentTime / (currSong.duration)) * 100;
        let stTime = document.querySelector("#st-time");
        stTime.innerText = currSong.currentTime.toFixed(0);
        if (stTime.innerText > 60) {
            stTime.innerText = (currSong.currentTime / 60).toFixed(2);
        }
        if (timeLine.value == 100) {
            if (repeat == true)
                currSong.play();
            else
                nextSong();
        }
    }
}, 1000);

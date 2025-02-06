let menuFlag = false;
function showMenu() {
    let menuBar = document.querySelector(".menu-bar");
    let menuBtn = document.querySelector(".menu-btn");
    if (!menuFlag) {
        menuBtn.innerText = 'X';
        menuBar.classList.remove("hide");
        menuBar.classList.add("show-flex");
        menuFlag = true;
    }
    else {
        menuBtn.innerText = '☰';
        menuBar.classList.remove("show-flex");
        menuBar.classList.add("hide");
        menuFlag = false;
    }
}


let homeBox = document.querySelector(".home");
let songsBox = document.querySelector(".songs");
let searchBox = document.querySelector(".search");
function home() {
    // console.log("HOME");
    homeBox.classList.remove("hide");
    homeBox.classList.add("show-block");
    songsBox.classList.add("hide");
    songsBox.classList.remove("show-block");
    searchBox.classList.add("hide");
    searchBox.classList.remove("show-block");
}

function songs() {
    // console.log("SONGS");
    songsBox.classList.remove("hide");
    songsBox.classList.add("show-block");
    homeBox.classList.add("hide");
    homeBox.classList.remove("show-block");
    searchBox.classList.add("hide");
    searchBox.classList.remove("show-block");
}

function Search() {
    // console.log("SEARCH");
    searchBox.classList.remove("hide");
    searchBox.classList.add("show-block");
    songsBox.classList.add("hide");
    songsBox.classList.remove("show-block");
    homeBox.classList.add("hide");
    homeBox.classList.remove("show-block");
}

let hindiSongs = document.querySelector(".hindiSongs");
let bhojpuriSongs = document.querySelector(".bhojpuriSongs");
let punjabiSongs = document.querySelector(".punjabiSongs");
let bhaktiSongs = document.querySelector(".bhaktiSongs");
function hindiSong() {
    hindiSongs.classList.remove('hide');
    hindiSongs.classList.add('show-block');
    bhojpuriSongs.classList.add('hide');
    bhojpuriSongs.classList.remove('show-block');
    punjabiSongs.classList.add('hide');
    punjabiSongs.classList.remove('show-block');
    bhaktiSongs.classList.add('hide');
    bhaktiSongs.classList.remove('show-block');
}

function bhojpuriSong() {
    bhojpuriSongs.classList.remove('hide');
    bhojpuriSongs.classList.add('show-block');
    hindiSongs.classList.add('hide');
    hindiSongs.classList.remove('show-block');
    punjabiSongs.classList.add('hide');
    punjabiSongs.classList.remove('show-block');
    bhaktiSongs.classList.add('hide');
    bhaktiSongs.classList.remove('show-block');
}

function punjabiSong() {
    punjabiSongs.classList.remove('hide');
    punjabiSongs.classList.add('show-block');
    bhojpuriSongs.classList.add('hide');
    bhojpuriSongs.classList.remove('show-block');
    hindiSongs.classList.add('hide');
    hindiSongs.classList.remove('show-block');
    bhaktiSongs.classList.add('hide');
    bhaktiSongs.classList.remove('show-block');
}

function bhaktiSong() {
    bhaktiSongs.classList.remove('hide');
    bhaktiSongs.classList.add('show-block');
    punjabiSongs.classList.add('hide');
    punjabiSongs.classList.remove('show-block');
    bhojpuriSongs.classList.add('hide');
    bhojpuriSongs.classList.remove('show-block');
    hindiSongs.classList.add('hide');
    hindiSongs.classList.remove('show-block');
}
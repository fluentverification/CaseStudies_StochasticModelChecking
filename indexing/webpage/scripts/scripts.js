let advancedVisible = false;
let navExpanded = false;

function toggleAdvanced() {
	if (advancedVisible) {
		document.getElementById("advanced").classList.remove("visible");
		document.getElementById("toggle-advanced").classList.remove("toggled");
	}
	else {
		document.getElementById("advanced").classList.add("visible");
		document.getElementById("toggle-advanced").classList.add("toggled");
	}
	advancedVisible = !advancedVisible;
}

function toggleNavbar() {
	if (!navExpanded) {
		console.log("Expanding navbar");
		document.querySelectorAll(".navlink").forEach(a => a.classList.add('navlink-expanded'));
		document.getElementById("toggle-nav").innerHTML = "&times;";
	}
	else {
		console.log("Retracting navbar");
		document.querySelectorAll(".navlink").forEach(a => a.classList.remove('navlink-expanded'));
		document.getElementById("toggle-nav").innerHTML = "&#9776;";
	}
	navExpanded = !navExpanded;
}

function setDarkMode() {
	var rt = document.querySelector(":root");
	rt.style.setProperty("--color", "#eeeeee");
	rt.style.setProperty("--background", "#212121");

}

function setLightMode() {
	var rt = document.querySelector(":root");
	rt.style.setProperty("--color", "#444444");
	rt.style.setProperty("--background", "#ffffff");
}

let advancedVisible = false;

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

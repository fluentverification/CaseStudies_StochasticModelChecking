// TODO: this suggestions array needs to be populated with actual suggestions
let suggestions = [
	"foo"
	, "bar"
	, "baz"
	, "foobar"
	, "foobaz"
	, "fun"
	, "zedd"
	, "case"
	, "never"
	, "gonna"
	, "give"
	, "you"
	, "up"
];

function createTag() {
	// TODO
}

function showSuggestions() {
	let queryText = document.getElementById('query');
	let querySuggestions = document.getElementById('query-suggestions');
	let currentQuery = queryText.value;
	querySuggestions.innerHTML = "";
	if (currentQuery.length == 0) { return; }
	suggestions.forEach(s => {
		let locationIndex = s.indexOf(currentQuery)
		if (locationIndex >= 0 && s != currentQuery) {
			querySuggestions.innerHTML += "<div class=suggestion onclick=\"acceptSuggestion('" + s + "')\">" + s + "</div>";
			// console.log(s);
		}
		// else {
		// 	console.log("Omitting " + s + " since query is " + currentQuery);
		// }
	});
}

function acceptSuggestion(suggestion) {
	let queryText = document.getElementById('query');
	queryText.value = suggestion;
	showSuggestions();
}

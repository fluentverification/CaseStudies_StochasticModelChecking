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

let tagSuggestionsArray = [
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

const usedTags = new Set();

function hideAllSuggestions() {
	// console.log("hiding all suggestions");
	let querySuggestions = document.getElementById('query-suggestions');
	let tagSuggestions = document.getElementById('tag-suggestions');
	querySuggestions.innerHTML = "";
	tagSuggestions.innerHTML = "";
	querySuggestions.style.display = "None";
	tagSuggestions.style.display = "None";
}

/* Query Suggestions */

function showSuggestions() {
	let queryText = document.getElementById('query');
	let querySuggestions = document.getElementById('query-suggestions');
	let currentQuery = queryText.value.toLowerCase();
	querySuggestions.innerHTML = "";
	querySuggestions.style.display = "None";
	if (currentQuery.length == 0) { return; }
	if (suggestions.length > 0) { querySuggestions.style.display = "Block"; }
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

/* Tag suggestions */

function showTagSuggestions() {
	let tagText = document.getElementById('tags');
	let tagSuggestions = document.getElementById('tag-suggestions');
	let currentTag = tagText.value.toLowerCase();
	tagSuggestions.innerHTML = "";
	tagSuggestions.style.display = "None";
	if (currentTag.length == 0) { return; }
	if (suggestions.length > 0) { tagSuggestions.style.display = "Block"; }
	tagSuggestionsArray.forEach(s => {
		if (usedTags.has(s)) {
			return;
		}
		let locationIndex = s.indexOf(currentTag)
		if (locationIndex >= 0 && s != currentTag) {
			tagSuggestions.innerHTML += "<div class=suggestion onclick=\"createTag('" + s + "')\">" + s + "</div>";
		}
	});
}

function tagKeyPressHandler(event) {
	if (event.keyCode == 13) {
		createTag(document.getElementById('tags').value);
	}
}

function createTag(suggestion) {
	let tagText = document.getElementById('tags');
	tagText.value = "";
	if (usedTags.has(suggestion)) {
		// alert("Tag '" + suggestion +  "' exists!");
		hideAllSuggestions();
		return;
	}
	usedTags.add(suggestion);
	let tagList = document.getElementById('tags-box');
	tagList.innerHTML += "<span class=\"tag deletable\" id=tag-" + suggestion + " onclick=deleteTag('" + suggestion + "')>" + suggestion + "</span>";
	showTagSuggestions();
}

function deleteTag(tag) {
	document.getElementById('tag-' + tag).remove();
	usedTags.delete(tag);
}

function queryKeyPressHandler(event) {
	if (event.keyCode == 13) {
		search();
	}
}

function search() {
	alert("Search not implemented yet!");
	// TODO
}

function clearAllTags() {
	let tagList = document.getElementById('tags-box');
	tagList.innerHTML = "";
	usedTags.clear();
}

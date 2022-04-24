// AcroSlideX
// Acronym library
detect {
	// Detect acronyms
	// Markdown/ReStructuredText
	**<char>**<char> == <initial>
	// HTML5 (also part of Markdown and WikiText)
	<b>'char'</b>'char' == <initial>
	<em>'char'</b>'char' == <initial>
	<strong>'char'</strong>'char' == <initial>
	// For HTML5 examples, the 'char' between the tags is the initial. The second character after it indicates that it is a word, and should be slideable.
	// I need a method for acronyms with single letters (such as Not ;A; Number (NaN))
	The <initial> is the main thing that needs to be identified	
}
<initial> is the target character. Each initial, & whatever precedes/succeeds it should be expandable/collapsable
// More coming soon
// File version: 1 (2022, Saturday, April 23rd at 4:02 pm PST)

